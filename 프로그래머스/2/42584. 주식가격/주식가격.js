function solution(prices) {
    let answer = [];
    for (let i = 0; i < prices.length - 1; i++) {
        let target = prices[i]
        let cnt = 0
        let j = i + 1
        while(j < prices.length) {
            cnt += 1
            if (prices[j] < target) break
            j++
        }
        answer.push(cnt)
    }
    answer.push(0)
    return answer;
}