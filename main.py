import mysqlPython  # 導入mysql
# 字典 {key, value}
users = {}  # 會員(帳號:密碼)
products = {}  # 商品(商品名:售價)
cart = {}  # 購物車

def registr():  # 註冊
    NewuserName = input("請輸入欲註冊使用者名稱:")
    NewuserPassWord = input("請輸入欲註冊使用者密碼:")
    mysqlPython.add_user(NewuserName,NewuserPassWord)
    
def login(): # 登入
    userName = input("請輸入使用者名稱:")
    userPassWord = input("請輸入使用者密碼:")
    if mysqlPython.check_user(userName,userPassWord):
        return True
    
def addProduct():  # 新增商品
    productName = input("請輸入商品名稱:")
    price = float(input("請輸入商品售價:"))
    mysqlPython.add_product(productName,price)

def showProduct():  # 顯示商品列表
    # 呼叫 mysqlPython.showProduct() 來顯示資料庫中的商品
    mysqlPython.show_products()

def addToCart():  # 加入購物車
    wantBuy = input("請輸入欲購買的物品:")
    if wantBuy not in products:
        print(f"找不到此 {wantBuy} 商品")
        return
    howMuchWantBuy = int(input("請輸入欲購買的數量:"))
    if wantBuy in cart:
        cart[wantBuy] = cart[wantBuy] + howMuchWantBuy
    else:
        cart[wantBuy] = howMuchWantBuy
    print(f"{wantBuy} 已加入購物車, 數量為 {cart[wantBuy]} 個")

def shopping():  # 結帳
    if not cart:
        print("您的購物車是空的!")
        return
    totalMoney = 0
    for wantBuy, howMuchWantBuy in cart.items():
        x = products[wantBuy] * howMuchWantBuy
        # products 字典裡的 [wantBuy] (想買的東西) = 那個商品的售價
        # howMuchWantBuy = 上面 cart.items() 裡面的 value 幾個
        totalMoney = totalMoney + x
    print(f"總金額為: {totalMoney} 元")

# 主程式
login_in = False
while True:
    print("=== POS 系統 ===")
    print("1. 註冊帳號")
    print("2. 登入帳號")
    print("3. 新增商品")
    print("4. 顯示商品")
    print("5. 加入購物車")
    print("6. 結帳")
    print("7. 離開系統")
    
    if not login_in:
        print("請先登入或註冊!")
        choice = int(input("請選擇功能:"))
    else:
        choice = int(input("請選擇功能:"))
        
    if choice == 1:
        registr()
    elif choice == 2:
        login_in = login()
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
