/**
 * LeetCode 1. Two Sum (Easy)
 * https://leetcode.com/problems/two-sum/
 * 풀이일: 2026-10-13
 * 접근: 이중 반복문 (브루트포스) — 10-12 풀이 리팩터링 (break 제거, ===, 내부 for, 미발견 시 [] 반환)
 * 시간 O(n²) / 공간 O(1)
 */

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    for(let i = 0; i < nums.length; i++) {
        for(let j = i + 1; j < nums.length; j++) {
            if(nums[i] + nums[j] === target) {
                return [i, j];
            }
        }
    }
    return [];
};
