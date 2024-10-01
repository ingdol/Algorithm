from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

queue = deque() 
max_waiting = 0  
last_student = 0

for _ in range(N):
    command = input().strip().split()
    
    if command[0] == '1':
        student_number = int(command[1])
        queue.append(student_number)
        
        if len(queue) > max_waiting:
            max_waiting = len(queue)
            last_student = student_number 
        elif len(queue) == max_waiting:
            last_student = min(last_student, student_number)
        
    elif command[0] == '2':
        queue.popleft()

print(max_waiting, last_student)
