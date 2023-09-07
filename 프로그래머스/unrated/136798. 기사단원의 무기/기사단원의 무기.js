function solution(number, limit, power) {
    let answer = 1;
    for(let i = 2; i <= number; i++) {
        let cnt = 1;
        for(let j = 1; j <= i / 2; j++) {
            i % j === 0 && cnt++;
        }
        if(cnt > limit) cnt = power;
        answer += cnt;
    }
    return answer;
}