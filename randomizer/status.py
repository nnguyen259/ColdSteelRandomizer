import random, struct

statArray = ['hp', 'str', 'def', 'ats', 'adf', 'dex', 'agi', 'spd']
charList = ['rean', 'alisa', 'elliot', 'laura', 'machias', 'emma', 'jusis', 'fie', 'gaius', 'millium', 'crow', 'sara', 'angelica']

def randomizeBase(path=None, seed=None, variance=10, increaseBase=False):
    if seed:
        random.seed(seed)
    with open(path + 't_status.tbl', 'r+b') as file, open('result.txt', 'a') as resultfile:
        resultfile.write('\nBase Stat Result: ' + str(statArray) + '\n')
        
        for i in range(13):
            startOffset = 2 + (i*67 + 13)
            sum = 0
            statMultiplier = [0]*8
            for j in range(8):
                statOffset = j*6
                offset = startOffset + statOffset
                file.seek(offset)
                statMultiplier[j] = random.randint(10, variance)
                statValue = int.from_bytes(file.read(2), 'little')
                if j == 0:
                    statValue /= 10
                if j == 5:
                    statValue *= 2
                if j == 6:
                    statValue *= 3
                sum += statValue * statMultiplier[j]
            
            newStatArray = [0]*8
            while sum > 0:
                index = random.randint(0, 7)
                newStatArray[index] += 1
                sum -= 1
            newStatArray[0] *= 10
            newStatArray[5] = int(newStatArray[5] / 2)
            newStatArray[6] = int(newStatArray[6] / 3)
            
            
            for j in range(8):
                statOffset = j*6
                offset = startOffset + statOffset
                file.seek(offset)
                newStatArray[j] = int(newStatArray[j] / statMultiplier[j])
                if increaseBase:
                    if j == 0:
                        newStatArray[j] += 300
                    if j == 2:
                        newStatArray[j] += 30
                file.write(newStatArray[j].to_bytes(2, 'little'))
            resultfile.write(charList[i].title() + ': ' + str(newStatArray) + '\n')


def randomizeGrowth(path=None, seed=None, variance=0):
    if seed:
        random.seed(seed)
    with open(path + 't_status.tbl', 'r+b') as file, open('result.txt', 'a') as resultfile:
        resultfile.write('\nStat Growth Result: ' + str(statArray) + '\n')
        
        for i in range(13):
            startOffset = 2 + (i*67 + 15)
            sum = 0
            growthMultiplier = [0]*8
            for j in range(8):
                statOffset = j*6
                offset = startOffset + statOffset
                file.seek(offset)
                growthMultiplier[j] = random.randint(10, variance)
                statValue = struct.unpack('<f', file.read(4))[0]
                if j == 0:
                    statValue /= 20
                if j == 5 or j == 6:
                    statValue *= 50
                if j == 7:
                    statValue *= 10
                sum += statValue * growthMultiplier[j]
            sum = int(sum*variance)
            
            newStatArray = [0]*8
            while sum > 0:
                index = random.randint(0, 7)
                newStatArray[index] += 1
                sum -= 1

            for j in range(8):
                newStatArray[j] /= variance
            newStatArray[0] *= 20
            newStatArray[5] /= 50
            newStatArray[6] /= 50
            newStatArray[7] /= 10
            
            for j in range(8):
                statOffset = j*6
                offset = startOffset + statOffset
                file.seek(offset)
                newStatArray[j] = newStatArray[j] / growthMultiplier[j]
                file.write(struct.pack('<f', newStatArray[j]))
            resultfile.write(charList[i].title() + ': ' + str(newStatArray) + '\n')

if __name__ == "__main__":
    randomizeGrowth('data/text/dat_us/', variance=40)