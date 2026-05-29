function generateProducts() {
    let products = "";

    for (let i = 1; i <= 6; i++) {
        products +=
            "<div class='item'>" + "🛍 Product Card " +
            i + "<br>" + "💸 Price: ₹" +
            i * 500 + "</div>";
    }

    document.getElementById("output").innerHTML = products;
}
