import re

# Agora vamos usar estruturas mais sofisticadas de REGEX.

# 0. ".match" NO INÍCIO DA STRING:
# 0.1 Encontra a primeira aparição de expressão REGEX, retornando também a posição da lista e do elemento dela.
# 1. ".search" EM QUALQUER PARTE DA STRING:
# 1.1 Encontra a expressão REGEX e dá suas coordenadas independetemente da posição.
# OBS sobre "0" e "1": Tanto ".search" quanto ".match" usam o método "span", o qual nos dá NÃO A LOCALIZAÇÃO EXATA da
# Expressão REGEX, mas sim o intervalo no qual ela está contido. Por exemplo, se os valores estão na posição 1 e 3,
# O retorno será entre "1 e 4", ou seja, entre o 1º e o 4º caractere considerado.
# OBS da OBS: O retorno é entre "1 e 4", mas em Python seria o equivalnte às posições "1 e 3", ou seja, entre a segunda
# e a 4ª ocorrência. Além disso, tanto ".search" quanto ".findall" e ".match" analisam apenas a primeira aparição REGEX.
# 2. ".finditer". Permite iterações sobre a string. Diferentemente dos métodos anteriores, analisa TODAS as ocorrências
# REGEX. Em outras palavras, junta a lógica do ".search" com o ".findall".
# "[]" trata de sequências específicas e desordenadas.
# 3. "+", Dentro de uma expressão REGEX, significa "um caractere que aparecece UMA ou MAIS VEZES".
# 4. "*", Dentro de uma expressão REGEX, significa "um caractere que aparece ZERO ou MAIS VEZES" (ou seja, não precisa
# aparecer).
# 5. "{n}" em que n é um número natural. Define um número EXATO de repetições do padrão REGEX.
# 6. "{n, a}", n != a (não faria sentido ser igual, mas até poderia), define um intervalo nos NATURAIS, com "n" sendo
# mínimo de repetições do padrão REGEX e "a" o máximo.
# 7. "()" trata de sequências específicas e ordenadas.
# IMPORTANTE: "()" != "[]", como já dito. O primeiro é ordenado, no segundo a ordem não importa.
# 8. "|" significa "ou" (similar ao Js, "||").
# 9. "?" O caractere deve aparecer 0 ou 1 vez.
texto = 'arara'
p1 = re.compile(r'r')
check_findall = p1.findall(texto)
check_match = p1.match(texto)
check_search = p1.search(texto)
check_finditer = p1.finditer(texto)
correspondencias = check_finditer
print(check_findall)
print(check_match)
print(check_search)
print(check_finditer)
for correspondencia in correspondencias:
    print(correspondencia)

print(f'-='*7, 'OUTRO EXERCÍCIO', '-='*7)

texto = '''
KingTrator 1982
'''
p = re.compile(r'[a-zA-z0-9 ]')  # Pega algarismos de 0 a 9 e maiúsculas e minúsculas, mas não caracteres especiais.
correspondencias = p.finditer(texto)

for correspondencia in correspondencias:
    print(correspondencia)

print(f'-='*7, 'OUTRO EXERCÍCIO', '-='*7)
texto = 'a1'

p = re.compile(r'[a-zA-Z][0-9]')
correspondencias = p.finditer(texto)
for correspondencia in correspondencias:
    print(correspondencia)
print(f'-='*7, 'OUTRO EXERCÍCIO', '-='*7)
#  OBS: se você escrever "p = re.compiler(r'[a-zA-Z][0-9])  (sem espaço entre o alfa e o numérico)
# O padrão aceitará "a1", mas não aceitará "a 1". Enquanto no

# IMPORTANTE: Sem querer, descobri que é importante a ordem em que se escreve
# re.compile(r'[a-zA-Z] [0-9]') e correspondencias = p.finditer(texto), ou, generalizando,
# a ordem em que se põe o re.compile e o finditer():
# Se você pôr o ".finditer()" antes de definir a seleção a ser feita, no contexto atual...
# CORREÇÃO (SIM ME CORRIGI NO MEIO DO TEXTO, O QUE EU IA DIZER NÃO ERA PRECISO):
# Como eu estou mantendo as mesmas variáveis e o "re.compile" permite que uma variável herde os métodos
# da biblioteca "re", quando eu havia escrito "p.finditer(texto)' antes de definir qual era o padrão REGEX em
# re.compile, o meu "p" ainda estava usando o padrão REGEX anterior e por isso ao chamar re.finditer(texto) antes
# apesar de depois trocar o padrão REGEX, eu recebia o resultado do padrão anterior para a variável textoa atual.
# Se você chamar "p.finditer(texto)" antes de ter um padrão REGEX definido, retorna-se erro.
# Enfim, cuidado!
texto = '''
Arara 1982
Arara 1758
Peixe voando 48
Cu9
Arroba19muchacho
'''

p = re.compile(r'[a-zA-Z]+ [0-9]+')  # Tradução: pegue maiúsculas/minúsculas que aparecem uma ou + vezes, depois
# (quando achar o espaço) pegue o espaço e pegue os números que se seguem após o espaço, sendo que eles se seguem uma ou
# mais vezes. Tanto para letras quanto para números, pegue-os somente se não houver espaço entre eles.
# A expressão só estará correta se for no formato: M/m+ (whitespace) Números+
correspondencias = p.finditer(texto)
for correspondencia in correspondencias:
    print(correspondencia)

