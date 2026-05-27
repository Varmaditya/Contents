function loginUser() {
    let username = document.getElementById("username").value;
    let password = document.getElementById("password").value;

    if (username === "admin") {
        if (password === "1234") {
            document.getElementById("result").innerHTML =
                "✅ Login Successful<br>" + "🛡 Admin Dashboard Access Granted";
        } else {
            document.getElementById("result").innerHTML =
                "❌ Incorrect Password";
        }
    } else {
        document.getElementById("result").innerHTML = "❌ User Not Found";
    }
}
