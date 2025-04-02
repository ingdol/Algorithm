function solution(want, number, discount) {
    let wantObj = {}
    for (let i = 0; i < want.length; i++) {
        wantObj[want[i]] = number[i]
    }
    
    let answer = 0
    
    for (let i = 0; i < discount.length - 9; i++) {
        let discount10d = {}
        
        for (let j = i; j < i + 10; j++) {
          if (wantObj[discount[j]]) {
            discount10d[discount[j]] = (discount10d[discount[j]] || 0) + 1;
          }
        }

        if (isShallowEqual(discount10d, wantObj)) {
            answer += 1
        }
    }
    return answer;
}

function isShallowEqual(object1, object2) {
    const objKey1 = Object.keys(object1)
    const objKey2 = Object.keys(object2)

    if (objKey1.length !== objKey2.length) return false
    
    for (const key of objKey1) {
        if (object1[key] !== object2[key]) {
            return false
        }
    }
    return true
}