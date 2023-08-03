function solution(n, m) {
    var answer = [];
    let min = Math.min(n, m)
    let lcm = 1
    for(let i = 1; i <= min; i++) {
        if(Number.isInteger(n/i) && Number.isInteger(m/i)) {
            lcm *= i
            n = n/i
            m = m/i
            i = 1
        }
    }
    return [lcm, lcm*n*m];
}