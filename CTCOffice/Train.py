from signals import s

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
57, 0]

class Train():
  def __init__(self, line: str, destinations: list, train_id: int):
    self.id = train_id
    self.line = line
    self.current_block = 0
    self.route_block = 0
    self.destinations = destinations
  
class Train_Sim():
  def __init__(self):
    self.next_train_id = 1
    self.trains = {}
    self.green_authority = [0] * 151
    self.green_speeds = [0] * 151
    self.station_trains = {}

    self.second_count = 0

    s.send_TrackController_track_occupancy.connect(self.occupancy_update)
    s.send_CTC_test_track_occupancy.connect(self.occupancy_update)
    s.send_TrackModel_track_occupancy.connect(self.single_occupancy_update)

    s.timer_tick.connect(self.train_at_station)

  def create_train(self, line, destinations):
    train = Train(line, destinations, self.next_train_id)
    self.trains.update({self.next_train_id: train})
    self.next_train_id += 1
    self.update_authority(train.id)
    s.send_CTC_create_train.emit()

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
  
  def train_at_station(self, mult):
    trains_departing = []
    for i in range(0, len(self.station_trains)):
      train = self.station_trains[i]
      train [1] += 0.1 * mult
      if train[1] > 30:
        trains_departing.append()
        self.update_authority(train[0])

  
  def update_authority(self, train_id):
    train = self.trains.get(train_id)
    
    # If there are still destinations left
    if len(train.destinations) != 0:
      # If train is a station
      if train.current_block == train.destinations[0]:
        # Remove station from list
        train.destinations.pop(0)
        # Add train to station_trains list
        # self.station_trains.append([train_id, 0])
        self.station_trains.update({train_id: 0})
        return

    if(len(train.destinations) == 0):
      # Set authority from current block to yard to 1
      origin_block = train.current_block
      dest_block = -1
      self.set_authority_speed(train.line, train.route_block, origin_block, dest_block)
    else:
      # Set authority from current block to next station to 1
      origin_block = train.current_block
      dest_block = train.destinations[0]
      self.set_authority_speed(train.line, train.route_block, origin_block, dest_block)

  def set_authority_speed(self, line, route_block, origin, destination):
    if(line == 'Green'):
      location = green_route.index(origin)
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
      self.green_speeds[prevBlock] = 0

      authorities.append({'line': 'Green', 'block': prevBlock, 'authority': 0})
      speeds.append({'line': 'Green', 'block': prevBlock, 'speed': 0})
      
      for i in range(location, location + 3):
        # If at end of route break out of loop (avoid bounds error)
        if i > len(green_route):
          break
        
        # Get block of route
        block = green_route[i]

        # If the block is the current destination
        # Set authority and speed to 0 and break out of loop
        if block == destination:
          self.green_authority[block] = 0
          self.green_speeds[block] = 0

          authorities.append({'line': 'Green', 'block': block, 'authority': 0})
          speeds.append({'line': 'Green', 'block': block, 'speed': 0})
          break
        
        # If block is not destination
        # Set authority and speed to 1 and default
        else:
          self.green_authority[block] = 1
          self.green_speeds[block] = 30

          authorities.append({'line': 'Green', 'block': block, 'authority': 1})
          speeds.append({'line': 'Green', 'block': block, 'speed': 30})

      # Emit authority and speed signals
      s.send_CTC_authority.emit(authorities)
      s.send_CTC_suggested_speed.emit(speeds)

trains = Train_Sim()