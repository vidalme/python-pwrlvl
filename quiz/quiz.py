import json
import random

QUIZ_DATA = 'data.json'

# mensagem inicial
def open_message():
    print("***************************************")
    print("***************************************")
    print("***           Bem Vinda ao          ***")
    print("***            Super quiz           ***")
    print("***             MATILDA             ***")
    print("***************************************")
    print("***************************************")

def load_temas(data):    
    with open(data,'r',encoding='utf8') as dt:
        dt = json.load(dt)
        return dt['temas']

def escolhe_tema(tms):
    input_invalido = True
    while input_invalido:
        print("")
        print("Escolha o assunto do Quiz: ")
        # loop para criar as opçoes de tema baseado no json, acrescenta tb a caixinha com a letra associada para seleção
        letras = ord('A')
        for tm in tms:
            print(f" ( {chr(letras)} ) {tm['name']}")
            letras += 1
        print("")
        # guarda seleção do usuário e ja converte pra maiuscula para evitar conflitos de comparação
        letra_selecionada = input("").upper()
        print("")
        # checa se a opcao selecionada é valida
        if ( (len(letra_selecionada)>1) or ((ord(letra_selecionada) > ord('A')+len(tms)-1)) or (ord(letra_selecionada) < ord('A'))):
            print(f"***   A opção {letra_selecionada} é invalida!    ***") 
            print("")
            continue
        input_invalido = False
    # verifica o tema selecionado e retorna seu valor
    letras = ord('A')
    for tm in tms:
        if letra_selecionada == chr(letras):
            return tm
        letras+=1

def fim_jogo():
    print('Fim da Partida')
    print('( A ) jogar de novo')
    print('( Q ) para sair')
    inp = input('')
    if(inp.upper() == "A"):
        start_game()

def main_game(tema):

    #nome do tema para display
    name = tema['name']
    #total de rodadas maxima do jogo
    total_perguntas = len(tema['perguntas'])
    #valor da resposta correta
    valor = 10
    #a estrelinha bonita
    estrela = chr(9733)
    
    #contagem de perguntas que ja foram respondidas
    respondidas_perguntas = 0
    #acumula apos cada questao correta
    pontuacao = 0
    
    #alimentamos duas listas com todas as perguntas e repostas referente o tema dessa partida
    perguntas = []
    respostas = []
    for perg in tema['perguntas']:
        perguntas.append(perg['texto'])
        respostas.append(perg['respostas'])
    
    #texto de inicio da partida
    print(f"Vamos testar seu conhecimento em ### {name} ###!!")
        
    #loop da partida é aqui
    while respondidas_perguntas < total_perguntas:
        
        #escolhe um numer aleatorio para ser escolhido na lista de perguntas
        ale = random.randrange(0,len(perguntas))

        #com o numero aleatorio, seleciona a pergunta, item deve ser removido apos utilizar
        pergunta = perguntas[ale]
        

        #printa a pergunta da rodada
        print(f'{respondidas_perguntas+1}) {pergunta}')

        #salva a reposta correta antes de randomizar a ordem das respostas
        resposta_correta = respostas[ale][0].upper()
        #print(f"a resposta correta é: {resposta_correta}")

        #randomiza a ordem que as respostas vao ser displayed
        random.shuffle(respostas[ale])

        #display as respostas
        for resp in respostas[ale]:
            print(f"--> {resp}")
        
        #resposta do usuario
        resposta_player = input("Escreva sua resposta: ").upper()

        #se resposta for correta ganha pontos e uma mensagem de parabens
        if (resposta_player == resposta_correta):
            pontuacao += 1
            print('')
            print(f'Acertouuuu!!!!!')
            print(f'Voce tem um total de {pontuacao} estrela(s)!') 
            print('')
            print(f'{estrela*pontuacao}')
            print('')
        else:
            print('voce errou')
        
        perguntas.pop(ale)
        respostas.pop(ale)
        respondidas_perguntas +=1

        if respondidas_perguntas == total_perguntas:
            pass

    fim_jogo()    

def start_game():
    open_message()
    temas = load_temas(QUIZ_DATA)
    tema = escolhe_tema(temas)
    
    main_game(tema)

start_game()

