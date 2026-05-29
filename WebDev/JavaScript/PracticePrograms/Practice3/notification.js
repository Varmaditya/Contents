function generateNotifications() {
    let text = "";

    for (let i = 1; i <= 5; i++) {
        text += "<div class='item'>" + "📩 New Notification #" + i + "</div>";
    }

    document.getElementById("output").innerHTML = text;
}
