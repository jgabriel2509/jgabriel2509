import csv

nome_do_arquivo = 'OCORRENCIAS_2025.csv'
numero_de_armas = 0
numero_de_Espingarda = 0
numero_de_Fuzil = 0
numero_de_Carabina = 0
numero_de_Pistola = 0
numero_de_Pistolao = 0
numero_de_Garrucha = 0
numero_de_Rifle = 0
numero_de_Carabina_Fuzil = 0
numero_de_Garruchao = 0
try:
    exemplo_arquivo = open(nome_do_arquivo)
    exemplo_leitor = csv.reader(exemplo_arquivo,
                                delimiter=';',
                                dialect='excel')
    for linha in exemplo_leitor:
        '''print('linha #%s <%s>'
        % (exemplo_leitor.line_num, linha))'''
        if linha[4].strip(" ") == "Carabina":
            numero_de_Carabina += 1
        elif linha[4].strip(" ") == "Espingarda":
            numero_de_Espingarda += 1
        elif linha[4].strip(" ") == "Fuzil":
            numero_de_Fuzil += 1
        elif linha[4].strip(" ") == "Garrucha":
            numero_de_Garrucha += 1
        elif linha[4].strip(" ") == "Garruchao":
            numero_de_Garruchao += 1
        elif linha[4].strip(" ") == "Pistola":
            numero_de_Pistola += 1
        elif linha[4].strip(" ") == "Pistolao":
            numero_de_Pistolao += 1
        elif linha[4].strip(" ") == "Rifle":
            numero_de_Rifle += 1
        elif linha[4].strip(" ") == "Carabina/Fuzil":
            numero_de_Carabina_Fuzil += 1
        
    print(numero_de_Espingarda,numero_de_Fuzil,numero_de_Carabina,numero_de_Pistola,numero_de_Pistolao,numero_de_Garrucha,numero_de_Rifle,numero_de_Carabina_Fuzil,numero_de_Garruchao)
    exemplo_arquivo.close()
except FileNotFoundError:
    print('Arquivo não encontrado')