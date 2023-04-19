function solution(s) {
    let len = s.length
    let i = len / 2
    if(len % 2 === 1) return s.slice(i, i+1)
    else return s.slice(i-1, i+1)
}