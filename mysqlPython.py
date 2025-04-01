import mysql.connector
from mysql.connector import Error
import datetime

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
            if username=="admin" and password=="admin123":
                return "管理員登入成功"
            else:
                return "登入成功"
        else:
            return "找不到使用者或密碼錯誤"  # 找不到使用者或密碼錯誤
    except Error as e:
        print(f"資料庫操作錯誤: {e}")
        return "資料庫操作錯誤"
    finally:
        if conn:
            conn.close()

def add_product(product_name, price, have):  # 新增商品 #have是庫存
    conn = creat_connet()
    if conn is None:
        print("資料庫連接失敗")
        return "資料庫連接失敗"
    
    try:
        talk = conn.cursor()
        talk.execute("SELECT * FROM products WHERE name = %s", (product_name,))
        if talk.fetchone():
            return f"商品 {product_name} 已經存在!"
        
        talk.execute("INSERT INTO products (name, price, have) VALUES (%s, %s, %s)", (product_name, price, have))
        conn.commit()
        return f"商品 {product_name} 已成功新增!,售價是{price}元,庫存數量有{have}個"
    except Error as e:
        print(f"資料庫操作錯誤: {e}")
        return "資料庫操作錯誤"
    finally:
        if conn:
            conn.close()

def delete_product_by_id(product_id: int):  # 根據商品 ID 刪除商品
    conn = creat_connet()
    if conn is None:
        return "資料庫連接失敗"
    
    try:
        talk = conn.cursor()
        
        # 查找商品是否存在
        talk.execute("SELECT * FROM products WHERE id = %s", (product_id,))
        if not talk.fetchone():
            return f"商品 ID {product_id} 不存在"
        
        # 刪除商品
        talk.execute("DELETE FROM products WHERE id = %s", (product_id,))
        conn.commit()  # 提交更改
        return f"商品 ID {product_id} 已被刪除"
    except Error as e:
        conn.rollback()  # 若發生錯誤，回滾事務
        return f"刪除商品時發生錯誤: {e}"
    finally:
        if conn:
            conn.close()


def update_product_name_by_id(product_id: int, new_name: str):  # 根據商品 ID 更新商品名稱
    conn = creat_connet()
    if conn is None:
        return "資料庫連接失敗"
    try:
        talk = conn.cursor()
        # 查找商品是否存在
        talk.execute("SELECT * FROM products WHERE id = %s", (product_id,))
        if not talk.fetchone():
            return f"商品 ID {product_id} 不存在"
        
        # 更新商品名稱
        talk.execute("UPDATE products SET name = %s WHERE id = %s", (new_name, product_id))
        conn.commit()
        return f"商品 ID {product_id} 的名稱已更新為 {new_name}"
    except Error as e:
        conn.rollback()
        return f"更新商品名稱時發生錯誤: {e}"
    finally:
        if conn:
            conn.close()

def update_product_price_by_id(product_id: int, new_price: int):  # 根據商品 ID 更新商品價格
    conn = creat_connet()
    if conn is None:
        return "資料庫連接失敗"
    try:
        talk = conn.cursor()
        # 查找商品是否存在
        talk.execute("SELECT * FROM products WHERE id = %s", (product_id,))
        if not talk.fetchone():
            return f"商品 ID {product_id} 不存在"
        
        # 更新商品價格
        talk.execute("UPDATE products SET price = %s WHERE id = %s", (new_price, product_id))
        conn.commit()
        return f"商品 ID {product_id} 的價格已更新為 {new_price} 元"
    except Error as e:
        conn.rollback()
        return f"更新商品價格時發生錯誤: {e}"
    finally:
        if conn:
            conn.close()
            
