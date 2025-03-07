async function addToCart(user_id, product_id, many) {
    try {
        // 發送請求將商品加入購物車
        let response = await fetch(`http://127.0.0.1:8000/addToCart?user_id=${user_id}&product_id=${product_id}&many=${many}`, {
            method: 'GET',
        });
        
        let data = await response.json();
        alert(data.message); // 顯示回應訊息
    } catch (error) {
        console.error("加入購物車失敗:", error);
        alert("加入購物車失敗");
    }
}
//當寫 let response = await fetch(...) 時，這段代碼會發送一個 HTTP 請求，並且會等待該請求的回應。
//await 會讓程式碼等到 fetch() 執行完並得到回應後，再將結果儲存到 response 變數中。