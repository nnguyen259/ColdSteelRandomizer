import random, csv

charList = ['rean', 'alisa', 'elliot', 'laura', 'machias', 'emma', 'jusis', 'fie', 'gaius', 'millium', 'crow', 'sara', 'angelica']
craftNum = [5, 4, 5, 4, 4, 5, 4, 4, 4, 4, 4, 3, 3]

def randomize(path, seed=None, original=False):
    if seed:
        random.seed(seed)
    with open('input/Crafts/crafts.csv', newline='') as craftFile, open('input/Files/Magic.csv', newline='') as magicFile, open('result.txt', 'a') as resultFile:
        craftList = list(csv.reader(craftFile))
        magicList = list(csv.reader(magicFile))

        if original:
            with open('input/Crafts/original.csv', newline='') as originalFile:
                originalList = list(csv.reader(originalFile))
                craftList.extend(originalList)
        fullList = list()

        random.shuffle(craftList)

        resultFile.write('\nCraft Randomizer Result: \n')
        for i in range(13):
            resultFile.write(charList[i].title() + ":\n")
            levels = list()
            ids = list()
            with open('input/Crafts/' + charList[i] + '.txt', 'r') as referenceFile:
                lines = referenceFile.readlines()
                levels = lines[0].strip().split(' ')
                ids = lines[1].strip().split(' ')

            for j in range(craftNum[i]):
                craft = craftList.pop()
                craft[0] = int(ids[j])
                craft[1] = i
                craft[-3] = 'AniBtlCraft0' + str(j)
                craft[-4] = j
                craft[-5] = int(levels[j])
                magicList.append(craft)
                resultFile.write(craft[-2] + ', Level: ' + str(craft[-5]) + '\n')
                
            resultFile.write('\n')
        
        headers = magicList[0]

        for i in range(len(magicList) - 1):
            magic = {}
            data = magicList[i + 1]
            for j in range(len(data)):
                magic[headers[j]] = data[j]
            fullList.append(magic)

        testData = list(sorted(fullList, key=lambda item: int(item['id'])))

        __buildMagic(path=path, data=testData)


def __buildMagic(path=None, data=None):
    field_names = ['id', 'char_restriction', 'flags', 'category', 'type', 'element', 'targetting_type', 'targetting_range', 'targetting_size',
                    'effect1_id', 'effect1_data1', 'effect1_data2', 'effect2_id', 'effect2_data1', 'effect2_data2',
                    'cast_delay', 'recovery_delay', 'cost', 'unbalance_bonus', 'level', 'sort_id','animation', 'name', 'description']
    with open(path + '/data/text/dat_us/t_magic.tbl', 'wb') as destination:
        entry_num = len(data)

        destination.write(entry_num.to_bytes(2, 'little'))

        for magic in data:
            length = len(magic['flags'].encode('utf-8')) + len(magic['animation'].encode('utf-8')) + len(magic['name'].encode('utf-8')) + \
                    len(magic['description'].replace('\r', '').encode('utf-8')) + 32

            destination.write(b'magic\x00')
            destination.write(length.to_bytes(2, 'little'))

            destination.write(int(magic['id']).to_bytes(2, 'little'))
            destination.write(int(magic['char_restriction']).to_bytes(2, 'little'))

            destination.write(magic['flags'].encode('utf-8') + b'\x00')

            destination.write(int(magic['category']).to_bytes(1, 'little'))
            destination.write(int(magic['type']).to_bytes(1, 'little'))
            destination.write(int(magic['element']).to_bytes(1, 'little'))

            destination.write(int(magic['targetting_type']).to_bytes(1, 'little'))
            destination.write(int(magic['targetting_range']).to_bytes(1, 'little'))
            destination.write(int(magic['targetting_size']).to_bytes(1, 'little'))

            destination.write(int(magic['effect1_id']).to_bytes(1, 'little'))
            destination.write(int(magic['effect1_data1']).to_bytes(2, 'little'))
            destination.write(int(magic['effect1_data2']).to_bytes(2, 'little'))
            
            destination.write(int(magic['effect2_id']).to_bytes(1, 'little'))
            destination.write(int(magic['effect2_data1']).to_bytes(2, 'little'))
            destination.write(int(magic['effect2_data2']).to_bytes(2, 'little'))

            destination.write(int(magic['cast_delay']).to_bytes(1, 'little'))
            destination.write(int(magic['recovery_delay']).to_bytes(1, 'little'))
            destination.write(int(magic['cost']).to_bytes(2, 'little'))

            destination.write(int(magic['unbalance_bonus']).to_bytes(1, 'little'))
            destination.write(int(magic['level']).to_bytes(1, 'little'))
            destination.write(int(magic['sort_id']).to_bytes(2, 'little'))

            destination.write(magic['animation'].encode('utf-8') + b'\x00')
            destination.write(magic['name'].encode('utf-8') + b'\x00')
            destination.write(magic['description'].replace('\r', '').encode('utf-8') + b'\x00')

if __name__ == "__main__":
    randomize('./')