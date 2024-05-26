from Services.FuncoesService import FuncoesBasicas

class MenuPrograma:
    def Opcao(self):
        self.OpcaoMenu: dict = {
            "1": "Converte de base64",
            "2": "Converte para base64"
        }
    def __init__(self):
        while True:
            self.OpcaoMenu: dict = {
                "1": "Converte de base64",
                "2": "Converte para base64"
            }
            for key, value in self.OpcaoMenu.items():
                print(f"[{key}] -> {value}")
            opcao: str = input("Escolha uma opção: ")
            match opcao:
                case "1":
                    NomeArquivo: str = str(input("Digite um nome para o arquivo: "))
                    StringBase64: str = str(input("Digite o texto: "))
                    FuncoesBasicas().Descriptografar(Base64_str=StringBase64, NomeArquivo=NomeArquivo)
                    break
                case "2":
                    print("2")
                    break
                case _:
                    print("opção inválida, tente novamente")

if __name__ == "__main__":
    MenuPrograma()