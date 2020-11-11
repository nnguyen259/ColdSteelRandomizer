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


if __name__ == "__main__":
    randomizeMasterQuartzLocation(path='D:\SteamLibrary\steamapps\common\Trails of Cold Steel/')