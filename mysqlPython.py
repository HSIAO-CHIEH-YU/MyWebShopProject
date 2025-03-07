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
            return "註冊成功"
        
    except Error as e:
        return f"資料庫操作錯誤: {e}"
    finally:
        if conn:
            conn.close()

def check_user(username, password):  # 登入檢查
    conn = creat_connet()
    if conn is None:
        print("資料庫連接失敗")
        return "資料庫連接失敗"
    try:
        talk = conn.cursor()
        talk.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        result = talk.fetchone()
        if result:
            return "登入成功"
        else:
            return "找不到使用者或密碼錯誤"  # 找不到使用者或密碼錯誤
    except Error as e:
        print(f"資料庫操作錯誤: {e}")
        return "資料庫操作錯誤"
    finally:
        if conn:
            conn.close()

def add_product(product_name, price):  # 新增商品
    conn = creat_connet()
    if conn is None:
        print("資料庫連接失敗")
        return "資料庫連接失敗"
    
    try:
        talk = conn.cursor()
        talk.execute("SELECT * FROM products WHERE name = %s", (product_name,))
        if talk.fetchone():
            return f"商品 {product_name} 已經存在!"
        
        talk.execute("INSERT INTO products (name, price) VALUES (%s, %s)", (product_name, price))
        conn.commit()
        return f"商品 {product_name} 已成功新增!,售價是{price}"
    except Error as e:
        print(f"資料庫操作錯誤: {e}")
        return "資料庫操作錯誤"
    finally:
        if conn:
            conn.close()

def show_products():  # 顯示商品
    conn = creat_connet()
    if conn is None:
        print("資料庫連接失敗")
        return "資料庫連接失敗"
    
    try:
        talk = conn.cursor()
        talk.execute("SELECT * FROM products")
        products = talk.fetchall()
        if not products:
            return "目前沒有商品"
        product_list=[]
        for product in products:
            product_list.append({"id":product[0],"name":product[1],"price":product[2]})
        return product_list
    except Error as e:
        print(f"資料庫操作錯誤: {e}")
        return "資料庫操作錯誤"
    finally:
        if conn:
            conn.close()

def addToCart(user_id, product_id, many):  # 加入購物車
    conn = creat_connet()
    if conn is None:
        print("資料庫連接失敗")
        return "資料庫連接失敗"
    
    try:
        talk = conn.cursor()
        
        # 確認使用者是否存在
        talk.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        user = talk.fetchone()
        if not user:
            return "找不到使用者"
        
        # 確認商品是否存在於 products 表中
        talk.execute("SELECT * FROM products WHERE id = %s", (product_id,))
        product = talk.fetchone()
        if not product:
            return "找不到商品"
        
        # 查詢商品是否已經在購物車中
        talk.execute("SELECT * FROM productsCar WHERE user_id = %s AND product_id = %s", (user_id, product_id))
        existing_product = talk.fetchone()
        
        if existing_product:
            # 如果商品已存在，更新數量
            new_quantity = existing_product[3] + many  # 假設 'many' 是第四個欄位
            talk.execute("UPDATE productsCar SET many = %s WHERE user_id = %s AND product_id = %s", 
                         (new_quantity, user_id, product_id))
        else:
            # 如果商品不在購物車中，插入新資料
            talk.execute("INSERT INTO productsCar (user_id, product_id, many) VALUES (%s, %s, %s)", 
                         (user_id, product_id, many))
        
        conn.commit()
        return "加入購物車成功"
    except Error as e:
        print(f"資料庫操作錯誤: {e}")
        return "資料庫操作錯誤"
    finally:
        if conn:
            conn.close()