print(f'-='*7, 'OUTRO EXERCÍCIO', '-='*7)
texto = 'ra8ar raa'

p = re.compile(r'[ra]*')  # Estou dizendo que eu ACEITO que apareça "ra".
correspondencias = p.finditer(texto)
for correspondencia in correspondencias:
    print(correspondencia)
# Resumo da ópera: PROCURE PELA SEQUÊNCIA 'ra', seja 'r', 'a' ou 'ra' em qualquer ordem.
# Caso apareça algo entre 'r' e 'a', encerre a sequência, iniciando uma nova.
# Para tudo o que não for 'ra', retorne uma string vazia ''.
# OBS: Por padrão, sempre teremos um último match sendo uma string vazia, o qual indica
# que a sequência se encerrou. Lembro que o Guanabara havia explicado isso lá atrás, quando eu me
# introduzia à manipulação de textos. Talvez eu devesse revisar isso.
print(f'-='*7, 'OUTRO EXERCÍCIO', '-='*7)
texto = '''
Spong Bob the 197 BO7
Arara 1987
raraliog é o rararaliog
'''

p = re.compile(r'[ra]{4}')  # Por padrão, só pega a primeira aparição de "rara"
correspondencias = p.finditer(texto)
for correspondencia in correspondencias:
    print(correspondencia)
# OBS: Note que se analisa string a string. Se você definir {1}, ele irá pegar
# uma string por vez. Se quiser pegar o padrão "rara", você precisará definir ao menos {4}, para pegar
# 4 strings por vez. Claro que isso não pega "rara" necessariamente, mas também "ar", "aa", "rr", etc.
print('-='*7, 'OUTRO EXERCÍCIO', '-='*7)
texto = '''
Spong Bob the 197 BO7
Arara 1987
raraliog é o rararaliog
'''

p = re.compile(r'[ra]{2,4}')  # Por padrão, só pega a primeira aparição de "rara"
correspondencias = p.finditer(texto)
for correspondencia in correspondencias:
    print(correspondencia)
# TRADUZINDO: Se tiver apenas "2" ocorrências pegue, mas verifique antes se não tem mais ocorrências, se tiver mais
# ocorrências, pegue no MÁXIMO 4 delas e então dê por encerrada a sequência.
# IMPORTANTE: escrever {2,4} é certo, escrever {2, 4} é errado e não retornará nada.
print('-='*7, 'OUTRO EXERCÍCIO', '-='*7)
texto = '''
Arara 1992
arara 1993
aaaa 1
'''

p = re.compile(r'([Aa])?[a-z]{4} [0-9]+')
# OBS: Originalmente, no Hastag Programação, a expressão usada foi (A|a), mas
# o Pycharm sugere [Aa] porque isso é mais eficiente para a biblioteca re.
# O ChatGPT-4 concordou. Então, para ainda assim tornar este um grupo de captura, apenas pus
# () envolta deles.

# Tradução: A expressão pode conter A ou a, aparecendo 0 e no máximo 1 vez,
# DEVE conter caracteres alfabéticos minúsculos de a-z,
# DEVE conter, após os caracteres de a-z, um espaço (whitespace), que apareçam EXATAMENTE 4 vezes.
# DEVE conter, após o espaço, caracteres numéricos de 0-9, que apareçam 1 uma mais vezes.
# IMPORTANTE: As opções OPCIONAIS (como (A|a)) são inferiores às necessárias,
# como [a-z]; por exemplo, no caso 'aaaa 1', a primeira parte fica com "0" aparições de "A" ou "a", pois
# assim é possível admitir 4 ocorrências em [a-z]{4}, que é parte necessária.
# ALém disso, é bom ter o lembrete sobre GREEDY EXPRESSIONS:
# Essa é uma GREEDY EXPRESSIONS (veja mais profundamente no Mundo 4 de Python),
# Quando não se digita "?" após a REGEX, ela é greedy e tentará achar a maior sequência possível que satisfaça
# a lógica proposta.
# Quando se põe "?" a ocorrência terminará na menor ocorrência possível.
# Isso é particularmente útil quando se usa "." e se quer a menor ocorrência possível
# Como já visto, "." é qualquer sequência de caracteres, mas usando
# ".?" a sequência ainda será qualquer, só que se, por alguma razão, houver uma expressão
# mais curta parte a expressão em que está ".", com ".?" ela será adotada em vez de a
# expressão mais longa.

correspondencias = p.finditer(texto)
for correspondencia in correspondencias:
    print(correspondencia)
    print(correspondencia.group(0))  # retorna toda a expressão REGEX
    print(correspondencia.group(1))  # primeira expressão REGEX a ter sido feita, no caso (A|a)?
# Note que para 'aaaa 1' o retorno é None porque, como já dito, o 'a' é assumido pela segunda expressão
# REGEX, a fim de torná-la verdadeira, haja vista que é NECESSÁRIA e, portanto, prioritária.
# IMPORTANTE: Outra diferença entre () e [] é que () permite usar grupos de captura.
# Isto é, não é possível um .group(2) aqui, para pegar o segundo item da expressão REGEX, porque este segundo
# item é um [], que não admite grupo de captura.
# Se quiser capturar a expressão, basta fazer ([]).
# Neste caso, curiosamente, () - que antes eu disse que só aceita expressões ordenadas, estará
# aceitando expressões desordenadas, porque nenhuma ordem prévia foi definida.
