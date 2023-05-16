function solution(id_pw, db) {
   const [userId, userPw] = id_pw
   for(const [dbId, dbPw] of db) {
       if(userId === dbId && userPw === dbPw) return 'login'
       else if(userId === dbId && userPw !== dbPw) return 'wrong pw'
   }
    return 'fail'
}