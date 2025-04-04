function solution(genres, plays) {
    let answer = [];
    let total_genres = {}
    let genres_dic = {}
    for (let i = 0; i < genres.length; i++) {
        if (total_genres[genres[i]]) total_genres[genres[i]] += plays[i]
        else total_genres[genres[i]] = plays[i]
        
        if(genres_dic[genres[i]]) genres_dic[genres[i]].push([i, plays[i]])
        else genres_dic[genres[i]] = [[i, plays[i]]]
    }
    let sorted_genres = Object.entries(total_genres).sort((a, b) => b[1] - a[1])
    
    for (let name of sorted_genres) {
        let sorted_dic = genres_dic[name[0]].sort((a, b) => b[1] - a[1])
        let max_num = 0
        while (max_num < 2) {
            answer.push(sorted_dic[max_num][0])
            if (sorted_dic.length < 2) break
            max_num++
        }
    }
    return answer;
}