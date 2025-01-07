import json

dataMahasiswa = {'Nama': "Alif Farid Rahman", 'usia': 23}

newData = json.dumps(dataMahasiswa)

decodeData = json.loads(newData)

print(decodeData['Nama']) 

with open('dataMahasiswa.json', 'w') as file:
    json.dump(dataMahasiswa, file)

print("Data berhasil diekspor ke file dataMahasiswa.json")
