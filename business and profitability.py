data = [
    ["Rice", 10, 100, 80],
    ["Headphones", 5, 800, 600],
    ["T-Shirt", 10, 300, 180]
]

total_sales = 0
total_cost = 0

print("RETAIL BUSINESS ANALYSIS")
print("------------------------")

for name, qty, price, cost in data:
    sales = qty * price
    profit = qty * (price - cost)

    total_sales += sales
    total_cost += qty * cost

    print(name, "- Profit:", profit)

profit = total_sales - total_cost
margin = profit / total_sales * 100

print("------------------------")
print("Total Sales:", total_sales)
print("Total Cost:", total_cost)
print("Total Profit:", profit)
print("Profit Margin:", round(margin, 2), "%")
print("Analysis Completed!")