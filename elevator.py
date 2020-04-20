
floor_count = 6

class Elevator:
    
    def __init__(self, starting_floor = 1, direction):
        self.current_floor = starting_floor
        self.motor_direction = None
        self.requests = 0
        self.person_count = 0
        self.destination_floors = []
        self.up_floor_requests = []
        self.down_floor_requests = []
    
    def call(self, floor_called, direction_called):
        assert floor_called >= 1 and floor_called <= floor_count
        assert direction_called in ['up','down']
        if floor_called == 1 and direction_called == 'down' or floor_called == floor_Count and direction_called == 'up':
            raise ValueError("Invalid floor request")
        self.new_request = True
        submit_request(floor_called, direction_called)
        
    def submit_request(self, floor_called, direction_called):
        if direction_called == 'up':
            self.up_floor_requests.append(floor_called)
            self.up_floor_requests.sort()
            self.up_floor_requests = list(set(self.up_floor_requests))
            
        elif direction_called == 'down':
            self.down_floor_requests.append(floor_called)
            self.down_floor_requests.sort()
            self.down_floor_requests = list(set(self.up_floor_requests))
            
        self.requests = len(self.up_floor_requests) + len(self.down_floor_requests)
        if self.motor_direction == None:
            self.motor_direction = direction_called
        self.new_request = False
        self.move()
            
        
    def person_in(self):
        self.person_count += 1
        
    def person_out(self):
        self.person_count -= 1
        
        
    def select_floor(self, destination_floor):
        self.destination_floors.append(destination_floor)
        
        
    def move(self):
        while self.requests is not None and self.new_request == False: 
            self.next_move()
    
    def stop(self):
        self.motor_direction = None
        
    def next_destination_floor(self):
        
        if self.motor_direction == 'up':
            up_floors = self.destination_floors + self.up_floor_requests
            if up_floors:
                return min(up_floors)     
        elif self.motor_direction == 'down':
            down_floors = self.destination_floors + self.down_floor_requests
            if down_floors:
                return max(down_floors)
        else:
            raise ValueError("Can't call next destination floor because no direction specified")
            
        return None
    
    def change_direction(self):
        
        if self.motor_direction == 'up':
            self.motor_direction = 'down'
        elif self.motor_direction == 'down':
            self.motor_direction = 'up'
    
            
    def next_move(self):        
        
        if self.current_floor != self.destination_floor: 
            next_floor = next_destination_floor()
            if not next_floor:
                change_direction()
                next_floor = next_destination_floor()
                    
            
            # down logic
            if self.motor_direction == 'down':
              
        
        if self.current_floor > 1 and self.current_floor >= floor_count:
            
        else:
            person_out()
            # pop request
        
    
        
    def step(self, direction):
        
        
                if self.motor_direction == 'up':
                    self.current_floor += 1
                    print(self.current_floor, '...')
                elif self.motor_direction == 'down':
                    self.current_floor -= 1
                    print(self.current_floor, '...')
                elif not self.motor_direction:
                    msg = (f'No direction')
                    raise ValueError(msg)

            else:
                self.motor_direction = None
        
        else:
            msg = (f'floor {self.current_floor} invalid floor')
            raise ValueError(msg)    
            
            
            
        
        
