function solution(record) {
    let answer = [];
    let nameList = {}
    for (let text of record) {
        let textArr = text.split(' ')
        if (textArr[0] !== 'Leave') {
            nameList[textArr[1]] = textArr[2]
        }
    }
    for (let text of record) {
        let textArr = text.split(' ')
        if (textArr[0] === 'Enter') {
            answer.push(`${nameList[textArr[1]]}님이 들어왔습니다.`)
        } else if (textArr[0] === 'Leave') {
            answer.push(`${nameList[textArr[1]]}님이 나갔습니다.`)
        }
    }
    return answer;
}