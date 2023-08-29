import os

import qrcode # pip install qrcode
import customtkinter as ctk # pip install customtkinter
from tkinter import messagebox
from PIL import Image, ImageTk

link = ""
name_qrcode = "qrcode.png"

def create_interface(): # Cria a interface

    main_frame = ctk.CTk()    # Criando frame principal
    main_frame.geometry("510x300")
    main_frame.title("QR code generator")
    main_frame.resizable(False, False)

    l_link = ctk.CTkLabel(master=main_frame, text="Insira a URL de destino:")
    l_link.place(x=45, y=90)

    c_link = ctk.CTkEntry(master=main_frame, width=200, height=30, corner_radius=8)
    c_link.place(x=10, y=120)

    def create_qrcode(): # Cria o qrcode
        global name_qrcode, link
        if os.path.exists(name_qrcode):  # Se tiver um arquivo existente com o mesmo nome, ele apaga e cria um novo, para a axibicao no frame
            try:
                os.remove(name_qrcode)
                print(f"Arquivo {name_qrcode} foi removido!")
            except OSError as e:
                print(f"Ocorreu um erro ao apagar o arquivo: {e}")
        try:
            link_path = c_link.get()
            if link_path != "": # Verifica se o link esta vazio
                if name_qrcode != "": # Verifica se o name do arquivo esta vazio
                    link = c_link.get() # Pega o link do c_link
                    image = qrcode.make(link)  # Controi o qrcode
                    image.save(name_qrcode)  # Salva ele no local selecionado
                    messagebox.showinfo("QR code", "Seu QR code foi gerado")

                    for widget in qrcode_frame.winfo_children(): # Remove o QR code anterior do frame qrcode_frame
                        widget.destroy()

                    # Carrega a imagem gerada e exibe-a no frame qrcode_frame
                    qr_image = Image.open(name_qrcode)
                    qr_image = qr_image.resize((550, 550), Image.LANCZOS)  # Usando LANCZOS para redimensionar
                    qr_photo = ImageTk.PhotoImage(qr_image)

                    qr_label = ctk.CTkLabel(master=qrcode_frame, image=qr_photo, width=280, height=280)
                    qr_label.image = qr_photo
                    qr_label.pack(fill="both", expand=True)
                else:
                    messagebox.showerror("Atencao", "Selecione um nome!")
            else:
                messagebox.showerror("Atencao", "Atenção, insira um link!")
        except Exception as e:
            messagebox.showerror("Atencao", f"Erro ao gerar QR code: {str(e)}")
            print(e)

    b_create = ctk.CTkButton(master=main_frame, width=200, height=30, text="Create QR code", command=create_qrcode)
    b_create.place(x=10, y=160)

    qrcode_frame = ctk.CTkFrame(master=main_frame, width=280, height= 280)
    qrcode_frame.place(x=220, y=10)

    main_frame.mainloop()

create_interface()




