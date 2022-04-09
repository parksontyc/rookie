# else
# elif
# 型別轉換

age = input('請輸入年紀：')
age = int(age) # 型別轉換

if age < 20:
    print('菜鳥哦')
elif age >= 20 and age < 30:
    print('有年紀了哦')
else:
    print('老人')