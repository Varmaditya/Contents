// CALCULATE BILL

function calculateOrder(){

    let customerName =
    document.getElementById(
        "customerName"
    ).value;

    let foodPrice =
    Number(
        document.getElementById(
            "foodItem"
        ).value
    );

    let quantity =
    Number(
        document.getElementById(
            "quantity"
        ).value
    );

    if(customerName === ""){
        alert("Please Enter Name");
        return;
    }

    if(quantity <= 0){
        alert("Please Enter Quantity");
        return;
    }

    let total = foodPrice * quantity;
    let discount = 0;

    if(total >= 3000){
        discount = 20;
    } else if(total >= 2000){
        discount = 15;
    } else if(total >= 1000){
        discount = 10;
    }

    let discountAmount = total * discount / 100;

    let finalBill = total - discountAmount;

    document.getElementById("orderSummary").innerHTML =
    `<h3>Order Details</h3>
    <p>
        👤 Customer:
        ${customerName}
    </p>
    <p>
        🍽 Food Price:
        ₹${foodPrice}
    </p>
    <p>
        🔢 Quantity:
        ${quantity}
    </p>
    <p>
        💰 Total:
        ₹${total}
    </p>

    <p>
        🎁 Discount:
        ${discount}%
    </p>
    <p>
        ✅ Final Bill:
        ₹${finalBill.toFixed(2)}
    </p>`;
}

// PLACE ORDER

function placeOrder(){
    alert( "🎉 Order Placed Successfully!");
}
