# 密碼重試程式
# password = 'a123456'
# 讓使用者重複輸入密碼
# 最多輸入3次
# 如果正確就印出"登入成功!"
# 如果不正確就印出"密碼錯誤! 還有_次機會"
try_time = 0
while True:
	try_time = try_time + 1
	if try_time <= 3:
		password = input("請輸入密碼: ")
		if password == 'a123456':
			print('登入成功')
			break
		elif try_time < 3:
			have_time = 3 - try_time
			print(f'密碼錯誤! 還有{have_time}次機會')
		else:
			print('密碼錯誤')
			break
	else:
		break
