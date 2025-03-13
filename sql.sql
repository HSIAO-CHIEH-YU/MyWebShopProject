create database shop_db;

USE shop_db;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL
);

CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE productsCar (
    id INT AUTO_INCREMENT PRIMARY KEY,              -- 設置 `id` 為主鍵，並使用 AUTO_INCREMENT 讓它自動遞增
    user_id INT NOT NULL,                           -- `user_id`，代表購物車中的使用者 ID，不能為 NULL
    product_id INT NOT NULL,                        -- `product_id`，代表購物車中的產品 ID，不能為 NULL
    many INT NOT NULL,                              -- `many`，代表該產品的購買數量，不能為 NULL
    FOREIGN KEY (user_id) REFERENCES users(id),     -- `user_id` 外鍵，參考 `users` 資料表的 `id` 欄位
    FOREIGN KEY (product_id) REFERENCES products(id)-- `product_id` 外鍵，參考 `products` 資料表的 `id` 欄位
);

CREATE TABLE orders (                             -- 建立 `orders` 資料表 下訂單的使用者
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    total_price FLOAT,
    order_time DATETIME
);

CREATE TABLE order_details (            -- 建立 `order_details` 資料表，用來紀錄訂單的詳細資訊
    id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    product_id INT,
    many INT,
    price FLOAT
);
