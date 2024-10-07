
import torch
import torch.nn as nn
import torch.nn.functional as F

import matplotlib.pyplot as plt


# ---------------------------------------------------
# Iris 회귀 모델 클래스
# ---------------------------------------------------




# ---------------------------------------------------
# Iris 2진 분류 모델 클래스
# ---------------------------------------------------



# ---------------------------------------------------
# Iris 다중 분류 모델 클래스
# ---------------------------------------------------

class IrisMCFModel(nn.Module):
    
    # 모델 구조 구성 및 인스턴스 생성 메서드
    def __init__(self):
        super().__init__()
        self.in_layer=nn.Linear(4, 10)
        self.hd_layer=nn.Linear(10, 5)
        self.out_layer=nn.Linear(5, 3)   # 다중분류 'Setosa', 'Versicolor', 'Virginica'
        
    # 순방향 학습 진행 메서드
    def forward(self, input_data):
        #- 입력층
        y=self.in_layer(input_data)   
        y=F.relu(y)                   
        
        # - 은닉층 : 10개의 숫자 값(>=0)
        y=self.hd_layer(y)            
        y=F.relu(y)                  
        
        #- 출력층 : 5개의 숫자 값 => 다중 분류 
        #- 손실함수 CrossEntropyLoss가 내부에서 softmax 진행 
        return self.out_layer(y)   
    

# ---------------------------------------------------
# 모델의 LOSS, SCORE plot
# SCORE, LOSS 2개
# ---------------------------------------------------
def showLossScore(SCORE_HISTORY, LOSS_HISTORY, 
                  title1='LOSS', title2='SCORE'):


    TH = len(SCORE_HISTORY[1])

    fg, axes=plt.subplots(1,2, figsize=(10,5), sharex=True)
    axes[0].plot(range(1, TH+1), LOSS_HISTORY[0][:TH], label='Train')
    axes[0].plot(range(1, TH+1), LOSS_HISTORY[1][:TH], label='Val')
    axes[0].grid()
    axes[0].legend()
    axes[0].set_xlabel("TH")
    axes[0].set_ylabel("Loss")
    axes[0].set_title(title1)

    axes[1].plot(range(1, TH+1), SCORE_HISTORY[0][:TH], label='Train')
    axes[1].plot(range(1, TH+1), SCORE_HISTORY[1][:TH], label='Val')
    axes[1].grid()
    axes[1].legend()
    axes[1].set_xlabel("TH")
    axes[1].set_ylabel(title2)
    axes[1].set_title(title2)
    plt.tight_layout()
    plt.show() 