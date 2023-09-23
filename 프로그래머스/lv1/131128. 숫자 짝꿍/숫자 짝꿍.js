function solution(X, Y) {
    let arrX = Array(10).fill(0);
    let arrY = Array(10).fill(0);
    [...X].forEach((n) => ++arrX[n]);
    [...Y].forEach((n) => ++arrY[n]);
    
    let res = '';
    for(let i = 9; i >= 0; i--) {
        if(arrX[i] === 0 || arrY[i] === 0) continue;
        res += String(i).repeat(Math.min(arrX[i], arrY[i]));
    }
    if(!res) return '-1';
    return res[0] === '0' ? '0' : res;
}