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

def Close(window):
    window.destroy()

def menu_bar(window) :
    # barre de menu
    bar = Menu(window)
    file_menu = Menu(bar, tearoff=0)
    file_menu.add_command(label="Nouveau")
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
    play_btn = Button(frame, text="Play", font=("Helvetica", 15), background='white', foreground='#41b77f', command=lambda: [display_board(), Close(welcome_page)])
    play_btn.pack(pady=25, fill=X)
    frame.pack(expand=YES)
    menu_bar(welcome_page)

def display_board() :
    # créer ne première fenêtre
    board_page = Tk()
    # personnaliser la fenêtre
    board_page.title("Tic-Tac-Toe")
    board_page.geometry("500x500")
    board_page.minsize(300, 300)
    board_page.config(background='#41b77f')

    board_frame = Frame(board_page, bg='#41b77f')
    for i in range(len(board)) :
        for j in range(len(board)) :
            if board[i][j] == 0 :
                Button(board_frame, background='grey', command=lambda x=i, y=j: [play(x, y)]).grid(row=i, column=j)
            elif board[i][j] == 1 :
               Label(board_frame, text="X", font=(50), background='grey', foreground='red').grid(row=i, column=j)
            else :
               Label(board_frame, text="O", font=(50), background='grey', foreground='blue').grid(row=i, column=j)

    menu_bar(board_page)

    board_frame.pack(expand=YES)

def play(x, y) :
    print_symbole(board, x, y, player)

start()
mainloop()

"""board[3][3] = [[0,0,0], [0,0,0], [0,0,0]]

def Close(window):
    window.destroy()


def menu(window):
    btn_retour = Button(window, text="Menu", command=lambda: [w_accueil(), Close(window)])
    btn_retour.pack(pady=10)

def w_accueil():
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