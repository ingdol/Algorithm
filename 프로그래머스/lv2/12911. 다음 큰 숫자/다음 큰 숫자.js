function solution(n) {
    let cnt = n.toString(2).split('1').length - 1
    let subN = Number(n)
    let subCnt = 0
    
    while (subCnt !== cnt) {
        subN += 1
        subCnt = subN.toString(2).split('1').length - 1
    }
    
    return subN;
}