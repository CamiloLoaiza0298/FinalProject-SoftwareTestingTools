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
const prod4 = {
  imgSrc: "media/octopus.jpg",
  name: "Articulated Octopus Figurine",
  price: 15,
  description: "Printed in 3D, this octopus figurine features movable tentacles for added realism and playability.",
};
const prod5 = {
  imgSrc: "media/phone.webp",
  name: "Smartphone Mechanical Stand",
  price: 25,
  description: "Printed in 3D, this mechanical smartphone stand offers adjustable angles and a sleek design for optimal viewing.",
};
const prod6 = {
  imgSrc: "media/joycon.webp",
  name: "Nintendo Switch Joy-Con Grip",
  price: 20,
  description: "Printed in 3D, this Nintendo Switch Joy-Con grip offers a comfortable and ergonomic design for extended gaming sessions.",
};
const prod7 = {
  imgSrc: "media/dragon.webp",
  name: "Dragon Pen Holder",
  price: 30,
  description: "Printed in 3D, this dragon pen holder keeps your pens organized while adding a touch of fantasy to your desk.",
};
const prod8 = {
  imgSrc: "media/groot.webp",
  name: "Baby Groot Figurine",
  price: 30,
  description: "Printed in 3D, this Baby Groot figurine adds a touch of charm and whimsy to any space.",
};

const arr = [
  prod1,
  prod2,
  prod3,
  prod4,
  prod5,
  prod6,
  prod7,
  prod8
];

// Function to display products on products.html
// If `query` is provided, filter products by name or description (case-insensitive)
const displayProducts = (query) => {
  if (!prodContProd) return;
  // clear existing
  prodContProd.innerHTML = "";
  const q = query ? query.trim().toLowerCase() : "";
  for (let i = 0; i < arr.length; i++) {
    // filter if query exists
    if (q) {
      const name = arr[i].name.toLowerCase();
      const desc = (arr[i].description || "").toLowerCase();
      if (!name.includes(q) && !desc.includes(q)) continue;
    }
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
  if (prodContIndex) prodContIndex.innerHTML = "";
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
  if (prodContCart) prodContCart.innerHTML = "";
  for (let i = 0; i < 2; i++) {
    // Get values
    let imgSrc = arr[i].imgSrc;
    let name = arr[i].name;
    let price = arr[i].price;
    createCartProd(imgSrc, name, price);
  }
};

// Helper: read URL query parameter
const getQueryParam = (name) => {
  try {
    const params = new URLSearchParams(window.location.search);
    return params.get(name);
  } catch (e) {
    return null;
  }
};

// Setup search input behavior across pages
const setupSearch = () => {
  const searchInput = document.getElementById('search-input');
  if (!searchInput) return;

  const isProductsPage = !!document.getElementById('products');

  const handleInput = (e) => {
    const value = searchInput.value || "";
    const q = value.trim();
    if (isProductsPage) {
      // live filter on products page
      displayProducts(q);
    } else {
      // on other pages only navigate on Enter
      if (e.type === 'keydown' && e.key === 'Enter') {
        const target = 'products.html' + (q ? `?q=${encodeURIComponent(q)}` : '');
        window.location.href = target;
      }
    }
  };

  // Enter key (both pages)
  searchInput.addEventListener('keydown', handleInput);
  // live updates only when on products page
  if (isProductsPage) searchInput.addEventListener('input', handleInput);
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
  setupSearch();
  // If products page and URL has `q`, use it to filter
  if (document.getElementById('products')) {
    const q = getQueryParam('q');
    if (q) {
      const input = document.getElementById('search-input');
      if (input) input.value = q;
      displayProducts(q);
    }
  }
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
  if (toggle) {
    toggle.addEventListener('change', function () {
      const p = document.getElementById('password');
      const c = document.getElementById('confirm-password');
      const type = this.checked ? 'text' : 'password';
      if (p) p.type = type;
      if (c) c.type = type;
    });
  }

  const form = document.getElementById('register-form');
  if (form) {
    form.addEventListener('submit', function (e) {
      const pEl = document.getElementById('password');
      const cEl = document.getElementById('confirm-password');
      const msg = document.getElementById('register-msg');
      const p = pEl ? pEl.value : '';
      const c = cEl ? cEl.value : '';
      // Regex: min 8 chars, at least one uppercase, one lowercase, one digit, one special char
      const regex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,}$/;
      let error = '';
      if (p !== c) {
        error = 'Passwords do not match.';
      } else if (!regex.test(p)) {
        error = 'Password must be at least 8 characters and include uppercase, lowercase, number, and special character.';
      }
      if (error) {
        e.preventDefault();
        if (msg) {
          msg.textContent = error;
          msg.className = 'form-msg error';
        }
      }
    });
  }
})();

