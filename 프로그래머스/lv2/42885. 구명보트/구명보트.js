function solution(people, limit) {
    let cnt = 0;
    let arr = people.sort((a, b) => a - b)
    let sum = 0
    let lt = 0;
    let rt = arr.length - 1;
    while (lt < rt) {
        sum = arr[lt] + arr[rt]
        if(sum <= limit) lt += 1;
        rt -= 1;
        cnt += 1;
    }
    if (rt === lt) cnt += 1;
    return cnt;
}