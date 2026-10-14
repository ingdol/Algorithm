/**
 * LeetCode 707. Design Linked List (Medium)
 * https://leetcode.com/problems/design-linked-list/
 * 풀이일: 2026-10-14
 * 접근: 단일 연결리스트 직접 구현 (head + size, 센티널 없음, tail 없음)
 * 시간 get/addAtIndex/deleteAtIndex O(index), addAtHead O(1), addAtTail O(n) / 공간 O(n)
 */

// 상자 하나
var Node = function(val) {
    this.val = val;     // 자기 값
    this.next = null;   // 다음 상자 (처음엔 없음)
};

// 리스트 전체
var MyLinkedList = function() {
    this.head = null;   // 첫 번째 상자
    this.size = 0;      // 상자 개수
};

/** 
 * @param {number} index
 * @return {number}
 */
MyLinkedList.prototype.get = function(index) {
    // 값을 가져옴, 없으면 -1
    if (index < 0 || index >= this.size) return -1;

    let cur = this.head;
    for (let i = 0; i < index; i++) {
        cur = cur.next;
    }
    return cur.val;
    
};

/** 
 * @param {number} val
 * @return {void}
 */
MyLinkedList.prototype.addAtHead = function(val) {
    // val을 처음 노드에 넣음
    let node = new Node(val);
    node.next = this.head;   // 기존 첫 상자에 연결
    this.head = node;        // head를 새 상자로
    this.size++;
};

/** 
 * @param {number} val
 * @return {void}
 */
MyLinkedList.prototype.addAtTail = function(val) {
    // val을 마지막에 넣음
    if (this.size === 0) {
        this.addAtHead(val);
        return;
    }

    let node = new Node(val);
    let cur = this.head;
    while (cur.next !== null) {   // 마지막 상자까지 이동
        cur = cur.next;
    }
    cur.next = node;   // 마지막 상자 뒤에 연결
    this.size++;
};

/** 
 * @param {number} index 
 * @param {number} val
 * @return {void}
 */
MyLinkedList.prototype.addAtIndex = function(index, val) {
    // val을 index 노드에 넣음
    // 만약 index랑 list 길이가 같다면 , 마지막에 넣음
    // 길이보다 크다면, 안넣음
    if (index < 0 || index > this.size) return;   // size와 같으면 맨 끝에 넣으므로 허용
    if (index === 0) {
        this.addAtHead(val);
        return;
    }

    let node = new Node(val);
    let cur = this.head;
    for (let i = 0; i < index - 1; i++) {   // 넣을 위치 "바로 앞" 상자까지 이동
        cur = cur.next;
    }
    node.next = cur.next;   // 새 상자 → 원래 그 자리 상자
    cur.next = node;        // 앞 상자 → 새 상자
    this.size++;
};

/** 
 * @param {number} index
 * @return {void}
 */
MyLinkedList.prototype.deleteAtIndex = function(index) {
    // 해당 index가 있으면 삭제
    if (index < 0 || index >= this.size) return;

    if (index === 0) {
        this.head = this.head.next;   // head를 두 번째 상자로
    } else {
        let cur = this.head;
        for (let i = 0; i < index - 1; i++) {   // 지울 상자 "바로 앞"까지 이동
            cur = cur.next;
        }
        cur.next = cur.next.next;   // 지울 상자를 건너뛰고 연결
    }
    this.size--;
};

/** 
 * Your MyLinkedList object will be instantiated and called as such:
 * var obj = new MyLinkedList()
 * var param_1 = obj.get(index)
 * obj.addAtHead(val)
 * obj.addAtTail(val)
 * obj.addAtIndex(index,val)
 * obj.deleteAtIndex(index)
 */
