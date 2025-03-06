document.getElementById("loginForm").addEventListener("submit", function(event){
    event.preventDefault();
    
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    fetch("http://127.0.0.1:8000/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ username: username, password: password })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);// 顯示來自後端的訊息
        if (data.message == "登入成功")
        {
            window.location.href = "pos.html";  // 跳轉到pos頁面
        }
    })
    .catch(error => alert.log(error));
}); 