function solution(arr) {
    let answer = 0;
    let div = 2;
    let divState = false;
    let divArr = arr
    let arr = []
    divArr.map((x) => {
        let divNum = x/div
        if(Number.isInteger(divNum)) {
            arr.push(divNum)
        } else {
            divState = true
        }
        divArr = arr
    })
    console.log(divArr)
//     while(divState) {
//         ++div
        
//     }
    return answer;
}