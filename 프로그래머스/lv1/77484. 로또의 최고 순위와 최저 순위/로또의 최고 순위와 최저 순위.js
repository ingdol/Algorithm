function solution(lottos, win_nums) {
    let cnt = 0;
    let max = 0;
    const dic = [0, 6, 5, 4, 3, 2, 1];
    for(let i = 0; i < lottos.length; i++) {
        if(win_nums.indexOf(lottos[i]) !== -1) cnt++;
        else if (lottos[i] === 0) max++;
    }
    if(cnt === 6 && max === 0) return [1, 1];
    else if(max === 6 && cnt === 0) return [1, 6];
    else if(max === 0 && cnt === 0) return [6, 6];
    else return [dic[max + cnt] || 6, dic[cnt] || 1];
}
