function solution(record) {
    let answer = [];
    let checkList = []
    let nameList = {}
    for (let text of record) {
        let textArr = text.split(' ')
        checkList.push([textArr[0], textArr[1]])
        if (textArr[0] !== 'Leave') {
            nameList[textArr[1]] = textArr[2]
        }
    }
    for (let check of checkList) {
        if (check[0] === 'Enter') {
            answer.push(`${nameList[check[1]]}님이 들어왔습니다.`)
        } else if (check[0] === 'Leave') {
            answer.push(`${nameList[check[1]]}님이 나갔습니다.`)
        }
    }
    return answer;
}