from tkinter import *
import math
root = Tk()
class add_number:
    def n0():
        x = sun.get()
        if len(x) != 0: sun.insert(END,"0")
    def n1(): sun.insert(END,"1")
    def n2(): sun.insert(END,"2")
    def n3(): sun.insert(END,"3")
    def n4(): sun.insert(END,"4")
    def n5(): sun.insert(END,"5")
    def n6(): sun.insert(END,"6")
    def n7(): sun.insert(END,"7")
    def n8(): sun.insert(END,"8")
    def n9(): sun.insert(END,"9")
class erfun:
    def CE(vb):
        x = vb.get()
        for i in range(len(x)):
            vb.delete(0)
        
    def jam(vb):
        x = vb.get()
        if "+" in x or "-" in x or "*" in x or "/" in x or "**" in x: pass
        elif len(x) == 0: pass
        else: vb.insert(END,"+")
    
    def men(vb):
        x = vb.get()
        if "+" in x or "-" in x or "*" in x or "/" in x or "**" in x: pass
        elif len(x) == 0: pass
        else: vb.insert(END,"-")

    def zar(vb):
        x = vb.get()
        if "+" in x or "-" in x or "*" in x or "/" in x or "**" in x: pass
        elif len(x) == 0: pass
        else: vb.insert(END,"*")
    
    def tag(vb):
        x = vb.get()
        if "+" in x or "-" in x or "*" in x or "/" in x or "**" in x: pass
        elif len(x) == 0: pass
        else: vb.insert(END,"/")

    def power(vb):
        x = vb.get()
        if "+" in x or "-" in x or "*" in x or "/" in x or "**" in x: pass
        elif len(x) == 0: pass
        else: vb.insert(END,"**")
    
    def Sqrt(vb):
        x = vb.get()
        try:
            if "+" in x or "-" in x or "*" in x or "/" in x: pass
            else:
                if len(x) != 0:
                    for i in range(len(x)):
                        vb.delete(0)
                    a = math.sqrt(float(x))
                    a = str(a)
                    for i in a:
                        vb.insert(END,i)
        except ValueError:
            for i in x: vb.delete(0)

    def numbersum(vb):
        x = vb.get()
        if len(x) != 0:
            ui = 0
            for i in x: ui += 1
            
            if x[ui-1] == "+" or x[ui-1] == "-" or x[ui-1] == "*" or x[ui-1] == "/": pass
            elif "+" in x or "-" in x or "*" in x or "/" in x or "**" in x:
                sub = vb.get()
                
                if "+" in sub:
                    try:
                        number1 = ''
                        number2 = ''
                        for i in sub:
                            if i != "+": number1 += i
                            else: break
                        # number1 ok
                        fg = list(sub)
                        for i in range(len(number1)+1): fg.pop(0)
                        for i in fg: number2 += i
                        # number2 ok
                        for i in sub: vb.delete(0)
                        hasel = float(number1) + float(number2)
                        for i in str(hasel): vb.insert(END,i)

                    except ValueError:
                        for i in sub: vb.delete(0)
                
                elif "-" in sub:
                    try:
                        number1 = ''
                        number2 = ''
                        for i in sub:
                            if i != "-": number1 += i
                            else: break
                        # number1 ok
                        fg = list(sub)
                        for i in range(len(number1)+1): fg.pop(0)
                        for i in fg: number2 += i
                        # number2 ok
                        for i in sub: vb.delete(0)
                        hasel = float(number1) - float(number2)
                        for i in str(hasel): vb.insert(END,i)
                    except ValueError: 
                        for i in sub: vb.delete(0)

                elif "**" in sub:
                    try:
                        number1 = ''
                        number2 = ''
                        for i in sub:
                            if i != "*": number1 += i
                            else: break
                        # number1 ok
                        fg = list(sub)
                        for i in range(len(number1)+2): fg.pop(0)
                        for i in fg: number2 += i
                        # number2 ok
                        for i in sub: vb.delete(0)
                        hasel = float(number1) ** float(number2)
                        for i in str(hasel): vb.insert(END,i)
                    except ValueError:
                        for i in sub: vb.delete(0)

                elif "*" in sub:
                    try:
                        number1 = ''
                        number2 = ''
                        for i in sub:
                            if i != "*": number1 += i
                            else: break
                        # number1 ok
                        fg = list(sub)
                        for i in range(len(number1)+1): fg.pop(0)
                        for i in fg: number2 += i
                        # number2 ok
                        for i in sub: vb.delete(0)
                        hasel = float(number1) * float(number2)
                        for i in str(hasel): vb.insert(END,i)
                    except ValueError:
                        for i in sub: vb.delete(0)

                elif "/" in sub:
                    try:
                        number1 = ''
                        number2 = ''
                        for i in sub:
                            if i != "/": number1 += i
                            else: break
                        # number1 ok
                        fg = list(sub)
                        for i in range(len(number1)+1): fg.pop(0)
                        for i in fg: number2 += i
                        # number2 ok
                        for i in sub: vb.delete(0)
                        hasel = float(number1) / float(number2)
                        for i in str(hasel): vb.insert(END,i)
                    except ValueError:
                        for i in sub: vb.delete(0)
                    except ZeroDivisionError:
                        for i in sub: vb.delete(0)
                        vb.insert(0,"Error")

