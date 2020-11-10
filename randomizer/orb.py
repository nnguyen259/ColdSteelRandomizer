import random

def randomize(path=None, seed=None, maxLine=8, minEleSlot=0, maxEleSlot=8):
    if seed:
        random.seed(seed)
    with open(path + 't_orb.tbl', 'wb') as outputfile:
        lineNums = 13*[0]
        for i in range(13):
            lineNums[i] = random.randint(1, maxLine)
        outputfile.write((sum(lineNums) + 13).to_bytes(2, byteorder='little'))

        for i in range(13):
            outputfile.write('BaseList'.encode('utf-8'))
            outputfile.write(b'\x00\x14\x00')
            outputfile.write(i.to_bytes(2, byteorder='little'))
            outputfile.write(lineNums[i].to_bytes(2, byteorder='little'))

            if minEleSlot > maxEleSlot:
                numEleSlots = random.randint(maxEleSlot, minEleSlot)
            else:
                numEleSlots = random.randint(minEleSlot, maxEleSlot)
            slots = 8*[0]
            for j in range(numEleSlots):
                slots[j] = random.randint(1, 7)
            random.shuffle(slots)

            for j in range(8):
                outputfile.write(slots[j].to_bytes(2, byteorder='little'))

            slotsleft = 8
            counter = 1
            for j in range(lineNums[i]):
                outputfile.write(b'OrbLineList\x00\x14\x00')
                outputfile.write(i.to_bytes(2, byteorder='little'))
                outputfile.write(j.to_bytes(2, byteorder='little'))
                if j < lineNums[i] - 1:
                    linesize = random.randint(1, slotsleft - (lineNums[i] - j) + 1)
                    slotsleft -= linesize
                else:
                    linesize = slotsleft
                line = 8*[65535]
                for k in range(8):
                    if k < linesize:
                        line[k] = counter
                        counter += 1
                    outputfile.write(line[k].to_bytes(2, byteorder='little'))                

if __name__ == "__main__":
    randomize('data/text/dat_us/')