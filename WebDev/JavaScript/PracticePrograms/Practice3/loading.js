function startLoading() {
    let loadingText = "";
    let progress = 10;

    while (progress <= 100) {
        loadingText += "<div class='item'>" + "⚡ Loading " + progress + "%" + "</div>";
        progress += 10;
    }

    document.getElementById("output").innerHTML = loadingText;
}
