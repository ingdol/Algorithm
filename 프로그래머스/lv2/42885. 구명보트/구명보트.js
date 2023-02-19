function solution(people, limit) {
    let arr = people.sort((a, b) => a - b);
    let cnt = sum = lt = 0;
    let rt = arr.length - 1;
    while (lt < rt) {
        sum = arr[lt] + arr[rt]
        if(sum <= limit) lt++;
        rt--;
        cnt++;
    }
    if (rt === lt) cnt++;
    return cnt;
}