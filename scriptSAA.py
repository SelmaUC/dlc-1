import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
archivo_csv = "apple_quality.csv"
datos = pd.read_csv(archivo_csv)

columna_x = 'Size'
columna_y = 'Weight'

# Crear el gráfico
plt.plot(datos[columna_x], datos[columna_y])
plt.title('Gráfico de datos')
plt.xlabel('Apple Size')
plt.ylabel('Apple Weight')

# Guardar el gráfico como una imagen
nombre_imagen = "grafico_datos.png"
plt.savefig(nombre_imagen)

# Mostrar el gráfico
plt.show()

print(f"El gráfico se ha guardado como {nombre_imagen}")
