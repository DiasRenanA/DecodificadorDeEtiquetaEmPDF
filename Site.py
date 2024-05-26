import streamlit as st
import base64
import os

class Site:
    # ------------------ Funções ----------------
    def DownloadPDF(self):
        self.Descriptografar()
        if self.pdf_string01 == "%":
            caminho_pdf = self.temp_pdf_file
            with open(caminho_pdf, "rb") as pdf_file:
                pdf_bytes = pdf_file.read()
            st.download_button(
                label='Baixar PDF',
                data=pdf_bytes,
                file_name=f'{self.temp_pdf_file}',
                mime='application/pdf'
            )
            os.remove(caminho_pdf)
        else:
            st.error("Erro: O texto fornecido não está em Base64 ou está corrompido.")

    def Descriptografar(self):
        try:
            pdf_data = base64.b64decode(self.Base64_str)  # Decodifique o texto Base64 para obter os dados binários do PDF
            pdf_string = pdf_data.decode('latin-1')  # Para transformar de binário para string
            self.pdf_string01 = pdf_string[0]
            self.temp_pdf_file = f"{self.NomePDF}.pdf"  # Crie um arquivo temporário para salvar os dados binários do PDF
            with open(self.temp_pdf_file, "wb") as f:
                f.write(pdf_data)
        except Exception as e:
            st.error(f"Erro ao descriptografar o texto Base64: {e}")

    # --------------------------------------------
    def __init__(self):
        self.pdf_string01 = ''
        self.temp_pdf_file = ''
        with st.container():  # Cabeçalho da página
            st.subheader("DECODIFICADOR DE PDF EM BASE64111")
            st.write("Preencha os campos abaixo para ter seu PDF decodificado")

        with st.container():  # Campo para preencher
            self.NomePDF = st.text_input("Digite um nome para o PDF:")
            self.Base64_str = st.text_area("Cole aqui o texto em Base64: ", height=400)
            if st.button('Descriptografar e Baixar PDF'):
                self.DownloadPDF()

if __name__ == "__main__":
    Site()
