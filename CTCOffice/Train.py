from signals import s
import CTCOffice.InitData as InitData

green_route = [0, # J
63, 64, 65, 66, 67, 68, # K
69, 70, 71, 72, 73, # L
74, 75, 76, # M
77, 78, 79, 80, 81, 82, 83, 84, 85, # N
86, 87, 88, # O
89, 90, 91, 92, 93, 94, 95, 96, 97, # P
98, 99, 100, # Q
85, 84, 83, 82, 81, 80, 79, 78, 77, # N (reverse)
101, # R
102, 103, 104, # S
105, 106, 107, 108, 109, # T
110, 111, 112, 113, 114, 115, 116, # U
117, 118, 119, 120, 121, # V
122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, # W
144, 145, 146, # X
147, 148, 149, # Y
150, # Z
28, 27, 26, 25, 24, 23, 22, 21, # F (Reverse)
20, 19, 18, 17, # E (Reverse)
16, 15, 14, 13, # D (Reverse)
12, 11, 10, 9, 8, 7, # C (Revers0)
6, 5, 4, # B (Reversed)
3, 2, 1, # A (Reversed)
13, 14, 15, 16, # D
17, 18, 19, 20, # E
21, 22, 23, 24, 25, 26, 27, 28, # F
29, 30, 31, 32, # G
33, 34, 35, # H 
36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, # I
58, 59, 60, 61, 62]

red_route = [0,
9, 8, 7, # C (reverse)
6, 5, 4, # B (reverse)
3, 2, 1, # A (reverse)
16, 17, 18, 19, 20, # F
21, 22, 23, # G
24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, # H
46, 47, 48, # I
49, 50, 51, 52, 53, 54,  # J
55, 56, 57, # K
58, 59, 60, # L
61, 62, 63, # M
64, 65, 66, # N
52, 51, 50, 49, # J (reverse)
48, 47, 46, # I (reverse)
45, 44, # H (reverse)
67, # O
68, 69, 70, # P 
71, # Q
38, 37, 36, 35, 34, 33, # H (reverse)
72,  # R
73, 74, 75, # S
76, # T
27, 26, 25, 24, # H (reverse)
23, 22, 21, # G (reverse)
20, 19, 18, 17, 16, # F (reverse)
15, 14, 13, # E (reverse)
12, 11, 10, # D (reverse)
0]

class Train():
  def __init__(self, line: str, destinations: list, train_id: int, time_to_dispatch: int):
    self.id = train_id
    self.line = line
    if (line == 'Green'):
      self.current_block = 63
    else:
      self.current_block = 9
    self.route_block = 1
    self.destinations = destinations
    self.is_dwelling = 0
    self.dwelling_t = 0
    self.at_yard = 1
    self.time_to_dispatch = time_to_dispatch
  
