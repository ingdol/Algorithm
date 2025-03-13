function solution(N, stages) {
    let answer = [];
    let playerCnt = stages.length;
    let stageCnt = new Array(N + 1).fill(0);
    
    for (let stage of stages) {
        if (stage <= N) stageCnt[stage]++;
    }
    
    let stageDic = {};
    for (let i = 1; i <= N; i++) {
        stageDic[i] = stageCnt[i] / playerCnt;
        playerCnt -= stageCnt[i];
    }
    
    let sortedFail = Object.entries(stageDic).sort((a, b) => b[1] - a[1])
    sortedFail.map((list) => answer.push(Number(list[0])))
    return answer;
}