function solution(a, b) {
    let mDay = [31,29,31,30,31,30,31,31,30,31,30,31];
    let week = ['FRI','SAT','SUN','MON','TUE','WED','THU'];
    let calender = [];
    let i = 0;
    for(let m = 1; m <= 12; m++) {
        let month = [];
        for(let d = 1; d <= mDay[m - 1]; d++) {
            month.push(week[i]);
            i++;
            if(i === 7) i = 0;
        }
        calender.push(month);
    }
    return calender[a - 1][b - 1];
}