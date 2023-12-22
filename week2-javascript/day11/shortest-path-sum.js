import fs from 'fs';
import dotenv from 'dotenv';
dotenv.config({
    path: 'day11/.env',
});

const fullMap = fs.readFileSync('day11/galaxy-map.txt', 'utf-8');

const mapLines = fullMap.split(/\r?\n/);

const rawMap = mapLines.map((line) => line.split(''));

const EXPANSION_MULTIPLIER = (process.env.EXPANSION_DISTANCE || 2) - 1;

const discoveredGalaxies = [];
const galaxyColumns = new Set([]);
const galaxyRows = new Set([]);
const noGalaxyRows = new Set([]);
const noGalaxyColumns = new Set([]);

for (let i = 0; i < rawMap.length; i++) {
    const mapLine = rawMap[i];
    for (let j = 0; j < mapLine.length; j++) {
        if (mapLine[j] === '#') {
            discoveredGalaxies.push({
                row: i,
                column: j,
            });
            noGalaxyRows.delete(i);
            noGalaxyColumns.delete(j);
            galaxyRows.add(i);
            galaxyColumns.add(j);
        } else {
            if (!galaxyRows.has(i)) {
                noGalaxyRows.add(i);
            }
            if (!galaxyColumns.has(j)) {
                noGalaxyColumns.add(j);
            }
        }
    }
}

// console.debug('Rows with no galaxies:', noGalaxyRows);
// console.debug('Columns with no galaxies:', noGalaxyColumns);

let shortestDistanceSum = 0;
discoveredGalaxies.forEach((galaxyA, i) => {
    const remainingGalaxies = discoveredGalaxies.slice(i+1);
    remainingGalaxies.forEach((galaxyB) => {
        // console.debug(`measuring distance between galaxy at [${galaxyA.row}, ${galaxyA.column}] to galaxy at [${galaxyB.row}, ${galaxyB.column}]`)
        const observedVerticalDistance = Math.abs(galaxyB.row - galaxyA.row);
        const observedHorizontalDistance = Math.abs(galaxyB.column - galaxyA.column);
        const verticalExpansionDistance = Array.from(noGalaxyRows.values()).filter((row) => {
            const smallestRow = Math.min(galaxyA.row, galaxyB.row);
            const largestRow = Math.max(galaxyA.row, galaxyB.row);
            return row > smallestRow && row < largestRow;
        }).length;
        const horizontalExpansionDistance = Array.from(noGalaxyColumns.values()).filter((column) => {
            const smallestColumn = Math.min(galaxyA.column, galaxyB.column);
            const largestColumn = Math.max(galaxyA.column, galaxyB.column);
            return column > smallestColumn && column < largestColumn;
        }).length;

        const shortestDistance = observedVerticalDistance + observedHorizontalDistance + ((verticalExpansionDistance + horizontalExpansionDistance) * EXPANSION_MULTIPLIER);
        // console.debug('shortest distance:', shortestDistance)
        shortestDistanceSum += shortestDistance;
    });
});

console.log('shortestDistanceSum:', shortestDistanceSum);
