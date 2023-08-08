function solution(sizes) {
    let w = 0, h = 0
    sizes.map((size) => {
        let [a, b] = size.sort((a, b) => b - a)
        if(a > w) w = a
        if(b > h) h = b
    })
    return w * h
}