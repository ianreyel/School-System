
lista =[]
def menu_principal():
    # Menu principal 
    while True:
        print("\n-- MENU PRINCIPAL --")
        print("1 - Gerenciar estudantes")
        print("2 - Gerenciar professores")
        print("3 - Gerenciar disciplinas")
        print("4 - Gerenciar turmas")
        print("5 - Gerenciar matrículas")
        print("6 - Sair")

        opcao = int(input("Informe a opção desejada: "))
        if opcao <=6:
            opcao = int(opcao)
            if opcao == 1:
                gerenciar_lista("Estudantes")
            elif opcao == 2:
                gerenciar_lista("Professores")
            elif opcao == 3:
                gerenciar_lista("Disciplinas")
            elif opcao == 4:
                gerenciar_lista("Turmas")
            elif opcao == 5:
                gerenciar_lista("Matrículas")
            elif opcao == 6:
                print("Saindo...")
                break
            else:
                print("Opção inválida!")
        else:
            print("Digite um número válido!")

def gerenciar_lista(nome_lista):
    while True:
        dic_aluno = {}
        
        print(f"\n-- [{nome_lista}] MENU DE OPERAÇÕES --")
        print("1 - Incluir")
        print("2 - Listar")
        print("3 - Atualizar")
        print("4 - Excluir")
        print("5 - Voltar ao menu principal")

        opcao = int(input("Informe a função desejada: "))
        if opcao <= 5:
            

            if opcao == 1:
                # adicionar 
                matricula = input(f"Informe o matricula do aluno: ")

                matricula_existe = False
                
                for veri in lista:
                    if veri['matricula'] == matricula:
                        matricula_existe = True
                        break
                

                if matricula_existe:
                    print(f"Matricula de numero: {matricula} ja esta na lista")
                else:
                    nome = input(f"Informe o nome do aluno: ")
                    cpf = input(f"Informe o cpf do aluno:: ")
                    turma = input(f"Informe o turma do aluno: ")
                    
                    dic_aluno = {
                        'matricula': matricula,
                        'nome': nome,
                        'cpf': cpf,
                        'turma': turma,
                    }
                    
                    lista.append(dic_aluno)
                    
                    

                    
            elif opcao == 2:
                # Listagem de alunos 
                print("\n-- LISTAR --")
                
                if lista != []:
                    for lis in lista:
                        print(f'matricula: {lis['matricula']}')
                        print(f'nome: {lis['nome']}')
                        print(f'cpf: {lis['cpf']}')
                        print(f'turma: {lis['turma']}')
                        print(f'---------------')
                else: 
                    print('-- lista vazia --')
                    
                
            elif opcao == 3:
                # fiz a mesma verificação de maneiras diferentes ja estou ficando maluko 
                if lista == []:
                    print("Lista vazia!")
                else:
                    
                    matricula = input("Informe a matrícula para atualização do aluno: ")
                
                    matricula_existe = False
                    
                    if matricula != None:
                        for indice,dic in enumerate(lista):
                            if dic['matricula'] == matricula:
                                matricula_existe = True
                                break

                    if matricula_existe == False:
                       print(f"Matrícula: '{matricula}' Não existe")
                    else:
                        
                        nome = input(f"Antigo nome: {dic['nome']} \nInforme o novo nome do aluno:")
                        cpf = input(f"Antigo CPF: {dic['cpf']} \nInforme o novo CPF do aluno: ")
                        turma = input(f"Antiga turma {dic['turma']} \nInforme a nova turma do aluno: ")
                        dic_aluno = {
                            'matricula': matricula,
                            'nome': nome,
                            'cpf': cpf,
                            'turma': turma,
                        }
                        lista[indice] = dic_aluno
                        print(f"\nIncluído com sucesso!")


                        
            elif opcao == 4:
                # Excluir
                # 3 tipos de verificação para a mesma verificação pq eu quis testar

                if not lista:
                    print("Lista vazia!")
                else:
                    excluir = input("Informe a matricula a ser excluído: ")

                    matricula_existe = False
                    
                    if matricula != None:
                        for indice,dic_exc in enumerate(lista):
                            if dic_exc['matricula'] == excluir:
                                matricula_existe = True
                                break
                    else: print('-- Matricula Não Informada --')

                    print('-- Aluno a Excluir --')
                    print(f'matricula: {dic_exc['matricula']}')
                    print(f'nome: {dic_exc['nome']}')
                    print(f'cpf: {dic_exc['cpf']}')
                    print(f'turma: {dic_exc['turma']}')
                    print('---------------')
                    confirm_exc = input('\nDeseja Confirmar Exclusão (s/n):')
                    
                    if confirm_exc == 's':
                        
                        lista.remove(dic_exc)
                        print(f"{dic_exc['nome']} excluído!")

                    else:
                        print('cancelando exclusão')
                        
                    


                    
            elif opcao == 5:
                # Saida dos loops
                print("Retornando ao menu principal...")
                break
            else:
                print("Opção inválida!")
        else:
            print("Digite um número válido!")

menu_principal()
