$(document).ready(function() {
    var form = $('#form_buying_product');
    console.log(form);

    function cartUpdate(product_id, nmb, is_delete) {

    if (!user_authenticated) {
        $('.basket-items').html('<li><span class="message">Для оформления заказа необходимо авторизоваться</a></span></li>');
        return;
    }
        var data = {};
        data.product_id = product_id;
        data.nmb = nmb;
        var csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;

        if (is_delete) {
            data["is_delete"] = true;
        }

        var url = form.attr("action");

        console.log(data);
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function(data) {
                console.log("OK");
                console.log(data.products_total_quantity);
                if (data.products_total_quantity || data.products_total_quantity === 0) {
                    $('#basket_total_nmb').text("(" + data.products_total_quantity + ")");
                    console.log(data.products);

                    $('.basket-items').html("");
                    if (data.products.length > 0) {
                        $.each(data.products, function(k, v) {
$('.basket-items').append('<li class="js-basket-item">' + v.name +" " + v.nmb + ' шт. по ' + v.reserve_price + ' ₽ ' +
    '<div class="clear-link-wrapper">'+'<a class="delete-item clear-cart-button" href="" data-product_id="' + v.id + '">Очистить</a>' +
    '</div></li>');

                        });
                        $('.basket-items').append('<p></p><li><a class="order-link create-order-button basket-order-link" href="/order/">Оформить заказ ✔</a></li>');
                    } else {
                        $('.basket-items').append('<li><span class="empty-cart-msg">Корзина пуста</span></li>');
                    }
                }
            },
            error: function() {
                console.log("ERROR");
            }
        });
    }

form.on('submit', function(e) {
    e.preventDefault();
    console.log('123');
    var nmb = $('#number').val();

    // Проверка на отрицательное число или ноль
    if (parseInt(nmb) <= 0) {
        alert('Количество товаров в корзине не может быть отрицательным или нулём :)');
        return;
    }

    console.log(nmb);
    var submit_btn = $('#submit_btn');
    var product_id = submit_btn.data('product_id');
    var product_name = submit_btn.data('name');
    var product_price = submit_btn.data('price');
    console.log(product_id);
    console.log(product_name);

    cartUpdate(product_id, nmb, is_delete = false);
});

    $(document).on('click', '.delete-item', function(e) {
        e.preventDefault();
        var product_id = $(this).data("product_id");
        var nmb = 0;
        cartUpdate(product_id, nmb, is_delete = true);
    });

    $(document).on('click', '.order-link', function(e) {
        e.preventDefault();
        var orderUrl = $(this).attr('href');
        window.location.href = orderUrl;
    });
});
