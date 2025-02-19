#註冊
NewuserName=str(input("請輸入欲註冊使用者名稱:"))
NewuserPassWord=str(input("請輸入欲註冊使用者密碼:"))
print("帳號註冊成功!!!")
#登入
userName=str(input("請輸入使用者名稱:"))
userPassWord=str(input("請輸入使用者密碼:"))
if(userName==NewuserName and userPassWord==NewuserPassWord):
    print("歡迎用戶:"+userName+"回來!!")
elif(userName!=NewuserName and userPassWord==NewuserPassWord):
    print("找不到用戶!")
elif(userName==NewuserName and userPassWord!=NewuserPassWord):
    print("用戶:"+userName+"密碼錯誤!")
#pos系統