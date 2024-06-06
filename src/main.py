from utils.clearConsole import clear_console
from dao.NumbersManager import NumbersManager

def main():
    try:
        nums = NumbersManager().load_state(True)

        options = [
            'analisis', 'pares', 'impares', 'cantidad de impares', 'cantidad de pares', 'exit', 'borrar', 'borrar numero', 'borrar lista', 'guardar', 'cambiar', 'histograma', 'exit', 'borrar todos los datos', 'borrar datos', 'media', 'mediana', 'moda', 'ordenar asc', 'ordenar desc', 'max', 'min', 'varianza', 'valor z', 'desviacion estandar', 'amplitud', 'proyecto final'
            ]

        numbers = nums.list

        n = input('\n>> ')
        n = n.lower()

        while n not in options:
            nums.push(float(n))
            clear_console()
            print(f'\nLista: {numbers}\n') 
            n = input('\n>> ')

        if n == 'pares':
            clear_console()
            print(f'\nPares: {nums.pares()}')

        elif n == 'impares':
            clear_console()
            print(f'\nimpares: {nums.impares()}')

        elif n == 'cantidad de pares':
            clear_console()
            print(f'\nCantidad de pares: {nums.cantidadDePares()}')

        elif n == 'cantidad de impares':
            clear_console()
            print(f'\nCantidad de impares: {nums.cantidadDeImpares()}')
        
        elif n == 'borrar':
            clear_console()
            nums.borrar()
        
        elif n == 'borrar numero':
            nums.borrar(int(input('\tNumero a borrar: ')))
            clear_console()
        
        elif n == 'borrar lista':
            clear_console()
            nums.clear()
        
        elif n == 'borrar todos los datos':
            r = input('\nEscribe "Confirm" para borrar: ')
            if r == 'Confirm':
                nums.clearAll()
                print('Se borraron los datos guardadas')
            clear_console()
        
        elif n == 'borrar datos':
            r = input('\nNombre de los datos: ')
            nums.borrarColeccion(r)
            clear_console()
            print(f'\tListas: \n\t\t{nums.datos}')
        
        elif n == 'guardar':
            print('\nAgrega un nombre (opcional) o presiona enter para guardar')
            nombre = input('\n\tNombre: ')
            clear_console()
            if nombre != '':
                nums.save(nombre)
            else: 
                nums.save(None)
            nums = NumbersManager().load_state(False)
            print(f'\tSe guardo la lista con exito')
            print(f'\tListas: \n\t\t{nums.datos}')
        
        elif n == 'cambiar':
            clear_console()
            print(f'Listas: \n\t{nums.datos}')
            lista = input('\nLista: ')
            nums.use(lista)
            clear_console()
        
        elif n == 'histograma':
            clear_console()
            nums.histograma()
        
        elif n == 'media':
            clear_console()
            print(f'\nMedia: {nums.media()}')
        
        elif n == 'mediana':
            clear_console()
            print(f'\nMediana: {nums.mediana()}')
        
        elif n == 'moda':
            clear_console()
            print(f'\nModa: {nums.moda()}')
        
        elif n == 'ordenar asc':
            clear_console()
            nums.ordenarAsc()
        
        elif n == 'ordenar desc':
            clear_console()
            nums.ordenarDesc()
        
        elif n == 'max':
            clear_console()
            print(f'\nValor maximo: {nums.valorMax()}')
        
        elif n == 'min':
            clear_console()
            print(f'\nValor minimo: {nums.valorMin()}')
        
        elif n == 'varianza':
            clear_console()
            print(f'\nVarianza: {nums.varianza()}')
        
        elif n == 'desviacion estandar':
            clear_console()
            print(f'\nDesviacion estandar: {nums.desvEstd()}')
        
        elif n == 'valor z':
            x = float(input('\nx = '))
            print(f'\nValor Z: {nums.valorZ(x)}')
        
        elif n == 'amplitud':
            clear_console()
            print(f'\nAmplitud: {nums.amplitud()}')
        
        elif n == 'exit':
            clear_console()
            return print(f'\n\tFin del programa\n')
        
        elif n == 'analisis':
            clear_console()
            print(
                f'\n\nPares: {nums.pares()}',
                f'\nCantidad de pares: {nums.cantidadDePares()}',
                f'\nimpares: {nums.impares()}',
                f'\nCantidad de impares: {nums.cantidadDeImpares()}',
                f'\nMedia: {nums.media()}',
                f'\nMediana: {nums.mediana()}',
                f'\nModa: {nums.moda()}',
                f'\nMax: {nums.valorMax()}',
                f'\nMin: {nums.valorMin()}',
                f'\nAmplitud: {nums.amplitud()}',
                f'\nVarianza: {nums.varianza()}',
                f'\nDesviacion estandar: {nums.desvEstd()}',
            )
            nums.histograma()
        
        elif n == 'proyecto final':
            clear_console()
            print(
                f'\n\nPares: {nums.pares()}',
                f'\nCantidad de pares: {nums.cantidadDePares()}',
                f'\n\nimpares: {nums.impares()}',
                f'\nCantidad de impares: {nums.cantidadDeImpares()}',
            )

        main()
    
    except ValueError:
        clear_console()
        print('\nError: Input invalido')
        main()
    
    except IndexError as err:
        clear_console()
        print(f'\nError: {err}')
        main()
    
    except OSError:
        clear_console()
        print('\nError al cargar las listas')
        main()
    
    except Exception as err:
        clear_console()
        if len(nums.list) <= 1:
            print('Error: Datos insuficientes')
        else:
            print(f'Error: {err}')
        main()

main()


