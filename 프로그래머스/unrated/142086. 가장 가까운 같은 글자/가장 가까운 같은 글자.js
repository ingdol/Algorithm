function solution(s) {
    const hash={};

    return [...s].map((v,i)=>{
        let result = hash[v] !== undefined ? i - hash[v] : -1;
        hash[v] = i;
        return result;
    });
//     let answer = [];
//     let arr = [...s];
//     let putArr = [];
//     arr.map((str, i) => {
//         if(putArr.indexOf(str) === -1) {
//             answer.push(-1)
//         } else {
//             let index = 0
//             putArr.map((c, j) => {
//                 if (c === str) index = i - j
//             })
//             answer.push(index)
//         }
//         putArr.push(str)
        
//     })
//     return answer;
}