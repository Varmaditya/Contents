function calculateDiscount() {
    let amount = Number(document.getElementById("amount").value);
    let discount;

    if (amount >= 10000) {
        discount = 30;
    } else if (amount >= 5000) {
        discount = 20;
    } else if (amount >= 2000) {
        discount = 10;
    } else {
        discount = 0;
    }

    let finalPrice = amount - (amount * discount) / 100;

    document.getElementById("result").innerHTML =
        "💸 Discount: " + discount + "%<br>" + "🧾 Final Price: ₹" + finalPrice;
}
