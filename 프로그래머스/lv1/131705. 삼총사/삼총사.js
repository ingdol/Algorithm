function solution(number) {
    let answer = 0, lf = 0;
    while(lf <= number.length - 3) {
        let rf = lf + 1
        while(rf < number.length - 1) {
            for(let i = rf + 1; i < number.length; i++) {
                let sum = number[lf] + number[rf] + number[i]
                if(sum === 0) answer++
            }
            rf++
        }
        lf++
    }
    return answer;
}