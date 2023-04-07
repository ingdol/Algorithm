function solution(arr, divisor) {
    let answer = [];
    arr.filter((a) => a % divisor === 0 && answer.push(a))
    return answer.length > 0 ? answer.sort((a, b) => a - b) : [-1];
}