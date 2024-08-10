import streamlit as st

# Define categories and their items
product_categories = {
    'Electronics': [
        {'name': 'Smartphone', 'price': 699},
        {'name': 'Laptop', 'price': 999},
        {'name': 'Headphones', 'price': 199}
    ],
    'Clothing': [
        {'name': 'T-Shirt', 'price': 25},
        {'name': 'Jeans', 'price': 50},
        {'name': 'Jacket', 'price': 120}
    ],
    'Home & Kitchen': [
        {'name': 'Blender', 'price': 89},
        {'name': 'Toaster', 'price': 30},
        {'name': 'Coffee Maker', 'price': 65}
    ]
}

def display_products(category):
    st.subheader(f"{category} Products")
    products = product_categories.get(category, [])
    for product in products:
        st.write(f"- {product['name']} - ${product['price']}")
        if st.button(f"Add {product['name']} to Cart"):
            cart[product['name']] = cart.get(product['name'], 0) + 1
            st.success(f"Added {product['name']} to cart")

def show_cart():
    st.subheader("Shopping Cart")
    if cart:
        for item, quantity in cart.items():
            st.write(f"{item}: {quantity}")
    else:
        st.write("Your cart is empty.")

# Initialize the cart as a session state variable
if 'cart' not in st.session_state:
    st.session_state.cart = {}

cart = st.session_state.cart

def main():
    st.title("Shopping App")

    st.sidebar.title("Select a Category")
    category = st.sidebar.selectbox("Choose a product category", list(product_categories.keys()))

    if st.sidebar.button("Show Cart"):
        show_cart()
    
    display_products(category)

if __name__ == "__main__":
    main()
