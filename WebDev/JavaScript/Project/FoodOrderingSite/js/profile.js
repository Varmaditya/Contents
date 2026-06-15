// UPDATE PROFILE

function updateProfile(){

    let name =
    document.getElementById(
        "userName"
    ).value;

    let email =
    document.getElementById(
        "userEmail"
    ).value;

    let phone =
    document.getElementById(
        "userPhone"
    ).value;

    let city =
    document.getElementById(
        "userCity"
    ).value;

    let favoriteFood =
    document.getElementById(
        "favoriteFood"
    ).value;

    if(name === ""){
        alert("Please Enter Name");
        return;
    }

    document.getElementById("profileCard").innerHTML =
    `<div class="profile-card">
        <h3>👤 ${name}</h3>
        <p>
            📧 ${email}
        </p>
        <p>
            📱 ${phone}
        </p>
        <p>
            📍 ${city}
        </p>
        <p>
            🍔 Favorite:
            ${favoriteFood}
        </p>
    </div>`;

    document.getElementById("foodDisplay").innerText =favoriteFood;

    document.getElementById("cityDisplay").innerText = city;
}
