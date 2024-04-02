usuario = 1
creditos_cartao = 0.0
valor_passagem = 6.0
senha = 1234
contador = 0
if usuario != 0:
    while usuario != 0:
        usuario = int(input('Qual seu usuário?\n'
                            'Administrador - 1\n'
                            'Usuário - 2\n'
                            'Sair - 0\n'))
        if usuario == 1:
            senha_autenticacao = int(input('Digite sua senha: \n'))
            if senha_autenticacao != senha:
                while senha_autenticacao != senha:
                    senha_autenticacao = int(input('Digite sua senha: \n'))
            opcoes = int(input('Bem vindo Administrador!\n'
                               'O que você deseja fazer?\n'
                               'Visualizar créditos do cartão - 1\n'
                               'Alterar Valor da passagem - 2\n'
                               'Sair - 0\n'))
            if opcoes == 1:
                print(f'O Usuário tem {creditos_cartao} créditos restantes.')
            elif opcoes == 2:
                valor_passagem = float(input('Qual valor da passagem você deseja definir? \n'))
                print(f'O Valor da passagem foi alterado para: R${valor_passagem:.2f}')
