import base64
import fitz  # PyMuPDF

class FuncoesBasicas:
    def Descriptografar(self, Base64_str: str, NomeArquivo: str):
        pdf_data = base64.b64decode(Base64_str) # Decodifique o texto Base64 para obter os dados binários do PDF

        temp_pdf_file = f"{NomeArquivo}.pdf" # Crie um arquivo temporário para salvar os dados binários do PDF
        with open(temp_pdf_file, "wb") as f: #Essa linha adiciona o texto decodificado ao PDF
            f.write(pdf_data)

        # Abra o arquivo PDF usando PyMuPDF
        '''pdf_document = fitz.open(temp_pdf_file)'''

        # Print do arquivo no console
        '''for numero_pagina in range(len(pdf_documento)):
            pagina = pdf_documento.carregar_pagina(numero_pagina)
            texto = pagina.pegar_texto()
            print(f"Conteúdo da página {numero_pagina + 1}:\n{texto}")'''

