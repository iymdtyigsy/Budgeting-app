from expense import Expense 


def main():
    print(f"Running Expense Tracker!")
    expense_file_path = "expense.csv"

    #Get use input for expense.
    #expense = get_user_expense()

    #Write their expense in a file.
    #save_expense_file(expense, expense_file_path)

    #Read file and summrize expenses.
    summarize_expenses(expense_file_path)
    

def get_user_expense():
    print(f"getting user expense")
    expense_name = input("Enter expense name:")
    expense_amount = float(input("Enter the amount of your expense: "))
    expense_catergories = [
        "food", 
        "Home", 
        "Work", 
        "Fun", 
        "Misc",
    ]

    while True:
        print("Select a catergory: ")
        for i, catergroy_name in enumerate(expense_catergories):
            print(f" {i + 1}. {catergroy_name}")
        
        value_range = f"[1- {len(expense_catergories)}]"
        selected_index = int(input(f"Enter a catergory number {value_range} : ")) - 1 
        
        if selected_index in range(len(expense_catergories)):
            selected_catergory = expense_catergories[selected_index]
            new_expense = Expense(
                name=expense_name, 
                catergory=selected_catergory, 
                amount=expense_amount
                )
            return new_expense
        else:
            print("Invalid Catergory. Please try again!")
            
def save_expense_file(expense: Expense, expense_file_path):
    print(f"saving user expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(F"{expense.name},{expense.amount},{expense.catergory}\n")

def summarize_expenses(expense_file_path):
    print(f"summarizing user expense")
    expenses: list[Expense] = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_amount, expense_catergory = line.strip().split(",")
            line_expense = Expense(
                name=expense_name, 
                amount=float(expense_amount), 
                catergory=expense_catergory
                )
            expenses.append(line_expense)

    amount_by_catergory = {}
    for expense in expenses:
        key = expense.catergory
        if key in amount_by_catergory:
            amount_by_catergory[key] += expense.amount
        else:
            amount_by_catergory[key] = expense.amount
    
    print("Expenses by catergories :")
    for key, amount in amount_by_catergory.items():
        print(f"  {key}: ${amount:.2f}")

if __name__ == "__main__":
    main()

