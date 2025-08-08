import json

pythonValue = {'isCat': True, 'mineCaught': 0, 'name': 'Zophie','felineIQ': None}


stringOfjsonData = json.dumps(pythonValue)

with open("pessoa.json", "a") as arquivo:
    arquivo.write(stringOfjsonData)