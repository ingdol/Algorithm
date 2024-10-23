from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_list = deque(truck_weights) 
    crossing_truck_list = deque()  
    
    truck_weight = 0 
    time = 0 
    
    while truck_list or crossing_truck_list:
        time += 1
        
        if crossing_truck_list:
            for i in range(len(crossing_truck_list)):
                crossing_truck_list[i][1] += 1

            if crossing_truck_list[0][1] > bridge_length:
                finished_truck = crossing_truck_list.popleft()
                truck_weight -= finished_truck[0]

        if truck_list:
            if truck_weight + truck_list[0] <= weight and len(crossing_truck_list) < bridge_length:
                truck = truck_list.popleft()
                crossing_truck_list.append([truck, 1])
                truck_weight += truck

    return time
