import random, os

def randomizeMasterQuartzLocation(path=None, seed=None):
    if seed:
        random.seed(seed)
    
    quartzFiles = [f for f in os.listdir('input/MSQ/') if os.path.isfile(os.path.join('input/MSQ/', f))]
    quartzList = [f[:-4] for f in quartzFiles]
    random.shuffle(quartzList)
    idList = [int(open('input/MSQ/' + f + '.txt', 'r').readline()) for f in quartzList]
    
    with open('result.txt', 'a') as resultFile:
        resultFile.write('\nQuartz Shuffle Result:\n')
        for quartzFile in quartzFiles:
            with open('input/MSQ/' + quartzFile, 'r') as file:
                data = file.readlines()[1:]
                newQuartzName = quartzList.pop()
                newId = idList.pop()
                resultFile.write(quartzFile[:-4].title() + ' -> ' + newQuartzName.title() + '\n')

                for specific in data:
                    details = specific.split(',')
                    with open(path + details[1].strip(), 'r+b') as location:
                        location.seek(int(details[0]))
                        location.write(newId.to_bytes(2, 'little'))

def buildMasterQuartz(path=None, seed=None, normalize=False, randomizeArts=False, artGainChance=40):
    artsId = {0 : (20, 28),
                1 : (35, 44),
                2 : (50, 58),
                3 : (65, 72),
                4 : (80, 86),
                5 : (95, 101),
                6 : (110, 116)}

    if seed:
        random.seed(seed)
    
    import json
    if normalize:
        fileName = 'MQ_Normalized.json'
    else:
        fileName = 'MQ_Base.json'

    data = json.load(open('input/Files/' + fileName, 'r', encoding='utf-8'))
    
    if randomizeArts:
        for id in data:
            artPool = list()
            for dataId in data[id]['data']:
                masterQuartzData = data[id]['data'][dataId]
                for i in range(2):
                    if random.randint(1, 100) > artGainChance:
                        masterQuartzData['art_' + str(i + 1)] = 65535
                    else:
                        while True:
                            element = random.randint(0, 6)
                            artId = random.randint(artsId[element][0], artsId[element][1])
                            if not artId in artPool:
                                masterQuartzData['art_' + str(i + 1)] = artId
                                artPool.append(artId)
                                break

    __buildMQFromData(path, data)

def __buildMQFromData(path=None, data=None):
    import struct
    stats = ['hp', 'ep', 'str', 'def', 'ats', 'adf', 'spd']
    with open(path + 't_mstqrt.tbl', 'wb') as destination:
        masterQuartzNum = len(data.keys())
        count = masterQuartzNum + 5*masterQuartzNum
        for id in data:
            count += len(data[id]['memo'])
        destination.write(count.to_bytes(2, 'little'))

        for id in data:
            destination.write(b'MasterQuartzBase\x00\x06\x00')
            destination.write(data[id]['id'].to_bytes(2, 'little'))
            destination.write(data[id]['sort_id'].to_bytes(2, 'little'))
            destination.write(data[id]['start_level'].to_bytes(2, 'little'))

            for i in range(5):
                destination.write(b'MasterQuartzData\x00\x40\x00')
                masterQuartzData = data[id]['data'][str(i + 1)]
                destination.write(masterQuartzData['id'].to_bytes(2, 'little'))
                destination.write(masterQuartzData['level'].to_bytes(2, 'little'))

                for stat in stats:
                    destination.write(masterQuartzData[stat].to_bytes(2, 'little'))

                for j in range(6):
                    destination.write(struct.pack('<f', masterQuartzData['effect_' + str(j + 1)]))

                for j in range(2):
                    destination.write(masterQuartzData['art_' + str(j + 1)].to_bytes(2, 'little'))

                for memo in masterQuartzData['memos']:
                    destination.write(memo.to_bytes(2, 'little'))

            for i in range(len(data[id]['memo'])):
                masterQuartzMemo = data[id]['memo'][str(i)]
                text = masterQuartzMemo['text'].encode('utf-8')
                length = 5 + len(text)
                destination.write(b'MasterQuartzMemo\x00')
                destination.write(length.to_bytes(2, 'little'))

                destination.write(masterQuartzMemo['id'].to_bytes(2, 'little'))
                destination.write(masterQuartzMemo['memo_id'].to_bytes(2, 'little'))
                destination.write(text + b'\x00')



if __name__ == "__main__":
    buildMasterQuartz(path='./', randomizeArts=False, normalize=True)