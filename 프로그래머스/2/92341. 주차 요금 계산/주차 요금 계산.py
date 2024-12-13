from collections import defaultdict
import math

def solution(fees, records):
    answer = []
    dic = defaultdict(list)
    for record in records:
        time, car, state = record.split()
        time = time.split(':')
        if dic[car] and state == 'OUT':
            in_time = dic[car][-1][1]
            hour = int(time[0]) - int(in_time[0]) 
            minute = int(time[1]) - int(in_time[1])
            dic[car][-1] = ['fin', hour * 60 + minute]
        else: dic[car].append([state, time])
        
    fin_time_car = defaultdict(int)
    for dic_car in dic:
        for dic_time in dic[dic_car]:
            state, time = dic_time
            if state == 'fin':
                fin_time_car[dic_car] += time
            else: 
                hour = 23 - int(time[0]) 
                minute = 59 - int(time[1]) 
                fin_time_car[dic_car] += hour * 60 + minute
    
    fee_default_time, fee_default_cost, fee_min_time, fee_min_const = fees
    for fin_car in fin_time_car:
        time = fin_time_car[fin_car]
        if time <= fee_default_time:
            fin_time_car[fin_car] = fee_default_cost
        else:
            fin_time_car[fin_car] = fee_default_cost + math.ceil((time - fee_default_time) / fee_min_time) * fee_min_const
    sort_car_list = sorted(fin_time_car.keys())
    for car in sorted(fin_time_car.keys()):
        answer.append(fin_time_car[car])
    
    return answer