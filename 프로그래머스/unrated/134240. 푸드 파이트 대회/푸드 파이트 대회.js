function solution(food) {
    let answer = '';
    for(let i = 1; i < food.length; i++) {
        let num = Math.floor(food[i] / 2)
        while(num > 0) {
            answer += i
            num--
        }
    }
    return answer + '0' + [...answer].reverse().join("");
}