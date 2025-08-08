import json

dados_json = '{ "nome":"Ana", "idade":25, "cidade":"São Paulo" }'



dados_python = json.loads(dados_json)




print(dados_python["nome"])
print(dados_python["idade"])


import json


pythonValue = {'isCat': True, 'mineCaught': 0, 'name': 'Zophie','felineIQ': None}


stringOfjsonData = json.dumps(pythonValue)
print(stringOfjsonData)