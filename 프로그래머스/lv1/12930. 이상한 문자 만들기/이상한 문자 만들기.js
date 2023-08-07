function solution(s) {
    let arr = [...s.toString()]
    let cnt = 1
    for(let i = 0; i < arr.length; i++) {
        if(arr[i] !== ' ') {
            if(cnt % 2 === 1) arr[i] = arr[i].toUpperCase()
            else arr[i] = arr[i].toLowerCase()
            cnt++
        } else {
            cnt = 1
        }
    }
    return arr.toString().replace(/,/gi, '')
}