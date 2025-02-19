users={}#會員(帳號:密碼)
products={}#商品(商品名:售價)
cart={}#購物車

def registr():#註冊
    NewuserName=input("請輸入欲註冊使用者名稱:")
    if NewuserName in users:
        print(f"使用者{NewuserName}已經存在!")
        return
    NewuserPassWord=input("請輸入欲註冊使用者密碼:")
    users[NewuserName]=NewuserPassWord
    print("帳號註冊成功!!!")
    
def login():#登入
    userName=input("請輸入使用者名稱:")
    userPassWord=input("請輸入使用者密碼:")
    if(userName in users and users[userName]==userPassWord):
        print(f"歡迎{userName}回來!")
        return True
    else:
        print("登入失敗 帳號或密碼錯誤!")
        return False
#測試用   
#registr()
#login()

#pos系統
def addProduct():#新增商品
    productName=input("請輸入商品名稱:")
    if productName in products:
        print("商品已經存在!")
        return
    price=float(input("請輸入商品售價:"))
    products[productName]=price
    print(f"已新增商品{productName},{price}元")
    
        
    
