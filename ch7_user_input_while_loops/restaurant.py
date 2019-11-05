diners = input("How many people are in your dinner group? ")
diners = int(diners)

if diners > 8:
    print(f"Please take a seat for a few moments"
          " while we find you a table for {diners}")
else:
    print(f"Your table for {diners} is now ready")
