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

###과제4
[MDP & RL] Peeking Blackjack

Peeking Blackjack이란 다음 카드를 엿볼 수 있는 Blackjack임

[주의사항]
1) blackjack.py의 BlackjackMDP 클래스의 succAndProbReward 멤버 함수 구현
2) _FILL_IN_을 지우고 구현
3) _FILL_IN와 __main__ 이외의 코드 수정 금지
4) python balckjack.py로 간단한 테스트를 수행 가능

## Computer Vision
