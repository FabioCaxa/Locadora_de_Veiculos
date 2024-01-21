import os

veiculos = [
    ("Chevrolet Tracker", 120),
    ("Chevrolet Onix", 90),
    ("Chevrolet Spin", 150),
    ("Hyundai HB20", 85),
    ("Hyundai Tucson", 120),
    ("Fiat Uno", 60),
    ("Fiat Mobi", 70),
    ("Fiat Pulse", 130)
]

veiculos_alugados = []
alugados = []

while True:
    print("====================")
    print("Bem-vindo à Locadora")
    print("====================")
    print("Selecione a opção desejada:")
    print("| 0 - Ver Veiculos Disponíveis | 1 - Alugar Veículo | 2 - Devolver Veículo | 3 - Sair |")
    escolha = input()

    if escolha == "0":
        os.system("cls" if os.name == "nt" else "clear")
        print("[Veículos Disponíveis:]")
        for i, (carro, preco) in enumerate(veiculos):
            print(f"[{i}] - {carro}: R${preco}/dia")

    elif escolha == "1":
        os.system("cls" if os.name == "nt" else "clear")
        print("[Alugar Veículo:]")
        for i, (veiculo, preco) in enumerate(veiculos):
            print(f"[{i}] - {veiculo}: R$ {preco}/dia")
        print("==========")

        while True:
            try:
                print("Selecione o Veículo que deseja Alugar:")
                selecionar_carro = int(input())
                if 0 <= selecionar_carro < len(veiculos):
                    break
                else:
                    raise ValueError("Opção inválida. Tente novamente.")
            except ValueError as ve:
                print(ve)

        selecionado = veiculos[selecionar_carro][0]

        while True:
            try:
                print(f"Selecione a quantidade de dias que deseja alugar o {selecionado}:")
                dias = int(input())
                if dias <= 0:
                    raise ValueError("Por favor, insira um número positivo para a quantidade de dias.")
                break
            except ValueError as ve:
                print(ve)

        total_pago = dias * veiculos[selecionar_carro][1]
        print("==========")
        print(f"Você gostaria de alugar o Veículo {selecionado} por {dias} dias, totalizando R${total_pago}?")
        print("| 0 - Sim | 1 - Não |")
        aluguel = input()

        if aluguel == "0":
            os.system("cls" if os.name == "nt" else "clear")
            print(f"Veículo {selecionado} alugado por {dias} dias. Total pago: R${total_pago}")
            alugados.append((selecionado, dias, total_pago))
            veiculos_alugados.append(veiculos.pop(selecionar_carro))
        elif aluguel == "1":
            continue

    elif escolha == "2":
        os.system("cls" if os.name == "nt" else "clear")
        print("[Devolver Veículo:]")
        if not alugados:
            print("Nenhum veículo foi alugado.")
        else:
            print("Veículos alugados:")
            for i, (veiculo, dias, total_pago) in enumerate(alugados):
                print(f"[{i}] - {veiculo}: Alugado por {dias} dias. Total pago: R${total_pago}")

            while True:
                try:
                    print("Selecione o veículo que deseja devolver:")
                    devolver_carro = int(input())
                    if 0 <= devolver_carro < len(alugados):
                        break
                    else:
                        raise ValueError("Opção inválida. Tente novamente.")
                except ValueError as ve:
                    print(ve)

            veiculo_devolvido, dias_alugados, total_pago = alugados[devolver_carro]
            alugados.pop(devolver_carro)
            veiculos_alugados.pop(devolver_carro)
            veiculos.append((veiculo_devolvido, total_pago // dias_alugados))

            print(f"Veículo {veiculo_devolvido} devolvido com sucesso! Alugado por {dias_alugados} dias. Total pago: R${total_pago}")

    elif escolha == "3":
        print("Obrigado por utilizar a Locadora. Até logo!")
        break

    else:
        print("Opção inválida. Tente novamente.")
