let input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
input.map((text) => {
  console.log(text);
});