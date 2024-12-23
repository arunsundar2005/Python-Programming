book_price = int(input("Enter the book price"))
status = input("Are you a facuty [y/n]").lower()
faculty = True if status == 'y' else False

if faculty:
    price = book_price - (0.15*book_price)
else:
    price = book_price - (0.10 * book_price)

print(f"The finalized book price after discount is ruppes {int(price)}")