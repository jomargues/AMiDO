######################################################################################################

# AMiDO (Analisador Mecânico-inteligente de Dados Ordenados)

######################################################################################################

# Importação de Módulos

import easygui as eg
import matplotlib.pyplot as plt
import pandas as pd
import scipy.signal as sp

######################################################################################################

# Funções

def pega_arquivo():
    arquivo = eg.fileopenbox()

    return arquivo


def df(arquivo):
    df = pd.read_csv(str(arquivo), index_col=False)

    return df


def t_normalizacao(df, coluna):
    df1 = df[coluna]
    df.loc[:, coluna] = df[coluna].apply(lambda x: x - df1[0])

    return df


def m_normalizacao(df, coluna):
    df.loc[:, coluna] = df[coluna].apply(lambda x: x - df[coluna].mean())

    return df


def grafico(df, titulo, x, nome_x, y, nome_y):
    t = df[x].values
    f = df[y].values

    plt.plot(t, f)

    plt.xlabel(nome_x)
    plt.ylabel(nome_y)
    plt.title(titulo)

    return plt.show()


def graf_hist(df, titulo, x, nome_x, y, nome_y, bins):
    t = df[x].values
    f = df[y].values

    fig = plt.figure()

    ax1 = fig.add_subplot(2, 1, 1)
    ax1.set_xlabel(nome_x)
    ax1.set_ylabel(nome_y)
    plt.plot(t, f)
    plt.title(titulo)

    ax2 = fig.add_subplot(2, 1, 2)
    ax2.set_xlabel(nome_y)
    ax2.set_ylabel("Frequência")
    plt.hist(f, bins=bins)

    return plt.show()


def graf_aprox(df, titulo, x, nome_x, y, nome_y, pontos, grau):
    t = df[x].values
    f = df[y].values
    fm = sp.savgol_filter(f, pontos, grau)

    plt.plot(t, f)
    plt.plot(t, fm, color='r')

    plt.xlabel(nome_x)
    plt.ylabel(nome_y)
    plt.title(titulo)

    return plt.show()


def graf_hist_gauss(df, titulo, x, nome_x, y, nome_y, bins):
    t = df[x].values
    f = df[y].values

    fig = plt.figure()

    ax1 = fig.add_subplot(2, 1, 1)
    ax1.set_xlabel(nome_x)
    ax1.set_ylabel(nome_y)
    plt.plot(t, f)
    plt.title(titulo)

    ax2 = fig.add_subplot(2, 1, 2)
    ax2.set_xlabel(nome_y)
    ax2.set_ylabel("Frequência")
    plt.hist(f, bins=bins)
    ax2a = ax2.twinx()
    ax2a.set_ylabel("Densidade")
    df[y].plot.density(color='r')

    return plt.show()


def graf_aprox_hist_gauss(df, titulo, x, nome_x, y, nome_y, pontos, grau, bins):
    t = df[x].values
    f = df[y].values
    fm = sp.savgol_filter(f, pontos, grau)

    fig = plt.figure()

    ax1 = fig.add_subplot(2, 1, 1)
    ax1.set_xlabel(nome_x)
    ax1.set_ylabel(nome_y)
    plt.plot(t, f)
    plt.plot(t, fm, color='r')
    plt.title(titulo)

    ax2 = fig.add_subplot(2, 1, 2)
    ax2.set_xlabel(nome_y)
    ax2.set_ylabel("Frequência")
    plt.hist(f, bins=bins)
    ax2a = ax2.twinx()
    ax2a.set_ylabel("Densidade")
    df[y].plot.density(color='r')

    return plt.show()


######################################################################################################

# Interface e Funcionalidade

imagem = 'C:\\Users\\jmarc\\PycharmProjects\\AMiDO\\AMiDO Pixel Art\\AMiDO (resize).png'
msg1 = 'Olá! Eu sou o AMiDO (Analisador Mecânico-inteligente de Dados Ordenados).'
escolhas1 = ['Continuar', 'Sair']

resposta1 = eg.buttonbox(msg1, 'AMiDO - "Hello and, again, welcome to the Aperture Science computer-aided enrichment '
                               'center"', image=imagem, choices=escolhas1)

if resposta1 == 'Continuar':
    pass
if resposta1 == 'Sair':
    exit(0)

