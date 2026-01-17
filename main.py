from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext, messagebox
from tkcalendar import DateEntry
from datetime import datetime, date
# Cores
Co0 = "#f0f3f5"
co1 = "#feffff"
co2 = "#4fa882"
co3 = "#38576b"
co4 = "#403d3d"
co5 = "#e06636"
co6 = "#038cfc"
co7 = "#3fbfb9"
co8 = "#263238"
co9 = "#e9edf5"

# Cores modernas
cor_fundo = "#f7f9fc" # fundo do aplicativo
cor_frame = "#ffffff" # fundo dos frames
cor_principal = "#4a90e2" # cor principal (azul)
cor_texto = "#4a4a4a" # texto escuro
cor_destaque = "#d0021b" # cor de botões de destaque (vermelho)
cor_borda = "#d9e3f0" # borda leve

# Configuração da janela principal
janela = Tk()
janela.title("Formulário de Consultoria")
janela.geometry("943x453")
janela.configure(background=co9)
janela.resizable(width=FALSE,height=FALSE)

# frames
frameCima = Frame(janela, width=340, height=50, bg=co5, relief="flat")
frameCima.grid(row=0, column=0)

frameBaixo = Frame(janela, width=310, height=403, bg=co1, relief="flat")
frameBaixo.grid(row=1, column=0, pady=1, padx=0, stick=NSEW)

frameDireita = Frame(janela, width=600, height=403, bg=co1, relief="flat")
frameDireita.grid(row=0, column=1, rowspan=2, pady=1, padx=0, stick=NSEW)

#Divisão do frameDireita
frameDireitaCima = Frame(frameDireita, width=600, height=50, bg=co1, relief="flat")
frameDireitaCima.grid(row=0, column=0)

frameDireitaBaixo = Frame(frameDireita, width=600, height=403, bg=co1, relief="flat")
frameDireitaBaixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)



# Execução da janela
app_ = Label(frameCima, text=" ♠ Formulário de consultoria", anchor=CENTER, font=('verdana', 14, 'bold'), bg=co5, fg=co1)
app_.place(relx=0.5,y=25, anchor=CENTER)

# Campo de entrada de texto
l_nome = Label(frameBaixo, text="Nome *", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_nome.place(x=10, y=10)
e_nome = Entry(frameBaixo, width=35, justify='left', relief="solid", font=('verdana', 10))
e_nome.place(x=15, y=40)


l_email = Label(frameBaixo, text="Email *", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_email.place(x=10, y=80)
e_email = Entry(frameBaixo, width=35, justify='left', relief="solid", font=('verdana', 10))
e_email.place(x=15, y=110)


l_telefone = Label(frameBaixo, text="Telefone *", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_telefone.place(x=10, y=150)
e_telefone = Entry(frameBaixo, width=20, justify='left', relief="solid", font=('verdana', 10))
e_telefone.place(x=15, y=180)


l_cal = Label(frameBaixo, text="Data da Consulta *", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_cal.place(x=160, y=150)
e_cal = DateEntry(frameBaixo, width=12, background="darkblue", foreground='white', borderwidth=2, year=datetime.now().year, month=datetime.now().month, day=datetime.now().day, date_pattern='dd/mm/yyyy', font=('verdana', 10))
e_cal.place(x=165, y=180)


l_assunto = Label(frameBaixo, text="Assunto *", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_assunto.place(x=10, y=220)
e_assunto = Text(frameBaixo, width=34, height=5, relief="solid", font=('verdana', 10), wrap='word')
e_assunto.place(x=15, y=250)


#botoes
botao_inserir = Button(frameBaixo, text="Inserir", width=10, height=1, bg=co6, fg=co1, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
botao_inserir.place(x=15, y=340)


botao_Atualizar = Button(frameBaixo, text="Atualizar", width=10, height=1, bg=co5, fg=co1, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
botao_Atualizar.place(x=120, y=340)

botao_Deletar = Button(frameBaixo, text="Deletar", width=10, height=1, bg=co7, fg=co1, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
botao_Deletar.place(x=225, y=340)

janela.mainloop()