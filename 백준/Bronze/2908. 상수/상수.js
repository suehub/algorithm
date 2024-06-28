let fs = require("fs");
let [n, m] = fs.readFileSync("/dev/stdin").toString().split(" ");

n = Number(n.charAt(2) + n.charAt(1) + n.charAt(0));
m = Number(m.charAt(2) + m.charAt(1) + m.charAt(0));

console.log(Math.max(n, m));
