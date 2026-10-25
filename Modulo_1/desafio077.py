palavras = ('PYthOn', 'java', 'javascript','ruby','go','c+','c','c#','c++','neymar','ronaldinho','pele','pepe','coutinho')
for c in range(0,len(palavras)):
    vogais = ''
    for p in range(0,len(palavras[c])):
        if palavras[c][p].lower() in 'aeiou':
            vogais += f'{palavras[c][p]} '
    print(f'{palavras[c]} tem as vogais: {vogais}', )
