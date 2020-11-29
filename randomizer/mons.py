import random

mainStatArray = ['str', 'def', 'ats', 'adf']
subStatArray = ['dex', 'agi', 'spd']

def randomize(path=None, seed=None, variance=10, randomStat=True, randomEleRes=True, randomAfflictionRes=True, randomUnbalance=True, keepDeathblow=False):
    if seed:
        random.seed(seed)
    
    with open(path + 't_mons.tbl', 'r+b') as file: 
        entries = int.from_bytes(file.read(2), 'little')
        i = 0
        index = 9
        while i < entries - 2:
            file.seek(index)
            length = int.from_bytes(file.read(2), 'little')
            file.seek(index + 2)

            count = 0
            while count < 3:
                char = file.read(1)
                if char == b'\x00':
                    count += 1
            file.read(42)

            newHead = file.tell()

            if randomStat:
                includeATS = True
                mainStatSum = 0
                newMainStat = [0]*4
                mainStatMultiplier = [0]*4
                for j in range(4):
                    mainStatMultiplier[j] = random.randint(10, variance)
                    number =  int.from_bytes(file.read(2), 'little')
                    if number == 0 and j == 2:
                        includeATS = False
                    mainStatSum += number * mainStatMultiplier[j]
                while mainStatSum > 0:
                    statIndex = random.randint(0, 3)
                    while (not includeATS) and statIndex == 2:
                        statIndex = random.randint(0,3)
                    newMainStat[statIndex] += 1
                    mainStatSum -= 1

                file.seek(newHead)
                for j in range(4):
                    newMainStat[j] = int(newMainStat[j] / mainStatMultiplier[j])
                    file.write(newMainStat[j].to_bytes(2, 'little'))


            if randomEleRes:
                file.seek(newHead + 18)
                for j in range(7):
                    newEleRes = random.randrange(0, 201, 5)
                    file.write(newEleRes.to_bytes(1, 'little'))

            if randomAfflictionRes:
                file.seek(newHead + 18 + 7)
                for j in range(15):
                    if keepDeathblow:
                        if j == 7 or j == 10 or j == 13:
                            file.seek(file.tell() + 1)
                            continue
                    newAfflictionRes = random.randrange(0, 201, 5)
                    file.write(newAfflictionRes.to_bytes(1, 'little'))

            if randomUnbalance:
                file.seek(newHead + 18 + 7 + 15)
                unbalanceNum = [0, 10, 50, 100, 200, 400]
                for j in range(4):
                    file.write(random.choice(unbalanceNum).to_bytes(2, 'little'))
            index += length + 9
            i += 1

if __name__ == "__main__":
    randomize('data/text/dat_us/', variance=60, randomStat=False, randomEleRes=False, randomAfflictionRes=True, randomUnbalance=False, keepDeathblow=True)