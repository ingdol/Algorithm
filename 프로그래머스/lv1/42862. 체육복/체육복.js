function solution(n, lost, reserve) {
    let answer = 0;
    let arr = Array(n).fill(1);
    lost = lost.sort((a, b) => a - b);
    reserve = reserve.sort((a, b) => a - b);
    lost.map((l) => arr[l - 1] = 0);
    reserve.map((r) => {
        if(lost.indexOf(r) !== -1) arr[r - 1] = 1;
        else arr[r - 1] = 2;
    })
    for(let i = 0; i < arr.length; i++) {
        arr[i] > 0 && answer++;
        if(arr[i] === 0) {
            arr[i] = 1;
            if(arr[i - 1] === 2) arr[i - 1] = 1;
            else if(arr[i + 1] === 2) arr[i + 1] = 1;
            else arr[i] = 0;
            if(arr[i] === 1) answer++;
        }
    }
    return answer;
}