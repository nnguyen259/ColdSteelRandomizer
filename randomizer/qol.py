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

if __name__ == "__main__":
    reduceSlotCost('data/text/dat_us/')