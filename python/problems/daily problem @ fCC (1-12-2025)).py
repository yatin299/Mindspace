# Given a distance in miles as a number, return the equivalent distance in kilometers.

# The input will always be a non-negative number.
# 1 mile equals 1.60934 kilometers.
# Round the result to two decimal places.
# Remove unnecessary trailing zeros from the rounded result.
# vice versa and in validation (coming soon)

miles = float(input("Please enter your miles to convert to km : "))

def convert_to_km(miles):
    miles = miles * 1.60934
    miles = round(miles, 2)
    return miles
km = convert_to_km(miles)
print (f"Km = {km}")
