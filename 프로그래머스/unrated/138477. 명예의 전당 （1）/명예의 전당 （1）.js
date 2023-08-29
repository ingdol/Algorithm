function solution(k, score) {
    let answer = [];
    let day = [];
    for(let i = 0; i < score.length; i++) {
        day.push(score[i]);
        day.sort((a, b) => b - a);
        day = day.slice(0, k);
        answer.push(day[day.length - 1]);
    }
    return answer;
}