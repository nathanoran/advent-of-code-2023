import math

all_data = open('day5/almanac.txt', 'r')
almanac: list[str] = all_data.readlines()

class Seed:
    min: int = 0
    max: int = 0

class AlmanacMap:
    destMin: int = 0
    sourceMin: int = 0
    sourceMax: int = 0

rawSeeds = almanac.pop(0)[7:-1:].split(' ')
print(len(rawSeeds))
seeds: list[Seed] = []
for i in range(int(len(rawSeeds) / 2)):
    seed = Seed()
    seed.min = int(rawSeeds.pop(0))
    seed.max = seed.min + int(rawSeeds.pop(0)) - 1
    seeds.append(seed)
print(len(seeds))

almanac.pop(0)

def transformValue(value: int, map: AlmanacMap):
    diff = value - map.sourceMin
    return map.destMin + diff

def transformSeeds(maps: list[AlmanacMap], seeds: list[int]):
    transformedSeeds = []
    while len(seeds) > 0:
        seed = seeds.pop(0)
        print(f'evaluating seed range {seed.min}, {seed.max}')
        for map in maps:
            isMinInRange = seed.min >= map.sourceMin and seed.min <= map.sourceMax
            isMaxInRange = seed.max >= map.sourceMin and seed.max <= map.sourceMax
            isRangeSubsetOfSeed = seed.min < map.sourceMin and seed.max > map.sourceMax

            if isMinInRange and isMaxInRange:
                print(f'entire seed range: {seed.min}, {seed.max} belongs is in this set: {map.sourceMin}, {map.sourceMax}. destination min: {map.destMin}')
                # entire seed stays as one seed
                transformedSeed = Seed()
                transformedSeed.min = transformValue(seed.min, map)
                transformedSeed.max = transformValue(seed.max, map)
                transformedSeeds.append(transformedSeed)
                # adjust seed such that we will know it has been entirely transformed
                seed.min = -1
                seed.max = -1
        
            elif isMinInRange and not isMaxInRange:
                print(f'lower portion of seed range: {seed.min}, {seed.max} belongs is in this set: {map.sourceMin}, {map.sourceMax}. destination min: {map.destMin}')
                # Split lower portion into a transformed seed
                transformedSeed = Seed()
                transformedSeed.min = transformValue(seed.min, map)
                transformedSeed.max = transformValue(map.sourceMax, map)
                transformedSeeds.append(transformedSeed)
                # adjust original seed to to only contain remaining upper values
                seed.min = map.sourceMax + 1

            elif not isMinInRange and isMaxInRange:
                print(f'upper portion of seed range: {seed.min}, {seed.max} belongs is in this set: {map.sourceMin}, {map.sourceMax}. destination min: {map.destMin}')
                # Split upper portion into a transformed seed
                transformedSeed = Seed()
                transformedSeed.min = transformValue(map.sourceMin, map)
                transformedSeed.max = transformValue(seed.max, map)
                transformedSeeds.append(transformedSeed)
                # adjust original seed to to only contain remaining lower values
                seed.max = map.sourceMin - 1

            elif isRangeSubsetOfSeed:
                print(f'inner portion of seed range: {seed.min}, {seed.max} is this set: {map.sourceMin}, {map.sourceMax}. destination min: {map.destMin}')
                # Transform full range of map into a seed, then persist the remaining higher and lower value ranges as separate seeds
                transformedSeed = Seed()
                transformedSeed.min = transformValue(map.sourceMin, map)
                transformedSeed.max = transformValue(map.sourceMax, map)
                transformedSeeds.append(transformedSeed)
                # Add a new seed for the upper values, which we will hit next
                upperSeed = Seed()
                upperSeed.min = map.sourceMax + 1
                upperSeed.max = seed.max
                seeds = [upperSeed] + seeds
                # Update current seed to check the lower values in future maps
                seed.max = map.sourceMin - 1
                

        if seed.min != -1 and seed.max != -1:
            print(f'seed values {seed.min}, {seed.max} were not transformed, so the values persist in the next map')
            transformedSeeds.append(seed)

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

smallestFinalSeed = seeds[0].min
for seed in seeds:
    if seed.min < smallestFinalSeed:
        smallestFinalSeed = seed.min

print(smallestFinalSeed)



