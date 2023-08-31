function solution(cards1, cards2, goal) {
    let arr1 = cards1.reverse();
    let arr2 = cards2.reverse();
    for(let i = 0; i < goal.length; i++) {
        if(cards1.indexOf(goal[i]) !== -1) {
            if(arr1[arr1.length - 1] === goal[i]) arr1.pop()
            else return 'No'
        } else if(cards2.indexOf(goal[i]) !== -1) {
            if(arr2[arr2.length - 1] === goal[i]) arr2.pop()
            else return 'No'
        } else return 'No'
    }
    return 'Yes'
}