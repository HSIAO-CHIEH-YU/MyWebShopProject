// 載入商品列表
async function loadProducts() {
    try {
        let response = await fetch("http://127.0.0.1:8000/show_products");
        let data = await response.json();
        const productListContainer = document.getElementById("product-list");
        productListContainer.innerHTML = ''; // 清空列表

        if (data.products && data.products.length > 0) {
            data.products.forEach(product => {
                const productElement = document.createElement("div");
                productElement.innerHTML = `
                    <h3>商品名稱: ${product.name}<input type="name" id="name-${product.id}" value="${product.name}">
                        <button onclick="updateProductName(${product.id})">更新商品名稱</button>
                    </h3>
                    <p>價格: <input type="number" id="price-${product.id}" value="${product.price}">
                        <button onclick="updateProductPrice(${product.id})">更新價格</button>
                    </p>
                    <p>庫存數量: <input type="number" id="stock-${product.id}" value="${product.have}">
                        <button onclick="updateProductStock(${product.id})">更新庫存</button>
                    </p>
                    <button onclick="deleteProduct(${product.id})">刪除</button>
                    <hr>
                `;
                productListContainer.appendChild(productElement);
            });
        } else {
            productListContainer.innerText = "目前沒有商品";
        }
    } catch (error) {
        console.error("載入商品列表失敗:", error);
    }
}

// 更新商品名稱
async function updateProductName(productId) {
    const newName = document.getElementById(`name-${productId}`).value.trim();
    if (!newName) {
        alert("商品名稱不能為空");
        return;
    }

    try {
        let response = await fetch(`http://127.0.0.1:8000/update_product_name/${productId}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name: newName })
        });

        let data = await response.json();
        alert(data.message);
        loadProducts(); // 重新載入商品列表
    } catch (error) {
        console.error("修改商品名稱失敗:", error);
        alert("修改商品名稱失敗");
    }
}

// 更新商品價格
async function updateProductPrice(productId) {
    const newPrice = parseFloat(document.getElementById(`price-${productId}`).value);
    if (isNaN(newPrice) || newPrice <= 0) {
        alert("請輸入有效的價格");
        return;
    }

    try {
        let response = await fetch(`http://127.0.0.1:8000/update_product_price/${productId}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ price: newPrice })
        });

        let data = await response.json();
        alert(data.message);
        loadProducts(); // 重新載入商品列表
    } catch (error) {
        console.error("修改價格失敗:", error);
        alert("修改價格失敗");
    }
}

// 更新商品庫存
async function updateProductStock(productId) {
    const newStock = parseInt(document.getElementById(`stock-${productId}`).value);
    if (isNaN(newStock) || newStock < 0) {
        alert("請輸入有效的庫存數量");
        return;
    }

    try {
        let response = await fetch(`http://127.0.0.1:8000/update_product_have/${productId}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ have: newStock })
        });

        let data = await response.json();
        alert(data.message);
        loadProducts(); // 重新載入商品列表
    } catch (error) {
        console.error("修改庫存失敗:", error);
        alert("修改庫存失敗");
    }
}

// 刪除商品
async function deleteProduct(id) {
    if (confirm("確定要刪除此商品嗎？")) {
        try {
            let response = await fetch(`http://127.0.0.1:8000/delete_product/${id}`, {
                method: 'DELETE',
            });

            let data = await response.json();

            if (response.ok) {
                alert(data.message);
                loadProducts(); // 重新載入商品列表
            } else {
                alert(data.message); // 顯示返回的錯誤訊息
            }
        } catch (error) {
            console.error("刪除商品失敗:", error);
            alert("刪除商品失敗");
        }
    }
}

// 新增商品
document.getElementById("add-form").addEventListener("submit", async (event) => {
    event.preventDefault();

    const name = document.getElementById("add-name").value;
    const price = parseFloat(document.getElementById("add-price").value);
    const have = parseInt(document.getElementById("add-have").value);

    if (!name.trim() || isNaN(price) || isNaN(have) || price <= 0 || have < 0) {
        alert("請輸入有效的商品名稱、價格和庫存數量");
        return;
    }

    try {
        let response = await fetch("http://127.0.0.1:8000/add_product", {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name, price, have }),
        });

        let data = await response.json();
        alert(data.message);
        loadProducts(); // 重新載入商品列表
    } catch (error) {
        console.error("新增商品失敗:", error);
        alert("新增商品失敗");
    }
});

// 頁面加載時載入商品
window.onload = loadProducts;
