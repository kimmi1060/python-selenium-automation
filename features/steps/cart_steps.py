from behave import given, when, then

@given('Open target main page')
def open_main_page(context):
    context.app.main_page.open_main_page()

@when('Search for {product}')
def search_product(context, product):
    context.app.header.search_product(product)

@when('Add the product to cart')
def add_product_to_cart(context):
    context.app.search_results_page.add_to_cart()

@when('Click on Cart icon')
def click_cart_icon(context):
    context.app.cart_page.click_cart_icon()

@then('Verify product is in the cart')
def verify_product_in_cart(context):
    context.app.cart_page.verify_product_in_cart()
