import mysqlPython  # 導入mysql
import requests

# 字典 {key, value}
users = {}  # 會員(帳號:密碼)
products = {}  # 商品(商品名:售價)
cart = {}  # 購物車

def registr():  # 註冊
    NewuserName = input("請輸入欲註冊使用者名稱:")
    NewuserPassWord = input("請輸入欲註冊使用者密碼:")
    #向api發送請求
    response = requests.post("http://127.0.0.1:8000/register", json={"username": NewuserName, "password": NewuserPassWord})
    print(response.json()['message'])
    
def login(): # 登入
    userName = input("請輸入使用者名稱:")
    userPassWord = input("請輸入使用者密碼:")
    response = requests.post("http://127.0.0.1:8000/login", json={"username": userName, "password": userPassWord})
    message=response.json()['message']
    print(message)
    if message=="登入成功":
        return True
    else:
        return False
def addProduct():  # 新增商品
    productName = input("請輸入商品名稱:")
    price = float(input("請輸入商品售價:"))
    response = requests.post("http://127.0.0.1:8000/add_product", json={"name": productName, "price": price})
    print(response.json()['message'])

def showProduct():  # 顯示商品列表
    response = requests.get("http://127.0.0.1:8000/show_products")
    data = response.json()
    global products  # 讓它可以修改外部的 `products` 變數
    products = {item["name"]: item["price"] for item in data["products"]}
    print(products)


def addToCart():  # 加入購物車
    wantBuy = input("請輸入欲購買的物品:")
    if wantBuy not in products:
        print(f"找不到此 {wantBuy} 商品")
        return
    howMuchWantBuy = int(input("請輸入欲購買的數量:"))
    cart[wantBuy] = cart.get(wantBuy, 0) + howMuchWantBuy
    print(f"{wantBuy} 已加入購物車, 數量為 {cart[wantBuy]} 個")

def shopping():  # 結帳
    if not cart:
        print("您的購物車是空的!")
        return
    
    showProduct()  # 確保商品清單最新

    totalMoney = 0
    for wantBuy, howMuchWantBuy in cart.items():
        if wantBuy not in products:
            print(f"商品 {wantBuy} 已被移除，無法結帳！")
            continue
        totalMoney += products[wantBuy] * howMuchWantBuy
    if totalMoney == 0:
        print("沒有可結帳的商品!")
    else:
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
