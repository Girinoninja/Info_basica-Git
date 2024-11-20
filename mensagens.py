def resumo():
    mensagem = "Sobre Ada Lovelace"
    return mensagem


def quem_e():
    mensagem = (
        "Augusta Ada Byron King, atualmente conhecida como Ada Lovelace, nasceu em 10 de Dezembro de 1815, em Londres, Inglaterra. "
        "Ada foi uma matemática e escritora, responsável por escrever aquele que veio a ser conhecido como o primeiro algoritmo de computador da história. "
        "Filha de George Gordon Byron, 6º Barão de Byron (conhecido como Lord Byron), e Annabella Byron, Lady Wentworth, "
        "Lovelace teve uma infância abastada e muito confortável financeiramente, tendo se tornado ao longo de sua vida muito próxima da corte da rainha Vitória."
  
    )
    return mensagem




def referencias():
    mensagem = ("https://www.sciencefocus.com/future-technology/how-ada-lovelaces-notes-on-the-analytical-engine-created-the-first-computer-program"
                "https://www.ufmg.br/espacodoconhecimento/ada-lovelace-a-primeira-programadora-da-historia/#:~:text=Aug%2010%C2%B7P%C3%ADlulas%20do%20Conhecimento&text=Augusta%20Ada%20Byron%20King%2C%20atualmente,algoritmo%20de%20computador%20da%20hist%C3%B3ria.")
    return mensagem


def citacoes():
    mensagem = ("Ela costumava dizer que a metafísica era tão importante quanto a matemática," 
                "sendo ambas ferramentas essenciais para investigar “mundos invisíveis ao nosso redor.”"
                "Já mais velha, Ada se tornou amiga do matemático britânico Charles Babbage, cooperando "
                "com ele em seu trabalho sobre uma Máquina Analítica, uma máquina que teria como propósito realizar cálculos utilizando determinadas funções.")
    return mensagem


def sair():
    mensagem = "\nObrigado pela leitura!"
    return mensagem


def erro():
    mensagem = "\nOpção inválida!"
    return mensagem


print("\nBoa noite! Você está aprendendo sobre  Ada Lovelace.\n")

continuar = True
while continuar == True:

    opcao = int(
        input(
"""
\nDigite o número correspondente ao menu que você deseja acessar:
1- Resumo
2 - Quem e
3 - Contribuições
4 - Citações
5 - Sair\n
"""
        )
    )

    if opcao == 1:
        print("1 - Resumo")
        mensagem = resumo()

    elif opcao == 2:
        print("2 - Quem e")
        mensagem = doutorado()

    elif opcao == 3:
        print("3 - Contribuições")
        mensagem = contribuicoes()

    elif opcao == 4:
        print("4 - Citações")
        mensagem = artigos()

    elif opcao == 5:
        mensagem = sair()
        continuar = False

    else:
        mensagem = erro()

    print(mensagem)
