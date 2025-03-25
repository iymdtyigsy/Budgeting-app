def main():
    print(f"Running Expense Tracker!")

    #Get use input for expense.
    get_user_expense()

    #Write their expense in a file.
    save_expense_file()

    #Read file and summrize expenses.
    summarize_expenses()
    

def get_user_expense():
    print(f"getting user expense")
    expense_name = input("Enter expense name:")
    expense_amount = float(input("Enter the amount of your expense: "))
    print(f"You've entered {expense_name}, {expense_amount}")

    expense_catergory = [
        "food", 
        "Home", 
        "Work", 
        "Fun", 
        "Misc",
    ]

    while True:
        print("Select a catergory: ")
        for i, catergroy_name in enumerate(expense_catergory):
            print(f" {i + 1}. {catergroy_name}")
        
        value_range = f"[1- {len(expense_catergory)}]"
        selected_index = int(input(f"Enter a catergory number {value_range} : ")) - 1 
        

        if selected_index in range(len(expense_catergory)):
            break
        else:
            print("Invalid Catergory. Please try again!")
            
def save_expense_file():
    print(f"saving user expense")
    input("Enter expense name: ")

def summarize_expenses():
    print(f"summarizing user expense")
    input("Enter expense name: ")

if __name__ == "__main__":
    main()

