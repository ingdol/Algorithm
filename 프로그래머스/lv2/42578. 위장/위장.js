function solution(clothes) {
    var answer = 1;
    let kind = new Map();
    let cnt = 0;
    console.log(clothes)
    clothes.map((arr) => {
        let cnt = kind.get(arr[1]) || 0
        cnt++
        kind.set(arr[1], cnt)
    })
    kind.forEach((valuse) => answer *= (valuse + 1))
    return answer - 1;
}