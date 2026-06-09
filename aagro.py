#Algoritmo e Lógica de Programação
#SISTEMA DE GESTÃO AGROPECUÁRIA - FAZENDA AGROPAI
#Dupla: Pedro Vyttor, Marcus Vinicius

usuarios = [["admin", "123", "ADM"], ["cliente", "123", "CLIENTE"]]

rebanho = []
producao = []
compras = []
agendamentos = []

faturamento_total = 0.0

blacklist = ['fezes', 'urina', 'cocô']

while True:
    print("\n==========================================")
    print("   SISTEMA DE GESTÃO - FAZENDA AGROPAI")
    print("==========================================")
    print("1 - login")
    print("2 - cadastro de usuário (cliente)")
    print("0 - sair do sistema")
    print("==========================================")

    menu = int(input("escolha uma opçao: "))

    #menulogin
    if menu == 1:
        usuario = input("usuario: ")
        senha = input("senha: ")
        login = False

        for u in usuarios:
            if usuario == u[0] and senha == u[1]:
                login = True
                tipo_usuario = u[2]

        if login == True:
            print(f"\n-> login realizado com sucesso! bem-vindo, {usuario}.")

            #paineladmin
            if tipo_usuario == "ADM":
                while True:
                    print("\n==========================================")
                    print("          PAINEL ADMINISTRATIVO (ADM)")
                    print("==========================================")
                    print("1 - cadastrar animal (brinco)")
                    print("2 - listar/buscar rebanho")
                    print("3 - atualizar Status de Animal")
                    print("4 - remover animal do rebanho")
                    print("5 - registrar produção / derivados")
                    print("6 - visualizar estoque da produção")
                    print("7 - balanço financeiro da fazenda (tema livre)")
                    print("8 - cadastrar novo usuario")
                    print("9 - listar usuarios cadastrados")
                    print("10 - banir usuario do sistema")
                    print("11 - relatorio geral")
                    print("0 - fazer logout")
                    print("==========================================")

                    op = int(input("escolha uma opcao: "))

                    if op == 1:
                        tipo_animal = input("tipo do animal: ")

                        while True:
                            numero_animal = input("identificação (brinco/número): ")
                            eh_numero_valido = True
                            if len(numero_animal) == 0:
                                eh_numero_valido = False

                            for caractere in numero_animal:
                                if not ('0' <= caractere <= '9'):
                                    eh_numero_valido = False

                            if eh_numero_valido == True:
                                numero_repetido = False
                                for animal in rebanho:
                                    if numero_animal == animal[1]:
                                        numero_repetido = True

                                if numero_repetido == True:
                                    print("ERRO: ja existe um animal cadastrado com este brinco")
                                else:
                                    break
                            else:
                                print("ERRO: o brinco deve conter apenas dígitos numéricos positivos")

                        status_animal = input("status (ex: em lactação, para engorda, disponível para venda): ")
                        rebanho.append([tipo_animal, numero_animal, status_animal])
                        print("animal registrado no rebanho com sucesso!")

                    elif op == 2:
                        if len(rebanho) == 0:
                            print("o rebanho está vazio")
                        else:
                            print("\n=== REBANHO FAZENDA SERTÃO ===")
                            for animal in rebanho:
                                print(f"tipo: {animal[0]} | brinco: {animal[1]} | status: {animal[2]}")

                    elif op == 3:
                        if len(rebanho) == 0:
                            print("não ha animais cadastrados para atualizar")
                        else:
                            busca_brinco = input("digite o brinco do animal que deseja atualizar: ")
                            achou = False
                            for animal in rebanho:
                                if animal[1] == busca_brinco:
                                    achou = True
                                    print(f"status atual: {animal[2]}")
                                    novo_status = input("digite o NOVO status do animal: ")
                                    animal[2] = novo_status
                                    print("status updated com sucesso!")
                            if not achou:
                                print("animal não encontrado com este brinco.")

                    elif op == 4:
                        if len(rebanho) == 0:
                            print("sem animais registrados.")
                        else:
                            numero = input("numero do brinco para remover: ")
                            removido = False

                            for animal in list(rebanho):
                                if numero == animal[1]:
                                    rebanho.remove(animal)
                                    removido = True
                                    print("animal removido do rebanho")
                                    break

                            if removido == False:
                                print("animal não encontrado")

                    elif op == 5:
                        while True:
                            produto = input("nome do produto (ex: leite in natura, queijo coalho, queijo manteiga): ")
                            produto_proibido = False
                            for termo in blacklist:
                                if termo in produto.lower():
                                    produto_proibido = True

                            if produto_proibido == True:
                                print("ERRO: Nome invalido ou nao permitido")
                            else:
                                break

                        while True:
                            qtd_input = input("quantidade produzida (litros/kg): ")
                            eh_qtd_valida = True
                            if len(qtd_input) == 0:
                                eh_qtd_valida = False

                            for caractere in qtd_input:
                                if not ('0' <= caractere <= '9'):
                                    eh_qtd_valida = False

                            if eh_qtd_valida == True:
                                quantidade = int(qtd_input)
                                if quantidade > 0:
                                    break
                                else:
                                    print("ERRO: a quantidade deve ser maior do que zero")
                            else:
                                print("ERRO: digite um número inteiro positivo")

                        while True:
                            valor_input = input("valor de venda por unidade/kg (R$): ")
                            eh_valor_valido = True
                            pontos = 0
                            if len(valor_input) == 0:
                                eh_valor_valido = False

                            for caractere in valor_input:
                                if caractere == '.':
                                    pontos += 1
                                elif not ('0' <= caractere <= '9'):
                                    eh_valor_valido = False

                            if pontos > 1:
                                eh_valor_valido = False

                            if eh_valor_valido == True:
                                valor_venda = float(valor_input)
                                if valor_venda > 0:
                                    break
                                else:
                                    print("ERRO: o valor de venda deve ser maior do que zero")
                            else:
                                print("ERRO: digite um valor numérico positivo válido")

                        existe_no_estoque = False
                        for p in producao:
                            if p[0].lower() == produto.lower():
                                p[1] += quantidade
                                p[2] = valor_venda
                                existe_no_estoque = True
                                print("quantidade adicionada ao estoque existente")

                        if not existe_no_estoque:
                            producao.append([produto, quantidade, valor_venda])
                            print("novo lote de produção adicionado ao estoque")

                    elif op == 6:
                        if len(producao) == 0:
                            print("estoque de produção vazio")
                        else:
                            print("\n=== ESTOQUE DE PRODUTOS DISPONÍVEIS ===")
                            for p in producao:
                                print(f"produto: {p[0]} | disponível: {p[1]} (kg/L) | preço de venda: R$ {p[2]:.2f}")

                    elif op == 7:
                        print("\n=== BALANÇO FINANCEIRO DA FAZENDA ===")
                        print(f"faturamento total com vendas efetuadas: R$ {faturamento_total:.2f}")

                        valor_estimado_estoque = 0.0
                        for p in producao:
                            valor_estimado_estoque += (p[1] * p[2])
                        print(f"valor estimado do estoque atual: R$ {valor_estimado_estoque:.2f}")

                    elif op == 8:
                        novo_usuario = input("novo usyario: ")

                        usuario_invalido = False
                        if len(novo_usuario) == 0:
                            usuario_invalido = True
                        for caractere in novo_usuario:
                            if not ('a' <= caractere <= 'z' or 'A' <= caractere <= 'Z' or caractere == ' '):
                                usuario_invalido = True

                        na_blacklist = False
                        for termo in blacklist:
                            if termo in novo_usuario.lower():
                                na_blacklist = True

                        usuario_repetido = False
                        for u in usuarios:
                            if novo_usuario == u[0]:
                                usuario_repetido = True

                        if usuario_invalido == True:
                            print("ERRO: o nome de usuario não pode conter numeros ou simbolos")
                        elif na_blacklist == True:
                            print("ERRO: nome de usuario proibido pelas diretrizes do sistema")
                        elif usuario_repetido == True:
                            print("ERRO: este nome de usuario ja esta cadastrado")
                        else:
                            nova_senha = input("senha (minimo 4 dígitos): ")
                            while len(nova_senha) < 4:
                                print("ERRO: a senha deve ter pelo menos 4 dígitos")
                                nova_senha = input("senha (mínimo 4 dígitos): ")

                            tipo = input("tipo (ADM/CLIENTE): ").upper()
                            while tipo != "ADM" and tipo != "CLIENTE":
                                print("tipo inválido!")
                                tipo = input("tipo (ADM/CLIENTE): ").upper()

                            usuarios.append([novo_usuario, nova_senha, tipo])
                            print(f"usuario {novo_usuario} ({tipo}) cadastrado")

                    elif op == 9:
                        print("\n=== USUARIOS DO SISTEMA ===")
                        for u in usuarios:
                            print(f"login: {u[0]} | tipo: {u[2]}")

                    elif op == 10:
                        user_banir = input("nome do usuário a ser banido: ")
                        if user_banir == "admin":
                            print("ERRO: o administrador principal não pode ser banido")
                        else:
                            banido = False
                            for u in list(usuarios):
                                if user_banir == u[0]:
                                    usuarios.remove(u)
                                    banido = True
                                    print("usuário banido e removido do sistema")
                            if banido == False:
                                print("usuario nao encontrado")
                    elif op ==11:
                        print(" ==========================================") 
                        print(" RELATÓRIO GERAL DA FAZENDA") 
                        print("==========================================")
                        tipos_animais = {} for animal in rebanho: tipo = animal[0] 
                            if tipo in tipos_animais: tipos_animais[tipo] += 1 else: tipos_animais[tipo] = 1 print(" --- Rebanho por Tipo ---") 
                            if len(tipos_animais) == 0: print("Nenhum animal cadastrado.") 
                                else:
                                    for tipo, quantidade in tipos_animais.items(): 
                                        print(f"{tipo}: {quantidade} animal(is)") 
                                        total_leite = 0  
                                        estoque_queijos = {} 
                                        for produto in producao: nome = produto[0].lower() quantidade = produto[1] 
                                        if "leite" in nome:
                                            total_leite += quantidade 
                                            if "queijo" in nome:
                                                estoque_queijos[produto[0]] = quantidade 
                                                print(" --- Produção de Leite ---") 
                                                print(f"Total em estoque: {total_leite} litro(s)") 
                                                print(" --- Estoque de Queijos ---") 
                                                if len(estoque_queijos) == 0: 
                                                    print("Nenhum queijo em estoque.") 
                                                else:
                                                    for queijo, quantidade in estoque_queijos.items(): 
                                                        print(f"{queijo}: {quantidade} kg/L") 
                            print(" ==========================================")


                    elif op == 0:
                        print("logout do ADM realizado")
                        break
                    else:
                        print("opcao invalida")

            #menucliente
            elif tipo_usuario == "CLIENTE":
                while True:
                    print("\n==========================================")
                    print("            MENU DO CLIENTE")
                    print("==========================================")
                    print("1 - visualizar produtos e preços")
                    print("2 - efetuar compra (produtos / lotes)")
                    print("3 - agendar retirada / transporte")
                    print("4 - extrato detalhado de compras (tema livre)")
                    print("0 - fazer logout")
                    print("==========================================")

                    op = int(input("escolha uma opção: "))

                    if op == 1:
                        if len(producao) == 0:
                            print("a fazenda não possui produtos disponiveis para venda no momento")
                        else:
                            print("\n=== VITRINE DE PRODUTOS DA FAZENDA ===")
                            for p in producao:
                                print(f"produto: {p[0]} | estoque: {p[1]} kg/L | preço: R$ {p[2]:.2f}")

                    elif op == 2:
                        if len(producao) == 0:
                            print("nao há produtos no estoque para comprar")
                        else:
                            produto_desejado = input("digite o nome do produto que deseja comprar: ")
                            existe = False

                            for p in producao:
                                if produto_desejado.lower() == p[0].lower():
                                    existe = True
                                    print(f"produto encontrado! estoque disponivel: {p[1]} kg/L")

                                    while True:
                                        qtd_input = input("quantidade/peso que deseja comprar: ")
                                        eh_qtd_valida = True
                                        if len(qtd_input) == 0:
                                            eh_qtd_valida = False

                                        for caractere in qtd_input:
                                            if not ('0' <= caractere <= '9'):
                                                eh_qtd_valida = False

                                        if eh_qtd_valida == True:
                                            qtd_compra = int(qtd_input)
                                            if qtd_compra > 0:
                                                break
                                            else:
                                                print("quantidade invalida! deve ser maior que zero")
                                        else:
                                            print("quantidade invalida! digite apenas números positivos")

                                    if qtd_compra <= p[1]:
                                        p[1] = p[1] - qtd_compra

                                        valor_pago = qtd_compra * p[2]
                                        faturamento_total += valor_pago

                                        compras.append([p[0], qtd_compra, valor_pago])
                                        print(f"compra de {qtd_compra} kg/L de {p[0]} realizada com sucesso!")

                                        if p[1] == 0:
                                            producao.remove(p)
                                    else:
                                        print("ERRO: a fazenda não possui essa quantidade em estoque")

                            if existe == False:
                                print("produto não encontrado na vitrine da fazenda")

                    elif op == 3:
                        if len(compras) == 0:
                            print("você precisa efetuare uma compra antes de agendar uma retirada")
                        else:
                            print("\n=== AGENDAMENTO DE TRANSPORTE ===")
                            data = input("digite a data da retirada (ex: 25/05/2026): ")
                            horario = input("digite o horário (ex: 08:30): ")
                            placa = input("digite a placa do caminhão/veículo de carga: ")

                            agendamentos.append([data, horario, placa])
                            print("retirada agendada com sucesso! o produtor foi notificado")

                    #extratodecompras temalivre
                    elif op == 4:
                        if len(compras) == 0:
                            print("voce ainda não realizou nenhuma compra")
                        else:
                            print("\n==========================================")
                            print("      EXTRATO DETALHADO DE COMPRAS")
                            print("==========================================")
                            total_geral = 0.0
                            for c in compras:
                                print(f"produto: {c[0]} | qtd: {c[1]} | total: R$ {c[2]:.2f}")
                                total_geral += c[2]
                            print("------------------------------------------")
                            print(f"VALOR TOTAL INVESTIDO: R$ {total_geral:.2f}")

                            if len(agendamentos) > 0:
                                print("\n--- retiradas agendadas ---")
                                for a in agendamentos:
                                    print(f"data: {a[0]} às {a[1]} | caminhão placa: {a[2]}")
                            else:
                                print("\n[AVISO]: voce ainda não agendou a retirada das suas compras")
                            print("==========================================")

                    elif op == 0:
                        print("logout do cliente realizado")
                        break
                    else:
                        print("opcao invalida")
        else:
            print("usuarios ou senha incorretos")

    elif menu == 2:
        novo_usuario = input("digite o nome de usuairo desejado: ")

        usuario_invalido = False
        if len(novo_usuario) == 0:
            usuario_invalido = True
        for caractere in novo_usuario:
            if not ('a' <= caractere <= 'z' or 'A' <= caractere <= 'Z' or caractere == ' '):
                usuario_invalido = True

        na_blacklist = False
        for termo in blacklist:
            if termo in novo_usuario.lower():
                na_blacklist = True

        usuario_repetido = False
        for u in usuarios:
            if novo_usuario == u[0]:
                usuario_repetido = True

        if usuario_invalido == True:
            print("ERRO: o nome de usuario não pode conter números ou simbolos")
        elif na_blacklist == True:
            print("ERRO: Nome de usuario não permitido pelas regras do sistema")
        elif usuario_repetido == True:
            print("ERRO: este nome de usuairo já está cadastrado!")
        else:
            nova_senha = input("crie uma senha (mínimo 4 dígitos): ")
            while len(nova_senha) < 4:
                print("ERRO: a senha deve ter pelo menos 4 dígitos")
                nova_senha = input("crie uma senha (minimo 4 dígitos): ")
            usuarios.append([novo_usuario, nova_senha, "CLIENTE"])
            print("cadastro efetuado! agora voce pode realizar o login (opção 1)")

    #fecharsistematotal
    elif menu == 0:
        print("finalizando o Sistema de Gestão - fazenda AgroPai. até breve, consagrado(a)!")
        break

    else:
        print("opcao inválida no menu principal")
