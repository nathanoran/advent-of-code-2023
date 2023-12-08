all_data = open('day5/almanac.txt', 'r')
almanac: list[str] = all_data.readlines()

seeds = almanac.pop(0)[7:-1:].split(' ')
for i in range(len(seeds)):
    seed = seeds.pop(0)
    seeds.append(int(seed))
print(seeds)
almanac.pop(0)

class AlmanacMap:
    destMin: int = 0
    sourceMin: int = 0
    sourceMax: int = 0

def getSourceMin(almanacMap: AlmanacMap):
    return almanacMap.sourceMin

def transformSeeds(maps: list[AlmanacMap], seeds: list[int]):
    transformedSeeds = []
    for seed in seeds:
        seedTransformed = seed
        for map in maps:
            if seed >= map.sourceMin and seed <= map.sourceMax:
                print(f'seed: {seed} belongs is in this set: {map.sourceMin}, {map.sourceMax}. destination min: {map.destMin}')
                diff = seed - map.sourceMin
                seedTransformed = map.destMin + diff

        print('transformed seed:', seedTransformed)
        transformedSeeds.append(seedTransformed)

    if (len(seeds) != len(transformedSeeds)):
        print('MAJOR ERROR TRANSFORMATION FAILED')
    return transformedSeeds

almanacMaps = {
    'seed-to-soil': [],
    'soil-to-fertilizer': [],
    'fertilizer-to-water': [],
    'water-to-light': [],
    'light-to-temperature': [],
    'temperature-to-humidity': [],
    'humidity-to-location': []
}

currentMap = 'seed-to-soil'

for line in almanac:
    line = line[:-1:] # remove new line char
    splitLine = line.split(' ')

    if (len(splitLine) == 2):
        currentMap = splitLine[0]
        print('')
        print(currentMap)
    elif(len(splitLine) == 3):
        mapEntry = AlmanacMap()
        mapEntry.destMin = int(splitLine[0])
        mapEntry.sourceMin = int(splitLine[1])
        range = int(splitLine[2])

        mapEntry.sourceMax = mapEntry.sourceMin + range - 1
        almanacMaps[currentMap].append(mapEntry)
    else:
        seeds = transformSeeds(almanacMaps[currentMap], seeds)

seeds = transformSeeds(almanacMaps[currentMap], seeds)

smallestFinalSeed = seeds[0]
for seed in seeds:
    if seed < smallestFinalSeed:
        smallestFinalSeed = seed

print(smallestFinalSeed)



