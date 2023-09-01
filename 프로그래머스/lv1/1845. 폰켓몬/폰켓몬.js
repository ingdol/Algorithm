function solution(nums) {
    let max = nums.length / 2;
    let arr = [...new Set(nums)].length;
    
    return arr < max ? arr : max;
    // let dic = {};
    // nums.map((n) => {
    //     if(dic[n]) {
    //         let cnt = dic[n];
    //         dic[n] = ++cnt;
    //     } else {
    //         dic[n] = 1;
    //     }
    // })
    // return nums.length / 2 <= Object.keys(dic).length ? nums.length / 2 : Object.keys(dic).length ;
}