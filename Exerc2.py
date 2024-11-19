#Neste desafio, você irá explorar as aplicações 
# práticas da Inteligência Artificial (IA) em diversos setores. 
# A IA está sendo utilizada para resolver problemas reais 
# e melhorar processos em áreas como agricultura, finanças,
#  varejo e recursos humanos. Seu objetivo será associar 
# corretamente cada aplicação prática da IA com sua descrição 
# correspondente, aprofundando seu entendimento sobre como essa
# tecnologia está sendo aplicada no dia a dia.

#Não se preocupe com a linguagem de programação, pois o 
# foco aqui é entender os conceitos. Aproveite para explorar
#  uma das linguagens suportadas pela IA.

#Entrada
#A entrada consistirá na aplicação prática da IA 
# para a qual você deve retornar a descrição. Nesse contexto, 
# os seguintes conceitos são considerados válidos para este desafio de código:
#"agricultura"
#"finanças"
#"varejo"
#"recursos humanos"
##Saída
#A saída esperada é a descrição associada ao conceito fornecido como entrada. 
# Seguem as saídas possíveis, listadas aleatoriamente, para que 
# você possa analisar e associar corretamente considerando o 
# template de código deste desafio:

# Recebe a Entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber uma área de aplicação e retornar sua respectiva descrição.
def descrever_aplicacao(conceito):
    if conceito == "agricultura":
        return "monitoramento de culturas e previsão de colheitas"
        
    # COMPLETE AQUI: Preencha corretamente cada área de aplicação, considerando as descrições abaixo:                               
    elif conceito == "recursos humanos":
        return "seleção automatizada de candidatos e análise de desempenho"
        
    elif conceito == "varejo":
        return "personalização de ofertas e gestão de estoque"
                
    elif conceito == "finanças":
        return "detecção de fraudes e análise de crédito"   
        
# Imprime a descrição da aplicação na área recebido na "entrada" através da função "descrever_aplicacao". 
print(descrever_aplicacao(entrada))