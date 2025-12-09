function solution(dirs) {
    const dic = {U: [0, 1], L: [-1, 0], R: [1, 0], D: [0, -1]}
    let start = [0, 0]
    let result = new Set()
    for (const dir of dirs) {
        const x = dic[dir][0]
        const y = dic[dir][1]
        let moveX = start[0] + x
        let moveY = start[1] + y
        if(moveX >= -5 && moveX <= 5 && moveY >= -5 && moveY <= 5) {
        result.add(`${start[0]}${start[1]}${moveX}${moveY}`)
        result.add(`${moveX}${moveY}${start[0]}${start[1]}`)
            
        start = [moveX, moveY]
        }
    }
    return result.size / 2
}