from tkinter import *
import qrcode

root = Tk()
root.title("Qr generator")
root.geometry("1000x550")
root.config(bg="#AE2321")
root.resizable = (False, False)

# icon image

image_icon = PhotoImage(file="QR/icon.png")
root.iconphoto(False, image_icon)


def generate():
    name = title.get()
    text = entry.get()
    qr = qrcode.make(text)
    qr.save("QR/" + str(name) + ".png")

    global Image
    Image= PhotoImage(file="QR/" + str(name) + ".png")
    Image_view.config(image=Image)


Image_view = Label(root, bg="#AE2321")
Image_view.pack(padx=50, pady=10, side=RIGHT)

Label(root, text="Title", fg="white", bg="#AE2321", font=15).place(x=50, y=150)
title = Entry(root, width=13, font="arial 15")
title.place(x=50, y=180)

Label(root, text="URL", fg="white", bg="#AE2321", font=15).place(x=50, y=230)
entry = Entry(root, width=28, font="arial 15")
entry.place(x=50, y=260)

Button(root, text="Generate", width=20, height=2, bg="black", fg="white", command=generate).place(x=50, y=310)

root.mainloop()
