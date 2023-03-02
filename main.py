import pandas as pd
#----------INÍCIO Quadro-----------------------------------------------------------------------------------------------------------------------------
menu3 = { "|              Adicionais              |": ["| 0 - Não desejo mais nada (encerrar)  |", "| 1- Passar 10 peças de roupas         |", "| 2- Limpeza de 1 Forno/Micro-ondas    |", "| 3- Limpeza de 1 Geladeira/Freezer    |"],
            " Valor (R$) |": [" R$ 0,00  |", "  R$ 10,00 |", " R$ 12,00 |", " R$ 20,00 |"]
        }
#----------FIM Quadro---------------------------------------------------------------------------------------------------------------------------------
#----------INÍCIO Funções ------------------------------------------------------------------------------------------------------------------------------------
#----------INÍCIO Função metragem_limpeza---------------------------------------------------------------------------------------------------------------------
def metragem_limpeza():

    print("--------------------MENU 1 de 3 - Metragem Limpeza--------------------")
    while True:
        try:
            metragem = int(input("Digite a metragem que deverá ser limpa: "))
            if metragem >= 30 and metragem <= 300:
                return 60 + 0.3 * metragem
            elif metragem >= 300 and metragem <= 700:
                return 120 + 0.5 * metragem
            else:
                print("Não aceitamos áreas com metragem menor que 30m² ou maior que 700m², por favor digite uma metragem válida!")
                continue    
        except ValueError:
            print("Valor inválido, por favor, tente novamente utilizando números inteiros.")
#----------FIM Função metragem------------------------------------------------------------------------------------------------------------------
#----------INÍCIO Função tipos_limpeza-----------------------------------------------------------------------------------------------------------
def tipos_limpeza():
    while True:
        print("--------------------MENU 2 de 3 - Tipos de Limpeza--------------------")
        print("B – Básica - Indicada para sujeiras semanais ou quinzenais. \nC – Completa (30% mais cara)- Indicada para sujeiras antigas e/ou não rotineiras.")
        tipos = input("Digite a opção que corresponde com o tipo de limpeza que melhor irá lhe servir. (B/C):").strip().upper()[0]
        if tipos == "B":
            return 1.00
        elif tipos == "C":
            return 1.30
        else:
            print("Opção inválida, por favor entre com uma opção válida!")
            continue
#----------FIM Função tipo_limpeza--------------------------------------------------------------------------------------------------------------
#----------INÍCIO Função adicional_limpeza------------------------------------------------------------------------------------------------------
def adicional_limpeza():
    mais = 0
    while True:
        adicional = int(input("Digite uma das opções correspondente: "))
        if adicional == 0:
            return mais
        elif adicional == 1:
            mais = mais + 10
            continue
        elif adicional == 2:
            mais = mais + 12
            continue
        elif adicional == 3:
            mais = mais + 20
            continue
        else:
            print("Opção inválida, por favor entre com uma opção válida!")
#----------FIM Função adicional_limpeza---------------------------------------------------------------------------------------------------------
#----------Programa Principal ---------------------------------------------------------------------------------------------------------------------------------
print("Boas-vindas ao programa de serviços de limpeza do Alessandro Aguiar da Silva")
ml = metragem_limpeza()
print(ml)
tp = tipos_limpeza()
print(tp)
menu3_df = pd.DataFrame(menu3)
print(menu3_df)
al = adicional_limpeza()
print(al)
total = (ml * tp) + al
print(f"TOTAL: R$ {total :.2f} (Metragem: R$ {ml :.2f} + Tipo de Limpeza R$ {tp :.2f} + Adicional R$ {al :.2f})")
print("Volte sempre!")
#----------FIM ---------------------------------------------------------------------------------------------------------------------------------