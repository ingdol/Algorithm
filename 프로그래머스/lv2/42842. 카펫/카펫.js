function solution(brown, yellow) {
    let answer = [];
    let S = brown + yellow
    let sArr = []
    for(let h = 1; h <= S; h++) {
        let w = S/h
        if(Number.isInteger(w) && w >= h) sArr.push([w, h])
    }
    sArr.map((s) => {  
        if((s[0] - 2) * (s[1] - 2) === yellow) answer = s }
    )
    return answer;
}