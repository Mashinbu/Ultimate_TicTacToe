# Nome: Josué Marinho Hinrichs
# Matrícula: 496655

def matriz(lins, cols, val_inic): 
    #função para criar matriz intuitivamente
    m = [[val_inic] * cols for _ in range(lins)]
    return m

velha = matriz(3,3,' ') 
#matriz 3x3 usada para referenciar as coordenadas solicitadas (a tabela do jogo da velha é 3x3)

def tabela(): 
#uma função que imprime na tela a configuração mais recente da tabela. As posições onde ficarão os símbolos da velha fiicarão na matriz "velha"
    print('  A   B   C  ')
    print('1',velha[0][0],'|',velha[1][0],'|',velha[2][0],'1')
    print(' ---+---+--- ')
    print('2',velha[0][1],'|',velha[1][1],'|',velha[2][1],'2')
    print(' ---+---+--- ')
    print('3',velha[0][2],'|',velha[1][2],'|',velha[2][2],'3')
    print('  A   B   C')
    print('')

def checagem(): 
    #uma função que verifica se algum dos jogadores ganhou/vai ganhar a rodada
    auxiliar = matriz(3,3,' ')  
    #esta matriz vai ajudar para o programa não identificar uma única possibilidade de ganhar como duas. Ex: 2 "X" e um branco em uma coluna, 2 "X" e um branco em uma linha, mas o branco dessas duas possibilidades é o mesmo, ou seja, é apenas uma possibilidade.
    fechou=False 
    #se algum dos jogadores tiver ganho, "fechou" será True, e então a função irá retornar True e a condição de vitória terá sido atiginda
    possibilidade_x=0 
    #essa variável armazena o número de possibilidades do jogador do símbolo "X" ganhar
    possibilidade_o=0 
    #essa é o número de possibilidades do jogador do símbolo "O" ganhar
    #se alguma dessas variáveis de possibilidade for maior que 1, é porque o jogador do símbolo respectivo tem duas possibilidades de ganhar.
    if (velha[0][0]==velha[1][1] and velha[1][1]==velha[2][2] and velha[1][1]!=' ') or (velha[2][0]==velha[1][1] and velha[1][1]==velha[0][2] and velha[1][1]!=' '): 
        #esse if verifica caso alguma das diagonais foi preenchida.
        fechou=True
        return (fechou,possibilidade_o,possibilidade_x)
    else:
        for i in range(3): 
            #esse for serve para identificar se alguma linha ou coluna foi totalmente preenchida por algum símbolo
            if velha[i][0]==velha[i][1] and velha[i][1]==velha[i][2] and velha[i][1]!=' ':
                fechou=True
                return (fechou,possibilidade_o,possibilidade_x)
            elif velha[0][i]==velha[1][i] and velha[1][i]==velha[2][i] and velha[1][i]!=' ':
                fechou=True
                return (fechou,possibilidade_o,possibilidade_x)
    for i in range(3): 
        contagem_vazio=0 
        #essas váriaveis armazenam, respectivamente, a quantidade de espaços em branco, o número de símbolos "X" e o número de símbolos "O", que são todos inicialmente 0, pois não houve contagem ainda
        contagem_x=0
        contagem_o=0
        for j in range(3):  
            #esses ifs vão contabilizar o número de cada símbolo e de vazio em cada COLUNA
            if velha[i][j]=='X':
                contagem_x += 1
            elif velha[i][j]=='O':
                contagem_o += 1
            else:
                contagem_vazio += 1
                local_vazio=j   
                #ao identificar o vazio, ele guarda o valor "j" no qual ele foi identificado, para a situação de duas possibilidades serem na verdade uma só.
            

        #se ocorrer dois símbolos iguais e um vazio em alguma coluna, há uma possibilidade do jogador com o respectivo símbolo que se repetiu ganhar, e então a variável de possibilidade aumenta em 1:
        if contagem_vazio==1 and contagem_x==2 and auxiliar[i][local_vazio]==' ':
            possibilidade_x += 1
            auxiliar[i][local_vazio]='o'  
            #na matriz "auxiliar", o vazio é preenchido com um "o", para mostrar que aquele espaço já é de uma possibilidade.
        elif contagem_vazio==1 and contagem_o==2 and auxiliar[i][local_vazio]==' ':
            possibilidade_o += 1
            auxiliar[i][local_vazio]='o'

        #já aqui será contabilizado cada símbolo e cada vazio em cada LINHA, e por isso os valores de contagem são reiniciados para 0
        contagem_vazio=0
        contagem_x=0
        contagem_o=0
        for j in range(3):
            if velha[j][i]=='X':
                contagem_x += 1
            elif velha[j][i]=='O':
                contagem_o += 1
            else:
                contagem_vazio += 1
                local_vazio=j

        #de modo similiar,ao ocorrer dois símbolos iguais e um vazio em alguma linha, há uma possibilidade do jogador com o respectivo símbolo que se repetiu ganhar e então a variável de possibilidade aumenta em 1:
        if contagem_vazio==1 and contagem_x==2 and auxiliar[local_vazio][i]==' ':
            auxiliar[local_vazio][i]='o'
            possibilidade_x += 1
        elif contagem_vazio==1 and contagem_o==2 and auxiliar[local_vazio][j]==' ':
            auxiliar[local_vazio][i]='o'
            possibilidade_o += 1
        
    #o caso das duas diagonais é separado do "for" das linhas e das colunas, pois é um pouco diferente devido às "coordenadas" de cada uma das diagonais
    contagem_vazio=0 
    contagem_x=0
    contagem_o=0
    for i in range(3):
        if velha[i][i]=='X':
            contagem_x += 1
        elif velha[i][i]=='O':
            contagem_o += 1
        else:
            contagem_vazio += 1
            local_vazio=i
    if contagem_vazio==1 and contagem_x==2 and auxiliar[local_vazio][local_vazio]==' ':
        auxiliar[local_vazio][local_vazio]='o'
        possibilidade_x += 1
    elif contagem_vazio==1 and contagem_o==2 and auxiliar[local_vazio][local_vazio]==' ':
        auxiliar[local_vazio][local_vazio]='o'
        possibilidade_o += 1

    #processo similar para a outra diagonal:
    contagem_vazio=0
    contagem_x=0
    contagem_o=0
    j=2 
    #"j" é simplesmente uma auxiliar de "i"
    for i in range(3):
        if velha[i][j]=='X':
            contagem_x += 1
        elif velha[i][j]=='O':
            contagem_o += 1
        else:
            contagem_vazio += 1
            local_vazio=i
            local_vazio_j=j
        j-=1
    if contagem_vazio==1 and contagem_x==2 and auxiliar[local_vazio][local_vazio_j]==' ':
        auxiliar[local_vazio][local_vazio_j]='o'
        possibilidade_x += 1
    elif contagem_vazio==1 and contagem_o==2 and auxiliar[local_vazio][local_vazio_j]==' ':
        auxiliar[local_vazio][local_vazio_j]='o'
        possibilidade_o += 1

    return (fechou,possibilidade_o,possibilidade_x) 
    #ao final da função, são retornados os valores de "fechou" e a quantidade de possibilidades de cada um dos dois símbolos de ganhar.
    
