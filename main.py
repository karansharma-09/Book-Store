import sqlite3
def process_purchase():
    Mybookstore = sqlite3.connect("bookstore.db")
    curstore = Mybookstore.cursor()

    total_cost = 0.0
    while True:

        print("====Bookstore Management System ====")
        input_title = input("Enter the title of the book:").strip()
        curstore.execute('''SELECT * FROM books WHERE LOWER(title) = LOWER(?)''',(input_title,))
        result = curstore.fetchone()

        if result:
            print(f"{result[0]},'{result[1]}',{result[2]},{result[3]}")
            price = result[3]
            try:
                copies = int(input("Enter no. of copies:"))
                if copies>0:
                    total_cost += price*copies
                else:
                    print("Quantity must be greater than 0.")
                    continue
            except ValueError:
                print("Invalid quantity")
                continue
        else:
            print(f"Book '{input_title}' not found in database.")
            continue
        add_more = input("Add more books(Y/N)").strip().upper()
        print()
        
        if add_more == 'N':
            break
    
    print(f"Total cost is {total_cost}")
    Mybookstore.close()
if __name__=="__main__":
    process_purchase()
