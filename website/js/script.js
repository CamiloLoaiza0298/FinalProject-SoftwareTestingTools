// Variables
const prodContProd = document.querySelector("#products");
const prodContIndex = document.querySelector("#prod-index");
const prodContCart = document.querySelector("#prod-cart");

const prod1 = {
  imgSrc: "media/dino.jpg",
  name: "Articulated T-Rex",
  price: 10,
  description: "Printed in 3D, this T-Rex model features movable joints for added realism and playability.",
};
const prod2 = {
  imgSrc: "media/bulbasaur.jpg",
  name: "Bulbasaur Plant Pot",
  price: 25,
  description: "Printed in 3D, this Bulbasaur-themed plant pot adds a touch of greenery and charm to any space.",
};
const prod3 = {
  imgSrc: "media/darthvader.jpg",
  name: "Darth Vader Can Holder",
  price: 30,
  description: "Printed in 3D, this Darth Vader can holder keeps your drinks cool while showcasing your love for Star Wars.",
};

const arr = [
  prod1,
  prod2,
  prod3,
  prod1,
  prod2,
  prod3,
  prod1,
  prod2,
  prod3,
  prod1,
  prod2,
  prod3,
];

// Function to display products on products.html
const displayProducts = () => {
  for (let i = 0; i < arr.length; i++) {
    // Get values
    let imgSrc = arr[i].imgSrc;
    let name = arr[i].name;
    let price = arr[i].price;
    const check = "prod";
    createProd(imgSrc, name, price, check);
  }
};

// Function to display products on index.html
const displayProdIndex = () => {
  for (let i = 0; i < 3; i++) {
    // Get values
    let imgSrc = arr[i].imgSrc;
    let name = arr[i].name;
    let price = arr[i].price;
    const check = "index";
    createProd(imgSrc, name, price, check);
  }
};

const displayProdCart = () => {
  for (let i = 0; i < 2; i++) {
    // Get values
    let imgSrc = arr[i].imgSrc;
    let name = arr[i].name;
    let price = arr[i].price;
    createCartProd(imgSrc, name, price);
  }
};

// Function to create elements
const createProd = (imgSrc, name, price, check) => {
  let divProd = document.createElement("div");
  let imgProd = document.createElement("img");
  let nameProd = document.createElement("h4");
  let priceProd = document.createElement("p");
  let buttonProd = document.createElement("button");
  let divOverlay = document.createElement("div");
  let prodDesc = document.createElement("p");
  let buttonMore = document.createElement("button");
  buttonMore.addEventListener("click", () => {
    window.location.href = "products.html";
  });

  // Set values on elements
  imgProd.src = imgSrc;
  nameProd.innerText = name;
  priceProd.innerText = "$" + price;
  buttonProd.innerText = "Add to cart";
  prodDesc.innerText = arr.find(p => p.name === name).description;
  buttonMore.innerText = "More info";

  // Add classes on elements
  priceProd.className = "price";
  buttonProd.className = "atc-btn";
  buttonMore.className = "rm-btn";
  divOverlay.className = "overlay";
  prodDesc.className = "description";
  divProd.className = "img-products";

  // Attach add-to-cart behavior
  buttonProd.dataset.name = name;
  buttonProd.dataset.price = price;
  buttonProd.dataset.img = imgSrc;
  buttonProd.addEventListener("click", () => {
    addToCart({ name, price, imgSrc });
  });

  // Add elements to div
  divOverlay.appendChild(prodDesc);
  divOverlay.appendChild(buttonMore);
  divOverlay.appendChild(buttonProd);
  divProd.appendChild(imgProd);
  divProd.appendChild(nameProd);
  divProd.appendChild(priceProd);
  divProd.appendChild(divOverlay);
  if (check === "prod") {
    prodContProd.appendChild(divProd);
  } else if (check === "index") {
    prodContIndex.appendChild(divProd);
  }
};

// --- Cart helpers ---
const getCart = () => {
  try {
    const raw = localStorage.getItem("cart");
    return raw ? JSON.parse(raw) : [];
  } catch (e) {
    return [];
  }
};

const saveCart = (cart) => {
  localStorage.setItem("cart", JSON.stringify(cart));
  updateCartCount();
};

const updateCartCount = () => {
  const cart = getCart();
  const total = cart.reduce((s, item) => s + (item.qty || 1), 0);
  const el = document.getElementById("cart-count");
  if (el) el.innerText = total;
};

const addToCart = (product) => {
  const cart = getCart();
  // try to find same product by name
  const idx = cart.findIndex((p) => p.name === product.name);
  if (idx > -1) {
    cart[idx].qty = (cart[idx].qty || 1) + 1;
  } else {
    cart.push({ ...product, qty: 1 });
  }
  saveCart(cart);
};

// Initialize cart count when DOM is ready
document.addEventListener("DOMContentLoaded", () => {
  updateCartCount();
});

const createCartProd = (imgSrc, name, price) => {
  let divProd = document.createElement("div");
  let imgProd = document.createElement("img");
  let descProd = document.createElement("div");
  let nameProd = document.createElement("h4");
  let priceProd = document.createElement("p");
  let amountDiv = document.createElement("div");
  let plusIcon = document.createElement("i");
  let minusIcon = document.createElement("i");
  let amount = document.createElement("p");
  let icons = document.createElement("div");
  let closeIcon = document.createElement("p");
  let favoriteIcon = document.createElement("i");

  // Set values on elements
  imgProd.src = imgSrc;
  nameProd.innerText = name;
  priceProd.innerText = "$" + price;
  amount.innerText = " 1 ";

  divProd.className = "cart-prod";
  descProd.className = "desc-prod";
  amountDiv.className = "amount-div";
  plusIcon.className = "fa-regular fa-square-plus";
  minusIcon.className = "fa-regular fa-square-minus";
  icons.className = "cart-icons";
  closeIcon.className = "fa-regular fa-rectangle-xmark";
  favoriteIcon.className = "fa-solid fa-heart";

  // Add elements to div
  divProd.appendChild(imgProd);
  descProd.appendChild(nameProd);
  descProd.appendChild(priceProd);
  amountDiv.appendChild(minusIcon);
  amountDiv.appendChild(amount);
  amountDiv.appendChild(plusIcon);
  descProd.appendChild(amountDiv);
  divProd.appendChild(descProd);
  icons.appendChild(closeIcon);
  icons.appendChild(favoriteIcon);
  divProd.appendChild(icons);
  prodContCart.appendChild(divProd);
};

// Function for mobile menu
const hamburgerMenu = () => {
  var x = document.getElementById("myLinks");
  if (x.style.display === "block") {
    x.style.display = "none";
  } else {
    x.style.display = "block";
  }
};


// Password toggle and validation for register.html
(function(){
        const toggle = document.getElementById('toggle-pass');
        if(toggle){
          toggle.addEventListener('change', function(){
            const p = document.getElementById('password');
            const c = document.getElementById('confirm-password');
            const type = this.checked ? 'text' : 'password';
            if(p) p.type = type;
            if(c) c.type = type;
          });
        }

        const form = document.getElementById('register-form');
        if(form){
          form.addEventListener('submit', function(e){
            const p = document.getElementById('password').value;
            const c = document.getElementById('confirm-password').value;
            const msg = document.getElementById('register-msg');
            if(p !== c){
              e.preventDefault();
              if(msg) msg.textContent = 'Passwords do not match.';
            }
          });
        }
      })();