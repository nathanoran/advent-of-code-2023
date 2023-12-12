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

const navigate = (start, end) => {
    let currentPosition = start;
    let i = 0;

    while (i === 0 || !currentPosition.match(end)) {
        // console.debug(`Current Position: ${currentPosition}\nDirection: ${directions[i % directions.length]}\nMap: (L: ${maps[currentPosition].left}, R: ${maps[currentPosition].right})`);
        if (directions[i % directions.length] === 'R') {
            currentPosition = maps[currentPosition].right;
        } else {
            currentPosition = maps[currentPosition].left;
        }
        i++;
    }

    return {
        finalPosition: currentPosition,
        steps: i
    }
}

const primeFactorization = (value) => {
    const primes = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997,1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069
    ];
    const primeFactors = {};

    const primesReversed = primes.reverse();

    let currentFactor = value
    while (!primes.includes(currentFactor) && currentFactor > 1) {
        primesReversed.forEach((prime) => {
            while (currentFactor % prime === 0) {
                // console.log(currentFactor);
                if (primeFactors[prime] === undefined) {
                    primeFactors[prime] = 1;
                } else {
                    primeFactors[prime]++;
                }
                currentFactor = currentFactor / prime;
            }
        });
    }
    return primeFactors;
}

const {steps: humanNavSteps} = navigate('AAA', 'ZZZ');

console.log(`Human/Camel Navigation (part 1) tooks ${humanNavSteps} steps`);

const startingPositions = Object.keys(maps).filter((key) => key.endsWith('A'));

const lcmPrimeFactors = startingPositions.reduce((prev, position) => {
    const { steps } = navigate(position, /(([A-Z][A-Z]Z))/);
    const primeFactors = primeFactorization(steps);
    Object.entries(primeFactors).forEach(([prime, count]) => {
        if (prev[prime] === undefined) {
            prev[prime] = count;
        } else {
            prev[prime] = Math.max(prev[prime], count);
        }
    });
    return prev;
}, {})

console.log(lcmPrimeFactors);

const lcm = Object.entries(lcmPrimeFactors).reduce((prev, [primeStr, count]) => {
    for (let i = 0; i < count; i++) {
        prev = prev * parseInt(primeStr);
    }
    return prev;
}, 1)

console.log(`Ghost Navigation (part 2) tooks ${lcm} steps`);
