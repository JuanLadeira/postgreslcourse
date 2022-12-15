import database

menu = """ Por favor selecione um das seguintes opções:
1) Adicionar novo filme.
2) Ver filmes prestes a lançar
3) Ver todos os filmes
4) Assistir um filme
5) Ver filmes já assistidos
6) sair

Sua seleção: """

bemvindo= "Seja bem vindo ao Watchlist App"

print(bemvindo)
database.create_tables()

while (user_input := input(menu)) != "6":
    if user_input == '1':
        pass
    elif user_input == '2':
        pass
    elif user_input == '3':
        pass
    elif user_input == '4':
        pass
    elif user_input == '5':
        pass
    else:
        print("Esta seleção não é uma das opções validas, por favor tente novamente")
        
