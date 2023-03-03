function solution(n, left, right) {
    let arr = []
    while(left <= right) {
        let x = Math.floor(left/n);
        let y = left%n
        arr.push(Math.max(x, y) + 1)
        left++
    }
    return arr;
}