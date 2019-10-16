# simulation_hw2
## Q1
![](https://github.com/ArielWu0203/simulation_hw2/blob/master/Chap%203.12.png?raw=true)
```
python3 uniform.py -n 100
2.79
python3 uniform.py -n 1000
2.745
python3 uniform.py -n 10000
2.7042
```
根據計算出的期望值 n 約等於 2.7，可以發現平均上來說，約做 2~3 次的 uniform random 可以使總和(U1+U2+...) 大於 1。    

## Q2
![](https://github.com/ArielWu0203/simulation_hw2/blob/master/4.4.png?raw=true)
```
python3 shuffle.py -n 100
expectation : 1.060000
variance : 1.076400
python3 shuffle.py -n 1000
expectation : 0.932000
variance : 0.939376
python3 shuffle.py -n 10000
expectation : 0.991100
variance : 0.982221
```
* 預估     
  E[X] = n * (1/n) = 1          
  Var[X] = E[X^2] - 1 = 1 + n(n+1) * (1 / (n(n+1))) -1 = 1
