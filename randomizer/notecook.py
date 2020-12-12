import random, csv

def randomize(path=None, seed=None):
    if seed:
        random.seed(seed)

    with open('input/Files/Notecook.csv', newline='') as cookFile:
        recipeList = list(csv.DictReader(cookFile))

        for recipe in recipeList:
            results = []
            chars = []
            
            for i in range(4):
                text = []
                text.append(recipe['result' + str(i+1) + '_id'])
                text.append(recipe['result' + str(i+1) + '_text1'])
                text.append(recipe['result' + str(i+1) + '_text2'])
                results.append(text)
            
            for i in range(11):
                chars.append(recipe['char' + str(i+1)])
            
            random.shuffle(results)
            random.shuffle(chars)

            for i in range(4):
                recipe['result' + str(i+1) + '_id'] = results[i][0]
                recipe['result' + str(i+1) + '_text1'] = results[i][1]
                recipe['result' + str(i+1) + '_text2'] = results[i][2]

            for i in range(11):
                recipe['char' + str(i+1)] = chars[i]
            
        __buildNoteCook(path=path, data=recipeList)

def __buildNoteCook(path=None, data=None):
    with open(path + '/data/text/dat_us/t_notecook.tbl', 'wb') as destination:
        entry_num = len(data)

        destination.write(entry_num.to_bytes(2, 'little'))

        for noteCook in data:
            length = len(noteCook['name'].encode('utf-8')) + len(noteCook['result1_text1'].encode('utf-8')) + len(noteCook['result1_text2'].encode('utf-8')) + \
                    len(noteCook['result2_text1'].encode('utf-8')) + len(noteCook['result2_text2'].encode('utf-8')) + \
                    len(noteCook['result3_text1'].encode('utf-8')) + len(noteCook['result3_text2'].encode('utf-8')) + \
                    len(noteCook['result4_text1'].encode('utf-8')) + len(noteCook['result4_text2'].encode('utf-8')) + 62

            destination.write(b'QSCook\x00')
            destination.write(length.to_bytes(2, 'little'))
            destination.write(noteCook['name'].encode('utf-8') + b'\x00')
            destination.write(int(noteCook['id']).to_bytes(2, 'little'))

            for i in range(8):
                destination.write(int(noteCook['mat' + str(i+1) + '_id']).to_bytes(2, 'little'))
                destination.write(int(noteCook['mat' + str(i+1) + '_amount']).to_bytes(2, 'little'))

            for i in range(4):
                destination.write(int(noteCook['result' + str(i+1) + '_id']).to_bytes(2, 'little'))
                destination.write(noteCook['result' + str(i+1) + '_text1'].encode('utf-8') + b'\x00')
                destination.write(noteCook['result' + str(i+1) + '_text2'].encode('utf-8') + b'\x00')

            for i in range(11):
                destination.write(int(noteCook['char' + str(i+1)]).to_bytes(1, 'little'))

if __name__ == "__main__":
    randomize('./')