roundcount = 1

aa = '  '
ab = '  '
ad = '  '

ba = '  '
bb = '  '
bd = '  '

da = '  '
db = '  '
dd = '  '

def x(x, y):
    if roundcount == 1:
        a = input('what spas')
    elif roundcount == 2:
        b = input('what spase a,b or c:')

def printstatis():
    print('  a    b   c')
    print('1' + aa + ' | ' + ab + ' | ' + ad)
    print(' ' + '-------------')
    print('2' + ba + ' | ' + bb + ' | ' + bd)
    print(' ' + '-------------')
    print('3' + da + ' | ' + db + ' | ' + dd)



def run():
    printstatis()
    print('x turn')
    x()


if __name__ == "__main__":
    run()