import os
valor: int = 0
dir: str = ''
arq: str = ''

def main():
    global valor

    i = 0
    resultado = 0
    valor = int(input("Digite um valor de 1 a 10: "))

    while (i <= 10):
        i = i + 1
        resultado = mult(valor, i)
        grava (i, resultado)

def mult(vlr, tab):
    res = vlr * tab
    return res

def grava (c, rslt):
    global dir, arq

    dir = '/temp/exercicios'
    arq = 'exercicio34.txt'

    file = ''
    tipo = ''
    enc = ''
    linha = ''

    if (os.path.exists(dir) and os.path.isdir(dir)):
        file = os.path.join(dir, arq)
        if (os.path.exists(file)):
            tipo = 'w'
            if (c > 0):
                tipo = 'a'
            else:
                tipo = 'w'
            linha = str(rslt) + '\n'
            enc = 'utf-8'
            with open(file, tipo, encoding=enc) as arquivo:
                arquivo.write(linha)
    os.mkdir('/tmp/exercicios', exist_ok=True)
    os.chmod('/tmp/exercicios', 0o744)

if (__name__ == '__main__'):
    main()