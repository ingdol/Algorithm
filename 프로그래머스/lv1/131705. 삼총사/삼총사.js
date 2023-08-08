function solution(number) {
    let answer = 0;
    for(let lf = 0; lf < number.length - 2; lf++) {
        for(let rf = lf + 1; rf < number.length - 1; rf++) {
            for(let i = rf + 1; i < number.length; i++) {
                let sum = number[lf] + number[rf] + number[i]
                if(sum === 0) answer++
            }
        }
    }
    return answer;
}