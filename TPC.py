#1

import re

# Abre o arquivo
with open('Camilo-A_Brasileira_de_Prazins.md', 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()

# Define um padrão de expressão regular para identificar os capítulos
padrao_capitulos = r'^#.+'

# Encontra todas as linhas que correspondem ao padrão
linhas_capitulos = re.findall(padrao_capitulos, texto, re.MULTILINE)

# Conta o número de capítulos
num_capitulos = len(linhas_capitulos)

# Exibe o número de capítulos
print("Número de capítulos:", num_capitulos)

#2
def adiciona_cardinais(match):
    capitulo = match.group(0)
    return str(linhas_capitulos.index(capitulo) + 1) + "º " + capitulo

# Substitui os cabeçalhos dos capítulos pelos números cardinais
texto_com_indice = re.sub(padrao_capitulos, adiciona_cardinais, texto)

# Exibe o texto com o índice numérico
print(texto_com_indice)

#3
def minusculas(match):
    return match.group(0).lower()

padrao_palavras = r'\w+'
palavras = re.findall(padrao_palavras, texto)
texto_com_palavras_minusculas = re.sub(padrao_palavras, minusculas, texto)

#4
padrao_separadores = r'[.!?]+'
separadores = re.findall(padrao_separadores, texto)
num_frases = len(separadores)

print("Número de frases:", num_frases)

#5
num_frases = len(separadores)
comprimento_medio = len(texto) / num_frases


print("Comprimento médio de uma frase:", comprimento_medio)

padrao_secoes = r'# .+'
# Encontra todas as ocorrências dos cabeçalhos de seções no texto
secoes = re.findall(padrao_secoes, texto)
resumo = '\n'.join(secoes)

print(resumo)



