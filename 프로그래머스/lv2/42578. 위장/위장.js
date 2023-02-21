function solution(clothes) {
    let answer = 1;
    let kind = new Map();
    clothes.map((arr) => {
        let cnt = kind.get(arr[1]) || 0
        cnt++
        kind.set(arr[1], cnt)
    })
    kind.forEach((valuse) => answer *= (valuse + 1))
    return answer - 1;
}