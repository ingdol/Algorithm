function solution(array, commands) {
    let answer = [];
    for (let command of commands) {
        let [i, j, k] = command
        let first_step = array.slice(i - 1, j)
        let second_step = first_step.sort((a, b) => a - b)
        answer.push(second_step[k - 1])
    }
    return answer;
}