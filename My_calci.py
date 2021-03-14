#Importing required library

from tkinter import*

#Arranging the screen

window=Tk()
window.geometry("354x460")
window.title("MY CALCI")
windowlabel = Label(window,text="MY CALCI",bg='White',font=("Times",30,'bold'))
windowlabel.pack(side=TOP)
window.config(background='Dark gray')

input_text=StringVar()
operator=""

def button_click(number):
     global operator
     operator=operator+str(number)
     input_text.set(operator)

def button_equal():
     global operator
     add=str(eval(operator))
     input_text.set(add)
     operator=''
def button_equal():
     global operator
     sub=str(eval(operator))
     input_text.set(sub)
     operator=''     
def button_equal():
     global operator
     mul=str(eval(operator))
     input_text.set(mul)
     operator=''
def button_equal():
     global operator
     div=str(eval(operator))
     input_text.set(div)
     operator=''    

def button_clear():
     input_text.set('')

     
windowtext=Entry(window,font=("Courier New",12,'bold'),textvar=input_text,width=25,bd=5,bg='antique white')
windowtext.pack()

#Creating buttons

button1=Button(window,padx=14,pady=14,bd=4,bg='white',cursor = "heart",command=lambda:button_click(1),text="1",font=("Courier New",16,'bold'))
button1.place(x=10,y=100)

button2=Button(window,padx=14,pady=14,bd=4,bg='white',cursor = "heart",command=lambda:button_click(2),text="2",font=("Courier New",16,'bold'))
button2.place(x=10,y=170)

button3=Button(window,padx=14,pady=14,bd=4,bg='white',cursor = "heart",command=lambda:button_click(3),text="3",font=("Courier New",16,'bold'))
button3.place(x=10,y=240)

button4=Button(window,padx=14,pady=14,bd=4,bg='white',cursor = "heart",command=lambda:button_click(4),text="4",font=("Courier New",16,'bold'))
button4.place(x=75,y=100)

button5=Button(window,padx=14,pady=14,bd=4,bg='white',cursor = "heart",command=lambda:button_click(5),text="5",font=("Courier New",16,'bold'))
button5.place(x=75,y=170)

button6=Button(window,padx=14,pady=14,bd=4,bg='white',cursor = "heart",command=lambda:button_click(6),text="6",font=("Courier New",16,'bold'))
button6.place(x=75,y=240)

button7=Button(window,padx=14,pady=14,bd=4,bg='white',cursor = "heart",command=lambda:button_click(7),text="7",font=("Courier New",16,'bold'))
button7.place(x=140,y=100)

button8=Button(window,padx=14,pady=14,bd=4,bg='white',cursor = "heart",command=lambda:button_click(8),text="8",font=("Courier New",16,'bold'))
button8.place(x=140,y=170)

button9=Button(window,padx=14,pady=14,bd=4,bg='white',cursor = "heart",command=lambda:button_click(9),text="9",font=("Courier New",16,'bold'))
button9.place(x=140,y=240)

button0=Button(window,padx=14,pady=14,bd=4,bg='white',cursor = "heart",command=lambda:button_click(0),text="0",font=("Courier New",16,'bold'))
button0.place(x=10,y=310)

button_dot=Button(window,padx=47,pady=14,bd=4,bg='white',cursor = "heart",command=lambda:button_click("."),text=".",font=("Courier New",16,'bold'))
button_dot.place(x=75,y=310)

button_add=Button(window,padx=14,pady=14,bd=4,bg='white',text="+",cursor = "heart",command=lambda:button_click("+"),font=("Courier New",16,'bold'))
button_add.place(x=205,y=100)

button_sub=Button(window,padx=14,pady=14,bd=4,bg='white',text="-",cursor = "heart",command=lambda:button_click("-"),font=("Courier New",16,'bold'))
button_sub.place(x=205,y=170)

button_mul=Button(window,padx=14,pady=14,bd=4,bg='white',text="*",cursor = "heart",command=lambda:button_click("*"),font=("Courier New",16,'bold'))
button_mul.place(x=205,y=240)

button_div=Button(window,padx=14,pady=14,bd=4,bg='white',text="/",cursor = "heart",command=lambda:button_click("/"),font=("Courier New",16,'bold'))
button_div.place(x=205,y=310)

button_clear=Button(window,padx=14,pady=119,bd=4,bg='white',text="CL",cursor = "heart",command=button_clear,font=("Courier New",16,'bold'))
button_clear.place(x=270,y=100)

button_equal=Button(window,padx=151,pady=14,bd=4,bg='white',cursor = "hand2",command=button_equal,text="=",font=("Courier New",16,'bold'))
button_equal.place(x=10,y=380)

window.mainloop()
