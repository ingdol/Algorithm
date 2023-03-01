function solution(progresses, speeds) {
    let answer = [];
    let daying = 0;
    let d = 0;
    
    for (let i = 0; i < progresses.length; i++) {
        let leftP = 100 - progresses[i]
        let leftDay = Math.ceil(leftP / speeds[i])
        
        if(leftDay > daying) {
            if(i !== 0) d += 1;
            daying = leftDay;
        }   
        answer[d] = answer[d] ? ++answer[d] : 1
    }
    return answer;
}