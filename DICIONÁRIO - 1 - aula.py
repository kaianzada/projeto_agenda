info = []
while True:
    menu = int(input("O que deseja? 1-Cadastro / 2-Listar / 3-Pesquisar / 4-Alterar / 5-Excluir / 9-sair: "))
    if menu == 1:
        aluno={}
        aluno['Nome']= str(input("Informe o nome do aluno: "))
        aluno['Disciplina']= str(input("Informe a disciplina: "))
        aluno['Nota-1']= float(input("Informe a primeira nota: "))
        aluno['Nota-2']= float(input("Informe a segunda nota: "))
        aluno['Nota-3']= float(input("Informe a terceira nota: "))
        aluno['Nota-4']= float(input("Informe a quarta nota: "))
        
        info.append(aluno)
    elif menu == 2:
        for i in info:
            print(i)
            media = (i["Nota-1"]+i["Nota-2"]+i["Nota-3"]+i["Nota-4"])/4
            if media >= 7:
                print("O(A) aluno(a) está aprovado(a) ")
            else :
                print("O(A) aluno(a) está reprovado(a) ")
    elif menu == 3:
        nome= str(input("Informe o nome do aluno: "))
        for i in info:
            if nome == i['Nome']:
                print(i)
                break
    elif menu == 4:
        nome= str(input("Informe o nome do aluno: "))
        for i in info:
            if nome == i['Nome']:
                i['Nome']= str(input("Informe o nome do aluno: "))
                i['Disciplina']= str(input("Informe a disciplina: "))
                i['Nota-1']= float(input("Informe a primeira nota: "))
                i['Nota-2']= float(input("Informe a segunda nota: "))
                i['Nota-3']= float(input("Informe a terceira nota: "))
                i['Nota-4']= float(input("Informe a quarta nota: "))
                break
    elif menu == 5:
        nome = str(input("Informe o nome do aluno: "))
        for i in info:
            if nome == i['Nome']:
                info.remove(i)
                print("Excluído com êxito.")
                break
    elif menu == 9:
        break