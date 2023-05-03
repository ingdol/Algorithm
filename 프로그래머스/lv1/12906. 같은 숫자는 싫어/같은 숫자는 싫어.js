function solution(arr)
{
    let answer = [];
    
    let i = 0;
    while (i < arr.length) {
        if(arr[i] !== arr[i+1]) {
            answer.push(arr[i])
        }
        i++
    }
    return answer;
}