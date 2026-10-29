/**
 * LeetCode 20. Valid Parentheses (Easy)
 * https://leetcode.com/problems/valid-parentheses/
 * 풀이일: 2026-10-29
 * 접근: 스택 — 여는 괄호를 만나면 짝이 되는 닫는 괄호를 push, 닫는 괄호는 top과 비교
 * 시간 O(n) / 공간 O(n)
 */

/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    const stack = [];
    for(const chr of s) {
        if(chr === '(') stack.push(')');
        else if(chr === '[') stack.push(']');
        else if(chr === '{') stack.push('}');
        else if(chr === stack[stack.length - 1]) stack.pop();
        else return false;
    }
    return stack.length === 0;
};
