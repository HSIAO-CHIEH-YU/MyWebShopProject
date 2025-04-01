// 假設 user_id 是登入時存到 localStorage
const user_id = localStorage.getItem("user_id");

async function loadCart() {
    if (!user_id) {
        alert("請先登入！");
        window.location.href = "login.html";  // 導向登入頁面
        return;
    }

    try {
        const response = await fetch(`http://127.0.0.1:8000/show_cart/${user_id}`);
        const data = await response.json();

        const cartItems = document.getElementById("cart-items");
        cartItems.innerHTML = "";  // 清空購物車內容

        if (data.cart === "目前購物車是空的") {
            cartItems.innerHTML = "<p>購物車是空的</p>";
            return;
        }

        // 顯示購物車內容
        data.cart.forEach(item => {
            const itemDiv = document.createElement("div");
            itemDiv.className = "cart-item";
            itemDiv.innerHTML = `
                <p>商品 ID: ${item.product_id}</p>
                <p>數量: ${item.many}</p>
                <hr>
            `;
            cartItems.appendChild(itemDiv);
        });

    } catch (error) {
        console.error("載入購物車失敗:", error);
    }
}

// 頁面載入時執行
window.onload = loadCart;
