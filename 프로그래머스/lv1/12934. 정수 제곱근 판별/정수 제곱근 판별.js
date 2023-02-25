function solution(n) {
    let s = Math.sqrt(n)
    return Number.isInteger(s) ? (s + 1) ** 2 : -1
}