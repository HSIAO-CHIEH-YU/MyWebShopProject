// 讀取 URL 中的 user_id 參數
function getUserIdFromURL() {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get('user_id');
}

// 顯示購物車
async function showCart() {
    const user_id = getUserIdFromURL();  // 取得 user_id
    if (!user_id) {
        alert("使用者未登入，無法顯示購物車！");
        return;
    }

    try {
        const response = await fetch(`http://127.0.0.1:8000/show_cart?user_id=${user_id}`);
        const data = await response.json();

        const cartDiv = document.getElementById("cart-list");
        cartDiv.innerHTML = "";  // 清空購物車內容

        if (data.length === 0) {
            cartDiv.innerHTML = "<p>您的購物車是空的。</p>";
        } else {
            data.forEach(item => {
                const cartItemDiv = document.createElement("div");
                cartItemDiv.innerHTML = `
                    <h3>商品名稱: ${item.name}</h3>
                    <p>數量: ${item.many}</p>
                    <p>價格: ${item.price} 元</p>
                `;
                cartDiv.appendChild(cartItemDiv);
            });
        }
    } catch (error) {
        console.error("顯示購物車失敗:", error);
    }
}

// 頁面載入時顯示購物車
window.onload = showCart;
