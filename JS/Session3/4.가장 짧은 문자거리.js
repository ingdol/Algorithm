// 가장 짧은 문자거리
// 한 개의 문자열 s와 문자 t가 주어지면 문자열 s의 각 문자가 문자 t와 떨어진 최소거리를 출
// 력하는 프로그램을 작성하세요.
// ▣ 입력설명
// 첫 번째 줄에 문자열 s와 문자 t가 주어진다. 문자열과 문자는 소문자로만 주어집니다.
// 문자열의 길이는 100을 넘지 않는다.
// ▣ 출력설명
// 첫 번째 줄에 각 문자열 s의 각 문자가 문자 t와 떨어진 거리를 순서대로 출력한다.
// ▣ 입력예제 1
// teachermode e
// ▣ 출력예제 1
// 1 0 1 2 1 0 1 2 2 1 0

function solution(str, t) {
  let res = [];
  let cnt = 1000; // 첫 문자열에 e가 없을 경우 e와의 떨어진 거리를 제대로 측정하지 못하기 때문
  for (let s of str) {
    s === t ? (cnt = 0) : cnt++;
    res.push(cnt);
  }

  cnt = 1000;
  for (let i = str.length - 1; i >= 0; i--) {
    if (t === str[i]) cnt = 0;
    else {
      cnt++;
      res[i] > cnt && (res[i] = cnt);
    }
  }
  return res.join(" ");
}

let str = "ttteachermodetttt";
console.log(solution(str, "e"));
