function solution(A,B){
    let answer = 0;
    const Asort = A.sort((a, b) => a-b)
    const Bsort = B.sort((a, b) => b-a)
    Asort.map((a, i) => answer += a*Bsort[i])

    return answer;
}