def entrada_valida(): 
    #essa função será utilizada toda vez que algum usuario tiver que entrar as coordenadas, para verificar se a entrada é válida ou não.
    valida=False 
    #"valida" se torna True se/quando o usuário digitar uma entrada válida.
    while valida==False: 
        #enquanto a entrada não for válida, "valida" será False, e será solicitado um novo input.
        coordenada=input()   
        #primeiramente, é solicitada a entrada de uma coordenada pelo jogador.
        #a sequência de "replace" a seguir remove caracteres indesejados do input, para ser aceito um escopo maior de entradas.
        coordenada = coordenada.replace(" ","")
        coordenada = coordenada.replace("-","")
        coordenada = coordenada.replace("_","")
        coordenada = coordenada.replace("/","")
        coordenada = coordenada.replace("(","")
        coordenada = coordenada.replace(")","")
        coordenada = coordenada.replace(",","")
        coordenada = coordenada.replace("0","")
        coordenada = coordenada.replace("x","")
        coordenada = list(coordenada)   
        #"coordenada" se torna um vetor com cada caractere mantido após a limpeza sendo um dos elementos.
        tamanho = len(coordenada) 
        #a função "len()" retorna o tamanho de um vetor, nesse caso, o tamanho de "coordenada". Assim, podemos determinar facilmente um "for" que percorra cada posição do vetor.
        
        for i in range(tamanho):    
            #para cada posição do vetor "coordenada", iremos trocar a string pelo seu correspondente inteiro, caso seja algum dos 3 números válidos. Isso vai ajudar para determinar casos de entrada "letra, letra" e "número,número".
            if coordenada[i]=='1':
                coordenada[i]=1
            elif coordenada[i]=='2':
                coordenada[i]=2
            elif coordenada[i]=='3':
                coordenada[i]=3

        if tamanho!=2 or type(coordenada[0])==type(coordenada[1]):   
            #se houverem mais ou menos de dois elementos ou elementos de tipos iguais, a entrada é inválida. Isso serve para não aceitar inputs "a", "33", "AB", "BA2", por exemplo.
            print('Entrada inválida! Entre uma coordenada válida:')
        else:
            caractere=False
            for i in range(2):
                if coordenada[i]==1 or coordenada[i]==2 or coordenada[i]==3 or coordenada[i]=='A' or coordenada[i]=='a' or coordenada[i]=='B' or coordenada[i]=='b' or coordenada[i]=='C' or coordenada[i]=='c': #Para cada uma das duas posições, verifico se é um dos caracteres válidos. Se sim, "continuar" se torna True, e as coordenadas podem prosseguir.
                    caractere=True

            if type(coordenada[0])==int:  
                #nesse if, caso a ordem esteja (número, letra), eu inverto para (letra, número). Eu detecto isso por meio do "type()", que retorna o tipo.
                temp=coordenada[1] 
                #"temp" é apenas uma váriavel auxiliar para que o valor entre duas variáveis possa ser trocado.
                coordenada[1]=coordenada[0]
                coordenada[0]=temp

            for i in range(2):  
                #transformando cada letra na sua respectiva coordenada da nossa matriz "velha".
                if coordenada[i]=='a' or coordenada[i]=='A' or coordenada[i]==1:
                        coordenada[i]=0
                elif coordenada[i]=='b' or coordenada[i]=='B' or coordenada[i]==2:
                        coordenada[i]=1
                else:
                    coordenada[i]=2
            if caractere == False: 
                print('Entrada inválida! Entre uma coordenada válida:')
            elif velha[coordenada[0]][coordenada[1]] != ' ':    
                #caso a coordenada escolhida já tenha sido utilizada na rodada, será solicitado um novo input.
                print('Espaço já preenchido! Entre uma coordenada válida:')
            else:
                valida=True  
                #"valida" se torna True, caso TODAS as condições de entrada sejam respeitadas, terminando, então, o loop do while.
    return(coordenada[0],coordenada[1]) 
    #retorno os valores das coordenadas validadas.