def KCE(): erfun.CE(sun)
def kojam(): erfun.jam(sun)
def kmen(): erfun.men(sun)
def kzar(): erfun.zar(sun)
def kteg(): erfun.tag(sun)
def kpow(): erfun.power(sun)
def ksqrt(): erfun.Sqrt(sun)
def sumer(): erfun.numbersum(sun)
root.title("calculaator")
root.geometry("280x350")
root.config(bg = "black")
root.resizable(False , False)
# math:
Button(root,text = "=",command = sumer).place(x = 219 , y = 291 , width = 60 , height = 60)
Button(root,text = "+",command = kojam).place(x = 219 , y = 224 , width = 60 , height = 60)
Button(root,text = "-",command = kmen).place(x = 219 , y = 157 , width = 60 , height = 60)
Button(root,text = "*",command = kzar).place(x = 219 , y = 90 , width = 60 , height = 60)
Button(root,text = "/",command = kteg).place(x = 219 , y = 23 , width = 60 , height = 60)
Button(root,text = "pow",command = kpow).place(x = 142 , y = 23 , width = 60 , height = 60)
Button(root,text = "sqrt",command = ksqrt).place(x = 75 , y = 23 , width = 60 , height = 60)
Button(root,text = "CE",command = KCE).place(x = 8 , y = 23 , width = 60 , height = 60)
# end math.
sun = Entry(root, font = ("Times 14",19),bg = "#9BA4B5");sun.pack()
# number:
Button(root,text = "0",command = add_number.n0).place(x = 8 , y = 291 , width = 60 , height = 60)
Button(root,text = "1",command = add_number.n1).place(x = 8 , y = 224 , width = 60 , height = 60)
Button(root,text = "2",command = add_number.n2).place(x = 75 , y = 224 , width = 60 , height = 60)
Button(root,text = "3",command = add_number.n3).place(x = 142 , y = 224 , width = 60 , height = 60)
Button(root,text = "4",command = add_number.n4).place(x = 8 , y = 157 , width = 60 , height = 60)
Button(root,text = "5",command = add_number.n5).place(x = 75 , y = 157 , width = 60 , height = 60)
Button(root,text = "6",command = add_number.n6).place(x = 142 , y = 157 , width = 60 , height = 60)
Button(root,text = "7",command = add_number.n7).place(x = 8 , y = 90 , width = 60 , height = 60)
Button(root,text = "8",command = add_number.n8).place(x = 75 , y = 90 , width = 60 , height = 60)
Button(root,text = "9",command = add_number.n9).place(x = 142 , y = 90 , width = 60 , height = 60)
# end nuber.
root.mainloop()