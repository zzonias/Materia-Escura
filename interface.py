import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import webbrowser
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation


def open_github():
    webbrowser.open("https://github.com/zzonias")


def open_linkedin():
    webbrowser.open("https://www.linkedin.com/in/amanda-carvalho-68062418a/")


def create_interface(x, y1, y2):
    root = tk.Tk()
    root.title("Detecção de Matéria Escura")
    root.geometry("1000x950")
    root.configure(bg="#0d1117")

    # Nome
    name_label = tk.Label(
        root,
        text="Amanda Carvalho",
        font=("Arial", 30, "bold"),
        bg="#0d1117",
        fg="#c9d1d9"
    )
    name_label.pack(pady=(30, 10))


    button_frame = tk.Frame(root, bg="#0d1117")
    button_frame.pack()

    github_button = ttk.Button(button_frame, text="GitHub", command=open_github)
    github_button.pack(side="left", padx=10)

    linkedin_button = ttk.Button(button_frame, text="LinkedIn", command=open_linkedin)
    linkedin_button.pack(side="left", padx=10)

    description = """Este  é o meu primeiro projeto, e ele simula a detecção indireta de matéria escura analisando
a curva de rotação de uma galáxia. Compara a velocidade observada
das estrelas com a velocidade esperada baseada apenas na massa visível."""

    desc_label = tk.Label(
        root,
        text=description,
        font=("Arial", 14),
        bg="#0d1117",
        fg="#8b949e",
        justify="center",
        wraplength=800
    )
    desc_label.pack(pady=30)

    # Gráfico
    fig, ax = plt.subplots(figsize=(8, 5), facecolor='#0d1117')
    ax.set_xlim(0, max(x) + 1)
    ax.set_ylim(0, max(max(y1), max(y2)) + 50)
    ax.set_title("Curva de Rotação Galáctica", color='white', fontsize=16)
    ax.set_xlabel("Raio (kpc)", color='white', fontsize=14)
    ax.set_ylabel("Velocidade (km/s)", color='white', fontsize=14)
    ax.tick_params(colors='white')
    ax.set_facecolor('#161b22')
    ax.grid(True, color='#30363d')

    line1, = ax.plot([], [], label="Velocidade Observada", color='#58a6ff', marker='o')
    line2, = ax.plot([], [], label="Velocidade Esperada", color='#f778ba', linestyle='--')
    ax.legend()

    chart_canvas = FigureCanvasTkAgg(fig, master=root)
    chart_canvas.draw()
    chart_canvas.get_tk_widget().pack(pady=20)

    x_data, y1_data, y2_data = [], [], []

    def animate(i):
        if i < len(x):
            x_data.append(x[i])
            y1_data.append(y1[i])
            y2_data.append(y2[i])
            line1.set_data(x_data, y1_data)
            line2.set_data(x_data, y2_data)
        return line1, line2

    ani = FuncAnimation(fig, animate, frames=len(x) + 5, interval=300, blit=True)

    root.mainloop()
