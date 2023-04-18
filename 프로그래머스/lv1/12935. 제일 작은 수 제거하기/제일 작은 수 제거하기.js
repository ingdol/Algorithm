function solution(arr) {
    let answer = [...arr]
    if (arr.length === 1) {
        return [-1]
    } else {
        let n = arr.sort((a, b) => b - a).pop()
        answer = answer.filter((e) => e !== n)
        return answer
    }
}