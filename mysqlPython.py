import mysql.connector
conn=mysql.connector.connect(
    host="localhost",#伺服器位置
    user="root",     #sql使用者名稱
    password="12345678",#sql密碼
    database="shop_db"#sql要使用的資料庫名稱
)
talk= conn.cursor()
def add_user(username, password):  # 新增使用者
    talk.execute("SELECT * FROM users WHERE username = %s", (username,))  # 檢查資料庫中是否已有此帳號
    if talk.fetchone():  # 如果資料庫中已經有這個帳號
        print(f"使用者{username}已經存在!")
        return False
    talk.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))  # 插入新帳號與密碼
    conn.commit()  # 提交更改
    print("帳號註冊成功!!!")  # 註冊成功訊息
    return True

def check_user(username, password):  # 登入檢查
    talk.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))  # 查詢是否匹配
    if talk.fetchone():  # 如果查詢結果有找到匹配的資料
        print(f"歡迎{username}回來!")  # 登入成功訊息
        return True
    else:
        print("登入失敗 帳號或密碼錯誤!")  # 登入失敗訊息
        return False
    # 關閉游標與資料庫連接
    cursor.close()  # 關閉游標
    conn.close()  # 關閉資料庫連接

def addProduct():  # 新增商品
    productName = input("請輸入商品名稱:")  # 輸入商品名稱
    # 查詢資料庫中是否已經有此商品
    talk.execute("SELECT * FROM products WHERE name = %s", (productName,))
    if talk.fetchone():  # 如果資料庫中已經有此商品
        print(f"商品{productName}已經存在!")
        return

    price = float(input("請輸入商品售價:"))  # 輸入商品價格
    # 插入新商品到資料庫
    talk.execute("INSERT INTO products (name, price) VALUES (%s, %s)", (productName, price))
    conn.commit()  # 提交更改
    print(f"已新增商品 {productName}, {price}元")  # 顯示成功訊息

def showProduct():  # 顯示商品列表
    # 查詢資料庫中的所有商品
    talk.execute("SELECT * FROM products")
    products = talk.fetchall()  # 獲取所有商品資料
    if not products:  # 如果資料庫中沒有商品
        print("目前沒有商品")
        return

    print("\n=====商品列表=====")
    for product in products:  # 顯示所有商品
        print(f"商品 {product[1]}: {product[2]}元")
        #product[0]是商品id是商品id
        #product[1] 是商品名稱
        #product[2] 是價格
