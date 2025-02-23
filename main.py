import mysqlPython#導入mysql
# 測試新增使用者
mysqlPython.add_user("admin", "password123")

# 測試新增商品
mysqlPython.add_product("Laptop", 1500.99)

# 關閉連線
mysqlPython.close_connection()
#字典{key,value}
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

def addProduct():#新增商品
    productName=input("請輸入商品名稱:")
    if productName in products:
        print("商品已經存在!")
        return
    price=float(input("請輸入商品售價:"))
    products[productName]=price
    print(f"已新增商品{productName},{price}元")
    
#測試用    
#addProduct()
#print(products)

def showProduct():#顯示商品列表
    if not products:
        print("目前沒有商品")
        return
    print("\n商品列表")
    for productName,price in products.items():
        print(f"商品{productName}:{price}元")
#showProduct()

def addToCart():#加入購物車
    wantBuy=input("請輸入欲購買的物品:")
    if wantBuy not in products:
        print(f"找不到此{wantBuy}商品")
        return
    howMuchWantBuy=int(input("請輸入欲購買的數量:"))
    if wantBuy in cart:
        cart[wantBuy]=cart[wantBuy]+howMuchWantBuy
    else:
        cart[wantBuy]=howMuchWantBuy
    print(f"{wantBuy}已加入購物車,數量為{cart[wantBuy]}個")

#測試  
#addProduct()
#showProduct()
#addToCart()

def shopping():#結帳
    if not cart:
        print("您的購物車是空的!")
        return
    totalMoney=0
    for wantBuy,howMuchWantBuy in cart.items():
        x=products[wantBuy]*howMuchWantBuy
        #products字典裡的[wantBuy](想買的東西)=那個商品的售價
        #howMuchWantBuy=上面cart.items()裡面的value 幾個
        totalMoney=totalMoney+x
    print(f"總金額為:{totalMoney}元")
    
#主程式
login_in=False
while True:
    print("===POS系統===")
    print("1.註冊帳號")
    print("2.登入帳號")
    print("3.新稱商品")
    print("4.顯示商品")
    print("5.加入購物車")
    print("6.結帳")
    print("7.離開系統")
    
    if login_in==False:
        print("請先登入或註冊!")
        choice=int(input("請選擇功能:"))
    else:
        choice=int(input("請選擇功能:"))
        
    if choice==1:
        registr()
    elif choice==2:
        login_in=login()
    elif choice == 3:
        if login_in:
            addProduct()
        else:
            print("請先登入!")
    elif choice == 4:
        if login_in:  
            showProduct()
        else:
            print("請先登入!")
    elif choice == 5:
        if login_in: 
            addToCart()
        else:
            print("請先登入!")
    elif choice == 6:
        if login_in:  
            shopping()
        else:
            print("請先登入!")
    elif choice == 7:
        print("感謝使用POS系統")
        break
    else:
        print("請輸入有效選項!")