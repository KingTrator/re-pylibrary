import re

# Aqui as coisas começam a ficar mais gostosas e desafiantes.

# 1. Para pegar um "." em uma string REGEX, usa-se "\.", haja vista
# que "." já tem significado semântico, que é o de "qualquer caracter exceto nova linha".
# 2. Dentro do [] eu posso usar ".", "+", etc, como normalmente usaria em uma string, ou seja,
# não são consideradores caracteres especiais do "re".
# IMPORTANTE: Para representar o hífen dentro de [], há duas opções:
# Primeira opção: Ponha-lo no final (ou começo) da expressão, assim [a-x-z-d+3@@$-]
# Segunda opção: Use a barra invertida + hífen: \-, fica assim: [a-x0-9\-+@]
# 3. [^ \n]+ pode ser um delimitador, pois captura QUALQUER COISA, EXCETO:
# Exceto Nova Linha
# Exceto Whitespace (Espaço em branco)
# Assim, pode ser mais eficiente que "." em um texto corrido, pois também não irá capturar nada mais
# se encontrar um espaço em branco, sendo um eficiente delimitador.
print('-='*7, 'EXERCÍCIO 1: URLs', '-='*7)
texto = '''
Sites diversos:
https://google.com/
https://www.gov.br/
https://www.kaiamba.com.br/
http://faetec.rj.gov.br/
'''

p = re.compile((r'https?://(www\.)?([a-zA-Z0-9]+\.)+(com\.br|gov\.br|com)'))
# OBS: Para especificar cada parte de uma string colocada em (), você deve
# usar uma expressão REGEX ao lado do caracter em específico.
# Aqui, por exemplo, o "?" (0 ou uma ocorrência) só faz efeito sobre o "s" e não de "https" em conjunto.
# Se fosse para pegar o conjunto, o "?" estaria do lado de fora de ()

correspondencias = p.finditer(texto)
for correspondencia in correspondencias:
    print(correspondencia)
    print(correspondencia.group(0))
    print(correspondencia.group(1))
    print(correspondencia.group(2))
    print(correspondencia.group(3))

print('-='*7, 'EXERCÍCIO 2: EMAILS', '-='*7)

texto = '''
Vários emails:
pedro@dominio.com
jose.candiotto@dominio.com.br
DANIEL@dominio.br
ALFREDO.CANDIOTTO@gov.br
danielcandiotto@dominio1.co
alfredo_candiotto1@dominio.dominio.net
ovo loko - não será capturado, inclusive este comentário
abora@   oii - não será capturado, inclusive este comentário
'''
p = re.compile(r'[a-zA-Z0-9_.+-]+@[^ \n]+')
correspondencias = p.finditer(texto)

for correspondencia in correspondencias:
    print(correspondencia)
