function solution(s) {
    const dic = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    dic.map((d, i) => {
        const regexString = new RegExp(d, 'gi')
        s = s.replace(regexString, i)
    })
    return Number(s);
}