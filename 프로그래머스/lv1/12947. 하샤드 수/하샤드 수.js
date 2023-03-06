function solution(x) {
    let divX = 0
    for(let y of String(x)) {
        divX += Number(y)
    }
    
    return x % divX === 0;
}