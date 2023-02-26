function solution(n) {
    let s = 1;
    while(n % s !== 1) s++
    return s;
}