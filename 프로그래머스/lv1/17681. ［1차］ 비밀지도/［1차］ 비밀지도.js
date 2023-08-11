function getArr(arr, setArr, n) {
    for(let a of arr) {
        let reArr = ''
        while(a > 0) {
            reArr += a % 2
            a = Math.floor(a / 2)
        }
        setArr.push(String(reArr.split("").reverse().join("")).padStart(n, '0'))
    }
}
function solution(n, arr1, arr2) {
    let answer = [];
    let setArr1 = []
    let setArr2 = []
    getArr(arr1, setArr1, n)
    getArr(arr2, setArr2, n)
    console.log(setArr1, setArr2)
    for(let i = 0; i < n; i++) {
        let shapArr = ''
        setArr1 && [...setArr1[i]].map((arr, j) => {
            if((Number(arr) || Number(setArr2[i][j])) === 1) {
                shapArr += '#'
            } else shapArr += ' '
        })
        answer.push(shapArr)
        
    }
    return answer;
}