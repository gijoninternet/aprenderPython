from tkinter import * 

raiz = Tk()

raiz.title("titulo")
# raiz.config(bg="blue")

# miFrame = Frame()
# miFrame.pack(fill="both",expand="True")
# miFrame.config(bg="red")
# miFrame.config(width="650",height="350")

miFrame=Frame(raiz)
miFrame.config(width="650",height="350")
miFrame.pack(fill="both",expand="True")


miLabel= Label(miFrame,text="Label de ejemplo")
miLabel.place(x=100,y=200)

raiz.mainloop()
