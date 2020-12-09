import random, itertools, csv

def randomize(path=None, seed=None, mode=0):
    if seed:
        random.seed(seed)

    items = {}
    maps = {}

    with open('input/Chests/items.txt', newline='', encoding='utf-8') as itemsFile, open('input/Chests/maps.txt', newline='', encoding='utf-8') as mapsFile:
        itemList = list(csv.reader(itemsFile))
        mapList = list(csv.reader(mapsFile))

        for item in itemList:
            items[item[1]] = item[0]
        
        for map in mapList:
            if map[0] and not map[1].endswith('Unused'):
                maps[map[0]] = map[1]
    
    pools = list()
    with open('input/Chests/normal.txt', 'r') as normalChest, open('input/Chests/rare.txt', 'r') as rareChest, open('input/Chests/monster.txt', 'r') as monsterChest:
        normal = normalChest.readlines()
        rare = rareChest.readlines()
        monster = monsterChest.readlines()

        if mode == 0:
            pools.append(normal)
            pools.append(rare)
            pools.append(monster)
        elif mode == 1:
            pools.append(normal)
            pools.append(list(itertools.chain(rare, monster)))
        else:
            pools.append(list(itertools.chain(normal, rare, monster)))

    for pool in pools:
        chestItems = list()
        mapFiles = list()
        offsets = list()

        for chest in pool:
            chest = chest.strip()
            chunks = chest.split(',')
            mapFiles.append(chunks[0])
            chestItems.append(chunks[1])
            offsets.append(chunks[2:])
        random.shuffle(chestItems)
        for i in range(len(mapFiles)):
            with open('result.txt', 'a') as resultFile, open(path + mapFiles[i] + '.dat', 'r+b') as mapFile:
                resultFile.write('\n' + maps[mapFiles[i]] + ': ' + items[chestItems[i]])
                for offset in offsets[i]:
                    mapFile.seek(int(offset))
                    mapFile.write(int(chestItems[i]).to_bytes(2, 'little'))

if __name__ == "__main__":
    randomize(path='./data/scripts/scena/dat_us/', mode=2)