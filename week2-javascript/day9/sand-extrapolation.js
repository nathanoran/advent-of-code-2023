import fs from 'fs';

const allData = fs.readFileSync('day9/sand-history.txt', 'utf-8');

const histories = allData.split(/\r?\n/);

const analyzeHistory = (history) => {
    if (history.some((value) => value !== 0)) {
        const analyzedHistory = [];
        for (let i = 0; i < history.length - 1; i++) {
            analyzedHistory.push(history[i + 1] - history[i]);
        }
        return [...analyzeHistory(analyzedHistory), analyzedHistory];
    } else {
        return [];
    }
}

let positivePredictionAcc = 0;
let negativePredictionAcc = 0;
for (const history of histories) {
    const historicalValues = history.split(' ').map(valueStr => parseInt(valueStr));

    const historicalAnalysis = [...analyzeHistory(historicalValues), historicalValues];

    let positivePrediction = 0;
    let negativePrediction = 0;
    historicalAnalysis.forEach((analysis, i) => {
        if (i > 0) {
            positivePrediction += analysis[analysis.length - 1];
            negativePrediction = analysis[0] - negativePrediction;
        }
    });
    positivePredictionAcc += positivePrediction;
    negativePredictionAcc += negativePrediction;
}
console.log(positivePredictionAcc);
console.log(negativePredictionAcc);
