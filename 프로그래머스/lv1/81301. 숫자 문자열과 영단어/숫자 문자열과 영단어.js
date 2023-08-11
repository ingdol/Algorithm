function solution(s) {
    const numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    let answer = s
    
    
    for(let i=0; i< numbers.length; i++) {
        let arr = answer.split(numbers[i]);
        console.log(arr)
        answer = arr.join(i);
        console.log(answer)
    }

    // numbers.map((n, i) => {
    //     const regexString = new RegExp(n, 'gi')
    //     s = s.replace(regexString, i)
    // })
    return Number(answer);
}