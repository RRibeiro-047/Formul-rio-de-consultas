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

# --- armazenamento em memória e exibição na direita ---
registros = []

# Treeview para mostrar todos os registros no lado direito
cols = ("nome", "email", "telefone", "data", "assunto")
tv = ttk.Treeview(frameDireitaBaixo, columns=cols, show='headings', height=18)
tv.heading('nome', text='Nome')
tv.heading('email', text='Email')
tv.heading('telefone', text='Telefone')
tv.heading('data', text='Data')
tv.heading('assunto', text='Assunto')
tv.column('nome', width=120, anchor=W)
tv.column('email', width=140, anchor=W)
tv.column('telefone', width=100, anchor=W)
tv.column('data', width=80, anchor=W)
tv.column('assunto', width=220, anchor=W)
tv.place(x=10, y=10)

sb = Scrollbar(frameDireitaBaixo, orient=VERTICAL, command=tv.yview)
tv.configure(yscrollcommand=sb.set)
sb.place(x=570, y=10, height=360)


def limpar_campos():
	e_nome.delete(0, END)
	e_email.delete(0, END)
	e_telefone.delete(0, END)
	try:
		e_cal.set_date(date.today())
	except Exception:
		pass
	e_assunto.delete('1.0', END)


def atualizar_treeview():
	for i in tv.get_children():
		tv.delete(i)
	for idx, r in enumerate(registros):
		resumo = r['assunto'].replace('\n', ' ')
		tv.insert('', END, iid=str(idx), values=(r['nome'], r['email'], r['telefone'], r['data'], resumo[:120]))


def inserir():
	nome = e_nome.get().strip()
	email = e_email.get().strip()
	telefone = e_telefone.get().strip()
	try:
		data_consulta = e_cal.get_date().strftime('%d/%m/%Y')
	except Exception:
		data_consulta = e_cal.get()
	assunto = e_assunto.get('1.0', END).strip()
	if not (nome and email and telefone and assunto):
		messagebox.showwarning('Campos faltando', 'Preencha todos os campos obrigatórios (*)')
		return
	registros.append({'nome': nome, 'email': email, 'telefone': telefone, 'data': data_consulta, 'assunto': assunto})
	atualizar_treeview()
	limpar_campos()


def selecionar_item(event=None):
	sel = tv.selection()
	if not sel:
		return
	idx = int(sel[0])
	r = registros[idx]
	e_nome.delete(0, END); e_nome.insert(0, r['nome'])
	e_email.delete(0, END); e_email.insert(0, r['email'])
	e_telefone.delete(0, END); e_telefone.insert(0, r['telefone'])
	try:
		d = datetime.strptime(r['data'], '%d/%m/%Y').date()
		e_cal.set_date(d)
	except Exception:
		pass
	e_assunto.delete('1.0', END); e_assunto.insert('1.0', r['assunto'])


def atualizar_registro():
	sel = tv.selection()
	if not sel:
		messagebox.showwarning('Selecionar', 'Selecione um registro para atualizar')
		return
	idx = int(sel[0])
	nome = e_nome.get().strip()
	email = e_email.get().strip()
	telefone = e_telefone.get().strip()
	try:
		data_consulta = e_cal.get_date().strftime('%d/%m/%Y')
	except Exception:
		data_consulta = e_cal.get()
	assunto = e_assunto.get('1.0', END).strip()
	if not (nome and email and telefone and assunto):
		messagebox.showwarning('Campos faltando', 'Preencha todos os campos obrigatórios (*)')
		return
	registros[idx] = {'nome': nome, 'email': email, 'telefone': telefone, 'data': data_consulta, 'assunto': assunto}
	atualizar_treeview()
	limpar_campos()


def deletar_registro():
	sel = tv.selection()
	if not sel:
		messagebox.showwarning('Selecionar', 'Selecione um registro para deletar')
		return
	idx = int(sel[0])
	if messagebox.askyesno('Confirmar', 'Deseja deletar o registro selecionado?'):
		registros.pop(idx)
		atualizar_treeview()
		limpar_campos()


# vincular botões
botao_inserir.config(command=inserir)
botao_Atualizar.config(command=atualizar_registro)
botao_Deletar.config(command=deletar_registro)
tv.bind('<<TreeviewSelect>>', selecionar_item)

janela.mainloop()