function solution(s, n) {
    let str = [...s]
    let codeS = 0
    str.map((s, i) => {
        if(s !== ' ') {
            codeS = s.charCodeAt() + n
            if((s === s.toUpperCase() && codeS >= 91) || codeS >= 123) codeS -= 26
            str[i] = String.fromCharCode(codeS)
        }
    })
    return str.toString().replace(/,/gi,'');
}