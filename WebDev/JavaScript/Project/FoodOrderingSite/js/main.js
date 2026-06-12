// GREETING MESSAGE

function showGreeting(){
    let hour =
    new Date().getHours();
    let greeting;

    if(hour < 12){
        greeting = "☀️ Good Morning Food Lover!";
    } else if(hour < 18){
        greeting = "🍔 Good Afternoon Food Lover!";
    } else{
        greeting = "🌙 Good Evening Food Lover!";
    }

    let heroHeading = document.querySelector(".hero-content h1");

    if(heroHeading){
        heroHeading.innerText = greeting;
    }
}

showGreeting();
