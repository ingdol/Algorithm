function solution(num_list) {
    let oddCnt = 0;
    let evenCnt = 0;
    for(let i = 0; i < num_list.length; i++) {
        if(num_list[i] % 2 === 0) {
            evenCnt += 1
        } else oddCnt += 1
    }
    return [evenCnt, oddCnt];
}