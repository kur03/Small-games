# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
from tkinter import *
from tkinter import messagebox
from game import print_symbole
from game import check
from game import isfilled

player = 1

def Close(window):
    window.destroy()


def menu_bar(window) :
    # barre de menu
    bar = Menu(window)
    """
    This is how to get a scrolling menu (menu déroulant)
    file_menu = Menu(bar, tearoff=0)
    file_menu.add_command(label="New", command=lambda :[Close(window), new_game(window)])
    file_menu.add_command(label="Leave", command=window.quit)
    bar.add_cascade(label="Options", menu=file_menu)
    """
    bar.add_cascade(label="New", command=lambda :[Close(window), display_board([[0,0,0], [0,0,0], [0,0,0]])])
    bar.add_cascade(label="Leave", command=window.quit)
    bar.add_cascade(label="Help", command=lambda :[help()])

    window.config(menu=bar)

def help():
    messagebox.askyesno("Help", "The aim is to have three cross aligned for player one, and three circles for player two.\nHave fun!")



# start page
def start() :
    # créer ne première fenêtre
    welcome_page = Tk()
    # personnaliser la fenêtre
    welcome_page.title("Tic-Tac-Toe")
    welcome_page.geometry("500x600")
    welcome_page.minsize(500, 600)
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
    play_btn = Button(frame, text="Play", font=("Helvetica", 15), background='white', foreground='#41b77f', command=lambda: [display_board([[0,0,0], [0,0,0], [0,0,0]]), Close(welcome_page)])
    play_btn.pack(pady=25, fill=X)
    frame.pack(expand=YES)
    menu_bar(welcome_page)


# display the game board
def display_board(board) :
    # créer ne première fenêtre
    board_page = Tk()
    # personnaliser la fenêtre
    board_page.title("Tic-Tac-Toe")
    board_page.geometry("500x600")
    board_page.minsize(500, 600)
    board_page.config(background='#41b77f')

    board_frame = Frame(board_page, bg='#41b77f')
    board_frame.grid_rowconfigure(0, weight=1)
    board_frame.grid_columnconfigure(0, weight=1)
    
    for i in range(len(board)) :
        for j in range(len(board)) :
                Button(board_frame, background='grey', height= 10, width=20, command=lambda x=i, y=j: [play(board_page, board_frame, board, x, y)]).grid(row=i, column=j)

    menu_bar(board_page)

    board_frame.pack(expand=YES)
    

def finished(window) :
    res = messagebox.askyesno("Game finished", "Do you wanna play again?")
    if res == True :
        Close(window)
        display_board([[0,0,0], [0,0,0], [0,0,0]])
    else :
        Close(window)
        start()


def play(window, frame, board, x, y) :
    global player
    print("player = %d"%player)
    symbole = print_symbole(board, x, y, player)
    if symbole == 0 :
        messagebox.showinfo("Error", "You cannot play here")

    if (player == 1) :
        Label(frame, text="X", font=(70), background='grey', foreground='red').grid(row=x, column=y)

    elif (player == 2) :
        Label(frame, text="O", font=(70), background='grey', foreground='blue').grid(row=x, column=y)

    # we check for a winner 1 if it's player 1 and 2 for player 2
    check_winner = 0
    check_winner = check(board, player)
    if ((check_winner == 1) or (check_winner == 2)) :
        messagebox.showinfo("Winner!!", "Player %d won!"%check_winner)
        player = 1
        finished(window)

    # if there is no winner (check_winner = 0) it's the other player turn
    else :
        if (player == 1) :
            player = 2

        else :
            player = 1

        # we check if the board is filled and we can play
        if (isfilled(board) == True) :
            messagebox.showinfo("Draw", "It's a draw!")
            finished(window)
    


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