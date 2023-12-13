import json

def pergunta():
    return input("\nPressione <I> para Inserir\n"+
          "Pressione <E> para Editar\n"+
          "Pressione <L> para Listar\n"+
          "Pressione <P> para Pesquisar\n"+
          "Pressione <Q> para Excluir\n"+
          "Pressione <T> para Esvaziar lista\n").upper()
    

def inserir(dicionario):
    dicionario[input("Produto...: ").upper()] = [input("\nNome......: ").upper(),
                                                                    float(input("Preco.....: R$")),
                                                                    int(input("Estoque...: "))]
    
    if input in dicionario:
        return print(f"{input} já está cadastrado.")
    else:
        return print("\nProduto adicionado!")


def editar(dicionario):
    chave = input("Digite o produto a ser editado: ").upper()
    if chave in dicionario:
        dicionario[chave] = [input("Nome......: ").upper(),
                            float(input("Preco.....: R$")),
                            int(input("Estoque...: "))]
                            
        return print(f"O produto {chave} foi atualizado!")
    else:
        return print("Produto não cadastrado!\n")
    

def pesquisar(dicionario):
    chave = input("Digite o produto que deseja pesquisar: ").upper()
    if chave in dicionario:
        return print(f"\nProduto...: {chave}\n"+
               f"Nome......: {dicionario[chave][0]}\n"+
               f"Preco.....: R${dicionario[chave][1]:.2f}\n"+
               f"Estoque...: {dicionario[chave][2]}u\n"+
               "-"*30)
    else:
        return print("Produto não cadastrado!\n")
    

def mostrar(dicionario):
    resultado = ""
    for chave in sorted(dicionario):
        resultado += (f"\nProduto...: {chave}\n"+
               f"Nome......: {dicionario[chave][0]}\n"+
               f"Preco.....: R${dicionario[chave][1]:.2f}\n"+
               f"Estoque...: {dicionario[chave][2]}u\n"+
               "-"*30)
    return print(resultado)


def excluir(dicionario):
    chave = input("Digite o produto que deseja excluir: ").upper()
    if chave in dicionario:
        if input("Tem certeza? S-sim ou N-não\n").upper() == "S":
            dicionario.pop(chave)
            return print("Produto removido com sucesso!\n")
        else:
            return print("Operação cancelada")
        

def esvaziar(dicionario):
    if input("Tem certeza?\nS-sim | N-nao\n").upper() == "S":
        dicionario.clear()
        return print("Lista limpa com sucesso!")
    else:
        return print("Operacao cancelada")


def salvar_catalogo(dicionario, catalogoProducts):
    with open(catalogoProducts, "w") as arquivo:
        json.dump(dicionario, arquivo)
    return print("Salvo no banco de dados")


def carregar_catalogo(catalogoProducts):
    with open(catalogoProducts, "r") as arquivo:
        return json.load(arquivo)

run = True
catalogo_carregado = carregar_catalogo('catalogo.json')

while run :

    perguntar = pergunta()  

    if perguntar == "I":
        inserir(catalogo_carregado)
        salvar_catalogo(catalogo_carregado, 'catalogo.json')
    elif perguntar == "L":
        mostrar(catalogo_carregado)
    elif perguntar == "E":
        editar(catalogo_carregado)
        salvar_catalogo(catalogo_carregado, 'catalogo.json')
    elif perguntar == "P":
        pesquisar(catalogo_carregado)
    elif perguntar == "Q":
        excluir(catalogo_carregado)
        salvar_catalogo(catalogo_carregado, 'catalogo.json')
    elif perguntar == "T":
        esvaziar(catalogo_carregado)
    else:
        break






