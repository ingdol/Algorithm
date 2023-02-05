function solution(s) {
    let zeroCnt = 0;
    let cnt = 0
    let zeroS = s
    while(zeroS != '1') {
        zeroCnt += zeroS.split('0').length - 1
        let zc = zeroS.replace(/0/gi,'').length
        let zc2 = ''
        while(zc !== 1) {
            zc2 += zc % 2
            zc = Math.floor(zc/2)
        }
        zc2 += '1'
        zeroS = zc2.split('').reverse().join('')
        cnt++
    }
    return [cnt, zeroCnt];
}