import mysql.connector
conn=mysql.connector.connect(
    host="localhost",#伺服器位置
    user="root",     #sql使用者名稱
    password="12345678",#sql密碼
    database="shop_db"#sql要使用的資料庫名稱
)

talk=conn.cursor()#用來執行SQL語句。是MySQL資料庫的一個操作接口通過它來執行查詢 插入 更新等操作。

def add_user(username,password):#新增使用者
    query = "INSERT INTO users (username, password) VALUES (%s, %s)"#INSERT INTO用來向資料表中插入資料的SQL命令
    talk.execute(query,(username,password))
    conn.commit()#類似github的快照
    print("用戶新增成功!")
    
def add_product(name,price):#新增商品
    query = "INSERT INTO product (name, price) VALUES (%s, %s)"#INSERT INTO用來向資料表中插入資料的SQL命令
    talk.execute(query,(name,price))
    conn.commit()#類似github的快照
    print("商品新增成功!")
    
add_user("tester","123")
add_product("game","1299.9")

talk.close()
conn.close()
        
        