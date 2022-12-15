import datetime
import database

menu = """ Por favor selecione um das seguintes opções:
1) Adicionar novo filme.
2) Ver proximo filme
3) Ver todos os filmes
4) Assistir um filme
5) Ver filmes já assistidos
6) sair

Sua seleção: """

bemvindo= "Seja bem vindo ao Watchlist App"

print(bemvindo)
database.create_tables()

def promp_add_movie():
    title = input("Titulo do filme")
    release_date = input("Data de lançamento (dd-mm-YYYY): (DIA-MES-ANO)")
    parsed_date = datetime.datetime.strptime(release_date, "%d-%m-%Y")
    timestamp = parsed_date.timestamp()
    database.add_movie(title, timestamp)

    

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

