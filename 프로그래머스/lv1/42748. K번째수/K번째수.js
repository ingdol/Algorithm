function solution(array, commands) {
    let answer = [];
    commands.map((arr) => {
        let sliceArr = array.slice(arr[0] - 1, arr[1])
        sliceArr.sort((a, b) => a - b) 
        answer.push(sliceArr[arr[2] - 1])
    })
    return answer;
}