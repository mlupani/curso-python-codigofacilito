import csv

# Configura aquí el nombre de tu archivo de entrada y salida
input_file = 'productos_euga.csv'  # Debe tener las columnas: Nº SABO, N° TMS, Descripción, Aplicación, MARCA, PRECIO LISTA
output_file = 'insert_productos_euga.sql'

# Configuración de los valores fijos
empresa_id = 184
caracteristica1 = "BOMBA DE AGUA"
caracteristica2 = "EUGA"
activo = 1

def limpiar_precio(precio_str):
    # Quita puntos de miles y cambia coma decimal por punto
    return precio_str.replace('.', '').replace(',', '.')

with open(input_file, encoding='utf-8') as csvfile, open(output_file, 'w', encoding='utf-8') as sqlfile:
    reader = csv.DictReader(csvfile, delimiter=';')  # Usa delimiter=',' si es CSV con comas
    for row in reader:
        codigo_producto = row['\ufeffCÓDIGO'].strip()
        descripcion = row['DESCRIPCIÓN'].strip()
        precio = limpiar_precio(row['PRECIO'])
        titulo = f"{descripcion}".strip()
        # Escapa comillas simples en el título
        titulo = titulo.replace("'", "''")
        insert = (
            f"INSERT INTO productos (empresa_id, titulo, codigo_producto, precio, caracteristica1, caracteristica2, activo) "
            f"VALUES ({empresa_id}, '{titulo}', '{codigo_producto}', {precio}, '{caracteristica1}', '{caracteristica2}', {activo});\n"
        )
        sqlfile.write(insert)

print(f"Script terminado. Sentencias SQL generadas en {output_file}")