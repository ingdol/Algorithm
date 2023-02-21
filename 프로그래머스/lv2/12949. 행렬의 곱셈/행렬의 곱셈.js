function solution(arr1, arr2) {
    let answer = [];
    for(let i = 0; i < arr1.length; i++) {
        let arrSum = []
        for(let x = 0; x < arr2[0].length; x++) {
            let sum = 0
            for (let y = 0; y < arr2.length; y++) {
                sum += arr1[i][y] * arr2[y][x]
            }
            arrSum.push(sum)
        }
        answer.push(arrSum)
    }
    return answer;
}