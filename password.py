#猜密碼程式
#設定password = 'a12345'
#讓使用者猜三次
#如果猜錯就顯示還剩幾次機會
#當剩0次時，就不印出來

password = 'a1234'
x = 3
while True:
    password1 = input('請輸入密碼:')
    if password1 == password:
        print('密碼正確')
        break
    elif password1 != password:
        x = x-1
        if x > 0:
            print('你還有', x, '機會')
        elif x == 0:
            print('重新申請')
            break


        
