frase_original = "I can only show you the door.\nYou’re the one that has to walk through it."

# Letras a serem substituídas
letras_substituir = "aro"

# Substitui cada caractere na frase se estiver presente no conjunto de letras
nova_frase = "".join(["*" if c in letras_substituir else c for c in frase_original])

# Exibe a nova frase
print(nova_frase)