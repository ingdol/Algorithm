function solution(n)
{
    let answer = 0;
    for(let c of String(n)) {
       answer += Number(c)
    }
    return answer;
}