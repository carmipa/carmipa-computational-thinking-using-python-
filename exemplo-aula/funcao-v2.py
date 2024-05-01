def aumento(valor, percentual):
    novoValor = (1 + percentual /100) * valor
    # print(novoValor) - não recomendável usar print como resultado da função
    return novoValor

# aumento(350.00, 15)

aux = aumento(1000, 15)

# função:
# posso escolher o que fazer como:
# gravar arquivo;
# gravar em BD;
# mandar para outro servidor;
# exibir na tela do celular ou navegador web.