from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext, messagebox

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

janela.mainloop()