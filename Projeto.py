opcao = -1
cont = 0
desi = 'p'

produtos = []
funcionarios = []
salario = []
gastos = []
ganhos = []
estoque = []
vendas = []

while True:
    while opcao > 5 or opcao < 0:
        print(f'{"[SUPER MERCADO]".center(40, "=")}')
        opcao = int(input(f'[0] Funcionario  [1] Estoque'
                          f'\n[2] Gastos       [3] Produtos\n'
                          f'[4] Vendas       [5] Sair\n{"".center(40, "=")}\nEscolha uma opção valida: '))

#OPÇÃO 0 IRA DISPONIBILIZAR O RELATORIO DE SALARIOS DE FUNCIONARIOS, NOME DOS FUNCIONARIOS CADASTRADOS, E CADASTRAR UM FUNCIONARIO NOVO
    if opcao == 0:
        opcao = -1
        cont = 0
        desi = 'p'

        print(f'{"[Funcionarios]".center(40, "=")}')
        while opcao > 4 or opcao < 1:
            opcao = int(input(f'[1] Cadastrados [2] Cadastrar [3] Salario '
                              f'\n[4] Sair\n{"".center(40, "=")}\nEscolha uma opção: '))

        if opcao == 1:
            if len(funcionarios) > 0:
                print('=' * 40)
                print('Os funcionario(s) cadastrado(s) são: ')
                for f in funcionarios:
                    print(f'{f}')

            else:
                print('=' * 40)
                print('Não existe funcionaros registrados.')
                print('=' * 40)
                while desi not in 'SN':
                    desi = str(input('Deseja Cadastrar o primeiro funcionario [S/N]? ').upper().strip())

                print('=' * 40)
                if desi == 'S':
                    desi = 'p'
                    funcionarios.append(str(input('Digite o nome do funcionario: ').capitalize().strip()))
                    salario.append(float(input('Digite o salario do funcionario: ')))

                    print('=' * 40)
                    desi = str(input('Esta correto as informações [S/N]? ').upper().strip())
                    print('=' * 40)
                    print('Cadastro realizado com sucesso.')
                    if desi == 'N':
                        funcionarios.clear()
                        salario.clear()
                        desi = 'p'
                        if len(funcionarios) == 0:
                            print('Descadastro feito com sucesso.')

        if opcao == 2:
            funcionarios.append(str(input('Digite o nome do funcionario: ').capitalize().strip()))
            salario.append(float(input('Digite o salario do funcionario: ').strip()))
            print('=' * 40)
            desi = str(input('Esta correto as informações [S/N]? ').upper().strip())
            print('=' * 40)

            if desi == 'S':
                print('Cadastro realizado com sucesso.')

            if desi == 'N':
                if len(funcionarios) > 0:
                    funcionarios.pop()
                    salario.pop()
                else:
                    funcionarios.clear()
                    salario.clear()
                desi = 'p'
                if len(funcionarios) == 0:
                    print('Descadastro feito com sucesso.')

        if opcao == 3:
            desi = 'p'
            print('=' * 40)
            if len(funcionarios) > 0:
                while desi not in 'SN':
                    desi = str(input('Deseja ver salario de algum funcionario [S/N]? ').strip().upper())

                if desi == 'S':
                    desi = str(input('Qual é o nome do funcionario? ').strip().capitalize())
                    print('=' * 40)
                    if desi in funcionarios:
                        print(f'O salario do {funcionarios[funcionarios.index(desi)]} '
                              f'é R${salario[funcionarios.index(desi)]:.2f}!')
                    else:
                        print(f'{desi} não é um funcionario cadastrado.')

                if desi == 'N':
                    desi = 'p'
                    while desi not in 'SN':
                        print('=' * 40)
                        desi = str(input('Deseja mudar o salario de algum funcionario [S/N]? ').strip().upper())
                        print('=' * 40)

                    if desi == 'S':
                        desi = str(input('Qual é o nome do funcionario? ').strip().capitalize())
                        salario[funcionarios.index(desi)] = \
                            float(input(f'Digite o novo salario do {funcionarios[funcionarios.index(desi)]}: '))

            else:
                print('Nenhum funcionario cadastrado.')

        if opcao == 4:
            print('=' * 40)
            print('[FUNCIONARIOS] Fechaando...')

        opcao = -1
        cont = 0
        desi = 'p'

    if opcao == 1:
        desi = 'p'
        opcao = -1
        cont = 0

        print(f'{"[ESTOQUE]".center(40, "=")}')
        while opcao > 3 or opcao < 1:
            opcao = int(input(f'[1] Ver estoque [2] Adicionar ao estoque\n[3] Sair\n{"".center(40, "=")}'
                              f'\nEscolha uma opção valida: ').strip())
        print('=' * 40)
        if opcao == 1 and len(estoque) > 0:
            print(f'Estoque contem {len(estoque) // 2} produtos. Lista abaixo:')
            print('=' * 40)
            for produto in estoque:
                cont += 1
                if cont % 2 == 1:
                    print(f'{produto.ljust(20, ".")} Quantidade: ', end='')
                else:
                    print(f'{produto}')

        elif opcao == 1 and len(estoque) <= 0:
            print('Estoque vazio!')

        if opcao == 2:
            desi = str(input('Nome do prduto: ').strip().capitalize())
            cont = int(input('Quantidade: ').strip())
            opcao = float(input('Preço gasto: ').strip())

            if desi in estoque:
                estoque[estoque.index(desi)] = desi
                estoque[estoque.index(desi) + 1] += cont
                gastos[estoque.index(desi)] += opcao

            else:
                estoque.append(desi)
                estoque.append(cont)
                gastos.append(opcao)

            print('=' * 40)
            while desi not in 'NS':
                desi = str(input('O cadastro está correto [S/N]? ').upper().strip())
                print('=' * 40)
                print('Cadastro realizado com sucesso.')
            if desi == 'N':
                if len(estoque) <= 0:
                    estoque.clear()
                    print('=' * 40)
                    print('Descadastro realizado com sucesso.')
                else:
                    estoque.pop()
                    estoque.pop()
                    print('=' * 40)
                    print('Descadastro realizado com sucesso.')

            desi = 'p'
            opcao = -1
            cont = 0

        if opcao == 3:
            print('[ESTOQUE] Fechaando...')

        desi = 'p'
        opcao = -1
        cont = 0

    if opcao == 2:
        opcao = -1
        cont = 0
        desi = 'p'

        print(f'{"[GASTOS]".center(40, "=")}')
        while opcao > 4 or opcao < 1:
            opcao = int(input(f'[1] Geral [2] Produtos [3] Funcionarios\n[4] Sair'
                              f'\n{"".center(40, "=")}\nEscolha uma opção valida: '))
        print('=' * 40)
        if opcao == 1 and len(ganhos) > 0 and len(gastos) > 0:
            ganh = 0
            gasto = 0

            for v in gastos:
                gasto += v

            for v in salario:
                gasto += v

            for v in ganhos:
                ganh += v

            porcen = ((ganh - gasto) * 100) // gasto

            print(f'Gastos TOTAL: R${gasto:.2f}.\nGanhos TOTAL: R${ganh:.2f}.'
                  f'\nIsso é {porcen:.0f}% do dinheiro da empresa.')


        if opcao == 2 and len(gastos) > 0:
            gasto = 0
            for preco in gastos:
                gasto += preco
            print(f'Os gastos do Estoque.\nDa um total de: R${gasto:.2f}.')

        if opcao == 3 and len(salario) > 0:
            gasto = 0
            for valo in salario:
                gasto += valo
            print(f'Os gastos com {len(funcionarios)} Funcionario(s).\nDa um total de: R${gasto:.2f}.')

        if len(salario) <= 0 or len(gastos) <= 0:
          if opcao == 1 or opcao == 2 and len(gastos) <= 0:
            print('Não ah nenhum valor registrado...')
          else:
            print('Valor indisponivel no momento...')
            
          if opcao == 3 and len(salario) <= 0:
            print('Não ah nenhum valor registrado...')
          else:
            print('Valor indisponivel no momento...')
          

        if opcao == 4:
            print('Fechando [GASTOS]...')

        opcao = -1
        cont = 0
        desi = 'p'

    if opcao == 3:
        opcao = -1
        desi = 'p'
        cont = 0
        print(f'{"[PRODUTOS]".center(40, "=")}')
        while opcao > 3 or opcao < 1:
            opcao = int(input(F'[1] Adicionar [2] Disponivel [3] Sair'
                              F'\n{"".center(40, "=")}\nEscolha uma opção valida: '))

        print('=' * 40)

        if opcao == 1 and len(estoque) > 0:
            while desi not in estoque:
                desi = str(input('Nome do produto: ').capitalize().strip())
                cont = int(input('Quantidade: ').strip())

            if cont >= estoque[estoque.index(desi) + 1]:
                cont = estoque[estoque.index(desi) + 1]
                del estoque[estoque.index(desi) + 1]
                del estoque[estoque.index(desi)]
            else:
                estoque[estoque.index(desi) + 1] = estoque[estoque.index(desi) + 1] - cont

            if desi in produtos:
                produtos[produtos.index(desi)] = desi
                produtos[produtos.index(desi) + 1] += cont

            else:
                produtos.append(desi)
                produtos.append(cont)

        elif opcao == 1 and len(estoque) <= 0:
            print('ESTOQUE VAZIO...')

        if opcao == 2 and len(produtos) > 0:
            for produto in produtos:
                cont += 1
                if cont % 2 == 1:
                    print(f'{produto.ljust(20, ".")} Quantidade: ', end='')
                else:
                    print(f'{produto}')

        elif opcao == 2 and len(produtos) <= 0:
            print('Você não adicionou nenhum produto!')

        if opcao == 3:
            print('[PRODUTOS] Fechaando...')

        cont = 0
        desi = 'p'
        opcao = -1

    if opcao == 4:
        print(f'{"[VENDAS]".center(40, "=")}')
        opcao = -1
        cont = 0
        desi = 'p'
        while opcao > 3 or opcao < 1:
            opcao = int(input('[1] Vender [2] Vendidos [3] Sair'
                              f'\n{"".center(40, "=")}\nEscolha uma opção valida: '))
        print('=' * 40)

        if opcao == 1:
            desi = str(input('Nome do produto: ').capitalize().strip())
            if desi not in produtos:
                print('=' * 40)
                print('Produto indisponivel...')
            else:
                cont = int(input('Quantidade: ').strip())

                if cont > 0 and desi in produtos:
                    if cont >= produtos[produtos.index(desi) + 1]:
                        cont = produtos[produtos.index(desi) + 1]

                    pre = desi
                    precod = 0

                    if pre in estoque:
                        frac = estoque.index(pre) // 2
                        soma = estoque[estoque.index(pre) + 1] + produtos[produtos.index(pre) + 1]
                        precod = (gastos[frac] / soma) * cont * 0.43

                    else:
                        frac = produtos.index(pre) // 2
                        precod = ((gastos[frac] / produtos[produtos.index(pre) + 1]) * cont) * 0.43

                    print('=' * 40)

                    print(f'Valor de {cont:.0f} unidade(s) de {desi} É: R${precod:.2f}.')

                    print('=' * 40)
                    while desi not in 'SN':
                        desi = str(input('Deseja efetuar a compra [S/N]? ').upper().strip())

                    if desi == 'S':
                        if cont >= produtos[produtos.index(pre) + 1]:
                            del produtos[produtos.index(pre) + 1]
                            del produtos[produtos.index(pre)]
                            ganhos.append(precod)

                        else:
                            produtos[produtos.index(pre) + 1] -= cont
                            ganhos.append(precod)

                        print('=' * 40)
                        print('Compra efetuada com sucesso...')

                    else:
                        print('=' * 40)
                        print('Compra cancelada com sucesso...')
                else:
                    print('=' * 40)
                    print(f'Não é possivel comprar {cont} unidades.')

        if opcao == 2:
            print(f'Foram vendidos um total de {len(ganhos)} mercadoria.')

        if opcao == 3:
            print('[VENDAS] Fechando...')

        opcao = -1
        cont = 0
        desi = 'p'

    if opcao == 5:
        print('=' * 40)
        print('[FECHANDO]....')
        print('=' * 40)
        break


