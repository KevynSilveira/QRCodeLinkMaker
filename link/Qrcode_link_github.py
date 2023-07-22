import qrcode # pip install qrcode
import customtkinter as ctk # pip install customtkinter
from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk

link = ""
generated_qrcode_path = ""

def create_interface():

    main_frame = ctk.CTk()    # Criando frame principal
    main_frame.geometry("600x300")
    main_frame.title("QR code generator")
    main_frame.resizable(False, False)

    l_link = ctk.CTkLabel(master=main_frame, text="Insira a URL de destino:")
    l_link.place(x=45, y=50)

    c_link = ctk.CTkEntry(master=main_frame, width=200, height=30, corner_radius=8)
    c_link.place(x=10, y=80)

    def select_path():  # Seleciona a pasta para salvar o arquivo
        pasta_selecionada = filedialog.askdirectory(title="Selecione uma pasta")  # Seleciona a pasta para salvar
        if pasta_selecionada:
            global generated_qrcode_path
            generated_qrcode_path = pasta_selecionada
            c_path.insert(tk.END, pasta_selecionada)
            return pasta_selecionada
        else:
            return None
            messagebox.showerror("Caminho destino", "Selecione um arquivo!")

    def create_qrcode():
        try:
            global generated_qrcode_path, link
            link = c_link.get()
            select_path()
            if c_link.get() != "" and generated_qrcode_path != "":
                image = qrcode.make(link)  # Controi o qrcode
                image.save(generated_qrcode_path)  # Salva ele no local selecionado
                messagebox.showinfo("QR code", "Seu QR code foi gerado")
            else:
                messagebox.showerror("Atencao", "Atencao, preencha todos os campos!")
        except:
            messagebox.showerror("Atencao", "Dados invalidos!")

    l_path = ctk.CTkLabel(master=main_frame, text="Insira a URL de destino:")
    l_path.place(x=45, y=110)

    c_path = ctk.CTkEntry(master=main_frame, width=200, height=30, corner_radius=8)
    c_path.place(x=10, y=140)

    b_create = ctk.CTkButton(master=main_frame, width=200, height=30, text="Create", command=create_qrcode)
    b_create.place(x=10, y=180)

    qrcode_frame = ctk.CTkFrame(master=main_frame, width=370, height= 280)
    qrcode_frame.place(x=220, y=10)



    main_frame.mainloop()


create_interface()




