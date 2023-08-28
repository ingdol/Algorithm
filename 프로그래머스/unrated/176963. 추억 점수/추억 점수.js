function solution(name, yearning, photo) {
    let answer = [];
    let dic = {};
    
    name.map((str, i) => {
        dic[str] = yearning[i];
    })
    
    for(let i = 0; i < photo.length; i++) {
        let sum = 0;
        for(let j = 0; j < photo[i].length; j++) {
            if(dic[photo[i][j]]) {
                sum += dic[photo[i][j]];
            }
        }
        answer.push(sum);
    }
    return answer;
}