msg2 = 'Estou aqui para fazer a análise dos seus dados experimentais - manipulações, plots, etc.\n' \
       'Para começar, selecione um arquivo no botão abaixo.'
escolhas2 = ['Selecionar Arquivo', 'Sair']

resposta2 = eg.buttonbox(msg2, 'AMiDO - "An escape hatch will open in three... Two... One."', choices=escolhas2)

if resposta2 == 'Selecionar Arquivo':
    arquivo = pega_arquivo()
    df = df(arquivo)
    print("-" * 120)
    print('')
    print('AMiDO (Analisador Mecânico-inteligente de Dados Ordenados)')
    print('')
    print("-" * 120)
    print('')
    print('Diretório: ' + arquivo)
    print('')
    print("-" * 120)
    print('')
    print('DataFrame:')
    print('')
    with pd.option_context('display.max_columns', None):
        print(df)
    print('')
    print("-" * 120)
    print('')
    print('Análise Estatística:')
    print('')
    with pd.option_context('display.max_columns', None):
        print(df.describe())
    print('')
    print("-" * 120)
    pass

if resposta2 == 'Sair':
    exit(0)

msg3 = 'Ótimo! Fiz um DataFrame com o seu arquivo para facilitar nosso trabalho.\n' \
       'Ele está sendo mostrado no console do Python.\n' \
       'Mantenha essa tabela em mãos porque precisaremos dela depois.\n' \
       'Além disso, também já exibi os dados estatísticos desse dataframe.'
escolhas3 = ['Continuar', 'Sair']

resposta3 = eg.buttonbox(msg3, 'AMiDO - "Your specimen has been processed..."', choices=escolhas3)

if resposta3 == 'Continuar':
    pass
if resposta3 == 'Sair':
    exit(0)

msg4 = 'Então, no que posso te ajudar hoje?'
escolhas4 = ['Analisar dados', 'Plotar dados']

resposta4 = eg.buttonbox(msg4, 'AMiDO - "... and we are now ready to begin the test proper"', choices=escolhas4)

if resposta4 == 'Analisar dados':
    msg5a = 'Eu consigo realizar as seguintes magias nos seus dados.'
    escolhas5a = ['Subtrair o valor médio de uma coluna de todos os valores dela',
                  'Subtrair o primeiro valor de uma coluna de todos os valores dela']

    resposta5a = eg.choicebox(msg5a, 'AMiDO - "Let\'s see what the next test is"', choices=escolhas5a)

    if resposta5a == 'Subtrair o valor médio de uma coluna de todos os valores dela':
        msg5aa = 'Então, me diga em qual coluna realizarei a mágica.'
        escolhas5aa = ['Nome da coluna']

        resposta5aa = eg.enterbox(msg5aa, 'AMiDO - "Subject name here"')

        df = m_normalizacao(df, resposta5aa)

        print('')
        print('DataFrame (M-normalizado):')
        print('')
        with pd.option_context('display.max_columns', None):
            print(df)
        print('')
        print("-" * 120)

        msg5ab = 'Seu novo Dataframe foi colocado no console do Python.\n' \
                 'Podemos salvá-lo com um novo nome, se você quiser.'
        escolhas5ab = ['Salvar Arquivo', 'Sair']

        resposta5ab = eg.buttonbox(msg5ab, 'AMiDO - "You did it! '
                                           'The Weighted Companion Cube certainly brought you good luck"', escolhas5ab)

        if resposta5ab == 'Salvar Arquivo':

            arquivo1 = eg.filesavebox(default=arquivo, filetypes='*.txt')

            df.to_csv(arquivo1, index=False)

            msg5ac = 'Pronto! Seu arquivo foi salvo com as alterações que você fez.\n' \
                     'Espero ter te ajudado com a análise dos seus dados.\n ' \
                     'Até!'
            escolhas5ac = ['Sair']

            resposta5ac = eg.buttonbox(msg5ac, 'AMiDO - "Now, I only want you gone."', escolhas5ac)

            if escolhas5ac == 'Sair':
                exit(0)

    if resposta5a == "Subtrair o primeiro valor de uma coluna de todos os valores dela":
        msg5ba = 'Então, me diga em qual coluna realizarei a mágica.'
        escolhas5ba = ['Nome da coluna']

        resposta5ba = eg.enterbox(msg5ba, 'AMiDO - "Subject name here"')

        df = t_normalizacao(df, resposta5ba)

        print('')
        print('DataFrame (T-normalizado):')
        print('')
        with pd.option_context('display.max_columns', None):
            print(df)
        print('')
        print("-" * 120)

        msg5bb = 'Seu novo Dataframe foi colocado no console do Python.\n' \
                 'Podemos salvá-lo com um novo nome, se você quiser.'
        escolhas5bb = ['Salvar Arquivo', 'Sair']

        resposta5bb = eg.buttonbox(msg5bb, 'AMiDO - "You did it! '
                                           'The Weighted Companion Cube certainly brought you good luck"', escolhas5bb)

        if resposta5bb == 'Salvar Arquivo':

            arquivo1 = eg.filesavebox(default=arquivo, filetypes='*.txt')

            df.to_csv(arquivo1, index=False)

            msg5bc = 'Pronto! Seu arquivo foi salvo com as alterações que você fez.\n' \
                     'Espero ter te ajudado com a análise dos seus dados.\n ' \
                     'Até!'
            escolhas5bc = ['Sair']

            resposta5bc = eg.buttonbox(msg5bc, 'AMiDO - "Now, I only want you gone."', escolhas5bc)

            if resposta5bc == 'Sair':
                exit(0)

