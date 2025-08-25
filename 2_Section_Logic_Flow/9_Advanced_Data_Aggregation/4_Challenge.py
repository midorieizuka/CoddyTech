"""
You are given two lists: temperatures containing daily temperatures in Fahrenheit, and humidity containing daily humidity percentages.
Your task is to write a program that:

Finds the highest and lowest temperature from the temperatures list using max() and min().
Finds the highest and lowest humidity from the humidity list using max() and min().
Prints the results in a specific format, including units.

Output Format Requirements:

For temperatures, the value should be followed by °F (degree Fahrenheit).
For humidity, the value should be followed by % (percentage sign).
Each result should be printed on a new line, clearly labeled.

Expected Output Example:

Highest temperature: 80°F
Lowest temperature: 65°F
Highest humidity: 70%
Lowest humidity: 50%
"""
temperatures = [72, 68, 75, 80, 65, 70, 78]
humidity = [60, 55, 65, 70, 50, 58, 62]

# TODO: Find the highest and lowest temperature from the 'temperatures' list using max() and min()
lowest_temp = min(temperatures)
highest_temp = max(temperatures)

# TODO: Find the highest and lowest humidity from the 'humidity' list using max() and min()
lowest_hum = min(humidity)
highest_hum = max(humidity)

# TODO: Print the highest temperature. Make sure to include the degree Fahrenheit symbol (°F).
# Example format: "Highest temperature: 80°F"
print(f"Highest temperature: {highest_temp}°F")

# TODO: Print the lowest temperature. Use the same format.
# Example format: "Lowest temperature: 65°F"
print(f"Lowest temperature: {lowest_temp}°F")

# TODO: Print the highest humidity. Make sure to include the percentage symbol (%).
# Example format: "Highest humidity: 70%"
print(f"Highest humidity: {highest_hum}%")

# TODO: Print the lowest humidity. Use the same format.
# Example format: "Lowest humidity: 50%"
print(f"Lowest humidity: {lowest_hum}%")