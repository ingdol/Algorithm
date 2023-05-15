function solution(arr1, arr2) {
    if(arr1.length > arr2.length) return 1
    else if(arr1.length < arr2.length) return -1
    else {
        let sum1 = 0
        arr1.map((x) => sum1 += x)
        let sum2 = 0
        arr2.map((y) => sum2 += y)
        
        if(sum1 > sum2) return 1
        else if(sum1 < sum2) return -1
        else return 0
    }
}