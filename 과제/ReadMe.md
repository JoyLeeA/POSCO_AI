## Machine Learning
### 과제1
Pytorch 튜토리얼" ppt의 가장 끝에 있는 문제풀이

### 과제2
MNIST 와 CIFAR10 학습 모델 생성
1. MNIST: test_accuracy 99% 이상
2. CIFAR10: test_accuacy 90% 이상

[주의사항]
1) 제출 코드 안에 print(test_accuracy)을 하는 코드를 작성하여, test_accuracy를 출력(train accuracy를 제출하실 경우 0점 처리)
2) 모델의 layer 개수, hidden node 개수 제한없음
3) activation function 제한 없음. 단, softmax함수의 경우 맨 끝단에만 사용.
4) dropout, batch normalization은 선택 사항임. 모델의 test_accuracy를 높이지 못한다면 굳이 사용할 필요 없음.

## Artificial Intelligence
### 과제3
[AI Search Algorithm] Joint Task를 구현

Joint Task란 띄어쓰기가 없고 모음이 없는 문자열에 띄어쓰기와 모음을 삽입해 자연스러운 문장을 생성하는 작업임
ex> "mgnllthppl" => "imagine all the people"

[주의사항]
1) joint_task.py의 JointSegmentationInsertionProblem 클래스의 succ_and_cost 멤버 함수 구현
2) raise NotImplementedError('not implemented') 지우고 구현
3) succ_and_cost와 __main__ 이외의 코드 수정 금지
4) python joint_task.py로 간단한 테스트를 수행 가능

### 과제4
[MDP & RL] Peeking Blackjack

Peeking Blackjack이란 다음 카드를 엿볼 수 있는 Blackjack임

[주의사항]
1) blackjack.py의 BlackjackMDP 클래스의 succAndProbReward 멤버 함수 구현
2) _FILL_IN_을 지우고 구현
3) _FILL_IN와 __main__ 이외의 코드 수정 금지
4) python balckjack.py로 간단한 테스트를 수행 가능

## Computer Vision
### 과제5 
Traditional Image Classification

1) extract_features 함수에 들어갈 적절한 코드를 작성 [50점]
2) HOG + SVM Classification 모델의 Test score 측정 [50점]
(Test score 1%당 1점, Test score 50% 이상 50점, 백분율 기준 소수 첫째자리에서 반올림)

### 과제6 
Transfer Learning

Cat과 Dog 분류모델을 학습시키고 학습 결과에서 Val_acc 최대로 만들기  
(맨 마지막으로 트렌하는 부분의 마지막 벨리데이션 값 제출(0.9526)으로 되어있는 부분)
1. Val_acc * 100 = 과제 점수
2. learning rate 바꿔보기
3. 더 많은 layer들을 학습시켜보기

[주의사항]
1) training acc가 1이면 안됨.
2) epoch는 10개 이하로 고정
3) 마지막 train-acc 가 ‘1’이면 안됨 (train-acc ‘1’일 시 과적합으로 과제 점수에서 ‘-5점’) 4) 아무런 코드 수정 없이 그대로 제출하면 안됨 (과제 점수에서 ‘-10점’) 5) 미제출 시 (0점)

### 과제7
Traditional Object Detection 과제

1. to do에 들어갈 적절한 코드를 작성 [90점] (단계별 코드 모두 완성시)
2. 결과 개선을 위한 추가적인 전처리 및 알고리즘에 따른 추가점수 [10점]

[참고 사항]
1) find contour - 등고선을 그려주는 함수
2) 템플릿을 여러개 쓰면, 개선된 결과가 나올 것임. 
3) 나만의 데이터 전처리 기법, 알고리즘 적용으로 더 좋은결과 산출.
4) opencv 라이브러리에서 실행 gpu없이 실행해도 된다.

## Natural Language Processing

