# Day 3

## 실습코드(MNIST) [20200515] 의 in [3] 부분
input image --> 1번째 convolution layer   --> 2번째 convolution layer
1x28x28	    --> 16x 28-5+1 x 28-25 +1	 -->   32 x 24-5+1 x 24-1+5

--> pooling			--> 3번째 convolution layer --> pooling
32 x  ((24-5+1)/2=)10 x 10   -->  64 x 6 x 6			   ---> 64 x 3 x 3

---------------
Convolution layer와 pooling layer를 통해서 fearture 추출 완료

flatten 시켜주기
64 x 3 x 3 --> vector 64 x 4 x 4

Classifier: Fully-connected layer
64 x 3 x 3 x 100
100 x 10(mnist는 10개의 숫자를 나타낸다)

-----------------
Mnist:  1 x 28 x 28

CIFAR10: 3 x 32 x 32 
color image <-- R, G B

## 실습코드(MNIST) [20200515] 의 in [3] 부분
input image --> 1번째 convolution layer   --> 2번째 convolution layer
3x32x32	    --> 16x 32-5+1 x 32-25 +1	 -->   32 x 28-5+1 x 28-1+5

--> pooling			--> 3번째 convolution layer --> pooling
32 x  ((28-5+1)/2=)12 x 12   -->  64 x 8 x 8	           ---> 64 x 4 x 4

--------------------
하나의 데이터가 하나의 벡터로

faltten
1, 64 x 4 x 4

fully-connted layer
64 x 4 x 4