def jogo(): 
    #a função "jogo" vai conter a parte principal do nosso programa.

    #solicito um input de símbolo para o Jogador 1, que pode ser "O" ou "X". O símbolo que sobrar vai para o Jogador 2. Cada símbolo respectivo é armazenado nas variáveis "simbolo_1" e "simbolo_2"
    print('Bem vindo ao Jogo da Velha! Entre o símbolo desejado para o Jogador 1 ("X" ou "O"):')
    valido=False
    while valido==False:    
        #caso o usuario entre um valor inválido para o símbolo do jogador 1, o programa forçará uma nova entrada até que esta seja válida.
        simbolo_1=input()
        if simbolo_1=='X' or simbolo_1=='x':
            print('Muito bem! O Jogador 1 fica com o "X" e o Jogador 2 com o "O"')
            simbolo_1 = 'X'
            simbolo_2 = 'O'
            valido=True
        elif simbolo_1=='O' or simbolo_1=='o':
            print('Muito bem! O Jogador 1 fica com o "O" e o Jogador 2 com o "X"')
            simbolo_1 = 'O'
            simbolo_2='X'
            valido=True
        else:
            print('Entrada inválida! Entre "X" ou "O" para o símbolo do jogador 1:')
    

    continuar = True 
    #continuar vira False caso os jogadores não queiram uma nova rodada, assim, o while abaixo, não rodará. 
    placar1=0 
    #placar de cada jogador, e o número de empates. Inicialmente possuem o valor 0.
    placar2=0
    empate=0
    rodada=0 
    #contar o número de rodadas que já ocorreram, será exibido junto ao placar.

    #enquanto "continuar" for True, uma nova rodada será iniciada.
    while continuar: 
        #nesse while está contido a rodada. Será executado o número de rodadas que os jogadores definirem: ao final de cada rodada, o programa verifica se o jogo deve continuar em uma nova rodada, reiniciar, ou terminar.
        for i in range(3): 
            #esses "for" resetam a matriz que contém os inputs, tornando a tabela vazia novamente a cada rodada.
            for j in range(3):
                velha[i][j]=' '
        tabela() 
        #"chama" a função "tabela()", que exibe na tela a configuração da tabela.
        
        terminada=False 
        #"terminada" muda para True caso a rodada tiver terminado
        ganhar=False 
        #a variável "ganhar" serve para verificar se algum dos jogadores ganhou, ou se houve empate. Se ganhar for True, houve vitória e a rodada poderá ser finalizada. Seu valor depende da função "checagem()".
        jogadas=0  
        #a variável "jogadas" conta o número de jogadas, para verificar se houve empate. Se jogadas > 9, houve empate.
        possibilidade_x = 0 
        #as variáveis "possibilidade_" armazenam o nº de possibilidades do jogador com o símbolo "X" e do jogador "O" ganhar. Seus valores vão depender da função "checagem()".
        possibilidade_o = 0
        while terminada==False: 
            #"terminada" vira True apenas quando a rodada acabar, só assim o while termina.
            if ganhar==False:   
                #caso o Jogador 2 não tenha ganho, o caminho é esse.
                #os valores das variáveis "possibilidade_o" e "possibilidade_x" vão impactar somente o jogador seguinte, exibindo uma mensagem caso o outro jogador já vá ganhar.
                if possibilidade_o >=2 and simbolo_1=='X' and possibilidade_x<1:    
                    #o aviso só se concretiza se o jogador não tiver nenhuma possibilidade de fechar, logicamente.
                    print('ATENÇÃO - Você já perdeu, o JOGADOR 2 tem ao menos duas possibilidades de fechar ----------------------------------')
                elif possibilidade_x >=2 and simbolo_1=='O' and possibilidade_o<1:
                    print('ATENÇÃO - Você já perdeu, o JOGADOR 2 tem ao menos duas possibilidades de fechar ----------------------------------')
                print('JOGADOR 1 (' + simbolo_1 + '), entre as coordenadas:') 
                #é solicitado, então, o input do jogador, no caso, do Jogador 1.
                x1,y1 = entrada_valida() 
                #o input é solicitado dentro da função "entrada_valida()", que vai avaliar as entradas. Quando forem validadas, os dois valores de coordenadas serão armazenados em "x1" e em "y1".
                velha[x1][y1] = simbolo_1   
                #assim, o endereço [x1][y1] da matriz "velha" vai receber o símbolo, nesse caso, do Jogador 1.
                print('')
                tabela()
                ganhar,possibilidade_o,possibilidade_x = checagem() 
                #ao final de cada jogada, vai acontecer a verificação de vitória ou de iminência de vitória por meio da função "checagem()", cujos valores retornados determinarão as variáveis "ganhar","possibilidade_o" e "possibilidade_x".
                jogadas += 1  
                #também ao final de cada jogada, a variável jogada recebe +1.
            else:  
                #se "ganhar" não for False, é porque o Jogador 2, e então "terminada" se torna True, pois a rodada deve terminar. Assim, 1 é somado ao placar do Jogador 2.
                print("JOGADOR 2 ganhou essa rodada!!")
                placar2+=1
                terminada=True

            #se o número de jogadas for igual a 9, todos os valores da tabela foram preenchidos. Se "ganhar" for False, é porque não houve vencedores. Assim, ocorre o empate e a rodada acaba("terminada" vira True).
            if jogadas==9 and ganhar==False:
                print("Empate! Não há vencedores nessa rodada.")
                empate+=1
                terminada=True
                ganhar=True

            #o processo ocorre de modo similar para o Jogador 2.
            if ganhar==False:
                if possibilidade_o >=2 and simbolo_1=='O' and possibilidade_x<1:
                    print('ATENÇÃO - Você já perdeu, o JOGADOR 1 tem ao menos duas possibilidades de fechar ----------------------------------')
                elif possibilidade_x >=2 and simbolo_1=='X' and possibilidade_o<1:
                    print('ATENÇÃO - Você já perdeu, o JOGADOR 1 tem ao menos duas possibilidades de fechar ----------------------------------')
                print('JOGADOR 2 (' + simbolo_2 + '), entre as coordenadas:')
                x2,y2=entrada_valida()
                velha[x2][y2]=simbolo_2
                print('')
                tabela()
                ganhar,possibilidade_o,possibilidade_x=checagem()
                jogadas+=1
            else:
                #se "terminada" já for True, é porque o Jogador 1 ganhou.
                if terminada==False:
                    print("JOGADOR 1 ganhou essa rodada!!")
                    placar1+=1
                    terminada=True
            

        rodada += 1
        #ao final de uma rodada, é mostrado o placar e perguntado se os jogadores desejam jogar mais uma rodada ou reiniciar o jogo.
        print('')
        print('O placar atual é:')
        print('JOGADOR 1 - %d | JOGADOR 2 - %d | EMPATES - %d | RODADAS - %d' %(placar1,placar2,empate,rodada))
        print('')
        print('Deseja jogar mais uma rodada? (S/N)')
        deseja = input()
        if deseja=='N' or deseja=='n' or deseja == 'nao' or deseja=='Não' or deseja=='não' or deseja == 'ñ' or deseja=='NÂO' or deseja=='NAO':
            continuar = False   
            #se o jogador escolher não jogar uma nova rodada, "continuar" vira False, encerrando o loop do while. Caso contrário, "continuar" ainda é True, e o while recomeça o processo da rodada.
            print('')
            print('O placar final ficou:')
            print('JOGADOR 1 - %d | JOGADOR 2 - %d | EMPATES - %d | RODADAS - %d' %(placar1,placar2,empate,rodada))
            print('')
            if placar1>placar2:
                print('PARABÉNS JOGADOR 1! Você ganhou o jogo com %d vitória(s).' %placar1)
            elif placar2>placar2:
                print('PARABÉNS JOGADOR 2! Você ganhou o jogo com %d vitória(s).' %placar2)
            else:
                print('O JOGO EMPATOU!')
            print('')
            print('Você gostaria de reiniciar o jogo e jogar novamente? (S/N)')
            deseja = input()
            print('')
            if deseja=='S' or deseja=='s' or deseja=='sim' or deseja=='Sim' or deseja =='SIM':
                print('Jogo reiniciado!--------------------------------------------------------------')
                print('')
                jogo()  
                #se o jogador optar por reiniciar o jogo, a função "jogo()" é executada novamente
            else:
                print('Até a próxima!  ----------------------------------------------------------------')
        else:
            print('Nova rodada iniciada!-------------------------------------------------------------')
            print('')

jogo()
