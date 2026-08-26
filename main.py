import pandas as pd



products = pd.read_csv("products.csv")

slow_products = products[products['price'] < 5]
print("product sales ")

print(products)
products["inventory"] = products["inventory"].fillna(0)


# slow sales and hight investment products
slow_products = products[
    (products["sales"] < 5) &
    (products["inventory"] > 10)
]


print(slow_products)

#predicting the price of products using linear regression
products["price_difference"] = (
    (products["price"] - products["competitor_price"])
    / products["competitor_price"]
) * 100
## create a rule for the predicted price difference
def predict_sales(product):

    if (
        product["sales"] < 5
        and product["inventory"] > 10
        and product["price"] > product["competitor_price"]
    ):
        return "HIGH RISK OF SLOW SALES"

    elif product["sales"] < 5:
        return "MEDIUM RISK"

    else:
        return "LOW RISK"

for index, product in products.iterrows():

    prediction = predict_sales(product)

    print(product["product"])
    print("Prediction:", prediction)
    print()