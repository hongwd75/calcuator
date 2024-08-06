from Values.kindButtonValue import KindButtonTYPE
from Values.CalcButton import CalcButton
from typing import Optional


import numpy as np
class Calculator:
    #===============================================================================
    # 초기화
    def __init__(self):
        self.reset()
        self.buttons = np.array([], dtype=CalcButton)

    #===============================================================================    
    # 버튼 관리
    def appendButton(self, button):
        self.buttons = np.append(self.buttons, button)
        
    def __getitem__(self,btnType:KindButtonTYPE,value:int = 0) -> Optional[CalcButton]:
        if btnType == KindButtonTYPE.NUMBER:
            return next((button for button in self.buttons if button.type == btnType and button.value == value),None)
        else:
            return next((button for button in self.buttons if button.type == btnType),None)

    #===============================================================================
    # 리셋
    def reset(self):
        self.prev_number = 0
        self.current_number = 0
        self.operation = KindButtonTYPE.NUMBER
        
    #===============================================================================    
    def update(self,value :int,sendType : KindButtonTYPE) -> str:
        if sendType == KindButtonTYPE.NUMBER:
            if self.operation == KindButtonTYPE.SUM:
                self.reset()
            else:
                self.current_number = self.current_number * 10 + value
        elif sendType in (KindButtonTYPE.MINUS, KindButtonTYPE.PLUS):
            self.operation = sendType
            if self.current_number != 0 :
                self.calculate(sendType)
        else:
            if self.operation == KindButtonTYPE.SUM:
                self.reset()
            elif self.operation in (KindButtonTYPE.MINUS, KindButtonTYPE.PLUS):
                self.calculate(self.operation)
                self.operation = KindButtonTYPE.SUM
                
        # SUM 버튼 갱신
        sumbtn = self.__getitem__(KindButtonTYPE.SUM)
        if sumbtn != None:
            if self.operation == KindButtonTYPE.SUM:
                sumbtn.config(text='CLEAR');
            else:
                sumbtn.config(text='=');
        # 출력
        if self.operation == KindButtonTYPE.NUMBER:
            return str(self.current_number)
        elif self.operation == KindButtonTYPE.SUM:
            return str(self.prev_number)
        return f"{self.prev_number} {'+' if self.operation == KindButtonTYPE.PLUS else '-'} {self.current_number}"
        
    #===============================================================================    
    # 계산
    def calculate(self,sendType : KindButtonTYPE):
        if sendType == KindButtonTYPE.PLUS:
            self.prev_number+=self.current_number
        elif sendType == KindButtonTYPE.MINUS:
            self.prev_number-=self.current_number
        self.current_number = 0
        
            
            