def update_product_have_by_id(product_id: int, new_have: int):  # 根據商品 ID 更新商品庫存
    conn = creat_connet()
    if conn is None:
        return "資料庫連接失敗"
    try:
        talk = conn.cursor()
        # 查找商品是否存在
        talk.execute("SELECT * FROM products WHERE id = %s", (product_id,))
        if not talk.fetchone():
            return f"商品 ID {product_id} 不存在"
        
        # 更新商品庫存
        talk.execute("UPDATE products SET have = %s WHERE id = %s", (new_have, product_id))
        conn.commit()
        return f"商品 ID {product_id} 的庫存已更新為 {new_have} 個"
    except Error as e:
        conn.rollback()
        return f"更新商品庫存時發生錯誤: {e}"
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
            product_list.append({"id":product[0],"name":product[1],"price":product[2],"have":product[3]})
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

def show_cart(user_id):  # 顯示購物車
    conn = creat_connet()
    if conn is None:
        print("資料庫連接失敗")
        return "資料庫連接失敗"
    
    try:
        talk = conn.cursor()
        talk.execute("SELECT products.name,products.price,productsCar.many From productsCar JOIN products ON productsCar.product_id=products.id WHERE productsCar.user_id=%s",(user_id,))
        productsCar = talk.fetchall()
        if not productsCar:
            return "目前購物車是空的"
        product_list=[]
        for product in productsCar:
            product_list.append({"name":product[0],"price":product[1],"many":product[2],"total":product[1]*product[2]})
        return product_list
    except Error as e:
        print(f"資料庫操作錯誤: {e}")
        return "資料庫操作錯誤"
    finally:
        if conn:
            conn.close()

def delete_from_cart(user_id, product_id):  # 從購物車刪除商品
    conn = creat_connet()
    if conn is None:
        print("資料庫連接失敗")
        return "資料庫連接失敗"
    
    try:
        talk = conn.cursor()
        talk.execute("SELECT * FROM productsCar WHERE user_id = %s AND product_id = %s", (user_id, product_id))
        product = talk.fetchone()

        if not product:
            return "購物車中找不到該商品"
        
        talk.execute("DELETE FROM productsCar WHERE user_id = %s AND product_id = %s", (user_id, product_id))
        conn.commit()
        return "刪除成功"
    except Error as e:
        print(f"資料庫操作錯誤: {e}")
        return "資料庫操作錯誤"
    finally:
        if conn:
            conn.close()

def buy(user_id):  #結帳
    conn = creat_connet()
    if conn is None:
        print("資料庫連接失敗")
        return "資料庫連接失敗"
    
    try:
        talk = conn.cursor()
        # 1. 查詢購物車中所有商品及數量，並計算總金額
        talk.execute("SELECT products.id, products.price, productsCar.many FROM productsCar JOIN products ON productsCar.product_id = products.id WHERE productsCar.user_id = %s", (user_id,))
        products_in_cart = talk.fetchall()
        
        if not products_in_cart:
            return "購物車是空的，無法結帳"
        
        total_price = 0
        for product in products_in_cart:
            total_price += product[1] * product[2]  #product[0]=商品id # price * many
        
        # 2. 插入訂單到 orders 資料表
        order_time = datetime.now()
        talk.execute("INSERT INTO orders (user_id, total_price, order_time)VALUES (%s, %s, %s)", (user_id, total_price, order_time))
        # 取得剛插入的訂單 ID
        order_id = talk.lastrowid
        
        # 3. 插入每一項訂單詳情到 order_details 資料表
        for product in products_in_cart:
            talk.execute("INSERT INTO order_details (order_id, product_id, many, price)VALUES (%s, %s, %s, %s)", (order_id, product[0], product[2], product[1]))
        
        # 4. 結帳後清空購物車
        talk.execute("DELETE FROM productsCar WHERE user_id = %s", (user_id,))
        
        conn.commit()
        return f"結帳成功，訂單ID為 {order_id}，總金額：{total_price} 元"
    
    except Error as e:
        print(f"資料庫操作錯誤: {e}")
        return "資料庫操作錯誤"
    
    finally:
        if conn:
            conn.close()