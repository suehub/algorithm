// 그룹 단어인지 체크하는 함수
function check(data) {
  let setData = new Set(data[0]);
  for (let i = 1; i < data.length; i++) {
    // 오른쪽 단어와 다르다면
    if (data[i] != data[i - 1]) {
      // 이미 등장한 적 있는 알파벳이라면
      if (setData.has(data[i])) return false;
      else setData.add(data[i]);
    } else {
      setData.add(data[i]);
    }
  }
  return true;
}

let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let n = Number(input[0]);
let cnt = 0;

for (let i = 1; i <= n; i++) {
  if (check(input[i])) cnt += 1;
}

console.log(cnt);
