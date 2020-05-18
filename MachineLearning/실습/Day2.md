# Day 2

## x,y(continuous)

	"layer1"							"layer 2"
x -> weight matrix1 -> non - linear activation -> weight matrix2 -> non - linear..->
	bias1								bias2

비선형 적인 non -linear activation 추가를 통해, 비선형적인 결과를 얻을 수 있음.

## hyperparameter: 사용자가 validation dataset을 통해 찾아야 하는 파라미터 값들
1.epoch
2.layer개수
3.각각의 layer의 weight의 크기

## epoch: 전체 데이터를 한 번 다 보는 것

## iteration: batch를 한번 보는 것

## nn.Linear() <-- neural network에서 layer를 나타냅니다. (weight matrix, bias vector)
nn.Linear(row의 개수, column의 개수)

하나의 layer는 weight matrix bias vector
data가 [1]
model = nn.linear(1,1)

model(data)
-> 내부적으로 data * weight matrix + bias

matrix의 shape: row의 개수와 column의 개수

입력 데이터 - > layer1 -> activation function -> layer2->y^
(1,1)           -> (1,1)    -> sigmoid                   -> (1,1)

Activator function
1. sigmoid
2. tann
3. ReLu

learning_rate = 1e-1, 1e-2, 1e-3 이런식으로 찾음.
epochs = 적당히 큰수, early stoping 사용

---------------

x와 y가 있고, y가 discrete

(binomial) logistic regression

log p/(1-p) = x
p= f(x) <-- f가 logistic function

softmax 함수 적용
1. 각각의 element들을 0에서 1사이의 값으로 변환
2. 모든 element들의 총 합이 1이 되도록 변환

softmax의 special case(binary)는 logistic

label y가 binary class를 가지고 있는 경우와, 그 이상(3개 이상)의 class를 가지고 있는 경우
label y를 예측하기 위하여 logistic function, softmax function

y와 predected label y^
loss함수로 cross entropy

data		layer
matrix	weight martrix
		bias vector

fully-connected layer의 경우, 입력되는 데이터 각각은 vector로 표현이 되어야 한다.

28x28
-->flatten시켜서 하나하나의 데이터(이미지)가 1x784로 만들어주어야 한다.

np.array.reshape(-1, 784)

Internal Covariate Shift
각각의 batch마다 distiribution이 달라져서 제대로 학습이 안되는 것(일정한 모양x)
각각의 layer의 출력에 대해서 화이트닝(표준정규분표화) 시켜줘서 해결

dropout: 특정 확률로 일부로 어떤 노드들을 꺼버리는 것(노드의 값을 0으로 조절했다)

voting effect

co-adaptation 효과:
하나의 layer에 3개의 노드 존재
1 5 1000000 -> 1000006
이렇게 되면 앞에 노드들의 영향력이 너무 작아짐
드롭아웃 사용 시 1 5 0
앞에 노드들이 반영됨
