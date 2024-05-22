from typing import Union, Optional
import os
import pickle
import math

class NumbersManager:

    __state_file = 'state.pkl'
    __dir = os.path.join('src', 'data')
    __path = os.path.join(__dir, __state_file)

    def __init__(self):
        """
        Inicializa un nuevo NumbersManager con una lista vacía y datos vacíos.
        """
        self.list = []
        self.datos = {}
        self.__list_number = 0

    def save(self, name: Optional[str] = None):
        """
        Guarda la lista actual en datos o actualiza los datos.

        Args:
            name (str, optional): El nombre de la lista a guardar. Si es None, se guarda con un índice incremental.

        Returns:
            dict: Los datos actualizados.
        """
        if name is None:
            self.datos.update({self.__list_number: self.list.copy()})
            self.__list_number += 1
            self.__save_state()
        elif name:
            if name not in self.datos.keys():
                self.__list_number += 1
            self.datos.update({name: self.list.copy()})
            self.__save_state()
        return self.datos
    
    def use(self, name: Union[int, str]):
        """
        Reutiliza datos.

        Args:
            name (Union[int, str]): El nombre de los datos o el índice de los datos.

        Raises:
            IndexError: Si el índice está fuera de rango.
            ValueError: Si los datos no existen.
        """
        try:
            name = int(name)
            keys = list(self.datos.keys())
            if name < 0 or name >= len(keys):
                raise IndexError(f'Índice {name} fuera de rango')
            name = keys[name]
            if self.datos.get(name) is not None:
                self.list = self.datos.get(name)
                self.__save_state()
        except ValueError:
            if self.datos.get(name) is not None:
                self.list = self.datos.get(name)
                self.__save_state()
            else:
                print(f'No existe la lista {name}')
    
    def push(self, numero: Union[int, float]):
        """
        Agrega un número a la lista.

        Args:
            numero (Union[int, float]): El número a agregar.
        """
        self.list.append(numero)
        self.__save_state()

    def ordenarAsc(self):
        """
        Ordena la lista en orden ascendente.
        """
        datos = sorted(self.list)
        self.list = datos.copy()
        self.__save_state()
    
    def ordenarDesc(self):
        """
        Ordena la lista en orden descendente.
        """
        datos = list(reversed(self.list))
        self.list = datos.copy()
        self.__save_state()

    def pares(self):
        """
        Obtiene una lista de los números pares en la lista.

        Returns:
            list: Una lista de números pares.
        """
        return list(filter(lambda n: n % 2 == 0 and n != 0, self.list))

    def impares(self):
        """
        Obtiene una lista de los números impares en la lista.

        Returns:
            list: Una lista de números impares.
        """
        return list(filter(lambda n: n % 2 != 0, self.list))
    
    def cantidadDePares(self):
        """
        Obtiene la cantidad de números pares en la lista.

        Returns:
            int: La cantidad de números pares.
        """
        return len(self.pares())
    
    def cantidadDeImpares(self):
        """
        Obtiene la cantidad de números impares en la lista.

        Returns:
            int: La cantidad de números impares.
        """
        return len(self.impares())
    
    def borrar(self, num: Optional[int] = None):
        """
        Borra el último número de la lista o un número específico.

        Args:
            num (int, optional): El número a borrar. Si es None, borra el último número.
        """
        if num is None:
            self.list.pop()
            self.__save_state()
        else:
            self.list.remove(num)
            self.__save_state()

    def clear(self):
        """
        Limpia la lista actual.
        """
        self.list.clear()
        self.__save_state()

    def borrarColeccion(self, name: str):
        """
        Borra una colección de datos.

        Args:
            name (str): El nombre de la colección de datos a borrar.

        Raises:
            IndexError: Si el índice está fuera de rango.
        """
        try:
            name = int(name)
            keys = list(self.datos.keys())
            if name < 0 or name >= len(keys):
                raise IndexError(f'Índice {name} fuera de rango')
            name = keys[name]
            if self.datos.get(name) is not None:
                self.datos.pop(name)
                self.__save_state()
        except ValueError:
            if self.datos.get(name) is not None:
                self.datos.pop(name)
                self.__save_state()
            else:
                print(f'No existe la lista {name}')

    def clearAll(self):
        """
        Borra todos los datos guardados.
        """
        self.datos = {}
        self.__save_state()

    def __freq(self):
        """
        Calcula la frecuencia de cada número en la lista.

        Returns:
            dict: Un diccionario con la frecuencia de cada número.
        """
        freq_dict = {}
        for num in self.list:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1
        return freq_dict

    def histograma(self):
        """
        Imprime un histograma de la frecuencia de los números en la lista.
        """
        freq = self.__freq()
        
        data = freq.values()

        max_value = max(data)
        width = 50
        scale = width / max_value

        print("Frecuencia de números:")
        for number, frequency in sorted(freq.items()):
            bar = '*' * int(frequency * scale)
            print(f'{number:>5}: {bar} ({frequency})')

    def media(self):
        """
        Calcula la media de los números en la lista.

        Returns:
            float: La media de los números.
        """
        return sum(self.list) / len(self.list)
    
    def moda(self):
        """
        Calcula la moda de los números en la lista.

        Returns:
            list: Una lista de los números que son moda.
        """
        freq = self.__freq()
        max_freq = max(freq.values())
        modas = [num for num, frecuencia in freq.items() if frecuencia == max_freq]
        return modas
    
    def mediana(self):
        """
        Calcula la mediana de los números en la lista.

        Returns:
            float: La mediana de los números.
        """
        numeros_ordenados = sorted(self.list)
        n = len(numeros_ordenados)
        mitad = n // 2
        
        if n % 2 == 0:
            return (numeros_ordenados[mitad - 1] + numeros_ordenados[mitad]) / 2
        else:
            return numeros_ordenados[mitad]
    
    def valorMax(self):
        """
        Obtiene el valor máximo en la lista.

        Returns:
            float: El valor máximo.
        """
        return max(self.list)
    
    def valorMin(self):
        """
        Obtiene el valor mínimo en la lista.

        Returns:
            float: El valor mínimo.
        """
        return min(self.list)
    
    def amplitud(self):
        """
        Calcula la amplitud de los números en la lista.

        Returns:
            float: La amplitud.
        """
        return self.valorMax() - self.valorMin()
    
    def varianza(self):
        """
        Calcula la varianza de los números en la lista.

        Returns:
            float: La varianza.
        """
        media = self.media()
        return sum((x - media) ** 2 for x in self.list) / len(self.list)
    
    def desvEstd(self):
        """
        Calcula la desviación estándar de los números en la lista.

        Returns:
            float: La desviación estándar.
        """
        return math.sqrt(self.varianza())
    
    def coeficienteDeVariacion(self):
        """
        Calcula el coeficiente de variación de los números en la lista.

        Returns:
            float: El coeficiente de variación.
        """
        return self.desvEstd() / self.media()
    
    def valorZ(self, x: Union[int, float]):
        """
        Calcula el valor Z de un número dado.

        Args:
            x (Union[int, float]): El número para el cual se va a calcular el valor Z.

        Returns:
            float: El valor Z del número dado.
        """
        return (x - self.media()) / self.desvEstd()

    def __save_state(self) -> None:
        """
        Guarda el estado actual de la instancia en un archivo.
        """
        os.makedirs(os.path.dirname(NumbersManager.__path), exist_ok=True)
        with open(NumbersManager.__path, 'wb') as file:
            pickle.dump(self, file)

    def load_state(self, flag: bool):
        """
        Carga el estado guardado de un archivo.

        Args:
            flag (bool): Si es True, imprime la lista cargada.

        Returns:
            NumbersManager: La instancia con el estado cargado.
        """
        if os.path.exists(NumbersManager.__path):
            with open(NumbersManager.__path, 'rb') as file:
                state = pickle.load(file)
                if flag: 
                    print(f'\nLista: {state.list}\n')
                return state
        return NumbersManager()


