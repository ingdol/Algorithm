function solution(s) {
    let answer = 0;
    let arr = [...s]
    for (let i = 0; i < s.length; i++) {
        if (isChecked(arr)) {
            answer += 1
        }
        arr.push(arr.shift())
    }
    return answer;
}

function isChecked(arr) {
    let pair = {'}':'{', ']':'[', ')':'('}
    let saveArr = []
    let flag = true
    for (let str of arr) {
        if (str === '[' || str === '(' || str === '{') {
            saveArr.push(str)
        } else {
            if (saveArr.pop() !== pair[str]) {
                flag = false
            }
        }
    }
    return saveArr.length === 0 && flag === true
}