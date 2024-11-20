def resumo():
    mensagem = "Sobre Ada Lovelace"
    return mensagem


def quem_e():
    mensagem = (
        "Augusta Ada Byron King, atualmente conhecida como Ada Lovelace, nasceu em 10 de Dezembro de 1815, em Londres, Inglaterra. "
        "Ada foi uma matemática e escritora, responsável por escrever aquele que veio a ser conhecido como o primeiro algoritmo de computador da história. "
        "Filha de George Gordon Byron, 6º Barão de Byron (conhecido como Lord Byron), e Annabella Byron, Lady Wentworth, "
        "Lovelace teve uma infância abastada e muito confortável financeiramente, tendo se tornado ao longo de sua vida muito próxima da corte da rainha Vitória."
        #parte ket
        #Em 1842, um jovem matemático e engenheiro italiano, chamado Luigi Federico Menabrea, publicou em francês um manuscrito de uma palestra dada por ele na Universidade de Turim.
        #  Ada se dedicou a traduzir esse artigo por pelo menos um ano, tendo terminado em 1843 e adicionado algumas anotações no final do livro. Nessas tais anotações, 
        #  Ada discorre sobre como a Máquina Analítica poderia ser usada para alavancar o progresso da sociedade e não só realizar meros cálculos, além de em sua última nota, 
        # escrever um algoritmo para que a máquina pudesse computar a Sequência de Bernoulli. Esse feito foi posteriormente reconhecido pela academia científica como sendo o 
        #  primeiro programa de computador da história.
    )
    return mensagem

#def contribuicoes():
    #mensagem1 = ("Ada passou a ser conhecida como Ada Lovelace quando herdou o título de seus antepassados,"
    #            "os Barões de Lovelace. A partir desse evento, ela e seu marido, William Lord King, passaram a ser conhecidos como, "
    #            "Conde e Lady Lovelace. Ada morreu no dia 27 de Novembro de 1852, aos 36 anos, vítima de uma câncer de útero, deixando "
    #            "para trás um legado que serviu não apenas para alavancar a ciência da computação, mas também para inspirar dezenas de gerações de jovens cientistas que vieram depois dela.")
    #O artigo é mais famoso pelo apêndice final, Nota G. Ele demonstra a operação da máquina dando o exemplo do cálculo dos chamados 'números de Bernoulli', que surgem em muitos lugares na matemática moderna. Os números de Bernoulli são particularmente passíveis de cálculo de máquina porque são definidos recursivamente: podemos usar o primeiro para determinar o segundo, o segundo para o terceiro, e assim por diante. Existem várias maneiras diferentes de calcular esses números, e Lovelace não escolheu a mais simples: ela observou, em vez disso, que o "objeto não é simplicidade ou facilidade de computação
    #return mensagem


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
