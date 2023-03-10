function solution(n) {
    let answer = 1;
    let arr = new Array(n).fill(1);
    console.log(arr)
    for(let i = 0; i < n; i++) {
        let z = i
        for(let j = 1 + z; j < n; j++) {
            arr[z] -= 1
            arr[j] += 1
            if(arr[j] === 3) return answer % 1234567
            answer += 1
            z += 1
        }
    }
    return answer % 1234567;
}