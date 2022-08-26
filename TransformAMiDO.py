######################################################################################################

# TransformAMiDO: Transformando TSV em CSV

######################################################################################################

# Importação de Módulos


import easygui as eg
import pandas as pd

######################################################################################################

# Funções

def pega_arquivo():
    arquivo = eg.fileopenbox()

    return arquivo

def tsv_to_csv(arquivo):
    tsv_csv = pd.read_table(arquivo, sep='\t')
    tsv_csv.to_csv(arquivo, index=False)

    pass


######################################################################################################

# Programa

imagem = 'C:\\Users\\jmarc\\PycharmProjects\\AMiDO\\AMiDO Pixel Art\\AMiDO (resize).png'
msg1 = 'Olá! Eu sou o TransformAMiDO (Transformador do Analisador Mecânico-inteligente de Dados Ordenados).'
escolhas1 = ['Continuar', 'Sair']

resposta1 = eg.buttonbox(msg1, 'TransformAMiDO - "Hello and, again, welcome to the Aperture Science '
                               'computer-aided enrichment '
                               'center"', image=imagem, choices=escolhas1)

if resposta1 == 'Continuar':
    pass
if resposta1 == 'Sair':
    exit(0)

msg2 = 'Estou aqui para transformar seus dados de um formato para outro (EX.: TSV em CSV).\n' \
       'Para começar, selecione um arquivo no botão abaixo.'
escolhas2 = ['Selecionar Arquivo', 'Sair']

resposta2 = eg.buttonbox(msg2, 'TransformAMiDO - "An escape hatch will open in three... Two... One."',
                         choices=escolhas2)

if resposta2 == 'Selecionar Arquivo':
    arquivo = pega_arquivo()
    print("-" * 120)
    print('')
    print('TransformAMiDO (Transformador do Analisador Mecânico-inteligente de Dados Ordenados)')
    print('')
    print("-" * 120)
    print('')
    print('Diretório: ' + arquivo)
    print('')
    print("-" * 120)
    pass

if resposta2 == 'Sair':
    exit(0)

msg3 = 'Ótimo! Aqui está o diretório do arquivo.\n' \
       'Ele está sendo mostrado no console do Python.'
escolhas3 = ['Continuar', 'Sair']

resposta3 = eg.buttonbox(msg3, 'AMiDO - "Your specimen has been processed..."', choices=escolhas3)

if resposta3 == 'Continuar':
    pass
if resposta3 == 'Sair':
    exit(0)

msg4 = 'Então, que tipo de transformação faremos hoje?'
escolhas4 = ['TSV para CSV', 'Dummy']

resposta4 = eg.choicebox(msg4, 'AMiDO - "... and we are now ready to begin the test proper"', choices=escolhas4)

if resposta4 == 'TSV para CSV':
    tsv_to_csv(arquivo)

    msg5 = 'Pronto! Agora seu arquivo TSV é do tipo CSV.\n' \
            'Ele foi salvo exatamente com o mesmo nome no mesmo diretório de antes.\n' \
            'Espero ter te ajudado. Até mais!'
    escolhas5 = ['Sair']

    resposta5 = eg.buttonbox(msg5, 'AMiDO - "Now I only wnat you gone"', choices=escolhas5)

    if resposta5 == 'Sair':
        exit(0)

if resposta4 == 'Dummy':
    exit(0)

######################################################################################################