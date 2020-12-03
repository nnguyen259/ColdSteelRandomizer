import random, csv

subStatArray = ['dex', 'agi', 'spd']

def randomize(path=None, seed=None, variance=10, randomStat=True, randomEleRes=True, randomAfflictionRes=True, randomUnbalance=True, keepDeathblow=False, increaseSepith=False, increaseMass=False, increaseExp=False):
    if seed:
        random.seed(seed)

    if randomEleRes:
        inputFile = 'Mons_Ele.csv'
    else:
        inputFile = 'Mons_Normal.csv'

    monsData = list(csv.DictReader(open('input/Files/' + inputFile, newline='', encoding='utf-8')))

    for mons in monsData:
        if randomStat:
            mainStatArray = ['str', 'def', 'ats', 'adf']
            includeATS = True
            mainStatSum = 0
            newMainStat = [0]*4
            mainStatMultiplier = [0]*4
            for j in range(4):
                mainStatMultiplier[j] = random.randint(10, variance)
                number = int(mons[mainStatArray[j]])
                if number == 0 and j == 2:
                    includeATS = False
                mainStatSum += number * mainStatMultiplier[j]
            while mainStatSum > 0:
                statIndex = random.randint(0, 3)
                while (not includeATS) and statIndex == 2:
                    statIndex = random.randint(0,3)
                newMainStat[statIndex] += 1
                mainStatSum -= 1

            for j in range(4):
                newMainStat[j] = int(newMainStat[j] / mainStatMultiplier[j])
                mons[mainStatArray[j]] = newMainStat[j]

        if randomEleRes:
            elementResList = ['earth_res', 'water_res', 'fire_res', 'wind_res', 'time_res', 'space_res', 'mirage_res']
            for eleRes in elementResList:
                mons[eleRes] = random.randrange(0, 201, 5)

        if randomAfflictionRes:
            afflictionResList = ['poison', 'seal', 'mute', 'blind', 'sleep',
                                    'burn', 'freeze', 'petrify', 'faint', 'confuse', 
                                    'deathblow', 'nightmare', 'delay', 'vanish', 'stat_down']
            if keepDeathblow:
                afflictionResList.remove('petrify')
                afflictionResList.remove('deathblow')
                afflictionResList.remove('vanish')
            for afflictionRes in afflictionResList:
                mons[afflictionRes] = random.randrange(0, 201, 5)

        if randomUnbalance:
            unbalanceList = ['slash', 'thrust', 'pierce', 'strike']
            unbalanceNum = [0, 10, 50, 100, 200, 400]
            for unbalance in unbalanceList:
                mons[unbalance] = random.choice(unbalanceNum)

        if increaseSepith:
            sepithList = ['earth', 'water', 'fire', 'wind', 'time', 'space', 'mirage']
            for sepith in sepithList:
                oldValue = int(mons[sepith])
                newValue = 3 * oldValue
                if newValue > 255:
                    newValue = 255
                mons[sepith] = newValue

        if increaseMass:
            oldValue = int(mons['mass'])
            newValue = 3 * oldValue
            if newValue > 255:
                newValue = 255
            mons['mass'] = newValue

        if increaseExp:
            oldValue = int(mons['exp'])
            newValue = 3 * oldValue
            if newValue > 65535:
                newValue = 65535
            mons['exp'] = newValue
    
    __buildMonsFromData(path, monsData)

