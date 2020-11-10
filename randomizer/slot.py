import random

charList = ['rean', 'alisa', 'elliot', 'laura', 'machias', 'emma', 'jusis', 'fie', 'gaius', 'millium', 'crow', 'sara', 'angelica']

def randomizeEP(path=None, seed=None, randomizeBase=True, randomizeGrowth=True):
    if seed:
        random.seed(seed)
    with open(path + 't_slot.tbl', 'r+b') as file, open('result.txt', 'a') as resultfile:
        resultfile.write('\nEP Randomizer Result\n\n')
        for i in range(13):
            resultfile.write(charList[i].title() + ':\n')
            startOffset = 2 + i*29 + 11
            if randomizeBase:
                file.seek(startOffset)
                newEP = random.randrange(0, 201, 5)
                file.write(newEP.to_bytes(2, 'little'))
                resultfile.write('Base EP: ' + str(newEP) + '\n')
            if randomizeGrowth:
                file.seek(startOffset + 2)
                growthArray = [0] * 8
                for j in range(8):
                    growthArray[j] = random.randrange(0, 201, 5)
                growthArray.sort()
                for j in range(8):
                    file.write(growthArray[j].to_bytes(2, 'little'))
                resultfile.write('EP Growth: ' + str(growthArray) + '\n')
            resultfile.write('\n')

if __name__ == "__main__":
    randomizeEP('data/text/dat_us/')