function solution(cards1, cards2, goal) {
    let front_card1 = cards1.shift()
    let front_card2 = cards2.shift()
    let front_goal = goal.shift()
    
    while(goal.length > 0) {
        if (front_card1 !== front_goal && front_card2 !== front_goal) {
            return 'No'
        } else if (front_card1 === front_goal) {
            front_card1 = cards1.shift()
            front_goal = goal.shift()    
        } else if (front_card2 === front_goal) {
            front_card2 = cards2.shift()
            front_goal = goal.shift()    
        } 
    }
    if (front_card1 !== front_goal && front_card2 !== front_goal) {
        return 'No'
    }
    return 'Yes';
}