def __buildMonsFromData(path=None, data=None):
    import struct
    statusText = ['enemy_script', 'texture', 'model']
    statusFloatBlock = ['unkn_float1', 'unkn_float2', 'unkn_float3', 'unkn_float4', 'unkn_float5']
    statusStatBlock = ['str', 'def', 'ats', 'adf', 'dex', 'agi', 'spd', 'move', 'exp']
    statusElementalAliment = ['earth_res', 'water_res', 'fire_res', 'wind_res', 'time_res', 'space_res', 'mirage_res', 'poison', 'seal', 'mute', 'blind', 'sleep',
                    'burn', 'freeze', 'petrify', 'faint', 'confuse', 'deathblow', 'nightmare', 'delay', 'vanish', 'stat_down']
    statusUnbalance = ['slash', 'thrust', 'pierce', 'strike']
    statusSepith = ['earth', 'water', 'fire', 'wind', 'time', 'space', 'mirage', 'mass']
    statusText2 = ['flag', 'name', 'desc']
    reviseFields = ['mult1', 'mult2', 'mult3', 'mult4', 'mult5', 'mult6']
    with open('input/Files/Mons_Revise.csv', newline='') as charFile, open(path + 't_mons.tbl', 'wb') as destination:
        charReader = list(csv.DictReader(charFile))
        entry_num = len(data) + len(charReader)

        destination.write(entry_num.to_bytes(2, 'little'))

        for status in data:
            length = len(status['enemy_script'].encode('utf-8')) + len(status['texture'].encode('utf-8')) + len(status['model'].encode('utf-8')) + len(status['flag'].encode('utf-8')) + len(status['name'].encode('utf-8')) + len(status['desc'].encode('utf-8')) + 118

            destination.write(b'status\x00')
            destination.write(length.to_bytes(2, 'little'))

            for text in statusText:
                destination.write(status[text].encode('utf-8'))
                destination.write(b'\x00')
            
            for unknFloat in statusFloatBlock:
                destination.write(struct.pack('<f', float(status[unknFloat])))

            destination.write(int(status['unkn_short1']).to_bytes(2, 'little'))
            destination.write(int(status['unkn_short2']).to_bytes(2, 'little'))
            destination.write(int(status['unkn_byte']).to_bytes(1, 'little'))
            destination.write(int(status['level']).to_bytes(1, 'little'))

            destination.write(int(status['max_hp']).to_bytes(4, 'little'))
            destination.write(int(status['start_hp']).to_bytes(4, 'little'))
            destination.write(int(status['max_ep']).to_bytes(2, 'little'))
            destination.write(int(status['start_ep']).to_bytes(2, 'little'))
            destination.write(int(status['max_cp']).to_bytes(2, 'little'))
            destination.write(int(status['start_cp']).to_bytes(2, 'little'))

            for stat in statusStatBlock:
                destination.write(int(status[stat]).to_bytes(2, 'little'))

            for element in statusElementalAliment:
                destination.write(int(status[element]).to_bytes(1, 'little'))

            for unbalance in statusUnbalance:
                destination.write(int(status[unbalance]).to_bytes(2, 'little'))

            for sepith in statusSepith:
                destination.write(int(status[sepith]).to_bytes(1, 'little'))

            destination.write(int(status['drop1_id']).to_bytes(2, 'little'))
            destination.write(int(status['drop1_chance']).to_bytes(1, 'little'))
            destination.write(int(status['drop2_id']).to_bytes(2, 'little'))
            destination.write(int(status['drop2_chance']).to_bytes(1, 'little'))

            destination.write(struct.pack('<f', float(status['unkn_float6'])))
            destination.write(struct.pack('<f', float(status['unkn_float7'])))

            for text in statusText2:
                destination.write(status[text].encode('utf-8'))
                destination.write(b'\x00')
        
        for revise in charReader:
            destination.write(b'char_revise\x00')
            length = len(revise['target']) + 13
            destination.write(length.to_bytes(2, 'little'))

            destination.write(revise['target'].encode('utf-8'))
            destination.write(b'\x00')
            
            for field in reviseFields:
                destination.write(int(revise[field]).to_bytes(2, 'little'))

if __name__ == "__main__":
    randomize('./', variance=60, randomStat=True, randomEleRes=True, randomAfflictionRes=True, randomUnbalance=True, keepDeathblow=True, increaseExp=True, increaseMass=True, increaseSepith=True)