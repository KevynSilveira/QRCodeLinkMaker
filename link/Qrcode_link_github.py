import qrcode # pip install qrcode
import customtkinter as ctk # pip install customtkinter
from tkinter import messagebox

link = ""
name_qrcode = "qrcode.png"

def create_interface():

    main_frame = ctk.CTk()    # Criando frame principal
    main_frame.geometry("600x300")
    main_frame.title("QR code generator")
    main_frame.resizable(False, False)

    l_link = ctk.CTkLabel(master=main_frame, text="Insira a URL de destino:")
    l_link.place(x=45, y=90)

    c_link = ctk.CTkEntry(master=main_frame, width=200, height=30, corner_radius=8)
    c_link.place(x=10, y=120)

    def create_qrcode():
        try:
            global name_qrcode, link
            link_path = c_link.get()
            if link_path != "":
                if name_qrcode != "":
                    link = c_link.get()
                    image = qrcode.make(link)  # Controi o qrcode
                    image.save(name_qrcode)  # Salva ele no local selecionado
                    messagebox.showinfo("QR code", "Seu QR code foi gerado")
                else:
                    messagebox.showerror("Atencao", "Selecione um nome!")
            else:
                messagebox.showerror("Atencao", "Atencao, insira um link!")
        except:
            messagebox.showerror("Atencao", "Dados invalidos!")

    b_create = ctk.CTkButton(master=main_frame, width=200, height=30, text="Create", command=create_qrcode)
    b_create.place(x=10, y=160)

    qrcode_frame = ctk.CTkFrame(master=main_frame, width=370, height= 280)
    qrcode_frame.place(x=220, y=10)

    main_frame.mainloop()

create_interface()




