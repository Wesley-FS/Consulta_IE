import requests
import time
import tkinter as tk
from tkinter import filedialog, scrolledtext
import threading
import math

class CNPJApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Consulta de CNPJs - Inscrição Estadual")
        self.root.geometry("700x500")

        self.label = tk.Label(root, text="Selecione o arquivo com os CNPJs:")
        self.label.pack(pady=5)

        self.btn_selecionar = tk.Button(root, text="Selecionar Arquivo", command=self.selecionar_arquivo)
        self.btn_selecionar.pack(pady=5)

        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20)
        self.text_area.pack(padx=10, pady=10)

        self.progress_label = tk.Label(root, text="")
        self.progress_label.pack()

    def selecionar_arquivo(self):
        caminho_arquivo = filedialog.askopenfilename(
            title="Selecione o arquivo com os CNPJs",
            filetypes=[("Arquivos de texto", "*.txt")]
        )

        if not caminho_arquivo:
            self.text_area.insert(tk.END, "Nenhum arquivo selecionado.\n")
            return

        threading.Thread(target=self.processar_cnpjs, args=(caminho_arquivo,), daemon=True).start()

    def processar_cnpjs(self, caminho_arquivo):
        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            cnpjs = [linha.strip() for linha in f if linha.strip()]

        total = len(cnpjs)
        tempo_total_segundos = total * 12
        tempo_estimado = self.formatar_tempo(tempo_total_segundos)
        self.text_area.insert(tk.END, f"Total de CNPJs: {total}\n")
        self.text_area.insert(tk.END, f"Tempo estimado: {tempo_estimado}\n\n")
        self.text_area.insert(tk.END, f"{'Nº':<5} | {'CNPJ':<12} | Inscrição Estadual\n")
        self.text_area.insert(tk.END, "-" * 41 + "\n")

        resultados = {}

        for i, cnpj in enumerate(cnpjs, start=1):
            self.progress_label.config(text=f"Processando {i}/{total} - CNPJ: {cnpj}")
            url = f"https://open.cnpja.com/office/{cnpj}"
            try:
                resposta = requests.get(url)

                if resposta.status_code == 200:
                    data = resposta.json()
                    campo_API = data.get("registrations", [{}])[0].get("number", "Não encontrado")
                elif resposta.status_code == 429:
                    campo_API = "Erro 429: limite da API"
                else:
                    campo_API = f"Erro: {resposta.status_code}"
            except Exception as e:
                campo_API = f"Erro ao conectar: {e}"

            resultados[cnpj] = campo_API
            self.text_area.insert(tk.END, f"{i}/{total} | {cnpj}: {campo_API}\n")
            self.text_area.see(tk.END)

            time.sleep(12)

        with open("inscricoes_estaduais.txt", "w", encoding="utf-8") as f:
            for cnpj, reg in resultados.items():
                f.write(f"{cnpj}: {reg}\n")

        self.text_area.insert(tk.END, "\nConsulta finalizada. Resultado salvo em 'inscricoes_estaduais.txt'.\n")
        self.progress_label.config(text="Concluído!")

    def formatar_tempo(self, segundos):
        minutos = segundos // 60
        segundos_restantes = segundos % 60
        return f"{minutos}m {segundos_restantes}s"

# Execução da interface
if __name__ == "__main__":
    root = tk.Tk()
    app = CNPJApp(root)
    root.mainloop()
