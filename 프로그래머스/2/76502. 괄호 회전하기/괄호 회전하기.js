function solution(s) {
    let answer = 0;
    let arr = [...s]
    let save = []
    let cnt = s.length
    while (cnt > 0) {
        let popStr = arr.shift()
        arr.push(popStr)
        let flag = 0
        for (let str of arr) {
            if (str === '[' || str === '(' || str === '{') {
                save.push(str)
            } else {
                let strPop = save.pop()
                if ((str === ']' && strPop === '[') || (str === ')' && strPop === '(') || (str === '}' && strPop === '{')) {
                } else {
                    flag = 1
                }
            }
        }
        if (save.length === 0 && flag === 0) {
            answer += 1
        }
        save = []
        cnt -= 1
        flag = 0
    }
    return answer;
}