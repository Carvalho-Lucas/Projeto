def adicionar(tarefas, nome_tarefa="Tarefa Padrão"):
   #Tarefa: Indica o nome da tarefa
   #Completada: status da tarefa
   tarefa = {"tarefa": nome_tarefa, "completada": False}
   tarefas.append(tarefa)
   print (f"A tarefa -> {nome_tarefa}, foi adicionada com sucesso!")
   return

def visualizar(tarefas):
    print("\nLista de tarefas: ")
    for indice, tarefa in enumerate(tarefas, start=1):
        status = "✓" if tarefa["completada"] else " "
        nome_tarefa = tarefa["tarefa"]
        print(f"Tarefa -> {indice}. Status -> [{status}] Nome Tarefa: {nome_tarefa}")
    return

def atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome):
    indice_tarefa_ajustado = int(indice_tarefa) -1
    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
        tarefas[indice_tarefa_ajustado]["tarefa"] = novo_nome
        print(f"\nTarefa {indice_tarefa} atualizada para {novo_nome} ")
    else:
        print(f"\n O indice {indice_tarefa} selecionado não é válido, tente novamente.. ")
    return
    
def completar_tarefa(tarefas, indice_tarefa):
    indice_tarefa_ajustado = int(indice_tarefa) -1
    tarefas[indice_tarefa_ajustado]["completada"] = True
    print (f"Tarefa {indice_tarefa}, concluída!\n")
    return

def deletar_tarefa_completada(tarefas):
    for tarefa in tarefas:
        if tarefa["completada"] == True:
            tarefas.remove(tarefa)
    print(f"Tarefa complatada DELETADA com sucesso!")
    return

tarefas = []

while True:

    print("Menu Gerenciador lista de tarefas")

    print("Opção 01 - Adicionar tarefa")
    print("Opção 02 - Ver tarefa")
    print("Opção 03 - Atualizar tarefa")
    print("Opção 04 - Completar tarefa")
    print("Opção 05 - Deletar tarefa")
    print("Opção 06 - Sair")

    escolha = input("Digite uma opção do Menu acima:")

    if escolha == "1":
        nome_tarefa = input("Digite o nome da tarefa: ")
        adicionar(tarefas, nome_tarefa)

    elif escolha == "2":
        visualizar(tarefas)
    
    elif escolha == "3":
        if not tarefas:
            print("Nenhuma tarefa disponível para atualizar.")
        else:    
            visualizar(tarefas)
            indice_tarefa = input("Digite o número da tarefa que deseja atualizar: ")
            novo_nome = input("Digite o novo nome da tarefa: ")
            atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome)

    elif escolha=="4":
        visualizar(tarefas)
        indice_tarefa = input("Digite o número da tarefa a ser completa:")
        completar_tarefa(tarefas, indice_tarefa)

    elif escolha == "5":
        visualizar(tarefas)
        deletar_tarefa_completada(tarefas)
        
    elif escolha == "6" or escolha >= "7":
        print("Saindo do programa!")
        break

