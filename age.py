drive = input('請問你有沒有開過車：')
if drive !='有' and drive !='沒有':
	print('只能輸入有或沒有')
	raise SystemExit
	
age = input('請問你年齡幾歲：')
age = int(age)

if drive =='沒有':
     if age <= 18:
        print('過幾年就可以考了！')
     else:
        print('你怎麼還不去考？')
elif drive == '有':
     if age < 18:
        print('奇怪你怎麼有開過車？')
     else:
        print('很好你考過了！')
