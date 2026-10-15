
import os
nome: str = ''
nota1: float = 0.0
nota2: float = 0.0
nota3: float = 0.0
nota4: float = 0.0
valor_media: float = 0.0
dir: str = ''
arq: str = ''

def main():
    i = 0
    while (i < 5):
        i = i + 1
        entrada()

def entrada():
    global nome, nota1, nota2, nota3, nota4, valor_media

    nome = input('Digite o nome do aluno: ')
    nota1 = float(input('Digite a nota 1: '))
    nota2 = float(input('Digite a nota 2: '))
    nota3 = float(input('Digite a nota 3: '))
    nota4 = float(input('Digite a nota 4: '))

    valor_media = med(nota1, nota2, nota3, nota4)

    print('Média:', valor_media)

    if (valor_media >= 6.0):
        print('APROVADO')
    elif (valor_media >= 3.0):
        print('EXAME')
    else:
        print('RETIDO')

    cadastro(nome, nota1, nota2, nota3, nota4, valor_media)

def med(n1, n2, n3, n4):
    media: float = 0.0

    media = (n1 + n2 + n3 + n4) / 4

    return media

def cadastro(nm, nt1, nt2, nt3, nt4, vlr_med):
    global dir, arq

    linha: str = ''

    dir = '/tmp/exercicios'
    arq = 'ex21.txt'

    linha = nm + ';' + str(nt1) + ';' + str(nt2) + ';' + str(nt3) + ';' + str(nt4) + ';' + str(vlr_med) + '\n'
    escreveArq(dir, arq, linha)

def escreveArq(caminho, arquivo, linha_cad):
    file: str = ''
    tipo: str = ''
    enc: str = ''

    if (os.path.exists(caminho) and os.path.isdir(caminho)):
        file = caminho + '/' + arquivo
        tipo = 'w'
        if (os.path.exists(file)):
            tipo = 'a'
        enc = 'utf-8'
        with open(file, tipo, encoding=enc) as arquivo:
            arquivo.write(linha_cad)
    else:
        print('Diretório inválido')
os.makedirs('/tmp/exercicios', exist_ok=True)
os.chmod('/tmp/exercicios', 0o744)

if (__name__ == '__main__'):
    main()
