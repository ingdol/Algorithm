function solution(arr1, arr2) {
    if(arr1.length > arr2.length) return 1
    else if(arr1.length < arr2.length) return -1
    else {
        let sum1 = arr1.reduce((x, y) => x + y)
        let sum2 = arr2.reduce((x, y) => x + y)
        
        if(sum1 > sum2) return 1
        else if(sum1 < sum2) return -1
        else return 0
    }
}