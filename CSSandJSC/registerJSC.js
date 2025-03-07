// 監聽註冊表單提交事件
document.getElementById("registerForm").addEventListener("submit",async function(event){
    event.preventDefault();  // 阻止表單的默認提交行為
    
    const username = document.getElementById("username").value;  // 獲取用戶名
    const password = document.getElementById("password").value;  // 獲取密碼

    // 發送 POST 請求到後端 API 進行註冊
    const response=await fetch("http://127.0.0.1:8000/register", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"  // 設定請求的內容類型為 JSON
        },
        body: JSON.stringify({ username: username, password: password })  // 將用戶名和密碼作為 JSON 傳送
    });
    const data= await response.json();  // 解析 JSON 響應
    
    if (data.message == "註冊成功")
    {
        alert(data.message);// 顯示來自後端的訊息
        window.location.href = "login.html";  // 跳轉到登入頁面
    }
    else
    {
        alert(data.message);// 若登入失敗，顯示錯誤訊息
    }
});