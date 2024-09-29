def calculate_cost(watts, hours_per_day):
    # Convert watts to kilowatts
    kilowatts = watts / 1000
    
    # Total units (kWh) consumed in 30 days
    total_units = kilowatts * hours_per_day * 30
    
    # Initialize cost
    cost = 0
    
    # Slab rates and limits (based on your bill)
    slab_limits = [19, 20, 38, 39, 10, 181, 180, 362, 361, 94]
    slab_rates = [3.00, 4.50, 6.50, 7.00, 8.00, 3.00, 4.50, 6.50, 7.00, 8.00]
    
    # Calculate the cost based on slabs
    for i in range(len(slab_limits)):
        if total_units > slab_limits[i]:
            cost += slab_limits[i] * slab_rates[i]
            total_units -= slab_limits[i]
        else:
            cost += total_units * slab_rates[i]
            break
    
    return cost

# Input from user
watts = float(input("Enter the power of your device in watts: "))
hours_per_day = float(input("Enter the number of hours the device is used per day: "))

# Calculate cost
cost = calculate_cost(watts, hours_per_day)

print(f"Estimated electricity cost for 30 days: ₹{cost:.2f}")
