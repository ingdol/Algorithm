function solution(s1, s2) {
    let answer = s1.filter((x) =>  s2.indexOf(x) !== -1)
    
    return answer.length;
}