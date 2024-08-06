import tkinter as tk
from Values.kindButtonValue import KindButtonTYPE

class CalcButton(tk.Button):
    startPositionX  = 16
    startPositionY  = 32
    BoxWidth        = 64
    BoxHeight       = 64

    #====================================================================================================
    # 초기화
    def __init__(self, master,value,type,command):
        self.value = value
        self.type = type
        self.callback = command
        tk.Button.__init__(self,master,command=self.onClick, text=self.GetTypeString())
        
        self.pack()
        
        if self.type == KindButtonTYPE.NUMBER:
            self.SetPoitionByNUMValue(self.value)
        else:
            self.SetPositionByCalcType()
        
    #====================================================================================================
    #callback 처리
    def onClick(self):
        self.callback(self.value,self.type)

    # 화면에 표시되는 문자열 출력
    def GetTypeString(self):
        if self.type == KindButtonTYPE.NUMBER:
            return self.value
        elif self.type == KindButtonTYPE.PLUS:
            return "+"
        elif self.type == KindButtonTYPE.MINUS:
            return "-"
        else: 
            return "="
        
    # 숫자들 화면 위치 설정    
    def SetPoitionByNUMValue(self,numvalue):
        witdh = self.BoxWidth
        height = self.BoxHeight
        
        if numvalue != 0 :
            py,px = divmod(numvalue-1,3)
            py = (height+4)*py
            px = (witdh+4)*px
        else:
            py,px = (height+4)*3,0
            witdh = (witdh+4)*3 - 4 
            
        self.place(x=px+self.startPositionX,y=py+self.startPositionY,width=witdh,height=height)
        
    def SetPositionByCalcType(self):
        witdh = self.BoxWidth
        height = self.BoxHeight
        
        if self.type == KindButtonTYPE.MINUS:
            px = (witdh+4) * 3
            py = 0
        elif self.type == KindButtonTYPE.PLUS:
            px = (witdh+4) * 3
            py = (height+4)
        elif self.type == KindButtonTYPE.SUM:
            px = (witdh+4) * 3
            py = (height+4) * 2
            height = height * 2 + 4
        self.place(x=px+self.startPositionX,y=py+self.startPositionY,width=witdh,height=height)
        