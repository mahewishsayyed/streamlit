import streamlit as st

# Define the categories and their items
food_categories = {
    'Desserts': ['Ice Cream', 'Cake', 'Brownie', 'Cupcake'],
    'Chinese': ['Noodles', 'Spring Rolls', 'Dumplings', 'Fried Rice'],
    'Meals': ['Burger', 'Pizza', 'Pasta', 'Sandwich'],
    'Dinners': ['Steak', 'Chicken Alfredo', 'Seafood Pasta', 'Grilled Salmon'],
    'Drinks': ['Soda', 'Coffee', 'Tea', 'Juice'],
    'Cakes': ['Chocolate Cake', 'Cheesecake', 'Red Velvet Cake', 'Carrot Cake'],
    'Tea': ['Green Tea', 'Black Tea', 'Herbal Tea', 'Oolong Tea']
}

def display_items(category):
    st.subheader(f"{category} Menu")
    items = food_categories.get(category, [])
    for item in items:
        st.write(f"- {item}")

def main():
    st.title("Food Delivery App")
    
    st.sidebar.title("Select a Category")
    category = st.sidebar.selectbox("Choose a food category", list(food_categories.keys()))

    st.sidebar.write(f"You selected: {category}")

    display_items(category)

if __name__ == "__main__":
    main()
