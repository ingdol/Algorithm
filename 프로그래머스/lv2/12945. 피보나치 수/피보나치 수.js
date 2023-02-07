function solution(n) {
    let x = 0;
    let y = 1;
    for(let i=2; i < n; i++) {
        if(i % 2 === 0) x = (x + y) % 1234567
        else y = (x + y) % 1234567
    }
    return (x + y) % 1234567;
}