import tkinter as tk
from tkinter import messagebox

# Variáveis globais
jogador_atual = "X"
quadro = [["" for _ in range(3)] for _ in range(3)]
placar = {"X": 0, "O": 0}

# Função para atualizar o placar
def atualizar_placar():
    placar_x.config(text=f"Jogador X: {placar['X']}")
    placar_o.config(text=f"Jogador O: {placar['O']}")

# Função para verificar o vencedor
def verificar_vencedor():
    for i in range(3):
        if quadro[i][0] == quadro[i][1] == quadro[i][2] != "":
            return quadro[i][0]
        if quadro[0][i] == quadro[1][i] == quadro[2][i] != "":
            return quadro[0][i]
    if quadro[0][0] == quadro[1][1] == quadro[2][2] != "":
        return quadro[0][0]
    if quadro[0][2] == quadro[1][1] == quadro[2][0] != "":
        return quadro[0][2]
    return None

# Função para verificar empate
def verificar_impate():
    for row in quadro:
        for cell in row:
            if cell == "":
                return False
    return True

# Função para processar um clique no tabuleiro
def on_click(row, col):
    global jogador_atual
    if quadro[row][col] == "":
        quadro[row][col] = jogador_atual
        botao[row][col].config(text=jogador_atual)
        vencedor = verificar_vencedor()
        if vencedor:
            placar[vencedor] += 1
            atualizar_placar()
            messagebox.showinfo("Jogo da Velha", f"O jogador {vencedor} venceu!")
            reset()
        elif verificar_impate():
            messagebox.showinfo("Jogo da Velha", "Empate!")
            reset()
        else:
            jogador_atual = "O" if jogador_atual == "X" else "X"

# Função para reiniciar o jogo
def reset():
    global jogador_atual, quadro
    jogador_atual = "X"
    quadro = [["" for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            botao[i][j].config(text="")
            
# Criar a janela principal
janela = tk.Tk()
janela.title("Jogo da Velha")

# Criar botões para o tabuleiro
botao = [[None, None, None] for _ in range(3)]
for i in range(3):
    for j in range(3):
        botao[i][j] = tk.Button(janela, text="", width=10, height=2,
                                 command=lambda row=i, col=j: on_click(row, col))
        botao[i][j].grid(row=i, column=j)

# Criar placar
placar_x = tk.Label(janela, text=f"Jogador X: {placar['X']}")
placar_o = tk.Label(janela, text=f"Jogador O: {placar['O']}")
placar_x.grid(row=4, column=0)
placar_o.grid(row=4, column=2)

# Botão para reiniciar o jogo
reset_button = tk.Button(janela, text="Reiniciar", command=reset)
reset_button.grid(row=3, column=1)

# Iniciar o jogo
janela.mainloop()
