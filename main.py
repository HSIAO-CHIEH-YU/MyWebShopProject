def registr():#註冊
    NewuserName=input("請輸入欲註冊使用者名稱:")
    NewuserPassWord=input("請輸入欲註冊使用者密碼:")
    print("帳號註冊成功!!!")
    return NewuserName,NewuserPassWord
def login(Nreg_user,Nreg_pass):#登入
    userName=input("請輸入使用者名稱:")
    userPassWord=input("請輸入使用者密碼:")
    if(userName==Nreg_user and userPassWord==Nreg_pass):
        print(f"歡迎用戶:{userName}回來!!")
    elif(userName!=Nreg_user and userPassWord==Nreg_pass):
        print("找不到用戶!")
    elif(userName==Nreg_user and userPassWord!=Nreg_pass):
        print(f"用戶:{userName}密碼錯誤!")

Nreg_user,Nreg_pass=registr()
login(Nreg_user,Nreg_pass)#登入比對註冊的帳密
#pos系統