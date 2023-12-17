import fs from 'fs';
import util from 'util';

const fullMap = fs.readFileSync('day10/pipe-map.txt', 'utf-8');

const mapLines = fullMap.split(/\r?\n/);

const rawMap = mapLines.map((line) => line.split(''));

const start = {
    i: -1,
    j: -1
}

const northConnectors = ['|', 'S', 'L', 'J'];
const eastConnectors = ['-', 'S', 'L', 'F'];
const southConnectors = ['|', 'S', '7', 'F'];
const westConnectors = ['-', 'S', '7', 'J'];

const parsedMap = [];

let i = 0;
while (i < rawMap.length) {
    const parsedRow = []
    let j = 0;
    while (j < rawMap[i].length) {
        const pipe = rawMap[i][j];
        const adjacents = [];
        if (pipe === 'S') {
            start.i = i;
            start.j = j;
        }

        // North Exit
        if (
            northConnectors.includes(rawMap[i][j]) &&
            rawMap[i-1] !== undefined &&
            rawMap[i-1][j] !== undefined &&
            southConnectors.includes(rawMap[i-1][j])
        ) {
            // console.log('detected adjacent pipe to the north!');
            adjacents.push({
                row: i-1,
                column: j
            });
        }
        if (
            eastConnectors.includes(rawMap[i][j]) &&
            rawMap[i][j+1] !== undefined &&
            westConnectors.includes(rawMap[i][j+1])
        ) {
            // console.log('detected adjacent pipe to the east!');
            adjacents.push({
                row: i,
                column: j+1
            });
        }
        if (
            southConnectors.includes(rawMap[i][j]) &&
            rawMap[i+1] !== undefined &&
            rawMap[i+1][j] !== undefined &&
            northConnectors.includes(rawMap[i+1][j])
        ) {
            // console.log('detected adjacent pipe to the south!');
            adjacents.push({
                row: i+1,
                column: j
            });
        }
        if (
            westConnectors.includes(rawMap[i][j]) &&
            rawMap[i][j-1] !== undefined &&
            eastConnectors.includes(rawMap[i][j-1])
        ) {
            // console.log('detected adjacent pipe to the west!');
            adjacents.push({
                row: i,
                column: j-1
            });
        }
        parsedRow.push({
            pipe,
            distance: undefined,
            visited: false,
            adjacents,
            position: [i, j],
        });
        j++;
    }
    parsedMap.push(parsedRow);
    i++;
}

let maxDistance = -1;
const evaluationQueue = [{
    row: start.i,
    column: start.j,
    distance: 0
}];

while (evaluationQueue.length > 0) {
    const [{ row: i, column: j, distance }] = evaluationQueue.splice(0, 1);
    const currentPipe = parsedMap[i][j];
    if (!currentPipe.visited) {
        currentPipe.distance = distance;
        currentPipe.visited = true;
        maxDistance = Math.max(maxDistance, currentPipe.distance);
        evaluationQueue.push(...currentPipe.adjacents.map((adj) => ({
            row: adj.row,
            column: adj.column,
            distance: distance + 1,
        })));
    }
    // console.log('evaluationQueue:',evaluationQueue.map(({row: n, column: o}) => parsedMap[n][o]));
}

console.log('Furthest Distance in loop:', maxDistance);
console.log('');

// Part 2 Solution
const resultMapVisual = [];
let containedArea = 0;
for (i = 0; i < parsedMap.length; i++) {
    resultMapVisual.push([]);
    let isCurrentlyInside = false;
    let lastFBendValid = false;
    let lastLBendValid = false;
    for (let j = 0; j < parsedMap[i].length; j++) {
        const pipe = parsedMap[i][j];
        if (pipe.visited) {
            if (pipe.pipe === '|') {
                isCurrentlyInside = !isCurrentlyInside;
                lastFBendValid = false;
                lastLBendValid = false;
            } else if (pipe.pipe === 'F') {
                lastFBendValid = true;
                lastLBendValid = false;
            } else if (pipe.pipe === 'L') {
                lastFBendValid = false;
                lastLBendValid = true;
            } else if (pipe.pipe === 'J' && lastFBendValid) {
                isCurrentlyInside = !isCurrentlyInside;
                lastFBendValid = false;
            } else if (pipe.pipe === '7' && lastLBendValid) {
                isCurrentlyInside = !isCurrentlyInside;
                lastLBendValid = false;
            } else if (!(pipe.pipe === '-' || pipe.pipe === 'S')) { // Or 'S' is added since I know that 'S' in my input is equivalent to a '-'
                lastFBendValid = false;
                lastLBendValid = false;
            }
            resultMapVisual[i].push(pipe.pipe);
        } else {
            lastFBendValid = false;
            lastLBendValid = false;
            if (isCurrentlyInside) {
                resultMapVisual[i].push('I');
                containedArea++;
            } else {
                resultMapVisual[i].push('O');
            }
            
        }
    }
}

resultMapVisual.forEach((line) => console.log(line.join('')));
console.log('');

console.log('Area contained by the loop:', containedArea);
