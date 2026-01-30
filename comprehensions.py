#list
tea_prices_inr = {
    "Masala Chai": 40,
    "Green Tea": 50,
    "Lemon Tea": 200
}
tea_prices_usd = {tea:price / 80 for tea, price in tea_prices_inr.items()}
print(tea_prices_usd)
#set
favourite_chais = [
    "Masala Chai", "Green Tea", "Masala Chai",
    "Lemon Tea", "Green Tea", "Elaichi Chai"
]
unique_chai = {chai for chai in favourite_chais }
print(unique_chai)
recipes = {
    "Masala Chai": ["ginger", "cardamom", "clove"],
    "Elaichi Chai": ["cardamom", "milk"],
    "Spicy Chai": ["ginger", "black pepper", "clove"],
}
unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}

print(unique_spices)
#dictionary
tea_prices_inr = {
    "Masala Chai": 40,
    "Green Tea": 50,
    "Lemon Tea": 200
}

tea_prices_usd = {tea:price / 80 for tea, price in tea_prices_inr.items()}
print(tea_prices_usd)
#generator
daily_sales = [5, 10, 12, 7, 3, 8, 9, 15]
total_cups = sum(sale for sale in daily_sales if sale > 5)
print(total_cups)