import mysql.connector
def getConnet():
    return mysql.connector.connect(
        host="localhost",#伺服器位置
        user="root",     #sql使用者名稱
        password="12345678",#sql密碼
        database="shop_db"#sql要使用的資料庫名稱
)

# 新增使用者
def add_user(username, password):
    connect = getConnet()  # 取得資料庫連線
    talk = connect.cursor()         # 創建游標，用來執行 SQL 查詢
    query = "INSERT INTO users (username, password) VALUES (%s, %s)"  # 插入使用者的 SQL 查詢
    talk.execute(query, (username, password))  # 執行查詢，並傳入參數
    connect.commit()  # 提交交易，確保資料已經寫入資料庫
    talk.close()  # 關閉游標
    connect.close()  # 關閉資料庫連線
    
# 查詢使用者是否存在
def check_user_exists(username):
    connection = getConnet()  # 取得資料庫連線
    talk = connection.cursor()         # 創建游標
    query = "SELECT * FROM users WHERE username = %s"  # 查詢使用者的 SQL 查詢
    talk.execute(query, (username,))  # 執行查詢，並傳入參數
    user = talk.fetchone()  # 取得查詢結果中的第一筆資料
    talk.close()  # 關閉游標
    connection.close()  # 關閉資料庫連線
    return user  # 如果找到使用者，則返回該使用者資料
    
# 新增商品
def add_product(name, price):
    connection = getConnet()  # 取得資料庫連線
    talk = connection.cursor()         # 創建游標
    query = "INSERT INTO products (name, price) VALUES (%s, %s)"  # 插入商品的 SQL 查詢
    talk.execute(query, (name, price))  # 執行查詢，並傳入商品名稱和價格
    connection.commit()  # 提交交易，確保資料已經寫入資料庫  
    talk.close()  # 關閉游標
    connection.close()  # 關閉資料庫連線

# 查詢所有商品
def show_all_products():
    connection = getConnet()  # 取得資料庫連線
    talk = connection.cursor()         # 創建游標
    query = "SELECT * FROM products"  # 查詢所有商品的 SQL 查詢
    talk.execute(query)  # 執行查詢
    products = talk.fetchall()  # 取得所有商品的資料
    talk.close()  # 關閉游標
    connection.close()  # 關閉資料庫連線
    return products  # 返回所有商品資料
        