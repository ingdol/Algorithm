function solution(id_list, report, k) {
    let answer = [];
    let report_list = {}
    let get_reported_list = {}
    
    for (let id of id_list) {
        report_list[id] = []
        get_reported_list[id] = 0
    }
    
    for (let id of report) {
        let id_arr = id.split(' ')
        if(!report_list[id_arr[0]].includes(id_arr[1])) {
            report_list[id_arr[0]].push(id_arr[1])
            get_reported_list[id_arr[1]]++
        }
    }
    for(let id of id_list) {
        let cnt = 0
        for(let name of report_list[id]) {
            if(get_reported_list[name] >= k) cnt++
        }
        answer.push(cnt)
    }
    return answer;
}