import os, subprocess

# Configuraciones
TEST_DIR = "."         # Directorio de pruebas
CODE_FILE = "main.c"        # Nombre del fichero a probar
COMPILER_TIMEOUT = 10.0     # Timeout de compilación en segundos
RUN_TIMEOUT = 10.0          # Timeout de ejecución en segundos

# Creamos paths absolutas desde las relativas
code_path = os.path.join(TEST_DIR, CODE_FILE)
app_path = os.path.join(TEST_DIR, "app")

#Compilación de programas (llamndo a make, gcc, etc...)
print("Compilando programa...")
try:
    ret = subprocess.run(["gcc", code_path, "-o", app_path],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        timeout=COMPILER_TIMEOUT) # Lanzamos subproceso de compilación
except Exception as e:
    print("ERROR: Compilación fallida.", str(e))
    exit(1) # Salimos mostrando código de error

# Parseamos la salida
output = ret.stdout.decode('utf-8')
print(output)
output = ret.stderr.decode('utf-8')
print(output)

# Comprobamos si el programa ha compilado de forma correcta
if ret.returncode != 0:
    print("ERROR: La compilación gcc ha fallado.")
    exit(1)

#Ejecutamos el programa compilado
print("Ejecutando...")
try:
    ret = subprocess.run([app_path],
                        stdout=subprocess.PIPE,
                        timeout=RUN_TIMEOUT)
except Exception as e:
    print("ERROR: Error al ejecutar el programa.", str(e))
    exit(1) # Salimos mostrando código de error

# Parseamos la salida
output = ret.stdout.decode('utf-8')
print("Salida del programa:", output)

# Todos los tests completados de forma correcta
print("Pruebas realizadas correctamente!")
exit(0)

