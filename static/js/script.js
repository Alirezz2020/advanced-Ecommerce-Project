// Navbar Scroll Effect
document.addEventListener('scroll', () => {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});
// Add a smooth scroll effect for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});
// Optionally, you can add JavaScript for any further interactivity if needed. Here’s an example for smooth focus transitions:
document.querySelector('.search-input').addEventListener('focus', function () {
    this.style.width = '300px'; // Expand input when focused
});

document.querySelector('.search-input').addEventListener('blur', function () {
    this.style.width = '250px'; // Shrink input when unfocused
});
document.addEventListener('DOMContentLoaded', function () {
    // Smooth Dropdown Toggle
    const dropdownMenu = document.querySelector('.navbar-nav .dropdown-menu');
    const dropdownToggle = document.querySelector('.navbar-nav .dropdown-toggle');

    dropdownToggle.addEventListener('click', function (e) {
        e.preventDefault();

        if (dropdownMenu.classList.contains('show')) {
            dropdownMenu.classList.remove('show');
        } else {
            dropdownMenu.classList.add('show');
        }
    });

    // Click outside to close the dropdown
    document.addEventListener('click', function (e) {
        if (!dropdownMenu.contains(e.target) && !dropdownToggle.contains(e.target)) {
            dropdownMenu.classList.remove('show');
        }
    });
});
document.addEventListener('DOMContentLoaded', function () {
    // Get references to the sidebar and toggle button
    const sidebar = document.getElementById('sidebar');
    const toggleButton = document.querySelector('.navbar-toggler');

    // Toggle the sidebar on button click
    toggleButton.addEventListener('click', function () {
        sidebar.classList.toggle('open');
    });

    // Close sidebar when clicking outside of it
    document.addEventListener('click', function (e) {
        if (!sidebar.contains(e.target) && !toggleButton.contains(e.target)) {
            sidebar.classList.remove('open');
        }
    });
});
// Smooth scrolling for Explore buttons
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

    // Ensure Bootstrap handles navbar toggling properly
    document.addEventListener('DOMContentLoaded', () => {
    const navbarToggler = document.querySelector('.navbar-toggler');
    const navbarCollapse = document.querySelector('#navbarNav');

    navbarToggler.addEventListener('click', () => {
    if (navbarCollapse.classList.contains('show')) {
    navbarCollapse.classList.remove('show');
} else {
    navbarCollapse.classList.add('show');
}
});
});

// Highlight search terms in results
document.addEventListener("DOMContentLoaded", function () {
    const searchQuery = new URLSearchParams(window.location.search).get("q");
    if (searchQuery) {
        const regex = new RegExp(searchQuery, "gi");
        document.querySelectorAll(".card-title").forEach((title) => {
            title.innerHTML = title.textContent.replace(
                regex,
                (match) => `<span style="background-color: yellow;">${match}</span>`
            );
        });
    }
});
// JavaScript for quick hover effect (optional)
document.querySelectorAll('.product-card').forEach(card => {
    card.addEventListener('mouseover', function() {
        const button = card.querySelector('.quick-view-btn');
        if (button) {
            button.style.display = 'block';
        }
    });

    card.addEventListener('mouseout', function() {
        const button = card.querySelector('.quick-view-btn');
        if (button) {
            button.style.display = 'none';
        }
    });
});
document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".remove-item").forEach((button) => {
        button.addEventListener("click", function () {
            let itemId = this.dataset.id;
            fetch(`/cart/remove/${itemId}/`, {
                method: "POST",
                headers: {
                    "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value
                }
            })
            .then(response => response.json())
            .then(data => {
                alert(data.message);
                location.reload();
            });
        });
    });
});
// static/js/orders.js
document.addEventListener("DOMContentLoaded", function () {
    const orderForm = document.getElementById("order-form");

    orderForm.addEventListener("submit", function (e) {
        e.preventDefault();

        const formData = new FormData(orderForm);
        fetch(orderForm.action, {
            method: "POST",
            body: formData,
            headers: {
                "X-CSRFToken": document.querySelector('[name=csrfmiddlewaretoken]').value
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert("Order created successfully!");
                window.location.href = data.redirect_url;
            } else {
                alert("There was an error creating your order.");
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert("An unexpected error occurred.");
        });
    });
});
// static/js/orders.js
document.addEventListener("DOMContentLoaded", function () {
    const orderForm = document.getElementById("order-form");

    orderForm.addEventListener("submit", function (e) {
        e.preventDefault();

        const formData = new FormData(orderForm);
        fetch(orderForm.action, {
            method: "POST",
            body: formData,
            headers: {
                "X-CSRFToken": document.querySelector('[name=csrfmiddlewaretoken]').value
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert("Order created successfully!");
                window.location.href = data.redirect_url;
            } else {
                alert("There was an error creating your order.");
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert("An unexpected error occurred.");
        });
    });
});
