$(document).ready(function () {
    // Notification element for AJAX success messages
    const successMessage = $("#jq-notification");

    // Handle click event for adding product to cart
    $(document).on("click", ".add-to-cart", function (e) {
        e.preventDefault(); // Prevent default action

        const goodsInCartCount = $("#goods-in-cart-count");
        let cartCount = parseInt(goodsInCartCount.text() || 0);

        // Get product ID from the data attribute
        const productId = $(this).data("product-id");

        // Get the URL for adding to the cart
        const addToCartUrl = $(this).attr("href");

        // Make AJAX POST request
        $.ajax({
            type: "POST",
            url: addToCartUrl,
            data: {
                product_id: productId,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },
            success: function (data) {
                // Display success message
                showNotification(data.message);

                // Update cart count
                updateCartCount(cartCount + 1);

                // Update cart items container with new HTML
                updateCartItems(data.cart_items_html);
            },
            error: function () {
                console.log("Error adding product to the cart.");
            },
        });
    });

    // Handle click event for removing product from the cart
    $(document).on("click", ".remove-from-cart", function (e) {
        e.preventDefault(); // Prevent default action

        const goodsInCartCount = $("#goods-in-cart-count");
        let cartCount = parseInt(goodsInCartCount.text() || 0);

        // Get cart ID and removal URL
        const cartId = $(this).data("cart-id");
        const removeFromCartUrl = $(this).attr("href");

        // Make AJAX POST request
        $.ajax({
            type: "POST",
            url: removeFromCartUrl,
            data: {
                cart_id: cartId,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },
            success: function (data) {
                // Display success message
                showNotification(data.message);

                // Update cart count after item removal
                updateCartCount(cartCount - data.quantity_deleted);

                // Update cart items container
                updateCartItems(data.cart_items_html);
            },
            error: function () {
                console.log("Error removing product from the cart.");
            },
        });
    });

    // Handle increment of product quantity
    $(document).on("click", ".increment", function () {
        const url = $(this).data("cart-change-url");
        const cartId = $(this).data("cart-id");
        const $input = $(this).closest('.input-group').find('.number');
        const currentValue = parseInt($input.val());

        $input.val(currentValue + 1);
        updateCart(cartId, currentValue + 1, 1, url);
    });

    // Handle decrement of product quantity
    $(document).on("click", ".decrement", function () {
        const url = $(this).data("cart-change-url");
        const cartId = $(this).data("cart-id");
        const $input = $(this).closest('.input-group').find('.number');
        const currentValue = parseInt($input.val());

        if (currentValue > 1) {
            $input.val(currentValue - 1);
            updateCart(cartId, currentValue - 1, -1, url);
        }
    });

    // Function to handle updating cart with new data
    function updateCart(cartId, quantity, change, url) {
        $.ajax({
            type: "POST",
            url: url,
            data: {
                cart_id: cartId,
                quantity: quantity,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },
            success: function (data) {
                showNotification(data.message);

                const goodsInCartCount = $("#goods-in-cart-count");
                let cartCount = parseInt(goodsInCartCount.text() || 0);
                updateCartCount(cartCount + change);
                updateCartItems(data.cart_items_html);
            },
            error: function () {
                console.log("Error updating cart.");
            },
        });
    }

    // Function to show notification message
    function showNotification(message) {
        successMessage.html(message);
        successMessage.fadeIn(400);
        setTimeout(function () {
            successMessage.fadeOut(400);
        }, 7000);
    }

    // Function to update cart item count
    function updateCartCount(newCount) {
        const goodsInCartCount = $("#goods-in-cart-count");
        goodsInCartCount.text(newCount);
    }

    // Function to update the cart items container
    function updateCartItems(cartItemsHtml) {
        const cartItemsContainer = $("#cart-items-container");
        cartItemsContainer.html(cartItemsHtml);
    }

    // Handle cart modal opening
    $('#modalButton').click(function () {
        $('#exampleModal').appendTo('body');
        $('#exampleModal').modal('show');
    });

    // Close the cart modal
    $('#exampleModal .btn-close').click(function () {
        $('#exampleModal').modal('hide');
    });

    // Handle delivery method selection
    $("input[name='requires_delivery']").change(function () {
        const selectedValue = $(this).val();
        if (selectedValue === "1") {
            $("#deliveryAddressField").show();
        } else {
            $("#deliveryAddressField").hide();
        }
    });

    // Format phone number input (xxx) xxx-xxxx
    document.getElementById('id_phone_number').addEventListener('input', function (e) {
        const x = e.target.value.replace(/\D/g, '').match(/(\d{0,3})(\d{0,3})(\d{0,4})/);
        e.target.value = !x[2] ? x[1] : '(' + x[1] + ') ' + x[2] + (x[3] ? '-' + x[3] : '');
    });

    // Validate phone number on form submission
    $('#create_order_form').on('submit', function (event) {
        const phoneNumber = $('#id_phone_number').val();
        const regex = /^\(\d{3}\) \d{3}-\d{4}$/;

        if (!regex.test(phoneNumber)) {
            $('#phone_number_error').show();
            event.preventDefault();
        } else {
            $('#phone_number_error').hide();

            // Clean the phone number before submission
            const cleanedPhoneNumber = phoneNumber.replace(/[()\-\s]/g, '');
            $('#id_phone_number').val(cleanedPhoneNumber);
        }
    });

    // Auto-close Django notification
    const notification = $('#notification');
    if (notification.length > 0) {
        setTimeout(function () {
            notification.alert('close');
        }, 7000);
    }
});