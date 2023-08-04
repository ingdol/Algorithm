function solution(arr)
{
    let res = [arr[0]];
    for(let i = 1; i < arr.length; i++) {
        res[res.length - 1] !== arr[i] && res.push(arr[i])
    }
    
    return res;
}