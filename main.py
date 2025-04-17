import csv
import math
from interface import create_interface

# Listas para armazenar dados
raios = []
velocidade_observadas = []

# Leitura dos dados do CSV
with open("dados_galaxia.csv", mode="r") as arquivo:
    leitor = csv.reader(arquivo)
    next(leitor)
    for linha in leitor:
        raios.append(float(linha[0]))
        velocidade_observadas.append(float(linha[1]))

G = 6.674 * (10 ** -11)
M = 2 * (10 ** 41)
kpc_em_metros = 3.086 * (10 ** 19)

# Cálculo das velocidades
velocidade_esperadas = []
for r_kpc in raios:
    r_metros = r_kpc * kpc_em_metros
    v = math.sqrt((G * M) / r_metros)
    v_km_s = v / 1000  # Converter para km/s
    velocidade_esperadas.append(v_km_s)
# Criar interface
create_interface(raios, velocidade_observadas, velocidade_esperadas)
