# CORMAC QUESTION : CHAT GPT SOLUTION

room_prices = {
    'new_york': {'monday': 200, 'tuesday': 180, 'wednesday': 220, 'thursday': 190, 'friday': 200, 'saturday': 210, 'sunday': 170},
    'los_angeles': {'monday': 180, 'tuesday': 170, 'wednesday': 200, 'thursday': 180, 'friday': 190, 'saturday': 200, 'sunday': 160},
    'chicago': {'monday': 190, 'tuesday': 160, 'wednesday': 210, 'thursday': 170, 'friday': 180, 'saturday': 220, 'sunday': 150}
}

# Set dictionary to track prices
day_prices = {}

# Loop through the room_prices dictionary to populate day_prices
for city, prices in room_prices.items():  # Correct: use room_prices.items() here
    for day, price in prices.items():  # Correct: use prices.items() here
        if day in day_prices:
            day_prices[day].append(price)
        else:
            day_prices[day] = [price]

# Calculate the average price and store in tuples
avg_day_prices = [(day, sum(prices) / len(prices)) for day, prices in day_prices.items()]

print(avg_day_prices)
