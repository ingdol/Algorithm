function solution(d, budget) {
    let cnt = 0
    d.sort((a, b) => a - b)
    while(budget >= 0) {
        budget -= d[cnt]
        cnt++
    }
    return cnt - 1
}