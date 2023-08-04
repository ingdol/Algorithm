function solution(n) {
    // let answer = 0
    // let trit = []
    // while(n >= 1) { 
    //     trit.push(n%3)
    //     n = Math.floor(n/3)
    // }
    // trit.reverse()
    // let threeNum = 1
    // trit.map((t, i) => 
    //      {
    //         answer +=  t * threeNum,
    //         threeNum *= 3 
    //     }  
    // )
    return parseInt([...n.toString(3)].reverse().join(''), 3);
}