// Forgot-password handler (separate from login)
(function(){
  const resetUsers = [
    { username: 'testuser1', code: '1234' },
    { username: 'sampleuser', code: '5678' },
    { username: 'demoaccount', code: '91011' }
  ];

  const toggle = document.getElementById('toggle-pass');
  if (toggle) {
    toggle.addEventListener('change', function () {
      const p = document.getElementById('new-password');
      const c = document.getElementById('confirm-new-password');
      const type = this.checked ? 'text' : 'password';
      if (p) p.type = type;
      if (c) c.type = type;
    });
  }

  const form = document.getElementById('login-form');
  if (form && document.getElementById('code')) {
    form.addEventListener('submit', function(e){
      e.preventDefault();
      const usernameEl = document.getElementById('username');
      const codeEl = document.getElementById('code');
      const passwordEl = document.getElementById('new-password');
      const confirmEl = document.getElementById('confirm-new-password');
      const msg = document.getElementById('login-msg');

      if (msg) { msg.textContent = ''; msg.className = 'form-msg'; }

      const user = usernameEl ? usernameEl.value.trim() : '';
      const code = codeEl ? codeEl.value.trim() : '';
      const pass = passwordEl ? passwordEl.value : '';
      const confirm = confirmEl ? confirmEl.value : '';

      if (!user || !code || !pass || !confirm) {
        if (msg) { msg.textContent = 'Please fill out all fields.'; msg.className = 'form-msg error'; }
        return;
      }

      const entry = resetUsers.find(u => u.username === user && u.code === code);
      if (!entry) {
        if (msg) { msg.textContent = 'Invalid username or code.'; msg.className = 'form-msg error'; }
        return;
      }

      const regex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,}$/;
      if (!regex.test(pass)) {
        if (msg) { msg.textContent = 'Password must be at least 8 characters and include uppercase, lowercase, number, and special character.'; msg.className = 'form-msg error'; }
        return;
      }

      if (pass !== confirm) {
        if (msg) { msg.textContent = 'Passwords do not match.'; msg.className = 'form-msg error'; }
        return;
      }

      if (msg) { msg.textContent = 'Password reset successful. Redirecting to login...'; msg.className = 'form-msg success'; }
      try { localStorage.setItem('loggedInUser', user); } catch (err) {}
      setTimeout(() => { window.location.href = 'login.html'; }, 900);
    });
  }
})();

// Login validation
(function(){
  const validUsers = [
    { username: 'testuser1', password: 'password123' },
    { username: 'sampleuser', password: 'mypassword' },
    { username: 'demoaccount', password: 'demopass' }
  ];

  const form = document.getElementById('login-form');
  if (!form || document.getElementById('code')) return;
  if (form) {
    form.addEventListener('submit', function(e){
      e.preventDefault();
      const usernameEl = document.getElementById('username');
      const passwordEl = document.getElementById('password');
      const msg = document.getElementById('login-msg');
      const user = usernameEl ? usernameEl.value.trim() : '';
      const pass = passwordEl ? passwordEl.value : '';

      // Clear previous message classes/text
      if (msg) {
        msg.textContent = '';
        msg.className = 'form-msg';
      }

      if (!user || !pass) {
        if (msg) {
          msg.textContent = 'Please fill out both username and password.';
          msg.className = 'form-msg error';
        }
        return;
      }

      const match = validUsers.some(u => u.username === user && u.password === pass);
      if (match) {
        if (msg) {
          msg.textContent = 'Login successful. Redirecting...';
          msg.className = 'form-msg success';
        }
        // Save login state (optional) so other pages can check it
        try { localStorage.setItem('loggedInUser', user); } catch (err) {}
        setTimeout(() => { window.location.href = 'index.html'; }, 700);
      } else {
        if (msg) {
          msg.textContent = 'Invalid username or password.';
          msg.className = 'form-msg error';
        }
      }
    });
  }
})();

