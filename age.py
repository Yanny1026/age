driving = input('請問你有無渣過車?')
if driving != '有' and driving != '無':
	print('只能輸入 有/無')
	raise SystemExit

age = input('請問你的年齡?')
age = int(age)
if driving == '有':
	if age >= 18:
		print('你通過啦')
	else:
		print('奇怪 你點解有渣過車')
elif driving == '無':
	if age >= 18:
		print('你可以考牌啊,點解唔去考?')
	else:
		print('很好,再過幾年就可以去考牌啦')