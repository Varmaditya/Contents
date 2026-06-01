function bookTickets() {
    // INPUT
    let userName = document.getElementById("name").value;
    let userAge = Number(document.getElementById("age").value);
    let ticketCount = Number(document.getElementById("tickets").value);

    // CONDITIONALS
    if (userAge < 18) {
        document.getElementById("summary").innerHTML =
            "❌ Booking Failed.<br>" + "You must be 18 or older.";

        document.getElementById("ticketArea").innerHTML = "";

        return;
    }

    // VARIABLES + OPERATORS
    let ticketPrice = 500;
    let totalAmount = ticketPrice * ticketCount;
    let discount = 0;

    if (ticketCount >= 5) {
        discount = 20;
    } else if (ticketCount >= 3) {
        discount = 10;
    } else {
        discount = 0;
    }

    let discountAmount = (totalAmount * discount) / 100;
    let finalAmount = totalAmount - discountAmount;

    // OUTPUT
    document.getElementById("summary").innerHTML =
        "✅ Booking Successful<br><br>" + "👤 Name: " +
        userName + "<br>" + "🎟️ Tickets: " + ticketCount +
        "<br>" + "💸 Discount: " + discount + "%<br>" +
        "💰 Final Amount: ₹" + finalAmount;

    // LOOP
    let ticketHTML = "";

    for (let i = 1; i <= ticketCount; i++) {
        ticketHTML +=
            "<div class='ticket'>" +  "<h3>🎟 Ticket #" +
            i +  "</h3>" + "<p>Name: " + userName +
            "</p>" + "<p>Seat Zone: General</p>" + "</div>";
    }

    document.getElementById("ticketArea").innerHTML = ticketHTML;
}
