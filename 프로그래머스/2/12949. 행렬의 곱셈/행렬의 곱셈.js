function solution(arr1, arr2) {
    var answers = [];
    for (let i = 0; i < arr1.length; i++) {
        let answer = []
        for (let x = 0; x < arr2[0].length; x++) {
            let sum = 0;
            for (let j = 0; j < arr1[0].length; j++) {
                sum += arr1[i][j] * arr2[j][x]
            }
            answer.push(sum)
        }
        answers.push(answer)
    }
    return answers;
}