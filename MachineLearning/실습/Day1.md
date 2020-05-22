# Day 1 

2020 5월 13일 

## [Regression]

y = f(x) + c
y를 잘 설명하는 f(x)를 찾는다 -> 리그레션을 푼다

성별 시력 몸무게 ->       키
1	1.5	100		200.5

## [Linear]
y= wx + b
x입력 -> y'(예측값)

y를 잘 설명하는 w와 b를 찾는게 목적
직선의 방정식으로 나타남

resudual: y - y'
linear regression = least square method = least squre regression: (y-y')^2을 모두 더한 것의 최소화 하는 w를찾는 것

1.해석적으로 문제를 푼다.

(y-y')^2, where y' = wx + b
Loss식을 0으로 만드는 점을 직접 찾을 수 있다.
w = closed form formula

2.수치적으로 문제를 푼다
grdient descent를 이용해서 모델의 파라미터를 점차적으로 수정해나가는 방식

## [Gradient Descent]
전체 데이터를 다 보고 한번 업데이트
40개를 다 봐야 1번 업데이트
100번 업데이트 -> 40 * 100

## [Stochastic Gradient Descent]
데이터 하나 보고 한번 업데이트
1개를 보고 1번 업데이트
40개 -> 40번 업데이트
미니 배치에서 사이즈를 1로 설정한 것과 동일
------
x와 y의 관계를 학습해서 x를 넣었을 때 y를 적절하게 찾아주는 것
epoch: 모델이 전체 데이터를 한번 본 것
iteration: 1번의 미니배치를 본 것

## [Rugularization]
deep neural network를 학습할 때 발생할 수 있는 ovrtfitting이라는 문제를 해결할수 있는 방안

## [Overfitting 해결]
모델을 학습 할 때, 로스에 모델의 파라미터에 대해서 regularization term을 추가
