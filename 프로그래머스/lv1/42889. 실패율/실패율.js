function solution(N, stages) {
    var answer = [];
    let total = stages.length;
    let dic = [];
    for(let i = 1; i <= N; i++) {
        let len = stages.filter((s) => s === i).length
        dic.push({'name' : i, 'num' : len / total});
        total -= len
    }
    dic.sort((a, b) => b.num - a.num)
    dic.map((d) => answer.push(Number(d.name)))
    return answer;
}