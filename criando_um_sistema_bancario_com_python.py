menu = """\
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def depositar(valor):
    global saldo, extrato
    saldo += valor
    extrato += f"Depósito: R$ {valor:.2f}\n"

def sacar(valor):
    global saldo, extrato, numero_saques
    if valor > saldo:
        return "Operação falhou! Você não tem saldo suficiente."
    elif valor > limite:
        return "Operação falhou! O valor do saque excede o limite."
    elif numero_saques >= LIMITE_SAQUES:
        return "Operação falhou! Número máximo de saques excedido."
    
    saldo -= valor
    extrato += f"Saque: R$ {valor:.2f}\n"
    numero_saques += 1
    return "Saque realizado com sucesso."

def exibir_extrato():
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def validar_valor(valor):
    try:
        valor = float(valor)
        return valor > 0, valor
    except ValueError:
        return False, 0

while True:
    opcao = input(menu)

    if opcao == "d":
        valor_input = input("Informe o valor do depósito: ")
        valido, valor = validar_valor(valor_input)
        if valido:
            depositar(valor)
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor_input = input("Informe o valor do saque: ")
        valido, valor = validar_valor(valor_input)
        if valido:
            resultado = sacar(valor)
            print(resultado)
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        exibir_extrato()

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
