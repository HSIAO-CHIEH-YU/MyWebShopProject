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
async function addToCart(product_id, many) {
    const user_id = localStorage.getItem("user_id"); // 從 localStorage 中取得 user_id

    if (!user_id) {
        alert("請先登入！");
        return;
    }

    try {
        // 這裡確保使用正確的 HTTP 方法，通常會是 POST，根據你的 API 設計
        const res = await fetch(`http://127.0.0.1:8000/addToCart`, {
            method: 'POST', // 改成 POST 方法
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                user_id: user_id,
                product_id: product_id,
                many: many
            })
        });
        const data = await res.json();
        alert(data.message);
    } catch (err) {
        console.error("加入購物車失敗", err);
    }
}


// 跳轉至購物車頁面
function goToCart() {
    window.location.href = "userCart.html";
}


// 頁面載入時載入商品
window.onload = loadProducts;
