function isNumeric(val) {
    return /^-?\d+$/.test(val);
}

function solution(s) {
    return s.length === 4 || s.length === 6 ? isNumeric(s) : false;
}