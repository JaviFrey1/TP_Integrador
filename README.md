# Comparación de Algoritmos de Ordenamiento

Este proyecto implementa y compara tres algoritmos de ordenamiento clásicos en Python: Ordenamiento Burbuja (Bubble Sort), Ordenamiento por Mezcla (Merge Sort) y Ordenamiento Rápido (Quick Sort).

## Autor

Javier Gomez Frey

## Link al video

[Youtube](https://www.youtube.com/watch?v=79eIMPWJCLg)

## Descripción

El programa realiza una comparación práctica de tres algoritmos de ordenamiento diferentes, midiendo sus tiempos de ejecución con arrays de distintos tamaños y generando visualizaciones comparativas.

### Algoritmos Implementados

1. **Ordenamiento Burbuja (Bubble Sort)**

   - Complejidad Temporal: O(n²)
   - Complejidad Espacial: O(1)
   - Mejor para: Arrays pequeños

2. **Ordenamiento por Mezcla (Merge Sort)**

   - Complejidad Temporal: O(n log n)
   - Complejidad Espacial: O(n)
   - Mejor para: Arrays grandes, cuando hay memoria disponible

3. **Ordenamiento Rápido (Quick Sort)**
   - Complejidad Temporal: O(n log n) promedio, O(n²) peor caso
   - Complejidad Espacial: O(log n)
   - Mejor para: Arrays grandes, uso general

## Requisitos

- Python 3.x
- matplotlib
- numpy

## Instalación

1. Clona este repositorio o descarga los archivos
2. Instala las dependencias:

```bash
pip install -r requirements.txt
```

## Uso

1. Ejecuta el programa:

```bash
python TI-GOMEZ_FREY.py
```

2. El programa:
   - Generará arrays aleatorios de diferentes tamaños
   - Medirá el tiempo de ejecución de cada algoritmo
   - Mostrará los resultados en la consola
   - Generará un gráfico comparativo ('comparacion_ordenamiento.png')

## Estructura del Proyecto

- `TI-GOMEZ_FREY.py`: Código fuente principal
- `requirements.txt`: Dependencias del proyecto
- `comparacion_ordenamiento.png`: Gráfico generado con los resultados
- `TI-GOMEZ_FREY.txt`: Documentación detallada del trabajo

## Resultados

El programa genera un análisis comparativo que muestra:

- Tiempos de ejecución para cada algoritmo
- Gráfico de rendimiento
- Comparación de eficiencia con diferentes tamaños de datos

Ejemplo de resultados (para 5000 elementos):

- Ordenamiento Burbuja: ~0.57 segundos
- Ordenamiento por Mezcla: ~0.005 segundos
- Ordenamiento Rápido: ~0.003 segundos

## Licencia

Este proyecto es parte de un trabajo académico para la Tecnicatura Universitaria en Programación de la UTN.