class Train_Sim():
  def __init__(self):
    init_data = InitData.InitData()
    self.green_lengths = init_data.get_lengths('Green')
    self.red_lengths = init_data.get_lengths('Red')
    self.green_speeds = init_data.get_speeds('Green')
    self.red_speeds = init_data.get_speeds('Red')

    self.next_train_id = 1
    self.trains = {}
    self.green_authority = [0] * 151


    self.red_authority = [0] * 77


    self.station_trains = {}

    self.second_count = 50400+3300

    s.send_TrackController_track_occupancy.connect(self.occupancy_update)
    s.send_CTC_test_track_occupancy.connect(self.occupancy_update)
    s.send_TrackModel_track_occupancy.connect(self.single_occupancy_update)

    s.timer_tick.connect(self.train_at_station)
    s.timer_tick.connect(self.increment_timer)
  
  # Called once every time_tick
  def increment_timer(self, mult):
    self.second_count += (0.1 * mult)
    # For each train in list
    for train in self.trains.values():
      # If the train is at a yard
      if train.at_yard == 1:
        # Decrease the remaining time to dispatch
        train.time_to_dispatch -= (0.1 * mult)
        # If remaining time to dispatch is 0
        #   Set at_yard to 0 and set current block to first block
        #   Call update authority to set authority correctly
        if train.time_to_dispatch < 0:
          s.send_CTC_create_train.emit(train.line)
          train.at_yard = 0
          train.current_block = 63
          self.update_authority(train.id)

  # Called when train is dispatched or scheduled
  def create_train(self, line, destinations, dest_time):
    # Calculate remaining time to dispatch (time at dest - current time)
    time_to_dispatch = dest_time - self.second_count

    # Create a train with passed in parameters
    train = Train(line, destinations, self.next_train_id, time_to_dispatch)
    # Add train to train list
    self.trains.update({self.next_train_id: train})
    # Increment traid id
    self.next_train_id += 1

  def single_occupancy_update(self, line, block, occupancy):
    if line == 'Green':
      # If block is occupied
      if int(occupancy) == 1:
        # For each train that exists
        for train in self.trains.values():
          # If train was 1 behind new occupancy or was in yard
          # Set train block to current block
          # Call update authority
          if (block == green_route[train.route_block + 1]) or (train.current_block == 0):
            train.current_block = block
            train.route_block += 1
            self.update_authority(train.id)
    if line == 'Red':
      # If block is occupied
      if int(occupancy) == 1:
        # For each train that exists
        for train in self.trains.values():
          # If train was 1 behind new occupancy or was in yard
          # Set train block to current block
          # Call update authority
          if (block == red_route[train.route_block + 1]) or (train.current_block == 0):
            train.current_block = block
            train.route_block += 1
            self.update_authority(train.id)
  
  def occupancy_update(self, occupancies):
    for occupancy_i in occupancies:
      line = occupancy_i['line']
      block = occupancy_i['block']
      occupancy = occupancy_i['occupancy']

      if line == 'Green':
        # If block is occupied
        if occupancy == 1:
          # For each train that exists
          for train in self.trains.values():
            # If train was 1 behind new occupancy or was in yard
            # Set train block to current block
            # Call update authority
            if (block == green_route[train.route_block + 1]) or (train.current_block == 0):
              train.current_block = block
              train.route_block += 1
              self.update_authority(train.id)

      if line == 'Red':
        if occupancy == 1:
          for train in self.trains.values():
            if (block == red_route[train.route_block + 1]) or (train.current_block == 0):
              train.current_block = block
              train.route_block += 1
              self.update_authority(train.id)
  
  # Called once every time tick
  def train_at_station(self, mult):
    # For each train
    for train in self.trains.values():
      # If train is at a station
      if train.is_dwelling == 1:
        # Increase total time train has been at station
        train.dwelling_t += (0.1 * mult)
        # If total time at station > 30 seconds
        #   Set train dwelling to 0
        #   Reset total train dwelling time
        #   Call update_authority
        if train.dwelling_t > 30:
          train.is_dwelling = 0
          train.dwelling_t = 0
          self.update_authority(train.id)

  
  def update_authority(self, train_id):
    train = self.trains.get(train_id)
    
    # If there are still destinations left
    if len(train.destinations) != 0:
      # If train is a station
      if train.current_block == train.destinations[0][0]:
        # Remove station from list
        train.destinations.pop(0)
        # Set train dwelling to 1
        train.is_dwelling = 1

        if (train.line == 'Green'):
          prevBlock = green_route[train.route_block-1]
          authority = {'line': 'Green', 'block': prevBlock, 'authority': 0}
          speed = {'line': 'Green', 'block': prevBlock, 'speed': 0}
        if (train.line == 'Red'):
          prevBlock = red_route[train.route_block-1]
          authority = {'line': 'Red', 'block': prevBlock, 'authority': 0}
          speed = {'line': 'Red', 'block': prevBlock, 'speed': 0}

        s.send_CTC_authority.emit([authority])
        s.send_CTC_suggested_speed.emit([speed])
        return

    if(len(train.destinations) == 0):
      # Set authority from current block to yard to 1
      origin_block = train.current_block
      dest_block = 0
      self.set_authority_speed(train.line, train.route_block, origin_block, dest_block, 0)
    else:
      # Set authority from current block to next station to 1
      origin_block = train.current_block
      dest_block = train.destinations[0][0]
      speed = self.calculate_speed_to_next(train.line, train.route_block, dest_block, 0)
      self.set_authority_speed(train.line, train.route_block, origin_block, dest_block, speed)

  def calculate_speed_to_next(self, line, route_block, destination, tts):
    distance = 0
    speed = 0
    if(line == 'Green'):
      cur_block = green_route[route_block]
      cur_route_index = route_block
      if destination == 0:
        destination = 57

      while cur_block != destination:
        distance += self.green_lengths[cur_block]
        cur_route_index += 1
        if(cur_route_index >= len(green_route)):
          cur_route_index = 1
        cur_block = green_route[cur_route_index]

      if tts == 0:
        speed = 0
      else:
        speed = (distance/1000)/((tts-30)/3600)
    
    if(line == 'Red'):
      cur_block = red_route[route_block]
      cur_route_index = route_block
      while cur_block != destination:
        distance += self.red_lengths[cur_block]
        cur_route_index += 1
        cur_block = red_route[cur_route_index]
    return speed 

  def set_authority_speed(self, line, route_block, origin, destination, speed):
    block_speed = 0
    if(line == 'Green'):
      location = route_block

      # List of dicts indicating authorities
      authorities = []
      # List of dicts indicating speeds
      speeds = []

      # Set authority to 1 for location + 2 blocks ahead
      # If any of the blocks ahead is the destination
      #   Set authority of that block to 0 and break
      prevBlock = green_route[location-1]
      self.green_authority[prevBlock] = 0

      authorities.append({'line': 'Green', 'block': prevBlock, 'authority': 0})
      speeds.append({'line': 'Green', 'block': prevBlock, 'speed': 0})
      
      for i in range(location, location + 3):
        # If at end of route break out of loop (avoid bounds error)
        if i >= len(green_route):
          break
        
        # Get block of route
        block = green_route[i]

        # If on block 57 and destination is the yard set authorities and break loop
        if block == 57 and destination ==0:

          if speed == 0:
            block_speed = self.green_speeds[block]

          authorities.append({'line': 'Green', 'block': block, 'authority': 1})
          speeds.append({'line': 'Green', 'block': block, 'speed': block_speed})

          authorities.append({'line': 'Green', 'block': 0, 'authority': 1})
          speeds.append({'line': 'Green', 'block': 0, 'speed': block_speed})
          break

        # If the block is the current destination
        # Set authority and speed to 0 and break out of loop
        if block == destination:
          self.green_authority[block] = 0

          authorities.append({'line': 'Green', 'block': block, 'authority': 0})
          speeds.append({'line': 'Green', 'block': block, 'speed': 0})
          break
        
        # If block is not destination
        # Set authority and speed to 1 and default
        else:
          self.green_authority[block] = 1
          if speed == 0:
            block_speed = self.green_speeds[block]

          authorities.append({'line': 'Green', 'block': block, 'authority': 1})
          speeds.append({'line': 'Green', 'block': block, 'speed': block_speed})

      # Emit authority and speed signals
      s.send_CTC_authority.emit(authorities)
      s.send_CTC_suggested_speed.emit(speeds)

    if(line == 'Red'):
      location = red_route.index(origin)
      location = route_block

      # List of dicts indicating authorities
      authorities = []
      # List of dicts indicating speeds
      speeds = []

      # Set authority to 1 for location + 2 blocks ahead
      # If any of the blocks ahead is the destination
      #   Set authority of that block to 0 and break
      prevBlock = red_route[location-1]
      self.red_authority[prevBlock] = 0
      self.red_speeds[prevBlock] = 0

      authorities.append({'line': 'Red', 'block': prevBlock, 'authority': 0})
      speeds.append({'line': 'Red', 'block': prevBlock, 'speed': 0})
      
      for i in range(location, location + 3):
        # If at end of route break out of loop (avoid bounds error)
        if i > len(red_route):
          break
        
        # Get block of route
        block = red_route[i]

        # If the block is the current destination
        # Set authority and speed to 0 and break out of loop
        if block == destination:
          self.red_authority[block] = 0
          self.red_speeds[block] = 0

          authorities.append({'line': 'Red', 'block': block, 'authority': 0})
          speeds.append({'line': 'Red', 'block': block, 'speed': 0})
          break
        
        # If block is not destination
        # Set authority and speed to 1 and default
        else:
          self.red_authority[block] = 1
          self.red_speeds[block] = 30

          authorities.append({'line': 'Red', 'block': block, 'authority': 1})
          speeds.append({'line': 'Red', 'block': block, 'speed': speed})

      # Emit authority and speed signals
      s.send_CTC_authority.emit(authorities)
      s.send_CTC_suggested_speed.emit(speeds)

trains = Train_Sim()