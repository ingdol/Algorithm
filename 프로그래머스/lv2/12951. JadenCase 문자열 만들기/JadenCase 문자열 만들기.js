function solution(s) {
    let arr = s.split(' ')
    let sen = arr.map((str, i) => str.charAt(0).toUpperCase() + str.slice(1).toLowerCase()).join(' ')
    return sen
}