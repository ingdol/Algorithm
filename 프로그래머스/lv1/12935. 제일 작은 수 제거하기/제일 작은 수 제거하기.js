function solution(arr) {
    let answer = [...arr]
    if (arr.length === 1) {
        return [-1]
    } else {
        console.log(Math.max(...arr))
        arr.splice(arr.indexOf(Math.min(...arr)), 1)
        return arr
    }
}