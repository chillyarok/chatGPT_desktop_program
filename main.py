'''import'''
import data
import openai
from tkinter import *
import os
'''data'''
openai.api_key = data.openai_token
'''func'''
def chatGPT(prompt):
    completion = openai.Completion.create(engine=data.engine,prompt=prompt,temperature=0.5,max_tokens=1000)
    return completion.choices[0]['text']
def obrabotka_zaprosa():
    op = open("zapros.txt","r")
    data.text = op.read()
    op.close()
    otvet = chatGPT(data.text)
    print(otvet)
    def vidacha_otveta():
        o = open("otvet.txt","w")
        o.write(otvet)
        o.close()
        signal["background"]="green"
        os.startfile("otvet.txt")
    vidacha_otveta()
def delall():
    otv = open("otvet.txt","w")
    otv.truncate()
    otv.close()
    op = open("zapros.txt","w")
    op.truncate()
    op.close()
    signal["background"] = "gray"
'''main'''
os.startfile("zapros.txt")
window = Tk()
b1 = Button(text="Сделать запрос",width=20,font=14,command=obrabotka_zaprosa)
b1.pack()
b2 = Button(text="Очистить",width=20,font=14,command=delall)
b2.pack()
signal = Label(width=20,font=14,bg = "gray")
signal.pack()
window.mainloop()


