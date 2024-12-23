import sys
input = sys.stdin.readline

score_dic = {
    'A+' : 4.5,
    'A0' : 4.0,
    'B+' : 3.5,
    'B0' : 3.0,
    'C+' : 2.5,
    'C0' : 2.0,
    'D+' : 1.5,
    'D0' : 1.0,
    'F' : 0.0,
}
result = 0.0
score_sum = 0.0
for _ in range(20):
    name, score, grade = input().split()
    if grade != 'P':
        score_sum += float(score)
        result += float(score) * score_dic[grade]

if result != 0.0:
    result = round(result / score_sum, 6)
print(format(result, '.6f'))