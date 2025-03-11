function solution(answers) {
    let answer = [];
    let score = [0, 0, 0];
    const ways = [[1, 2, 3, 4, 5, 1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    for (let i = 0; i < answers.length; i++) {
        if (ways[0][i%10] == answers[i]) {
            score[0] += 1
        }
        if (ways[1][i%16] == answers[i]) {
            score[1] += 1
        }
        if (ways[2][i%20] == answers[i]) {
            score[2] += 1
        }
    }
    const maxNum = Math.max(...score)
    for (let j = 0; j < score.length; j++) {
        if (maxNum == score[j]) {
            answer.push(j+1)
        }
    }
    return answer;
}