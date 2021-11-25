# Python_Porker

## USAGE
### Start Porker
```
python porker.py
```

### Change One Card
```
$ python porker.py
交換する手札を番号で入力してください
複数ある場合は","区切りで入力してください
0: [♠9]
1: [♠Q]
2: [♦7]
3: [♥6]
4: [♣J]
p: 手札交換をスキップします
0
[♠Q][♦7][♥6][♣J][♣3]
PE☆KE
```

### Change Some Cards
```
$ python porker.py
交換する手札を番号で入力してください
複数ある場合は","区切りで入力してください
0: [♦Q]
1: [♥K]
2: [♦3]
3: [♣J]
4: [♠J]
p: 手札交換をスキップします
0,1,2
[♣J][♠J][♦7][♣5][♠7]
My hand is TwoPair
```

### Skip
```
$ python porker.py
交換する手札を番号で入力してください
複数ある場合は","区切りで入力してください
0: [♦10]
1: [♠4]
2: [♦2]
3: [♣Q]
4: [♦8]
p: 手札交換をスキップします
p
exchange is pass
[♦10][♠4][♦2][♣Q][♦8]
PE☆KE
```
### 17 Porker

`python porker.py`実行時に `17` を渡すとライアーゲームで登場した17ポーカー(っぽい)動きをします。
J, Q, K, A と Joker しか存在しないポーカーです。

```
$ python porker.py 17
交換する手札を番号で入力してください
複数ある場合は","区切りで入力してください
0: [♠Q]
1: [♣K]
2: [♦K]
3: [♥K]
4: [♠A]
p: (pass)手札交換をスキップします
0,4
[♣K][♦K][♥K][♦Q][♠J]
My hand is ThreeCard
```

## TEST
```
python -m unittest discover -s ./tests -p "*_test.py"
```
