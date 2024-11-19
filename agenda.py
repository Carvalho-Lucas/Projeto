def adicionar(agenda, nome_pessoa):
    contatos = {"nome": nome_pessoa, "favorito": False}
    agenda.append(contatos) # Adiciona o elemento na ultima posição da lista
    print (f"{nome_pessoa}, foi adicionada a lista de favoritos!")
    return

def visualizar_contatos(agenda):
    print("\nLista de contatos: ")
    for indice, tarefa in enumerate(agenda, start=1):
        status = "★ " if tarefa["favorito"] else " "
        nome_contato = tarefa["nome"]
        print(f"Contato -> {indice}. Favorito -> [{status}] Nome Contato: {nome_contato}")
    return

def atualizar_nome_pessoa(agenda, indice_agenda, nome_alterado):
    indice_tarefa_ajustado = int(indice_agenda) -1
    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(agenda):
        agenda[indice_tarefa_ajustado]["nome"] = nome_alterado
        print(f"\nTarefa {indice_agenda} atualizada para {nome_alterado} ")
    else:
        print(f"\n O indice {indice_agenda} selecionado não é válido, tente novamente.. ")
    return

def deletar_contato(agenda, indice_agenda):
    indice_tarefa_ajustado = int(indice_agenda) - 1
    if 0 <= indice_tarefa_ajustado < len(agenda):
        del agenda[indice_tarefa_ajustado]
        print("Contato DELETADO com sucesso!")
    else:
        print(f"Índice {indice_agenda} inválido. Tente novamente.")
    return

def marcar_favorito(agenda, indice_agenda):
    indice_tarefa_ajustado = int(indice_agenda) -1
    agenda[indice_tarefa_ajustado]["favorito"] = True
    print (f"Contato {indice_agenda}, favoritado!\n")
    return

agenda = []


while True:
    print("\nAgenda de Contatos")
    print("Opção 01 - Salvar contato na Agenda")
    print("Opção 02 - Visualizar contatos")
    print("Opção 03 - Editar contato")
    print("Opção 04 - Deletar contato salvo")
    print("Opção 05 - Marcar contato como Favorito")
    print("Opção 06 - Sair do programa")

    escolha = input("\nDigite uma opção do Menu acima:")

    if escolha == "1":
        pessoa = input("Digite o nome da pessoa a ser adicionada na agenda:")
        adicionar(agenda, pessoa)

    elif escolha == "2":
        visualizar_contatos(agenda)

    elif escolha == "3":
        visualizar_contatos(agenda)
        indice_agenda = input("Digite o número da tarefa que deseja alterar:")
        nome_alterado =  input("Digite a alteração para o nome:")
        atualizar_nome_pessoa(agenda, indice_agenda, nome_alterado)

    elif escolha == "4":
        visualizar_contatos(agenda)
        indice_agenda = input("Digite o número da pessoa que deseja deletar:")
        deletar_contato(agenda, indice_agenda)

    elif escolha=="5":
        visualizar_contatos(agenda)
        indice_agenda = input("Digite o número da tarefa a ser completa:")
        marcar_favorito(agenda, indice_agenda)
    
    elif escolha == "6":
        print("Saindo do programa...")
    break