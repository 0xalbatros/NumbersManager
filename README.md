# NumbersManager

## Descripción

Este proyecto proporciona una clase `NumbersManager` para gestionar, analizar y manipular una lista de números. Las funcionalidades incluyen filtrar números pares e impares, ordenar números, calcular estadísticas (media, mediana, moda, etc.), y visualizar un histograma de frecuencias. Los datos se guardan y cargan automáticamente utilizando la serialización con `pickle`.

## Requerimientos

1. Git: Necesitas tener Git instalado en tu sistema para poder clonar el repositorio desde GitHub. Puedes descargar e instalar Git desde el sitio web oficial: https://git-scm.com/.

2. Python: Debes tener Python instalado en tu sistema para poder ejecutar el archivo de Python. Puedes descargar e instalar Python desde el sitio web oficial: https://www.python.org/. Asegúrate de configurar correctamente la variable de entorno PATH durante la instalación para que puedas ejecutar el comando python desde cualquier ubicación en tu terminal.

## Instalación

1. **Clonar el repositorio:**
   ```sh
   git clone https://github.com/0xalbatros/NumbersManager.git
   ```

2. **Navegar al directorio del proyecto:**
   ```sh
   cd NumbersManager
   ```

## Uso

### Ejecución del Programa Principal

Para ejecutar el programa principal, simplemente ejecuta el archivo `main.py`:

```sh
python main.py
```

El programa presentará un prompt donde podrás ingresar números para agregarlos a la lista o comandos para realizar diversas operaciones. A continuación, se muestra un ejemplo de uso priorizando la opción "proyecto final".

### Ejemplo: Opción "proyecto final"

1. **Ejecutar el programa:**
   ```sh
   python main.py
   ```

2. **Ingresar algunos números:**
   ```plaintext
   >> 10
   >> 15
   >> 20
   >> 25
   >> 30
   ```
   Simplemente presiona 'Enter' despues de escribir el numero que quieras ingresar.

3. **Ingresar la opción `proyecto final` para ver el análisis de los números ingresados:**
   ```plaintext
   >> proyecto final
   ```

4. **El programa mostrará el siguiente análisis:**
   ```plaintext
   Pares: [10, 20, 30]
   Cantidad de pares: 3

   impares: [15, 25]
   Cantidad de impares: 2
   ```

## Funcionalidades Principales

- `analisis`: Realiza un análisis completo de la lista de números, mostrando estadísticas como pares, cantidad de pares, impares, cantidad de impares, media, mediana, moda, valor máximo, valor mínimo, amplitud, varianza, desviación estándar y un histograma.
- `pares`: Muestra todos los números pares en la lista.
- `impares`: Muestra todos los números impares en la lista.
- `cantidad de pares`: Muestra la cantidad de números pares en la lista.
- `cantidad de impares`: Muestra la cantidad de números impares en la lista.
- `borrar`: Borra el último número de la lista.
- `borrar numero`: Borra un número específico de la lista.
- `borrar lista`: Borra todos los números de la lista actual.
- `borrar todos los datos`: Borra todos los datos guardados.
- `borrar datos`: Borra una lista de datos específica.
- `guardar`: Guarda la lista actual con un nombre específico o un índice incremental.
- `cambiar`: Cambia a una lista guardada específica.
- `histograma`: Muestra un histograma de frecuencias de los números en la lista.
- `media`: Calcula y muestra la media de los números en la lista.
- `mediana`: Calcula y muestra la mediana de los números en la lista.
- `moda`: Calcula y muestra la moda de los números en la lista.
- `ordenar asc`: Ordena la lista en orden ascendente.
- `ordenar desc`: Ordena la lista en orden descendente.
- `max`: Muestra el valor máximo en la lista.
- `min`: Muestra el valor mínimo en la lista.
- `varianza`: Calcula y muestra la varianza de los números en la lista.
- `desviacion estandar`: Calcula y muestra la desviación estándar de los números en la lista.
- `valor z`: Calcula y muestra el valor Z de un número específico.
- `amplitud`: Calcula y muestra la amplitud (rango) de los números en la lista.
- `proyecto final`: Muestra un análisis de los números ingresados, destacando la cantidad de números pares e impares.
- `exit`: Sale del programa.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
