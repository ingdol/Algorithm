let input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
input.map((text) => {
  console.log(text);
});