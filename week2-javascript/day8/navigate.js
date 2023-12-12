import fs from 'fs';

const pouch = fs.readFileSync('day8/maps.txt', 'utf-8');

const documents = pouch.split(/\r?\n/);

const directions = documents.splice(0, 2)[0].split('');

const maps = {};
documents.forEach((doc) => {
    const key = doc.substring(0, 3);
    const left = doc.substring(7, 10);
    const right = doc.substring(12, 15);
    maps[key] = {
        left,
        right,
    };
});

let currentPosition = 'AAA';
let i = 0;

while (currentPosition !== 'ZZZ') {
    if (directions[i % directions.length] === 'R') {
        currentPosition = maps[currentPosition].right;
    } else {
        currentPosition = maps[currentPosition].left;
    }
    i++;
}

console.log(i);
