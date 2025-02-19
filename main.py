def registr():#註冊
    NewuserName=input("請輸入欲註冊使用者名稱:")
    NewuserPassWord=input("請輸入欲註冊使用者密碼:")
    print("帳號註冊成功!!!")
def login():#登入
    userName=input("請輸入使用者名稱:")
    userPassWord=input("請輸入使用者密碼:")
    if(userName==registr() and userPassWord==registr()):
        print(f"歡迎用戶:{userName}回來!!")
    elif(userName!=registr() and userPassWord==registr):
        print("找不到用戶!")
    elif(userName==registr() and userPassWord!=registr()):
        print(f"用戶:{userName}密碼錯誤!")
#pos系統