const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split(' ');

const a = input[0];
const b = input[1];

if (a.length < b.length) {
    console.log(0);
} else {
    if (a === b) {
        console.log(a.split('8').length - 1);
    } else {
        let cnt = 0;
        for (let i = 0; i < a.length; i++) {
            if (a[i] === b[i]) {
                if (a[i] === '8') {
                    cnt++;
                }
                continue;
            } else {
                break;
            }
        }
        console.log(cnt);
    }
}
