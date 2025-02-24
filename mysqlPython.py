import mysql.connector
from mysql.connector import Error

def creat_connet():
    try:
        conn = mysql.connector.connect(
            host="localhost",  # 伺服器位置
            user="root",       # sql使用者名稱
            password="12345678",  # sql密碼
            database="shop_db"  # sql要使用的資料庫名稱
        )
        return conn
    except Error as e:
        print(f"資料庫連接錯誤: {e}")
        return None

def add_user(username, password):  # 新增使用者
    conn = creat_connet()
    if conn is None:
        return("資料庫連接失敗")
    
    try:
        talk = conn.cursor()  # 建立一個游標（cursor），讓我們可以對資料庫執行 SQL 查詢。
        talk.execute("SELECT * FROM users WHERE username = %s", (username,))
        if talk.fetchone():
            return(f"使用者 {username} 已經存在!")
        else: 
            talk.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            conn.commit()  # 類似git的快照
            return("註冊成功")
        
    except Error as e:
        return(f"資料庫操作錯誤: {e}")
    finally:
        if conn:
            conn.close()

def check_user(username, password):  # 登入檢查
    conn = creat_connet()
    if conn is None:
        return False ("資料庫連接失敗")
    try:
        talk = conn.cursor()
        talk.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        if talk.fetchone():
            return True
        else:
            return False 
    except Error as e:
        return False (f"資料庫操作錯誤: {e}")
    finally:
        if conn:
            conn.close()

def add_product(product_name, price):  # 新增商品
    conn = creat_connet()
    if conn is None:
        print("資料庫連接失敗")
    
    try:
        talk = conn.cursor()
        talk.execute("SELECT * FROM products WHERE name = %s", (product_name,))
        if talk.fetchone():
            print(f"商品 {product_name} 已經存在!")
        
        talk.execute("INSERT INTO products (name, price) VALUES (%s, %s)", (product_name, price))
        conn.commit()
        print(f"商品 {product_name} 已成功新增!,售價是{price}")
    except Error as e:
        print(f"資料庫操作錯誤: {e}")
    finally:
        if conn:
            conn.close()

def show_products():  # 顯示商品
    conn = creat_connet()
    if conn is None:
        print("資料庫連接失敗")
    
    try:
        talk = conn.cursor()
        talk.execute("SELECT * FROM products")
        products = talk.fetchall()
        if not products:
            print("目前沒有商品")
    
        product_list=[]
        print("=====商品列表=====")
        for product in products:
            product_list.append({"id":product[0],"name":product[1],"price":product[2]})
            print(f"商品:{product[1]} 售價:{product[2]}元")
    except Error as e:
        print(f"資料庫操作錯誤: {e}")
    finally:
        if conn:
            conn.close()
