function solution(s){
    let pLen = 0;
    let yLen = 0;
    
    for(let i = 0; i < s.length; i++) {
        let low = s[i].toLowerCase()
        if(low === 'p') pLen += 1
        else if(low === 'y') yLen += 1
    }

    return pLen === yLen ? true : false;
}