import qrcode # pip install qrcode
import customtkinter as ctk # pip install customtkinter

link = ""
generated_qrcode_path = ""

image = qrcode.make("https://github.com/KevynSilveira") # Controi o qrcode
image.save("qr_code_github.png") # Salva ele


# Função para converter o arquivo
def converter():
    # Obter o caminho do arquivo da entrada de texto
    file_path = caminho_arquivo.get()
    print(file_path)

    # Verificar se foi selecionado um arquivo
    if not file_path:
        print("Nenhum arquivo selecionado.")
        return

def create_interface():


    main_frame = ctk.CTk()    # Criando frame principal
    main_frame.geometry("600x300")
    main_frame.title("QR code generator")
    main_frame.resizable(False, False)

    l_link = ctk.CTkLabel(master=main_frame, text="Insira a URL de destino:")
    l_link.place(x=45, y=50)

    c_link = ctk.CTkEntry(master=main_frame, width=200, height=30, corner_radius=8)
    c_link.place(x=10, y=80)

    l_path = ctk.CTkLabel(master=main_frame, text="Insira a URL de destino:")
    l_path.place(x=45, y=110)

    c_path = ctk.CTkEntry(master=main_frame, width=200, height=30, corner_radius=8)
    c_path.place(x=10, y=140)

    b_create = ctk.CTkButton(master=main_frame, width=200, height=30, text="Create")
    b_create.place(x=10, y=190)

    qrcode_frame = ctk.CTkFrame(master=main_frame, width=370, height= 280)
    qrcode_frame.place(x=220, y=10)





    main_frame.mainloop()


create_interface()




