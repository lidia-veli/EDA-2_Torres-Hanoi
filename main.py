from pilaHanoi import Pila

def getTablero(n):
    '''Inicializa el tablero con n discos en la torre 1 y las otras dos vacías'''
    t1 = Pila(1)
    for i in range(n,0,-1):  # la torre 1 es donde empiezan todos los discos
        t1.push(i)  # los discos con mayor valor están en la parte inferior de la pila

    t2 = Pila(2)
    t3 = Pila(3)
    return t1, t2, t3


def hanoi(n, t_origen, t_destino, t_auxiliar, lista_mov):
    '''Función recursiva que devuelve la lista de movimientos para solucionar el problema de las torres de Hanoi para n discos'''

    if n==1:  # CASO BASE
        disco  = t_origen.pop()  # quitamos el único disco
        t_destino.push(disco)  # y lo llevamos directamente al destino
        mov = f'D{disco} from T{t_origen.num} to T{t_destino.num}'
        lista_mov.append(mov)
    
    else:
        # resuelve el caso anterior en la torre auxiliar
        hanoi(n-1, t_origen, t_auxiliar, t_destino, lista_mov)

        # movemos el disco más grande a la torre destino
        disco = t_origen.pop()
        t_destino.push(disco)
        mov = f'D{disco} from T{t_origen.num} to T{t_destino.num}'
        lista_mov.append(mov)

        # y resolvemos el problema n-1 origen=t_aux, destino=t_destino, aux=t_origen
        hanoi(n-1, t_auxiliar, t_destino, t_origen, lista_mov)

    
def main():
    n = int(input('Introduce el número de discos: '))
    t1, t2, t3 = getTablero(n)
    print()
    print('ESTADO INICIAL:')
    print(f'Torre 1: {t1.imprimir()}')
    print(f'Torre 2: {t2.imprimir()}')
    print(f'Torre 3: {t3.imprimir()}')

    lista_mov = []  # lista donde vamosa a guardar los movimientos
    # solucionador
    hanoi(n, t1, t2, t3, lista_mov)

    print()
    print('MOVIMIENTOS REALIZADOS:')
    for mov in lista_mov:
        print(mov)
    
    print()
    print('ESTADO FINAL:')
    print(f'Torre 1: {t1.imprimir()}')
    print(f'Torre 2: {t2.imprimir()}')
    print(f'Torre 3: {t3.imprimir()}')



# CODIGO EJECUTABLE -----------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
