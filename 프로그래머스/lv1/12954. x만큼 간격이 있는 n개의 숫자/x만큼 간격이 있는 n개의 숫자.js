function solution(x, n) {
    let arr = new Array(n).fill(x);
    let addX = x
    for(let i = 1; i < n; i++) {
        arr[i] += addX
        addX += x
    }
    return arr;
}