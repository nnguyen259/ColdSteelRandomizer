import random

def increaseDrop(path=None, seed=None, increaseEXP=True, increaseNormalSepith=True, increaseSepithMass=True):
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

            if increaseEXP:
                file.seek(newHead + 16)
                exp = 2 * int.from_bytes(file.read(2), 'little')
                if exp > 65535:
                    exp = 65535
                file.seek(newHead + 16)
                file.write(exp.to_bytes(2, 'little'))


            if increaseNormalSepith:
                file.seek(newHead + 48)
                for j in range(7):
                    sepith = 3 * int.from_bytes(file.read(1), 'little')
                    if sepith > 255:
                        sepith = 255
                    file.seek(file.tell() - 1)
                    file.write(sepith.to_bytes(1, 'little'))

            if increaseSepithMass:
                file.seek(newHead + 55)
                sepithMass = 3 * int.from_bytes(file.read(1), 'little')
                if sepithMass > 255:
                    sepithMass = 255
                file.seek(file.tell() - 1)
                file.write(sepithMass.to_bytes(1, 'little'))
            index += length + 9
            i += 1

def reduceSlotCost(path=None, seed=None):
    if seed:
        random.seed(seed)
    with open(path + 't_slot.tbl', 'r+b') as file:
        for i in range(8):
            file.seek(379 + 27*i + 13)
            for j in range(7):
                cost = int(int.from_bytes(file.read(2), 'little') / 2)
                file.seek(file.tell() - 2)
                file.write(cost.to_bytes(2, 'little'))

if __name__ == "__main__":
    reduceSlotCost('data/text/dat_us/')