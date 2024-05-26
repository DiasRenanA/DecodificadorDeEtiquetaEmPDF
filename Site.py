import streamlit as st
import base64
import os

class Site:
    def DownloadPDF(self):
        self.Descriptografar()
        if self.pdf_string01 == "%":
            caminho_pdf = self.temp_pdf_file
            with open(caminho_pdf, "rb") as pdf_file:
                pdf_bytes = pdf_file.read()
            st.write("PDF decodificado!")
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

    def __init__(self):
        self.pdf_string01 = ''
        self.temp_pdf_file = ''
        with st.container():
            st.subheader("DECODIFICADOR DE PDF EM BASE64")
            st.write("Preencha os campos abaixo para ter seu PDF decodificado")

        with st.container():
            self.NomePDF = st.text_input("Digite um nome para o PDF:")
            self.Base64_str = st.text_area("Cole aqui o texto em Base64: ", height=400)
            if st.button('Validar'):
                self.ValidarInputs()

    def ValidarInputs(self):
        if not self.NomePDF:
            st.error("Erro: O campo 'Digite um nome para o PDF' não pode estar vazio.")
        elif not self.Base64_str:
            st.error("Erro: O campo 'Cole aqui o texto em Base64' não pode estar vazio.")
        elif len(self.Base64_str) > 100000:
            st.error("Erro: O texto em Base64 excede o limite de 100000 caracteres.")
        else:
            self.DownloadPDF()


if __name__ == "__main__":
    Site()
