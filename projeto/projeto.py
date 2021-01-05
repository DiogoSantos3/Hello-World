from time import sleep
print('\33[1;30m-='*20)
print('\33[1;30m                NOTAS              ')
print('-='*20)
print(' ')
print('-' * 30)
print('\33[1;32mGuardar novas notas [A]')
print('\33[1;33mVer notas guardadas [B]')
print('\33[1;31mSair [C]')
print('\33[1;30m-'*30)
opçao=str(input('\33[1;30mDigita a tua opção: ').upper()[0].strip())
while True:
    if opçao == 'A':
        print('\33[1;37mDe quem queres guardar notas?')
        print('\33[1;30m-' * 30)
        print('\33[1;34mDiogo [D]\n'
              '\33[1;35mRita [R]\n'
              '\33[1;36mFilipa [F]')
        print('\33[1;31mSair [S]')
        print('\33[1;30m-' * 30)
        a = str(input('\33[1;30m Digita a tua opção: ').upper()[0].strip())
        if a == 'D':
            aD = str(input('\33[1;30m Digita aqui a notas que queres guardar (nota,disciplina): '))
            with open('Notas Diogo.txt', 'a') as fileD:
                fileD.write(' \n')
                fileD.write(aD)
        elif a == 'R':
            aR = str(input('Digita aqui a nota que queres guardar (nota,disciplina): '))
            with open('Notas Rita.txt', 'a') as fileR:
                fileR.write(' \n')
                fileR.write(aR)
        elif a == 'F':
            aF = str(input('Digita aqui a nota que queres guardar (nota,disciplina): '))
            with open('Notas Filipa.txt', 'a') as fileF:
                fileF.write(' \n')
                fileF.write(aF)
        elif a == 'S':
            print('\33[1;30mObrigado, volte sempre!')
            break
    if opçao == 'B':
        print('\33[1;37;m De quem queres ver as notas?\33[m')
        print('\33[1;30m-' * 30)
        print('\33[1;34mDiogo [D]\n'
              '\33[1;35mRita [R]\n'
              '\33[1;36mFilipa [F]')
        print('\33[1;31mSair [S]')
        print('\33[1;30m-' * 30)
        b = str(input('\33[1;30m Digita a tua opção: ').upper()[0].strip())
        if b == 'D':
            with open('Notas Diogo.txt', 'r+') as fileDR:
                fileDR.seek(0, 0)
                print(fileDR.read())
                print('-' * 30)
        elif b == 'R':
            with open('Notas Rita.txt', 'r+') as fileRR:
                fileRR.seek(0, 0)
                print(fileRR.read())
                print('\33[1;30m-' * 30)
        elif b == 'F':
            with open('Notas Filipa.txt', 'r+') as fileFR:
                fileFR.seek(0, 0)
                print(fileFR.read())
                print('\33[1;30m-' * 30)
        elif b== 'S':
            print('\33[1;30mObrigado, volte sempre!')
            break
    if opçao == 'C':
        print('\33[1;30mObrigado, volte sempre!')
        break


