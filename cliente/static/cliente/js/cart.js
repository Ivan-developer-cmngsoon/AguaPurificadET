document.addEventListener('DOMContentLoaded', () => {
    const cartItemsContainer = document.getElementById('cartItems');

    // Función para cargar los items del carrito desde localStorage
    function loadCartItems() {
        return JSON.parse(localStorage.getItem('cartItems')) || [];
    }

    // Función para guardar los items del carrito en localStorage
    function saveCartItems(items) {
        localStorage.setItem('cartItems', JSON.stringify(items));
    }

    // Función para renderizar los items del carrito
    function renderCartItems() {
        const cartItems = loadCartItems();
        cartItemsContainer.innerHTML = '';
        cartItems.forEach(item => {
            const itemElement = document.createElement('div');
            itemElement.classList.add('cart-item', 'mb-2');
            itemElement.innerHTML = `
                <div class="d-flex justify-content-between">
                    <span>${item.name} (${item.quantity})</span>
                    <span>$${item.price * item.quantity}</span>
                    <button class="btn btn-danger btn-sm remove-from-cart" data-id="${item.id}">Eliminar</button>
                </div>
            `;
            cartItemsContainer.appendChild(itemElement);
        });
    }

    // Función para añadir un item al carrito
    function addToCart(product) {
        const cartItems = loadCartItems();
        const existingItem = cartItems.find(item => item.id === product.id);
        if (existingItem) {
            existingItem.quantity += 1;
        } else {
            cartItems.push(product);
        }
        saveCartItems(cartItems);
        renderCartItems();
        $('#cartModal').modal('show'); // Mostrar el modal del carrito
    }

    // Función para eliminar un item del carrito
    function removeFromCart(productId) {
        let cartItems = loadCartItems();
        cartItems = cartItems.filter(item => item.id !== productId);
        saveCartItems(cartItems);
        renderCartItems();
    }

    // Llama a la función para renderizar los items del carrito al cargar la página
    renderCartItems();

    // Event listener para añadir items al carrito
    document.querySelectorAll('.add-to-cart').forEach(button => {
        button.addEventListener('click', function() {
            const product = {
                id: parseInt(this.dataset.id), // Asegúrate de convertir el id a entero
                name: this.dataset.name,
                price: parseFloat(this.dataset.price),
                quantity: 1
            };
            addToCart(product);
        });
    });

    // Event listener para eliminar items del carrito
    cartItemsContainer.addEventListener('click', function(event) {
        if (event.target.classList.contains('remove-from-cart')) {
            const productId = parseInt(event.target.dataset.id); // Asegúrate de convertir el id a entero
            removeFromCart(productId);
        }
    });
});

function clearCart() {
    localStorage.removeItem('cartItems');
    renderCartItems();
}

function renderCheckoutCartItems(cartItems) {
    const cartTableBody = document.getElementById('checkoutCartItems');
    cartTableBody.innerHTML = '';
    cartItems.forEach(item => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${item.name}</td>
            <td>${item.quantity}</td>
            <td>$${item.price}</td>
            <td>$${item.price * item.quantity}</td>
        `;
        cartTableBody.appendChild(row);
    });
}