function solution(s) {
    let answer = [];
    let arr = [...s];
    let putArr = [];
    arr.map((str, i) => {
        if(putArr.indexOf(str) === -1) {
            answer.push(-1)
        } else {
            let index = 0
            putArr.map((c, j) => {
                if (c === str) index = i - j
            })
            answer.push(index)
        }
        putArr.push(str)
        
    })
    return answer;
}