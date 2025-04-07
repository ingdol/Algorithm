function solution(nums) {
    let nums_set = new Set(nums)
    let n_length = nums.length / 2
    return Math.min(nums_set.size, n_length)
}