import mysql.connector

# 建立資料庫連線
def create_connection():
    return mysql.connector.connect(
        host="localhost",  # 資料庫主機
        user="root",       # 資料庫用戶
        password="12345678", # 資料庫密碼
        database="shop_db"  # 資料庫名稱
    )

# 新增使用者
def add_user(username, password):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
        print("註冊成功!")
    except mysql.connector.Error as err:
        print(f"資料庫錯誤: {err}")
    finally:
        cursor.close()
        conn.close()

# 檢查用戶是否存在
def check_user(username, password):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        if cursor.fetchone():
            return True
        else:
            return False
    except mysql.connector.Error as err:
        print(f"資料庫錯誤: {err}")
        return False
    finally:
        cursor.close()
        conn.close()
