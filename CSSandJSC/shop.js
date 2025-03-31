// 載入商品列表
async function loadProducts() {
    try {
        const response = await fetch("http://127.0.0.1:8000/show_products");
        const data = await response.json();

        const productList = document.getElementById("product-list");
        productList.innerHTML = ""; // 清空列表

        data.products.forEach(product => {
            const productDiv = document.createElement("div");
            productDiv.className = "product";
            productDiv.innerHTML = `
                <h3>商品名稱: ${product.name}</h3>
                <p>價格: ${product.price} 元</p>
                <p>庫存數量: ${product.have} 個</p>
                <button onclick="addToCart(1, ${product.id}, 1)">加入購物車</button>`;
            productList.appendChild(productDiv);
        });

    } catch (error) {
        console.error("載入商品失敗:", error);
    }
}

// 加入購物車
async function addToCart(user_id, product_id, many) {
    try {
        const res = await fetch(`http://127.0.0.1:8000/addToCart?user_id=${user_id}&product_id=${product_id}&many=${many}`);
        const data = await res.json();
        alert(data.message);
    } catch (err) {
        console.error("加入購物車失敗", err);
    }
}

// 跳轉至購物車頁面
function goToCart() {
    window.location.href = `cart.html?user_id=${user_id}`;  // 使用 user_id 傳遞參數
}


// 頁面載入時載入商品
window.onload = loadProducts;
