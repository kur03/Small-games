"""
Change buttons' size
Function to handle the chosen case by player
Change player turn and print player turn
"""

# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
from tkinter import *
from game import print_symbole
from game import check
from game import isfilled

board = [[0,0,0], [0,0,0], [0,0,0]]
player = 1
check_winner = 0

def Close(window):
    window.destroy()

def menu_bar(window) :
    # barre de menu
    bar = Menu(window)
    file_menu = Menu(bar, tearoff=0)
    file_menu.add_command(label="New")
    file_menu.add_command(label="Leave", command=window.quit)
    bar.add_cascade(label="Options", menu=file_menu)

    window.config(menu=bar)

# start page
def start() :
    # créer ne première fenêtre
    welcome_page = Tk()
    # personnaliser la fenêtre
    welcome_page.title("Tic-Tac-Toe")
    welcome_page.geometry("500x500")
    welcome_page.minsize(300, 300)
    welcome_page.config(background='#41b77f')

    frame = Frame(welcome_page, bg='#41b77f')

    # ajouter du text
    # Label(localsation, texte)
    label_title = Label(frame, text="Tic-Tac-Toe", font=("Helvetica", 30), background='#41b77f', foreground='white')
    # pour afficher le text
    label_title.pack()

    # ajouter un second text
    label_subtitle = Label(frame, text="Who is the best ?", font=("Helvetica", 15), background='#41b77f', foreground='white')
    label_subtitle.pack()

    # ajouter un btn
    play_btn = Button(frame, text="Play", font=("Helvetica", 15), background='white', foreground='#41b77f', command=lambda: [display_board(player, check_winner), Close(welcome_page)])
    play_btn.pack(pady=25, fill=X)
    frame.pack(expand=YES)
    menu_bar(welcome_page)

# display the game board
def display_board(player, check_winner) :
    # créer ne première fenêtre
    board_page = Tk()
    # personnaliser la fenêtre
    board_page.title("Tic-Tac-Toe")
    board_page.geometry("500x500")
    board_page.minsize(300, 300)
    board_page.config(background='#41b77f')

    filled = isfilled(board)
    if check_winner == 1 :
        Label(board_page, text="Player 1 won!", font=("Helvetica", 15), background='#41b77f', foreground='white').pack()
    elif check_winner == 2 :
        Label(board_page, text="Player 2 won!", font=("Helvetica", 15), background='#41b77f', foreground='white').pack()
    if filled != 1 :
        Label(board_page, text="It's a draw!",font=("Helvetica", 15), background='#41b77f', foreground='white').pack()

    else :
        board_frame = Frame(board_page, bg='#41b77f')
        board_frame.grid_rowconfigure(0, weight=1)
        board_frame.grid_columnconfigure(0, weight=1)
        for i in range(len(board)) :
            for j in range(len(board)) :
                if board[i][j] == 0 :
                    Button(board_frame, background='grey', height= 10, width=20, command=lambda x=i, y=j: [play(x, y, player), Close(board_page)]).grid(row=i, column=j)
                elif board[i][j] == 1 :
                    Label(board_frame, text="X", height= 8, width=8, font=(50), background='grey', foreground='red').grid(row=i, column=j)
                else :
                    Label(board_frame, text="O", height= 8, width=8, font=(50), background='grey', foreground='blue').grid(row=i, column=j)

        menu_bar(board_page)

        board_frame.pack(expand=YES)

def play(x, y, player) :
    symbole = print_symbole(board, x, y, player)
    if player == 1 :
        player = 2
    else :
        player = 1
    check_winner = check(board, x, y, player)
    print(check_winner)
    display_board(player, check_winner)


start()
mainloop()




"""def w_accueil():
    accueil = Tk()
    accueil.title("Tic-Tac-Toe")
    accueil.geometry("2048x1780")
    #creer image
    width = 330
    height = 300
    #IMAGE = PhotoImage(file="Bienvenue.png").zoom(9).subsample(6)
    canvas = Canvas(master=accueil, width=width, height=height)
    #canvas.create_image((1, 1), accueil, image=IMAGE)
    canvas.pack(expand=YES)

    btn_instru = Button(accueil, text="Aide", command=lambda: [w_aide(), Close(accueil)])
    btn_code = Button(accueil, text="Play", command=lambda: [w_game(), Close(accueil)])
    btn_instru.pack(pady=10)
    btn_code.pack(pady=10)
    w_exit(accueil)

def w_aide():
    Aide = Tk()
    Aide.title("Tic-Tac-Toe")
    Aide.geometry("2048x1780")
    menu(Aide)
    w_exit(Aide)

def w_game():
    game.title("Tic-Tac-Toe")
    game.geometry("2048x1780")


def h_input():
    w_hash = Tk()
    w_hash.title("Tic-Tac-Toe")
    w_hash.geometry("2048x1780")
    input_hash = Entry(w_hash)
    input_hash.pack()
    valider = Button(w_hash, text="Valider", command=lambda: [fonction(), Close(w_hash)])
    valider.pack(pady=10)
    menu(w_hash)
    w_exit(w_hash)

def w_exit(window):
    btn_exit = Button(window, text="Quitter", command=quitter)
    btn_exit.pack(pady=10)

def quitter():
    quit()"""