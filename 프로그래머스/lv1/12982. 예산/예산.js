function solution(d, budget) {
    let sum = 0, cnt = 0
    d.sort((a, b) => a - b)
    while(budget >= sum) {
        sum += d[cnt]
        cnt++
    }
    return cnt - 1
}