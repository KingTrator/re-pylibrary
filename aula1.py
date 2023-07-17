import re
# Adendo aos estudos sobre a biblioteca re
# LÓGICA PADRÃO: uma letra maiúscula é o inverso da maiúscula (exemplo, \d é o inverso de \D)
# 0. ".findall" procura por todas as ocorrências de uma dada expressão REGEX.
# 1. "." lê qualquer caractere, exceto linha nova.
# 2. "\." busca o caracter "."
# 3. "^" especifica qual é o primeiro caractere da string.
# 4. "[^]" diz para retornar na string tudo, exceto o que está dentro do colchetes.
# 5. "\d" qualquer algarismo de 0 a 9.
# 6. "\D" qualquer caractere que não seja um algarismo de 0 a 9.
# 7. "\s" Qualquer caracter que seja vazio.
# 8. "\S" Qualquer caracter que não seja vazio.
# 9. "\w" Qualquer caractere que seja alfanumérico.
# 10. "\W" Qualquer caractere que não seja alfanumérico.

texto = 'arara'
padrao = re.compile('ar.ra')  # Estou dizendo: este é um padrão que comece por ar + qualquer coisa, então outro "r" +
# qualquer coisa, então outro a, no final. (Obs: é preciso ter alguma coisa antes do r)
check = padrao.findall(texto)  # apresenta todas as strings com o padrão definido acima.
print(check)
p1 = re.compile('^a')
check = p1.findall(texto)
print(check)
p2 = re.compile('[^a]')
check = p2.findall(texto)
print(check)
texto = 'arara1993'
p1 = re.compile(r'\d')
check = p1.findall(texto)
print(check)
# O padrão das estruturas é sempre o mesmo:
# A. Fornece-se o texto (seja um arquivo aberto por pandas ou with open, seja uma string em uma variável como aqui faço)
# B. Usa-se uma variável para dizer qual a manipulação textual.
# C. Usa-se outra variável para dizer em qual texto (o fornecido) deve-se executar a manipulação.
# Ao final você pode printar o resultado para testá-lo.
p2 = re.compile(r'\D')
check = p2.findall(texto)
print(check)
texto = '  Olá ,  Mundo !' \
        '' \
        '\n' \
        '\n' \
        '' # o \s captará inclusive o "\n"
p1 = re.compile(r'\s')
check = p1.findall(texto)
print(check)
# OBS:
# Notei isso durante o estudo. Quando eu uso um método de "re" na minha variável
# (Como a variável p1) os métodos de "re" tornam-se acessíveis à variável sem ser preciso chamar
# a biblioteca novamete, por isso "p1.findall()" sem re.p1.findall()
# o ChatGPT-4 confirmou isso.
p1 = re.compile(r'\w')
check = p1.findall(texto)
print(check)
p2 = re.compile(r'\W')
check = p2.findall(texto)
print(check)
