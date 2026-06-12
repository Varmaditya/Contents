// FOOD DATA

let foods = [
    {   name:"Classic Burger",
        category:"Burger",
        price:199,
        image:"images/foods/burger.jpg" },

    {   name:"Cheese Pizza",
        category:"Pizza",
        price:349,
        image:"images/foods/pizza.jpg" },

    {   name:"Chicken Biryani",
        category:"Biryani",
        price:299,
        image:"images/foods/biryani.jpg" },

    {   name:"Chocolate Cake",
        category:"Dessert",
        price:149,
        image:"images/foods/cake.jpg" },

    {   name:"Veg Burger",
        category:"Burger",
        price:179,
        image:"images/foods/veg-burger.jpg" },

    {   name:"Farmhouse Pizza",
        category:"Pizza",
        price:399,
        image:"images/foods/farmhouse-pizza.jpg" }
];

// DISPLAY FOODS

function displayFoods(foodList){
    let menuGrid = document.getElementById("menuGrid");
    let cards = "";

    for(let i = 0; i < foodList.length; i++){
        cards +=
          `<div class="menu-card">
            <img src="${foodList[i].image}" alt="${foodList[i].name}">
            <div class="menu-content">
                <h3>${foodList[i].name}</h3>
                <p>Category: ${foodList[i].category} </p>

                <div class="food-price">
                    ₹${foodList[i].price}
                </div>
            </div>
          </div>`;
    }

    menuGrid.innerHTML = cards;
}

// SHOW ALL

function showAllFoods(){
    displayFoods(foods);
}

// FILTER CATEGORY

function filterCategory(category){
    let filteredFoods = [];

    for(let i = 0; i < foods.length; i++){
        if( foods[i].category === category){
            filteredFoods.push(foods[i]);
        }
    }

    displayFoods(filteredFoods);
}

// INITIAL LOAD

showAllFoods();
