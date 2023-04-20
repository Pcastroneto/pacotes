# Exemplo de AttributeError
a = "abc"
b = a.length 
print(b)
# str em Python não possui um 
# atributo length.

# Exemplo corrigido de # AttributeError
a = "abc"
b = len(a)
print(b)