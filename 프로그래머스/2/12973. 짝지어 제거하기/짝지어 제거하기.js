function solution(s)
{
    let str = [];
    
    for(let i = 0; i < s.length; i++) {
        if (!str.length || str[str.length - 1] !== s[i]) str.push(s[i]) 
        else str.pop(s[i])
    }
    return str.length === 0 ? 1 : 0
}