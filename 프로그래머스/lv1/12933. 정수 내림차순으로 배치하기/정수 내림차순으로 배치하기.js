function solution(n) {
    let answer = '';
    let numArr = Array.from(String(n), x => Number(x))
    numArr.sort((a, b) => b - a)
    numArr = numArr.map((a) => answer += String(a))
    return Number(answer);
}