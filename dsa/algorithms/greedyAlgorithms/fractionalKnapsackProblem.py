def fractional_knapsack(items, capacity):
    # Calculate the value-to-weight ratio for each item
    for item in items:
        item["ratio"] = item["value"] / item["weight"]

    # Sort items by the value-to-weight ratio in descending order
    items.sort(key=lambda x: x["ratio"], reverse=True)

    max_value = 0  # Maximum value in the knapsack
    knapsack = []  # Items selected for the knapsack

    for item in items:
        if capacity == 0:
            break

        if item["weight"] <= capacity:
            max_value += item["value"]
            capacity -= item["weight"]
            knapsack.append(item)
        else:
            fraction = capacity / item["weight"]
            max_value += fraction * item["value"]
            capacity = 0
            knapsack.append({"item": item["item"], "weight": item["weight"] * fraction, "value": item["value"] * fraction})

    return max_value, knapsack

# Example usage
items = [
    {"item": "item1", "value": 60, "weight": 10},
    {"item": "item2", "value": 100, "weight": 20},
    {"item": "item3", "value": 120, "weight": 30},
]

capacity = 50

max_value, selected_items = fractional_knapsack(items, capacity)
print("Maximum value:", max_value)
print("Selected items:")
for item in selected_items:
    print(f"Item: {item['item']}, Weight: {item['weight']}, Value: {item['value']}")
