import random, struct

charList = ['rean', 'alisa', 'elliot', 'laura', 'machias', 'emma', 'jusis', 'fie', 'gaius', 'millium', 'crow', 'sara', 'angelica']
craftNum = [5, 4, 5, 4, 4, 5, 4, 4, 4, 4, 4, 3, 3]

def randomize(path, seed=None):
    if seed:
        random.seed(seed)
    with open('input/crafts.txt') as f:
        craftList = f.read().splitlines()
    
    # Assigning Crafts
    magicFile = open(path + "t_magic.tbl", 'r+b')
    resultFile = open('result.txt', 'a')

    resultFile.write('\nCraft Randomizer Result: \n')
    for i in range(13):
        resultFile.write(charList[i].title() + ":\n")
        referenceList = list()
        for k in range(craftNum[i]):
            referenceList.append(list())
        referenceFile = open('input/' + charList[i] + '.txt')
        referenceLines = referenceFile.read().splitlines()
        referenceLevels = referenceLines[0].split(' ')
        for line in referenceLines[1:]:
            temp = line.split(',')
            referenceList[int(temp[0])-1].append(temp[1:])
        
        for j in range(craftNum[i]):
            craft = craftList.pop(random.randrange(len(craftList))).split(',')
            
            magicFile.seek(int(craft[2]))
            magicFile.write(struct.pack('b', i))
            
            magicFile.seek(int(craft[3]))
            magicFile.write(struct.pack('b', ord('0')+j))
            
            magicFile.seek(int(craft[3]) - 14)
            magicFile.write(struct.pack('b', j))

            level = int(referenceLevels[j])
            
            magicFile.seek(int(craft[3]) - 15)
            magicFile.write(struct.pack('b', level))
            
            resultFile.write(craft[0] + ' - Level Learn: ' + str(level) + '\n')
            
            for entry in referenceList[j]:
                scenaFile = open(path + '../../' + entry[0], 'r+b')
                scenaFile.seek(int(entry[1]))
                scenaFile.write(struct.pack('>H', int(craft[1], 16)))
            
        resultFile.write('\n')

if __name__ == "__main__":
    randomize('data/text/dat_us/')