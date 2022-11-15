from signals import s

green_route = [0, 62, # J
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
58, 0]

class Train():
  def __init__(self, line: str, destinations: list, train_id: int):
    self.id = train_id
    self.line = line
    self.current_block = 0
    self.destinations = destinations
  
class Train_Sim():
  def __init__(self):
    self.next_train_id = 1
    self.trains = {}
    self.green_authority = [0] * 151

    s.send_TrackController_track_occupancy.connect(self.occupancies_update)
    s.send_CTC_test_track_occupancy.connect(self.occupancy_update)

  def create_train(self, line, destinations):
    train = Train(line, destinations, self.next_train_id)
    self.trains.update({self.next_train_id: train})
    self.next_train_id += 1
    self.update_authority(train.id)

  def occupancies_update(self, line, occupancies):
    if line == 'Green':
      for block in range(0, len(occupancies)):
        if occupancies(block) == 1:
          for train in self.trains.values():
            if train.destinations[0] == block:
              train.current_block = block
              self.update_authority(train.id)
  
  def occupancy_update(self, line, block, occupancy):
    if line == 'Green':
      if occupancy == 1:
        for train in self.trains.values():
          if len(train.destinations) != 0:
            if train.destinations[0] == block:
              train.current_block = block
              self.update_authority(train.id)
  
  def update_authority(self, train_id):
    train = self.trains.get(train_id)
    
    if train.current_block == train.destinations[0]:
      train.destinations.pop(0)

    if(len(train.destinations) == 0):
      # Set authority from current block to yard to 1
      origin_block = train.current_block
      dest_block = 0
      self.set_authority(train.line, origin_block, dest_block)
    else:
      # Set authority from current block to next station to 1
      origin_block = train.current_block
      dest_block = train.destinations[0]
      self.set_authority(train.line, origin_block, dest_block)

  def set_authority(self, line, origin, destination):
    if(line == 'Green'):
      location = green_route.index(origin)

      for i in range(location, len(green_route)):
        block = green_route[i]
        if block == destination:
          self.green_authority[block] = 0
          break
        else:
          self.green_authority[block] = 1

      s.send_CTC_authority.emit('Green', self.green_authority)

trains = Train_Sim()