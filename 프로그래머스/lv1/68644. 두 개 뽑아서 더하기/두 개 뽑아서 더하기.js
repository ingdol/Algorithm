function solution(numbers) {
    let answer = new Set()
    numbers.sort((a, b) => a - b)
    console.log(numbers)
    for(let i = 0; i < numbers.length; i++) {
        for(let j = i + 1; j < numbers.length; j++) {
            let sum = numbers[i] + numbers[j]
            answer.add(sum)
        }
    }
    return [...answer].sort((a, b) => a - b);
}