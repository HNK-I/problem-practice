
'''
def categorize_age(age):
    """Takes an integer age and returns the corresponding category string."""
    if age < 0:
        return "Age cannot be negative."
    elif age < 13:
        return "child"
    elif age < 19:
        return "teenager"
    elif age < 60:
        return "adult"
    else:
        return "Senior"

def main():
    """Handles user input and prints the age category."""
    try:
        age = int(input("what is your age? "))
        category = categorize_age(age)
        print(f"A person aged {age} is a: {category}")

    except ValueError:
        print("Invalid input. Please enter a whole number for your age.")

# This standard Python construct ensures that main() is called only when
# the script is executed directly.
if __name__ == "__main__":
    main()
    
'''

'''

# function gets the age independently
def ticketSellAge(age):
    if age>=18:
        return 18
    else :
        return 12
    
# function gets the day independently    
def is_discount_day(day):
    """Checks if the given day qualifies for a discount. Returns True or False."""
    # .lower() makes the check case-insensitive (e.g., "Wednesday" also works)
    if day.lower() == "wednesday":
        return True
    return False

# main function with all the logic
def main():
    try:
        age = int(input("what is your age?\n"))
        price = ticketSellAge(age)
        
        # The str() call is redundant as input() already returns a string.
        day = input("what is day today?\n")
        
        # Corrected the function name and using the improved version.
        has_discount = is_discount_day(day)
            
        if has_discount:
            print(f"the ticket price will be {price-2}")
        else :
            print(f"the price will be {price}")
            
    except ValueError:
        print("Invalid input. Please enter a whole number for your age.")
        
if __name__ == "__main__":
    main()
'''

def gradeCalculator(grade):
    if grade < 0 or grade>100 :
        print("input valid number")
    elif grade<100 and grade>90:
        print("A")
    elif grade<89 and grade>80:
        print("B")
    elif grade<79 and grade>70:
        print("C")
    elif grade<100 and grade>90:
        print("D")
    else :
        print("fail")
        
    
    