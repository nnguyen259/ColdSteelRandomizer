import random

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

def replaceNeedleShoot(path=None):
    with open(path + 'data/scripts/scena/dat_us/m2500.dat', 'r+b') as file:
        file.seek(54260)
        file.write((2179).to_bytes(2, 'little'))

        file.seek(54336)
        file.write(b'6')

        file.seek(54341)
        file.write(b'La Forte    ')

if __name__ == "__main__":
    replaceNeedleShoot('./')