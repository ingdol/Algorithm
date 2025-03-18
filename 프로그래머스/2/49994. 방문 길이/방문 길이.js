function solution(dirs) {
    const dirs_dic = {
        'U': [0, 1],
        'D': [0, -1],
        'R': [1, 0],
        'L': [-1, 0]
    }
    let visited = []
    let start_dir = [0, 0]
    for (let dir of dirs) {
        const [x, y] = dirs_dic[dir] 
        const [cur_x, cur_y] = [start_dir[0] + x, start_dir[1] + y]
        if ((cur_x >= -5 && cur_x <= 5) && (cur_y >= -5 && cur_y <= 5)) {
            visited.push([start_dir[0], start_dir[1], cur_x, cur_y])
            visited.push([cur_x, cur_y, start_dir[0], start_dir[1]])
            start_dir = [cur_x, cur_y]
        }
    }
    const answer = Array.from(new Set(visited.map(a => JSON.stringify(a))), json => JSON.parse(json))
    return answer.length / 2
    
}