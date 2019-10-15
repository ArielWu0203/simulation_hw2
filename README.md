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
根據計算出的期望值 n 約等於 2.7，可以發現平均上來說，約做 2~3 次的 uniform random 就可以使總和(U1+U2+...) 大於 1。
## Q2
![](https://github.com/ArielWu0203/simulation_hw2/blob/master/4.4.png?raw=true)
```
python3 shuffle.py -n 100
expectation : 50.866667
variance : 915.615556
python3 shuffle.py -n 1000
expectation : 40.035494
variance : 800.117567
python3 shuffle.py -n 10000
expectation : 42.597697
variance : 799.951680
python3 shuffle.py -n 100000
expectation : 42.205831
variance : 790.682020
python3 shuffle.py -n 500000
expectation : 42.169712
variance : 794.302782
```
