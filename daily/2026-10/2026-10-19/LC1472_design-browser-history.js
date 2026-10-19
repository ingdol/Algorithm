/**
 * LeetCode 1472. Design Browser History (Medium)
 * https://leetcode.com/problems/design-browser-history/
 * 풀이일: 2026-10-19
 * 접근: 단일 연결리스트 + 현재 위치 인덱스(now), 매 연산마다 head부터 now까지 순회
 * 시간 visit/back/forward 모두 O(n) / 공간 O(n)
 */

var Node = function(val, next) {
    this.val = val;
    this.next = next;
}
/**
 * @param {string} homepage
 */
var BrowserHistory = function(homepage) {
    this.homepage = new Node(homepage);
    this.size = 1;
    this.now = 0;
    return null;
};

/** 
 * @param {string} url
 * @return {void}
 */
BrowserHistory.prototype.visit = function(url) {
    let node = new Node(url);
    let cur = this.homepage;
    for (let i = 0; i < this.now; i++) {
        cur = cur.next;
    }
    cur.next = node;
    this.now++;
    this.size = this.now + 1;
    return null;
};

/** 
 * @param {number} steps
 * @return {string}
 */
BrowserHistory.prototype.back = function(steps) {
    let cur = this.homepage;
    let first = this.now - steps;
    if (first < 0) {
        first = 0;
    }
    for (let i = 0; i < first; i++) {
        cur = cur.next;
    }
    this.now = first;
    return cur.val;
};

/** 
 * @param {number} steps
 * @return {string}
 */
BrowserHistory.prototype.forward = function(steps) {
    let cur = this.homepage;
    let end = this.now + steps;
    if (end >= this.size) {
        end = this.size - 1;
    }
    for (let i = 0; i < end; i++) {
        cur = cur.next;
    }
    this.now = end;
    return cur.val;
    
};

/** 
 * Your BrowserHistory object will be instantiated and called as such:
 * var obj = new BrowserHistory(homepage)
 * obj.visit(url)
 * var param_2 = obj.back(steps)
 * var param_3 = obj.forward(steps)
 */
