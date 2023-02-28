function solution(k, tangerine) {
    let answer = 0;
    let obj = {}
    tangerine.forEach((t) => obj[t] = ++obj[t] || 1)
    const kind = Object.values(obj).sort((a, b) => b - a)
    let sum = 0;
    for(let n of kind) {
        answer++;
        sum += n;
        if(sum >= k) break;
    }
    return answer;
}