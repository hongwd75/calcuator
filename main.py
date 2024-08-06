import tkinter as tk
from Values.kindButtonValue import KindButtonTYPE
from Values.CalcButton import CalcButton
from Values.Calculator import Calculator

def main():
    Calc = Calculator()
    def onBtnClick(value:int,type:KindButtonTYPE):
        result = Calc.update(value,type)
        label.config(text=result)
        
    window = tk.Tk()
    window.title("덧뺄셈 계산기")
    window.geometry("300x320")
    
    label = tk.Label(window, text="0",anchor="e",bd=2, relief="solid")
    label.pack()
    label.place(x = CalcButton.startPositionX,y = 0, width= (CalcButton.BoxWidth + 4) * 4)
    
    for btnType in KindButtonTYPE:
        if btnType == KindButtonTYPE.NUMBER:
            for i in range(10):
                button = CalcButton(window, i, KindButtonTYPE.NUMBER, command=onBtnClick)
        else:
            button = CalcButton(window,0,btnType, command=onBtnClick)
        Calc.appendButton(button)
            
    window.mainloop()
    
if __name__ == "__main__":
    main()    