if resposta4 == 'Plotar dados':
    msg5ca = 'Eu consigo realizar as seguintes magias nos seus dados.'
    escolhas5ca = ['Plot puro',
                  'Plot + Histograma',
                  'Plot + Aproximação (filtro savgol)',
                  'Plot + Histograma + Densidade',
                  'Plot + Aproximação (filtro savgol) + Histograma + Densidade']

    resposta5ca = eg.choicebox(msg5ca, 'AMiDO - "Let\'s see what the next test is"', choices=escolhas5ca)

    if resposta5ca == 'Plot puro':

        msg5cb = 'Ótimo! Só preciso do nome da coluna que vai ser "x", de qual vai ser o nome dela no gráfico,' \
                 'preciso do nome da coluna que vai ser "y" e de qual vai ser nome dela no gráfico.\n' \
                 'Ah, também dê um título para o seu gráfico.'
        escolhas5cb = ['Título', 'x', 'Nome eixo x', 'y', 'Nome eixo y']

        resposta5cb = eg.multenterbox(msg5cb, 'AMiDO - "Subject name here"', fields=escolhas5cb)

        msg5cc = 'Pronto! Seu arquivo foi plotado. Não se esqueça de salvar a imagem!\n' \
                 'Espero ter te ajudado com a análise dos seus dados.\n ' \
                 'Até!'
        escolhas5cc = ['Ver imagem e sair']

        resposta5cc = eg.buttonbox(msg5cc, 'AMiDO - "Now, I only want you gone."', escolhas5cc)

        if resposta5cc == 'Ver imagem e sair':

            grafico(df, resposta5cb[0], resposta5cb[1], resposta5cb[2], resposta5cb[3], resposta5cb[4])

            exit(0)

    if resposta5ca == 'Plot + Histograma':

        msg5cb = 'Ótimo! Só preciso do nome da coluna que vai ser "x", de qual vai ser o nome dela no gráfico,' \
                 'preciso do nome da coluna que vai ser "y" e de qual vai ser nome dela no gráfico.\n' \
                 'Ah, também dê um título para o seu gráfico e quantos bins você quer no seu histograma.'
        escolhas5cb = ['Título', 'x', 'Nome eixo x', 'y', 'Nome eixo y', 'Bins']

        resposta5cb = eg.multenterbox(msg5cb, 'AMiDO - "Subject name here"', fields=escolhas5cb)

        msg5cc = 'Pronto! Seu arquivo foi plotado. Não se esqueça de salvar a imagem!\n' \
                 'Espero ter te ajudado com a análise dos seus dados.\n ' \
                 'Até!'
        escolhas5cc = ['Ver imagem e sair']

        resposta5cc = eg.buttonbox(msg5cc, 'AMiDO - "Now, I only want you gone."', escolhas5cc)

        if resposta5cc == 'Ver imagem e sair':

            graf_hist(df, resposta5cb[0], resposta5cb[1], resposta5cb[2], resposta5cb[3], resposta5cb[4],
                      int(resposta5cb[5]))

            exit(0)

    if resposta5ca == 'Plot + Aproximação (filtro savgol)':

        msg5cb = 'Ótimo! Preciso do nome da coluna que vai ser "x", de qual vai ser o nome dela no gráfico,' \
                 'preciso do nome da coluna que vai ser "y" e de qual vai ser nome dela no gráfico.\n' \
                 'Ah, também dê um título para o seu gráfico, quantos pontos terá seu intervalo e qual ' \
                 'o grau do filtro.\n' \
                 'OBS.: O número de pontos deve ser ímpar!'
        escolhas5cb = ['Título', 'x', 'Nome eixo x', 'y', 'Nome eixo y', 'Pontos', 'Grau']

        resposta5cb = eg.multenterbox(msg5cb, 'AMiDO - "Subject name here"', fields=escolhas5cb)

        msg5cc = 'Pronto! Seu arquivo foi plotado. Não se esqueça de salvar a imagem!\n' \
                 'Espero ter te ajudado com a análise dos seus dados.\n ' \
                 'Até!'
        escolhas5cc = ['Ver imagem e sair']

        resposta5cc = eg.buttonbox(msg5cc, 'AMiDO - "Now, I only want you gone."', escolhas5cc)

        if resposta5cc == 'Ver imagem e sair':

            graf_aprox(df, resposta5cb[0], resposta5cb[1], resposta5cb[2], resposta5cb[3], resposta5cb[4],
                       int(resposta5cb[5]), int(resposta5cb[6]))

            exit(0)

    if resposta5ca == 'Plot + Histograma + Densidade':

        msg5cb = 'Ótimo! Só preciso do nome da coluna que vai ser "x", de qual vai ser o nome dela no gráfico,' \
                 'preciso do nome da coluna que vai ser "y" e de qual vai ser nome dela no gráfico.\n' \
                 'Ah, também dê um título para o seu gráfico e quantos bins você quer no seu histograma.'
        escolhas5cb = ['Título', 'x', 'Nome eixo x', 'y', 'Nome eixo y', 'Bins']

        resposta5cb = eg.multenterbox(msg5cb, 'AMiDO - "Subject name here"', fields=escolhas5cb)

        msg5cc = 'Pronto! Seu arquivo foi plotado. Não se esqueça de salvar a imagem!\n' \
                 'Espero ter te ajudado com a análise dos seus dados.\n ' \
                 'Até!'
        escolhas5cc = ['Ver imagem e sair']

        resposta5cc = eg.buttonbox(msg5cc, 'AMiDO - "Now, I only want you gone."', escolhas5cc)

        if resposta5cc == 'Ver imagem e sair':

            graf_hist_gauss(df, resposta5cb[0], resposta5cb[1], resposta5cb[2], resposta5cb[3], resposta5cb[4],
                            int(resposta5cb[5]))

            exit(0)

    if resposta5ca == 'Plot + Aproximação (filtro savgol) + Histograma + Densidade':

        msg5cb = 'Ótimo! Preciso do nome da coluna que vai ser "x", de qual vai ser o nome dela no gráfico,' \
                 'preciso do nome da coluna que vai ser "y" e de qual vai ser nome dela no gráfico.\n' \
                 'Ah, também dê um título para o seu gráfico, quantos pontos terá seu intervalo, qual ' \
                 'o grau do filtro e quantos bins você quer.\n' \
                 'OBS.: O número de pontos deve ser ímpar!'
        escolhas5cb = ['Título', 'x', 'Nome eixo x', 'y', 'Nome eixo y', 'Pontos', 'Grau', 'Bins']

        resposta5cb = eg.multenterbox(msg5cb, 'AMiDO - "Subject name here"', fields=escolhas5cb)

        msg5cc = 'Pronto! Seu arquivo foi plotado. Não se esqueça de salvar a imagem!\n' \
                 'Espero ter te ajudado com a análise dos seus dados.\n ' \
                 'Até!'
        escolhas5cc = ['Ver imagem e sair']

        resposta5cc = eg.buttonbox(msg5cc, 'AMiDO - "Now, I only want you gone."', escolhas5cc)

        if resposta5cc == 'Ver imagem e sair':

            graf_aprox_hist_gauss(df, resposta5cb[0], resposta5cb[1], resposta5cb[2], resposta5cb[3], resposta5cb[4],
                                  int(resposta5cb[5]), int(resposta5cb[6]), int(resposta5cb[7]))

            exit(0)

######################################################################################################
