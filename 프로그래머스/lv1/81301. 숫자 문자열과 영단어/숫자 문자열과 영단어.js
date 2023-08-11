function solution(s) {
    const numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    let answer = s
    numbers.map((n, i) => {
        const regexString = new RegExp(n, 'gi')
        answer = answer.replace(regexString, i)
    })
    return Number(answer);
}