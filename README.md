# 📄 Consulta Inscrição Estadual

Este projeto é uma aplicação Python com interface gráfica (GUI) que realiza **consultas de CNPJs para obter a Inscrição Estadual** usando uma **API pública**.

---

## 🔎 Sobre o Projeto

A ferramenta permite carregar um arquivo `.txt` com uma lista de CNPJs, um por linha, e realiza a consulta de cada CNPJ junto à API do [Open CNPJa](https://open.cnpja.com/). O resultado é exibido na tela em tempo real e salvo em um arquivo `inscricoes_estaduais.txt`.

⚠️ **Observação:** A API pública utilizada possui limitação de requisições. Para evitar bloqueio por excesso, o programa realiza uma pausa de **12 segundos entre cada consulta**.

---

## 🖥️ Interface Gráfica

A interface foi construída com `Tkinter` e conta com:

- Botão para selecionar o arquivo `.txt`
- Área de exibição dos resultados em tempo real
- Contador de progresso (ex: `3/15`)
- Estimativa de tempo de execução baseada na quantidade de CNPJs
- Cabeçalho com identificação de colunas: **CNPJ** e **Inscrição Estadual**

---

## 📂 Formato do Arquivo de Entrada

O arquivo `cnpjs.txt` deve conter **um CNPJ por linha**, sem vírgulas ou outros separadores:

12345678900000<br>
00000321654987<br>
92021458563186<br>

## 📤 Saída

Ao final da execução, um arquivo chamado `inscricoes_estaduais.txt` será gerado com o resultado de cada CNPJ consultado:

Total de CNPJs: 3 <br>
Tempo estimado:  36s <br>

Nº    | CNPJ         | Inscrição Estadual <br>
----------------------------------------- <br>
1/3 | 12345678900000: 256496790741 <br>
2/3 | 00000321654987: 963214752315 <br>
3/3 | 12345678900000: 963284554615 <br>



---

## ▶️ Como Usar

1. **Baixe o executável [ConsultaIE.exe](https://github.com/Wesley-FS/Consulta_IE/blob/main/ConsultaIE.exe)**  

2. **Execute o arquivo `ConsultaIE.exe`**

3. **Selecione o arquivo `.txt` contendo os CNPJs**

4. **Aguarde o processamento (12 segundos por CNPJ)**

5. **O resultado será salvo em `inscricoes_estaduais.txt` na mesma pasta do executável**

---

## ✅ Tecnologias Utilizadas

- [Python 3.x](https://www.python.org/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [Requests](https://pypi.org/project/requests/)
- [PyInstaller](https://www.pyinstaller.org/) (para empacotamento em `.exe`)

---

## 💡 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests com melhorias, correções ou sugestões.

---

## ✉️ Contato

Para dúvidas ou sugestões, entre em contato:

- Email: wesleyfs7534@gmail.com
- LinkedIn:[Wesley Silva](www.linkedin.com/in/wesley-fs)




