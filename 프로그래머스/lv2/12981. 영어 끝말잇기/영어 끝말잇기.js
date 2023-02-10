function solution(n, words) {
    const answer = [0, 0];
    let wordStack = []
    for(let i = 0; i < words.length; i++) {
        if(!wordStack.length || !wordStack.includes(words[i])) wordStack.push(words[i])
        else return [i%n+1, Math.floor(i/n)+1]
        if(i > 0 && wordStack[i-1].charAt(wordStack[i-1].length-1) !== wordStack[i].charAt(0)) return [i%n+1, Math.floor(i/n)+1]
    }
    return answer;
}