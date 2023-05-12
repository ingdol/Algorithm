function solution(cipher, code) {
    let answer = '';
    let i = code
    while(i <= cipher.length) {
        answer += cipher.charAt(i - 1)
        i += code
    }
    return answer;
}