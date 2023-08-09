function solution(t, p) {
    let answer = 0;
    for(let i = 0; i <= t.length - p.length; i++) {
        let subNum = Number(t.substr(i, p.length))
        if(p >= subNum) answer++
    }
    return answer;
}