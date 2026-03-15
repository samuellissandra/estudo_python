import sys
import argparse
import csv
import json
import os

print("=" * 50)
print("       EXEMPLOS DE ENTRADA DE DADOS - PYTHON")
print("=" * 50)

# ─────────────────────────────────────────
# 1. input() básico
# ─────────────────────────────────────────
print("\n📌 1. input() básico")
nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")

# ─────────────────────────────────────────
# 2. Convertendo tipos
# ─────────────────────────────────────────
print("\n📌 2. Convertendo tipos")
idade = int(input("Sua idade: "))
altura = float(input("Sua altura (ex: 1.75): "))
print(f"Em 10 anos você terá {idade + 10} anos.")
print(f"Altura registrada: {altura}m")

# ─────────────────────────────────────────
# 3. Validando entrada com try/except
# ─────────────────────────────────────────
print("\n📌 3. Validando entrada com try/except")
while True:
    try:
        nota = float(input("Digite sua nota (0-10): "))
        if 0 <= nota <= 10:
            break
        print("⚠️  Valor fora do intervalo! Tente novamente.")
    except ValueError:
        print("⚠️  Digite um número válido!")
print(f"Nota registrada: {nota}")

# ─────────────────────────────────────────
# 4. Múltiplos valores na mesma linha
# ─────────────────────────────────────────
print("\n📌 4. Múltiplos valores na mesma linha")
entrada = input("Digite números separados por espaço (ex: 10 20 30): ")
numeros = list(map(int, entrada.split()))
print(f"Números: {numeros}")
print(f"Soma: {sum(numeros)} | Média: {sum(numeros)/len(numeros):.2f}")

# ─────────────────────────────────────────
# 5. Várias linhas até sinal de parada
# ─────────────────────────────────────────
print("\n📌 5. Múltiplas linhas (linha vazia para encerrar)")
linhas = []
print("Digite as linhas:")
while True:
    linha = input("  > ")
    if linha == "":
        break
    linhas.append(linha)
print(f"Você digitou {len(linhas)} linha(s): {linhas}")

# ─────────────────────────────────────────
# 6. sys.argv (argumentos da linha de comando)
# ─────────────────────────────────────────
print("\n📌 6. sys.argv")
if len(sys.argv) >= 3:
    arg_nome = sys.argv[1]
    arg_idade = int(sys.argv[2])
    print(f"Via sys.argv → {arg_nome} tem {arg_idade} anos.")
else:
    print("Nenhum argumento passado. Execute assim para testar:")
    print("  python script.py SeuNome 25")

# ─────────────────────────────────────────
# 7. argparse (CLI estruturada)
# ─────────────────────────────────────────
print("\n📌 7. argparse")
parser = argparse.ArgumentParser(add_help=False)
parser.add_argument("--peso", type=float)
parser.add_argument("--altura_imc", type=float)
args, _ = parser.parse_known_args()

if args.peso and args.altura_imc:
    imc = args.peso / (args.altura_imc ** 2)
    print(f"IMC calculado via argparse: {imc:.2f}")
else:
    print("Passe --peso e --altura_imc para calcular o IMC.")
    print("  Exemplo: python script.py --peso 70 --altura_imc 1.75")

# ─────────────────────────────────────────
# 8. Lendo arquivo de texto
# ─────────────────────────────────────────
print("\n📌 8. Lendo arquivo de texto")
arquivo_txt = "exemplo.txt"
with open(arquivo_txt, "w", encoding="utf-8") as f:
    f.write(f"Nome: {nome}\nIdade: {idade}\nNota: {nota}")

with open(arquivo_txt, "r", encoding="utf-8") as f:
    conteudo = f.read()
print("Conteúdo do arquivo:")
print(conteudo)
os.remove(arquivo_txt)

# ─────────────────────────────────────────
# 9. Lendo CSV
# ─────────────────────────────────────────
print("\n📌 9. Lendo CSV")
arquivo_csv = "dados.csv"
with open(arquivo_csv, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["nome", "email"])
    writer.writeheader()
    writer.writerow({"nome": "Ana",    "email": "ana@email.com"})
    writer.writerow({"nome": "Carlos", "email": "carlos@email.com"})
    writer.writerow({"nome": nome,     "email": f"{nome.lower()}@email.com"})

with open(arquivo_csv, newline="", encoding="utf-8") as f:
    leitor = csv.DictReader(f)
    for linha in leitor:
        print(f"  Nome: {linha['nome']:10} | Email: {linha['email']}")
os.remove(arquivo_csv)

# ─────────────────────────────────────────
# 10. Entrada via JSON
# ─────────────────────────────────────────
print("\n📌 10. Entrada via JSON")
dados_json = json.dumps({"nome": nome, "idade": idade, "nota": nota})
print(f"JSON gerado: {dados_json}")
dados = json.loads(dados_json)
print(f"Lido do JSON → Nome: {dados['nome']} | Idade: {dados['idade']} | Nota: {dados['nota']}")

# ─────────────────────────────────────────
print("\n" + "=" * 50)
print("           FIM DOS EXEMPLOS")
print("=" * 50)