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

## TEST
```
python -m unittest discover -s ./tests -p "*_test.py"
```
