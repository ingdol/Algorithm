function solution(dartResult) {
    let answer = 0;
    let dic = {'S': 1, 'D': 2, 'T' : 3};
    let dart = [];
    let index = 0;
    for(let i = 0; i < dartResult.length; i++) { 
        if(dic[dartResult[i]]) {
            dart[index] = dart[index] ** dic[dartResult[i]];
            index++;
        } else if(dartResult[i] === '*') {
            dart[index - 1] *= 2;
            if(dart[index - 2]) dart[index - 2] *= 2;
        } else if(dartResult[i] === '#') {
            dart[index - 1] *= -1;
        } else if(dartResult[i] === '1' && dartResult[i + 1] === '0') {
            dart[index] = Number(10);
            i++;
        } else {
            dart[index] = Number(dartResult[i]);
        }
    }
    dart.map((x) => answer += x);
    return answer;
}