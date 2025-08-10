"""
This is the Budget menu when the user successfully logged in
"""
import customtkinter as ctk
from Database import (
    add_budget, 
    check_budget, 
    add_expenses, 
    add_goal,
    get_expense,
    get_user_data,
    delete_expense,
    edit_expense,
    edit_budget,
    edit_goal,
    update_budget_balance,
)

class BudgetMenu(ctk.CTk):
    """Main application window for the Budgeting App."""
    def __init__(self, username):
        """
        Initializes the BudgetMenu window.

        Args:
            username (str): The username of the logged-in user.
        """
        super().__init__()
        self.username = username

        self.title("Budget app")
        self.geometry("844x844")
        self.maxsize(844, 844)
        self.minsize(844, 844)

        self.mainframe = ctk.CTkFrame(
            self,
            fg_color="black",
            width=744,
            height=744
        )
        self.mainframe.pack(fill="both", expand=True)

        self.mainframe_holder = ctk.CTkFrame(
            self.mainframe,
            fg_color="#D9D9D9",
            width=644,
            height=644
        )
        self.mainframe_holder.pack(padx=10, pady=10, fill="both", expand=True)

        self.check_if_budget_exist()

    def delete_current(self):
        """Clears all widgets from the mainframe_holder."""
        for widget in self.mainframe_holder.winfo_children():
            widget.forget()

    def load_create_budget(self):
        """Loads the screen to prompt the user to create a budget."""
        self.delete_current()

        self.create_budget_frame = ctk.CTkFrame(
            self.mainframe_holder,
            fg_color="white",
            width=707,
            height=585
        )
        self.create_budget_frame.pack(padx=10, pady=10, expand=True)
        self.create_budget_frame.pack_propagate(False)

        self.create_budget_label = ctk.CTkLabel(
            self.create_budget_frame,
            text="""
looks like you don't 
have a budget.
Would you like to 
create one? 
        """,
            text_color="black",
            fg_color="white",
            font=("Bold", 55),
            corner_radius=5
        )
        self.create_budget_label.pack(padx=10, pady=5)

        self.yes_btn = ctk.CTkButton(
            self.create_budget_frame,
            text="yes",
            font=("Bold", 20),
            text_color="black",
            width=200,
            height=50,
            fg_color="#D9D9D9",
            command=self.load_set_budget
        )
        self.yes_btn.pack(padx=50, pady=10)

        self.return_btn = ctk.CTkButton(
            self.create_budget_frame,
            text="return",
            font=("Bold", 20),
            text_color="black",
            width=200,
            height=50,
            fg_color="#D9D9D9",
            command=None
        )
        self.return_btn.pack(padx=50, pady=10)

    def load_set_budget(self):
        """Loads the screen for the user to set their budget details."""
        self.delete_current()

        self.set_budget_frame = ctk.CTkFrame(
            self.mainframe_holder,
            fg_color="white",
            width=810,
            height=780
        )
        self.set_budget_frame.pack(padx=10, pady=10, expand=True)
        self.set_budget_frame.pack_propagate(False)

        self.set_budget_label = ctk.CTkLabel(
            self.set_budget_frame,
            text="Create Budget",
            text_color="black",
            fg_color="white",
            font=("Bold", 96)
        )
        self.set_budget_label.pack(padx=10, pady=20)

        self.set_budget_label_2 = ctk.CTkLabel(
            self.set_budget_frame,
            text="(Monthly)",
            text_color="black",
            fg_color="white",
            font=("Bold", 50)
        )
        self.set_budget_label_2.pack(padx=10, pady=20)

        self.budget_name_entry = ctk.CTkEntry(
            self.set_budget_frame,
            placeholder_text="Budget name",
            placeholder_text_color="black",
            text_color="black",
            font=("Bold", 40),
            fg_color="#D9D9D9",
            width=726,
            height=74
        )
        self.budget_name_entry.pack(padx=50, pady=30)

        self.budget_amount_entry = ctk.CTkEntry(
            self.set_budget_frame,
            placeholder_text="Budget amount",
            placeholder_text_color="black",
            text_color="black",
            font=("Bold", 40),
            fg_color="#D9D9D9",
            width=726,
            height=74
        )
        self.budget_amount_entry.pack(padx=50)

        self.budget_income_entry = ctk.CTkEntry(
            self.set_budget_frame,
            placeholder_text="Budget income",
            placeholder_text_color="black",
            text_color="black",
            font=("Bold", 40),
            fg_color="#D9D9D9",
            width=726,
            height=74
        )
        self.budget_income_entry.pack(padx=50, pady=30)

        self.set_budget_status_label = ctk.CTkLabel(
            self.set_budget_frame,
            text="",
            font=("Bold", 20),
            text_color="red"
        )
        self.set_budget_status_label.pack(pady=10)

        self.confirm_btn = ctk.CTkButton(
            self.set_budget_frame,
            text="confirm",
            font=("Bold", 40),
            text_color="black",
            width=293,
            height=51,
            fg_color="#D9D9D9",
            command=self.create_budget
        )
        self.confirm_btn.pack(padx=50, pady=10)

        self.return_btn = ctk.CTkButton(
            self.set_budget_frame,
            text="return",
            font=("Bold", 40),
            text_color="black",
            width=293,
            height=51,
            fg_color="#D9D9D9",
            command=None
        )
        self.return_btn.pack(padx=50, pady=10)

    def load_set_expense(self):
        """Loads the screen for the user to set their initial expenses."""
        self.delete_current()

        self.set_expense_frame = ctk.CTkFrame(
            self.mainframe_holder,
            fg_color="white",
            width=810,
            height=780
        )
        self.set_expense_frame.pack(padx=10, pady=10, expand=True)
        self.set_expense_frame.pack_propagate(False)

        self.set_expense_label = ctk.CTkLabel(
            self.set_expense_frame,
            text="Set Expenses",
            text_color="black",
            fg_color="white",
            font=("Bold", 64)
        )
        self.set_expense_label.pack(padx=10, pady=30)

        self.contain_scroll_frame = ctk.CTkFrame(
            self.set_expense_frame,
            width=757,
            height=411
        )
        self.contain_scroll_frame.grid_columnconfigure((0, 1), weight=1)
        self.contain_scroll_frame.grid_rowconfigure((0, 1), weight=1)
        self.contain_scroll_frame.pack(pady=20, padx=20)

        self.add_btn = ctk.CTkButton(
            self.contain_scroll_frame,
            text="add",
            font=("bold", 20),
            width=86,
            height=83,
            fg_color="#3EA428",
            command=self.load_set_your_expenses
        )
        self.add_btn.grid(row=0, column=0, sticky='nswe', pady=10, padx=10)

        self.scrollable_frame = ctk.CTkScrollableFrame(
            self.contain_scroll_frame,
            width=675,
            height=311,
            fg_color="#D9D9D9"
        )
        self.scrollable_frame.grid(row=0, column=1, sticky='nswe')

        self.confirm_btn = ctk.CTkButton(
            self.set_expense_frame,
            text="confirm",
            font=("Bold", 40),
            text_color="black",
            width=293,
            height=51,
            fg_color="#D9D9D9",
            command=self.load_set_goal
        )
        self.confirm_btn.pack(padx=50, pady=10)

        self.return_btn = ctk.CTkButton(
            self.set_expense_frame,
            text="return",
            font=("Bold", 40),
            text_color="black",
            width=293,
            height=51,
            fg_color="#D9D9D9",
            command=None
        )
        self.return_btn.pack(padx=50, pady=10)

        self.set_expense_feedback_label = ctk.CTkLabel(
            self.set_expense_frame,
            text="",
            font=("Bold", 20),
            text_color="red"
        )
        self.set_expense_feedback_label.pack(pady=10)

        self.create_expense_card(self.scrollable_frame)

    def load_set_your_expenses(self):
        """Loads the screen for the user to add a new expense during initial setup."""
        self.delete_current()

        self.set_expense_frame = ctk.CTkFrame(
            self.mainframe_holder,
            fg_color="white",
            width=810,
            height=780
        )
        self.set_expense_frame.pack(padx=10, pady=10, expand=True)
        self.set_expense_frame.pack_propagate(False)

        self.set_expense_label = ctk.CTkLabel(
            self.set_expense_frame,
            text="Set your expenses",
            text_color="black",
            fg_color="white",
            font=("Bold", 64)
        )
        self.set_expense_label.pack(padx=10, pady=40)

        self.set_expense_label_2 = ctk.CTkLabel(
            self.set_expense_frame,
            text="(Monthly)",
            text_color="black",
            fg_color="white",
            font=("Bold", 50)
        )
        self.set_expense_label_2.pack(padx=10, pady=20)

        self.set_expense_name_entry = ctk.CTkEntry(
            self.set_expense_frame,
            placeholder_text="Expense name",
            placeholder_text_color="black",
            text_color="black",
            font=("Bold", 53),
            fg_color="#D9D9D9",
            width=726,
            height=74
        )
        self.set_expense_name_entry.pack(pady=10)

        self.set_expense_amount_entry = ctk.CTkEntry(
            self.set_expense_frame,
            placeholder_text="Expense amount",
            placeholder_text_color="black",
            text_color="black",
            font=("Bold", 53),
            fg_color="#D9D9D9",
            width=726,
            height=74
        )
        self.set_expense_amount_entry.pack(pady=10)

        self.set_expense_status_label = ctk.CTkLabel(
            self.set_expense_frame,
            text="",
            font=("Bold", 20),
            text_color="red"
        )
        self.set_expense_status_label.pack(pady=10)

        self.confirm_btn = ctk.CTkButton(
            self.set_expense_frame,
            text="confirm",
            font=("Bold", 40),
            text_color="black",
            width=293,
            height=51,
            fg_color="#D9D9D9",
            command=lambda: self.create_expense("set_expense")
        )
        self.confirm_btn.pack(padx=50, pady=10)

        self.return_btn = ctk.CTkButton(
            self.set_expense_frame,
            text="return",
            font=("Bold", 40),
            text_color="black",
            width=293,
            height=51,
            fg_color="#D9D9D9",
            command=None
        )
        self.return_btn.pack(padx=50, pady=10)

    def load_set_goal(self):
        """Loads the screen for the user to set a financial goal."""
        self.delete_current()

        self.set_goal_frame = ctk.CTkFrame(
            self.mainframe_holder,
            fg_color="white",
            width=810,
            height=780
        )
        self.set_goal_frame.pack(padx=10, pady=10, expand=True)
        self.set_goal_frame.pack_propagate(False)

        self.set_goal_frame_label = ctk.CTkLabel(
            self.set_goal_frame,
            text="Set goal",
            text_color="black",
            fg_color="white",
            font=("Bold", 64)
        )
        self.set_goal_frame_label.pack(padx=10, pady=90)

        self.goal_name_entry = ctk.CTkEntry(
            self.set_goal_frame,
            placeholder_text="Goal name",
            placeholder_text_color="black",
            text_color="black",
            font=("Bold", 53),
            fg_color="#D9D9D9",
            width=726,
            height=74
        )
        self.goal_name_entry.pack(pady=10)

        self.goal_amount_entry = ctk.CTkEntry(
            self.set_goal_frame,
            placeholder_text="Goal amount",
            placeholder_text_color="black",
            text_color="black",
            font=("Bold", 53),
            fg_color="#D9D9D9",
            width=726,
            height=74
        )
        self.goal_amount_entry.pack(pady=10)

        self.set_goal_status_label = ctk.CTkLabel(
            self.set_goal_frame,
            text="",
            font=("Bold", 20),
            text_color="red"
        )
        self.set_goal_status_label.pack(pady=10)

        self.confirm_btn = ctk.CTkButton(
            self.set_goal_frame,
            text="confirm",
            font=("Bold", 40),
            text_color="black",
            width=293,
            height=51,
            fg_color="#D9D9D9",
            command=self.create_goal
        )
        self.confirm_btn.pack(padx=50, pady=10)

        self.return_btn = ctk.CTkButton(
            self.set_goal_frame,
            text="return",
            font=("Bold", 40),
            text_color="black",
            width=293,
            height=51,
            fg_color="#D9D9D9",
            command=None
        )
        self.return_btn.pack(padx=50, pady=10)

    def load_dashboard(self):
        """Loads the main dashboard screen."""
        self.delete_current()

        self.dashboard_frame = ctk.CTkFrame(
            self.mainframe_holder,
            fg_color="white",
            width=810,
            height=780
        )
        self.dashboard_frame.pack(padx=10, pady=10, expand=True)
        self.dashboard_frame.pack_propagate(False)

        self.username_label = ctk.CTkLabel(
            self.dashboard_frame,
            text=f"Hi, {self.username}",
            text_color="black",
            font=("Bold", 30),
            fg_color="#D9D9D9",
            width=312,
            height=45
        )
        self.username_label.place(relx=0.01, rely=0.01)

        self.add_expense_btn = ctk.CTkButton(
            self.dashboard_frame,
            text="add",
            font=("Bold", 36),
            text_color="black",
            width=140,
            height=39,
            fg_color="#D9D9D9",
            command=self.load_add_expense
        )
        self.add_expense_btn.place(relx=0.46, rely=0.01)

        self.edit_btn = ctk.CTkButton(
            self.dashboard_frame,
            text="edit",
            font=("Bold", 36),
            text_color="black",
            width=140,
            height=39,
            fg_color="#D9D9D9",
            command=self.load_edit_budget
        )
        self.edit_btn.place(relx=0.64, rely=0.01)

        self.log_out_btn = ctk.CTkButton(
            self.dashboard_frame,
            text="log out",
            font=("Bold", 36),
            text_color="black",
            width=140,
            height=39,
            fg_color="#D9D9D9",
            command=self.log_out
        )
        self.log_out_btn.place(relx=0.82, rely=0.01)

        self.budget_name_label = ctk.CTkLabel(
                self.dashboard_frame,
                text="Budget Name",
                text_color="black",
                font=("Bold", 32),
                fg_color="#D9D9D9",
                width=210,
                height=32
            )
        self.budget_name_label.place(relx=0.01, rely=0.25)

        self.balance_label = ctk.CTkLabel(
            self.dashboard_frame,
            text="Balance",
            text_color="black",
            font=("Bold", 90),
            fg_color="#D9D9D9",
            width=400,
            height=101
        )
        self.balance_label.place(relx=0.01, rely=0.3)

        self.progess_bar = ctk.CTkProgressBar(
            self.dashboard_frame,
            orientation="horizontal",
            width=734,
            height=36,
            progress_color="#3EA428",
        )
        self.progess_bar.place(relx=0.05, rely=0.45)

        self.goal_name_label = ctk.CTkLabel(
            self.dashboard_frame,
            text="goal name",
            text_color="black",
            font=("Bold", 32),
            fg_color="#D9D9D9",
            width=210,
            height=32
        )
        self.goal_name_label.place(relx=0.72, rely=0.33)

        self.goal_amount_label = ctk.CTkLabel(
            self.dashboard_frame,
            text="goal amount",
            text_color="black",
            font=("Bold", 32),
            fg_color="#D9D9D9",
            width=210,
            height=32
        )
        self.goal_amount_label.place(relx=0.72, rely=0.39)

        self.goal_status_label = ctk.CTkLabel(
            self.dashboard_frame,
            text="", # Will be updated by update_dashboard_labels
            text_color="black",
            font=("Bold", 20),
            fg_color="#D9D9D9",
            width=210,                                                                              
            height=32
        )
        self.goal_status_label.place(relx=0.72, rely=0.27)

        self.expense_scroll_frame = ctk.CTkScrollableFrame(
            self.dashboard_frame,
            width=673,
            height=320,
            fg_color="#D9D9D9"
        )
        self.expense_scroll_frame.place(relx=0.07, rely=0.53)

        self.dashboard_status_label = ctk.CTkLabel(
            self.dashboard_frame,
            text="",
            font=("Bold", 20),
            text_color="red"
        )
        self.dashboard_status_label.place(relx=0.07, rely=0.95)

        update_budget_balance(self.username)
        self.create_expense_card(self.expense_scroll_frame)
        self.update_dashboard_labels()

    def load_edit_budget(self):
        """Loads the screen for editing budget, expenses, or goals."""
        self.delete_current()

        self.edit_budget_frame = ctk.CTkFrame(
            self.mainframe_holder,
            fg_color="white",
            width=810,
            height=780
        )
        self.edit_budget_frame.pack(padx=10, pady=10, expand=True)
        self.edit_budget_frame.pack_propagate(False)

        self.edit_budget_btn = ctk.CTkButton(
            self.edit_budget_frame,
            text="edit budget",
            font=("Bold", 40),
            text_color="black",
            width=293,
            height=51,
            fg_color="#D9D9D9",
            command=self.load_edit_budget_screen
        )
        self.edit_budget_btn.pack(pady=50)

        self.edit_goal_btn = ctk.CTkButton(
            self.edit_budget_frame,
            text="edit goal",
            font=("Bold", 40),
            text_color="black",
            width=293,
            height=51,
            fg_color="#D9D9D9",
            command=self.load_edit_goal_screen
        )
        self.edit_goal_btn.pack(pady=50)

        self.return_edit_budget_btn = ctk.CTkButton(
            self.edit_budget_frame,
            text="return",
            font=("Bold", 40),
            text_color="black",
            width=293,
            height=51,
            fg_color="#D9D9D9",
            command=self.load_dashboard
        )
        self.return_edit_budget_btn.pack(pady=100)

    def load_edit_budget_screen(self):
        """Loads the screen for editing budget details."""
        self.delete_current()

        edit_budget_frame = ctk.CTkFrame(
            self.mainframe_holder,
            fg_color="white",
            width=810,
            height=780
        )
        edit_budget_frame.pack(padx=10, pady=10, expand=True)
        edit_budget_frame.pack_propagate(False)

        edit_budget_label = ctk.CTkLabel(
            edit_budget_frame,
            text="Edit Budget",
            text_color="black",
            fg_color="white",
            font=("Bold", 64)
        )
        edit_budget_label.pack(padx=10, pady=40)

        # Get current budget data to pre-fill the fields
        user_data = get_user_data(self.username)
        current_budget = user_data.get("budget", [{}])[0]
        old_name = current_budget.get("name", "")
        old_amount = current_budget.get("amount", "")
        old_income = current_budget.get("income", "") # Assuming 'income' is also stored and retrievable

        budget_name_entry = ctk.CTkEntry(
            edit_budget_frame,
            placeholder_text="Budget name",
            placeholder_text_color="black",
            text_color="black",
            font=("Bold", 53),
            fg_color="#D9D9D9",
            width=726,
            height=74
        )
        budget_name_entry.insert(0, old_name)
        budget_name_entry.pack(pady=10)

        budget_amount_entry = ctk.CTkEntry(
            edit_budget_frame,
            placeholder_text="Budget amount",
            placeholder_text_color="black",
            text_color="black",
            font=("Bold", 53),
            fg_color="#D9D9D9",
            width=726,
            height=74
        )
        budget_amount_entry.insert(0, old_amount)
        budget_amount_entry.pack(pady=10)

        budget_income_entry = ctk.CTkEntry(
            edit_budget_frame,
            placeholder_text="Budget income",
            placeholder_text_color="black",
            text_color="black",
            font=("Bold", 53),
            fg_color="#D9D9D9",
            width=726,
            height=74
        )
        budget_income_entry.insert(0, old_income)
        budget_income_entry.pack(pady=10)

        status_label = ctk.CTkLabel(
            edit_budget_frame,
            text="",
            font=("Bold", 20),
            text_color="red"
        )
        status_label.pack(pady=10)

        confirm_btn = ctk.CTkButton(
            edit_budget_frame,
            text="confirm",
            font=("Bold", 40),
            text_color="black",
            width=293,
            height=51,
            fg_color="#D9D9D9",
            command=lambda: self.update_budget(old_name, budget_name_entry, budget_amount_entry, budget_income_entry, status_label)
        )
        confirm_btn.pack(padx=50, pady=10)

        return_btn = ctk.CTkButton(
            edit_budget_frame,
            text="return",
            font=("Bold", 40),
            text_color="black",
            width=293,
            height=51,
            fg_color="#D9D9D9",
            command=self.load_edit_budget # Go back to the edit menu
        )
        return_btn.pack(padx=50, pady=10)

    def update_budget(self, old_name, new_name_entry, new_amount_entry, new_income_entry, status_label):
        """
        Handles the logic for updating a budget.

        Args:
            old_name (str): The original name of the budget.
            new_name_entry (ctk.CTkEntry): The entry widget for the new budget name.
            new_amount_entry (ctk.CTkEntry): The entry widget for the new budget amount.
            new_income_entry (ctk.CTkEntry): The entry widget for the new budget income.
            status_label (ctk.CTkLabel): The label to display status messages.
        """
        new_name = new_name_entry.get().strip()
        new_amount = new_amount_entry.get()
        new_income = new_income_entry.get()

        if not all([new_name, new_amount, new_income]):
            status_label.configure(text="Fill in all fields")
            return

        if new_name.isdigit() or not new_name.isalpha():
            status_label.configure(text="Name must be in letters")
            return

        if not new_amount.isdigit():
            status_label.configure(text="Amount must be a number/positive numbers")
            return

        if int(new_amount) <= 0:
            status_label.configure(text="Amount must be greater than 0")
            return

        if not new_income.isdigit():
            status_label.configure(text="Income must be a number/positive numbers")
            return
        
        if int(new_income) <= 0:
            status_label.configure(text="Income must be greater than 0")
            return

        success, message = edit_budget(self.username, old_name, new_name, new_amount, new_income)

        if success:
            self.load_dashboard() # Or go back to edit menu
        else:
            status_label.configure(text=message, text_color="red")

    def load_edit_goal_screen(self):
        """Loads the screen for editing a financial goal."""
        self.delete_current()

        edit_goal_frame = ctk.CTkFrame(
            self.mainframe_holder,
            fg_color="white",
            width=810,
            height=780
        )
        edit_goal_frame.pack(padx=10, pady=10, expand=True)
        edit_goal_frame.pack_propagate(False)

        edit_goal_label = ctk.CTkLabel(
            edit_goal_frame,
            text="Edit Goal",
            text_color="black",
            fg_color="white",
            font=("Bold", 64)
        )
        edit_goal_label.pack(padx=10, pady=40)

        # Get current goal data to pre-fill the fields
        user_data = get_user_data(self.username)
        current_goal = user_data.get("goals", [{}])[0]
        old_goal_name = current_goal.get("name", "")
        old_goal_amount = current_goal.get("amount", "")

        goal_name_entry = ctk.CTkEntry(
            edit_goal_frame,
            placeholder_text="Goal name",
            placeholder_text_color="black",
            text_color="black",
            font=("Bold", 53),
            fg_color="#D9D9D9",
            width=726,
            height=74
        )
        goal_name_entry.insert(0, old_goal_name)
        goal_name_entry.pack(pady=10)

        goal_amount_entry = ctk.CTkEntry(
            edit_goal_frame,
            placeholder_text="Goal amount",
            placeholder_text_color="black",
            text_color="black",
            font=("Bold", 53),
            fg_color="#D9D9D9",
            width=726,
            height=74
        )
        goal_amount_entry.insert(0, old_goal_amount)
        goal_amount_entry.pack(pady=10)

        status_label = ctk.CTkLabel(
            edit_goal_frame,
            text="",
            font=("Bold", 20),
            text_color="red"
        )
        status_label.pack(pady=10)

        confirm_btn = ctk.CTkButton(
            edit_goal_frame,
            text="confirm",
            font=("Bold", 40),
            text_color="black",
            width=293,
            height=51,
            fg_color="#D9D9D9",
            command=lambda: self.update_goal(old_goal_name, goal_name_entry, goal_amount_entry, status_label)
        )
        confirm_btn.pack(padx=50, pady=10)

        return_btn = ctk.CTkButton(
            edit_goal_frame,
            text="return",
            font=("Bold", 40),
            text_color="black",
            width=293,
            height=51,
            fg_color="#D9D9D9",
            command=self.load_edit_budget # Go back to the edit menu
        )
        return_btn.pack(padx=50, pady=10)

    def update_goal(self, old_name, new_name_entry, new_amount_entry, status_label):
        """
        Handles the logic for updating a financial goal.

        Args:
            old_name (str): The original name of the goal.
            new_name_entry (ctk.CTkEntry): The entry widget for the new goal name.
            new_amount_entry (ctk.CTkEntry): The entry widget for the new goal amount.
            status_label (ctk.CTkLabel): The label to display status messages.
        """
        new_name = new_name_entry.get().strip()
        new_amount = new_amount_entry.get()

        if not all([new_name, new_amount]):
            status_label.configure(text="Fill in name and amount")
            return

        if new_name.isdigit() or not new_name.isalpha():
            status_label.configure(text="Name must be in letters")
            return

        if not new_amount.isdigit():
            status_label.configure(text="Amount must be a number/positive numbers")
            return
        
        if int(new_amount) <= 0:
            status_label.configure(text="Amount must be greater than 0")
            return

        success, message = edit_goal(self.username, old_name, new_name, new_amount)

        if success:
            self.load_dashboard() # Or go back to edit menu
        else:
            status_label.configure(text=message, text_color="red")

    def log_out(self):
        """Displays a confirmation prompt for logging out."""
        self.delete_current()

        self.log_out_frame = ctk.CTkFrame(
            self.mainframe_holder,
            fg_color="white",
            width=810,
            height=780
        )
        self.log_out_frame.pack(padx=10, pady=10, expand=True)
        self.log_out_frame.pack_propagate(False)

        self.confirm_label = ctk.CTkLabel(
            self.log_out_frame,
            text="""Are you sure you want 
to log out?""",
            text_color="black",
            font=("Bold", 70),
            fg_color="white",
            width=210,
            height=40
        )
        self.confirm_label.pack(pady=100)

        self.confirm_btn = ctk.CTkButton(
            self.log_out_frame,
            text="confirm",
            font=("Bold", 40),
            text_color="black",
            width=293,
            height=51,
            fg_color="#D9D9D9",
            command=self.perform_logout
        )
        self.confirm_btn.place(relx=0.3, rely=0.5)

        self.return_btn = ctk.CTkButton(
            self.log_out_frame,
            text="return",
            font=("Bold", 40),
            text_color="black",
            width=293,
            height=51,
            fg_color="#D9D9D9",
            command=self.load_dashboard
        )
        self.return_btn.place(relx=0.3, rely=0.6)
        
    def load_add_expense(self):
        """Loads the screen for adding a new expense from the dashboard."""
        self.delete_current()

        self.set_expense_frame = ctk.CTkFrame(
            self.mainframe_holder,
            fg_color="white",
            width=810,
            height=780
        )
        self.set_expense_frame.pack(padx=10, pady=10, expand=True)
        self.set_expense_frame.pack_propagate(False)

        self.set_expense_label = ctk.CTkLabel(
            self.set_expense_frame,
            text="Add Expenses",
            text_color="black",
            fg_color="white",
            font=("Bold", 64)
        )
        self.set_expense_label.pack(padx=10, pady=30)

        self.contain_scroll_frame = ctk.CTkFrame(
            self.set_expense_frame,
            width=757,
            height=411
        )
        self.contain_scroll_frame.grid_columnconfigure((0, 1), weight=1)
        self.contain_scroll_frame.grid_rowconfigure((0, 1), weight=1)
        self.contain_scroll_frame.pack(pady=20, padx=20)

        self.add_btn = ctk.CTkButton(
            self.contain_scroll_frame,
            text="add",
            font=("bold", 20),
            width=86,
            height=83,
            fg_color="#3EA428",
            command=self.load_add_your_expenses
        )
        self.add_btn.grid(row=0, column=0, sticky='nswe', pady=10, padx=10)

        self.scrollable_frame = ctk.CTkScrollableFrame(
            self.contain_scroll_frame,
            width=675,
            height=311,
            fg_color="#D9D9D9"
        )
        self.scrollable_frame.grid(row=0, column=1, sticky='nswe')

        self.confirm_btn = ctk.CTkButton(
            self.set_expense_frame,
            text="confirm",
            font=("Bold", 40),
            text_color="black",
            width=293,
            height=51,
            fg_color="#D9D9D9",
            command=self.load_dashboard
        )
        self.confirm_btn.pack(padx=50, pady=10)

        self.return_btn = ctk.CTkButton(
            self.set_expense_frame,
            text="return",
            font=("Bold", 40),
            text_color="black",
            width=293,
            height=51,
            fg_color="#D9D9D9",
            command=self.load_dashboard
        )
        self.return_btn.pack(padx=50, pady=10)

        self.add_expense_feedback_label = ctk.CTkLabel(
            self.set_expense_frame,
            text="",
            font=("Bold", 20),
            text_color="red"
        )
        self.add_expense_feedback_label.pack(pady=10)

        self.create_expense_card(self.scrollable_frame)

    def load_add_your_expenses(self):
        """Loads the screen for the user to input details for a new expense."""
        self.delete_current()

        self.add_expense_frame = ctk.CTkFrame(
            self.mainframe_holder,
            fg_color="white",
            width=810,
            height=780
        )
        self.add_expense_frame.pack(padx=10, pady=10, expand=True)
        self.add_expense_frame.pack_propagate(False)

        self.add_expense_label = ctk.CTkLabel(
            self.add_expense_frame,
            text="Add your expenses",
            text_color="black",
            fg_color="white",
            font=("Bold", 64)
        )
        self.add_expense_label.pack(padx=10, pady=40)

        self.add_expense_name_entry = ctk.CTkEntry(
            self.add_expense_frame,
            placeholder_text="Expense name",
            placeholder_text_color="black",
            text_color="black",
            font=("Bold", 53),
            fg_color="#D9D9D9",
            width=726,
            height=74
        )
        self.add_expense_name_entry.pack(pady=10)

        self.add_expense_amount_entry = ctk.CTkEntry(
            self.add_expense_frame,
            placeholder_text="Expense amount",
            placeholder_text_color="black",
            text_color="black",
            font=("Bold", 53),
            fg_color="#D9D9D9",
            width=726,
            height=74
        )
        self.add_expense_amount_entry.pack(pady=10)

        self.add_expense_status_label = ctk.CTkLabel(
            self.add_expense_frame,
            text="",
            font=("Bold", 20),
            text_color="red"
        )
        self.add_expense_status_label.pack(pady=10)

        self.confirm_btn = ctk.CTkButton(
            self.add_expense_frame,
            text="confirm",
            font=("Bold", 40),
            text_color="black",
            width=293,
            height=51,
            fg_color="#D9D9D9",
            command=lambda: self.create_expense("add_expense")
        )
        self.confirm_btn.pack(padx=50, pady=10)

        self.return_btn = ctk.CTkButton(
            self.add_expense_frame,
            text="return",
            font=("Bold", 40),
            text_color="black",
            width=293,
            height=51,
            fg_color="#D9D9D9",
            command=None
        )
        self.return_btn.pack(padx=50, pady=10)

    def check_if_budget_exist(self):
        """Checks if a budget exists for the current user and loads the appropriate screen."""
        exist = check_budget(self.username)

        if exist:
            self.load_dashboard()
        else:
            self.load_create_budget()

    def create_budget(self):
        """Handles the creation of a new budget."""
        name = self.budget_name_entry.get().strip()
        amount = self.budget_amount_entry.get()
        income = self.budget_income_entry.get()
        username = self.username

        if not all([name, amount, income]):
            self.set_budget_status_label.configure(
                text="Fill in all fields")
            return

        if name.isdigit() or not name.isalpha():
            self.set_budget_status_label.configure(
                text="Name must be in letters")
            return

        if amount.isdigit() is False:
            self.set_budget_status_label.configure(
                text="Amount must be a number/positive numbers")
            return

        if amount.isdigit() and int(amount) <= 0:
            self.set_budget_status_label.configure(
                text="Amount must be greater than 0")
            return

        if income.isdigit() is False:
            self.set_budget_status_label.configure(
                text="Income must be a number/positive numbers")
            return
        
        if income.isdigit() and int(income) <= 0:
            self.set_budget_status_label.configure(
                text="Income must be greater than 0")
            return

        success, message = add_budget(username, name, amount, income)
        if success:
            self.set_budget_status_label.configure(
                text=message, text_color="green")
            self.load_set_expense()
            return
        else:
            self.set_budget_status_label.configure(text=message)
            return

    def create_goal(self):
        """Handles the creation of a new financial goal."""
        name = self.goal_name_entry.get().strip()
        amount = self.goal_amount_entry.get()
        username = self.username

        if not all([name, amount]):
            self.set_goal_status_label.configure(
                text="Fill in name and amount")
            return

        if name.isdigit() or not name.isalpha():
            self.set_goal_status_label.configure(
                text="Name must be in letters")
            return

        if amount.isdigit() is False:
            self.set_goal_status_label.configure(
                text="Amount must be a number/positive numbers")
            return

        if amount.isdigit() and int(amount) <= 0:
            self.set_goal_status_label.configure(
                text="Amount must be greater than 0")
            return

        success, message = add_goal(username, name, amount)
        if success:
            self.set_goal_status_label.configure(
                text=message, text_color="green")
            self.load_dashboard()
            return
        else:
            self.set_goal_status_label.configure(text=message)
            return

    def create_expense(self, location):
        """
        Handles the creation of a new expense.

        Args:
            location (str): The screen from which the expense is being created ("set_expense" or "add_expense").
        """
        username = self.username
        
        if location == "set_expense":
            name_entry = self.set_expense_name_entry
            amount_entry = self.set_expense_amount_entry
            status_label = self.set_expense_status_label
            success_callback = self.load_set_expense
        elif location == "add_expense":
            name_entry = self.add_expense_name_entry
            amount_entry = self.add_expense_amount_entry
            status_label = self.add_expense_status_label
            success_callback = self.load_add_expense
        else:
            return

        name = name_entry.get().strip()
        amount = amount_entry.get()

        if not all([name, amount]):
            status_label.configure(text="Fill in name and amount")
            return
        
        if name.isdigit() or not name.isalpha():
            status_label.configure(text="Name must be in letters")
            return

        if not amount.isdigit():
            status_label.configure(text="Amount must be a number/positive numbers")
            return
        
        if int(amount) <= 0:
            status_label.configure(text="Amount must be greater than 0")
            return
        
        success, message = add_expenses(username, name, amount)
        if success:
            status_label.configure(text=message, text_color="green")
            success_callback()
        else:
            status_label.configure(text=message)

    def create_expense_card(self, scrollable_frame):
        """
        Creates and displays expense cards in the given scrollable frame.

        Args:
            scrollable_frame (ctk.CTkScrollableFrame): The frame to which the expense cards will be added.
        """
        for widget in scrollable_frame.winfo_children():
            widget.forget()

        expense_label = ctk.CTkLabel(
                scrollable_frame,
                text="Expenses",
                text_color="black",
                font=("Arial", 24),
                fg_color="#FFFFFF",
                corner_radius=10
            )
        expense_label.pack(side="top", pady=10)

        username = self.username
        expenses = get_expense(username)

        if not expenses:
            ctk.CTkLabel(
                scrollable_frame,
                text="No expense found.",
                text_color="black",
                font=("Arial", 20),
                fg_color="white",
                width=675,
                height=50,
                corner_radius=10,
            ).pack(pady=20)

        for expense in expenses:
            name = expense.expense_name
            amount = expense.expense_amount

            expense_frame = ctk.CTkFrame(
                scrollable_frame,
                width=675,
                height=50,
                fg_color="white",
                corner_radius=20
            )
            expense_frame.pack(fill="x", pady=5, padx=10)

            name_label = ctk.CTkLabel(
                expense_frame,
                text=name,
                font=("Arial", 20),
                anchor="w",
                fg_color="white",
                text_color="black"
            )
            name_label.pack(side="left", fill="x", expand=True, padx=10)

            amount_label = ctk.CTkLabel(
                expense_frame,
                text=f"-${amount}",
                font=("Arial", 20),
                anchor="e",
                fg_color="white",
                text_color="black"
            )
            amount_label.pack(side="right", padx=10)

            edit_btn = ctk.CTkButton(
                expense_frame,
                text="Edit",
                font=("Arial", 16),
                width=50,
                command=lambda name=name, amount=amount: self.load_edit_expense(name, amount)
            )
            edit_btn.pack(side="right", padx=5)

            delete_btn = ctk.CTkButton(
                expense_frame,
                text="Delete",
                font=("Arial", 16),
                width=50,
                fg_color="red",
                command=lambda expense_name=name: self.delete_expense(expense_name)
            )
            delete_btn.pack(side="right", padx=5)

    def load_edit_expense(self, old_name, old_amount):
        """
        Loads the screen for editing an expense.

        Args:
            old_name (str): The original name of the expense.
            old_amount (int): The original amount of the expense.
        """
        self.delete_current()

        edit_expense_frame = ctk.CTkFrame(
            self.mainframe_holder,
            fg_color="white",
            width=810,
            height=780
        )
        edit_expense_frame.pack(padx=10, pady=10, expand=True)
        edit_expense_frame.pack_propagate(False)

        edit_expense_label = ctk.CTkLabel(
            edit_expense_frame,
            text="Edit Expense",
            text_color="black",
            fg_color="white",
            font=("Bold", 64)
        )
        edit_expense_label.pack(padx=10, pady=40)

        new_name_entry = ctk.CTkEntry(
            edit_expense_frame,
            text_color="black",
            font=("Bold", 53),
            fg_color="#D9D9D9",
            width=726,
            height=74
        )
        new_name_entry.insert(0, old_name)
        new_name_entry.pack(pady=10)

        new_amount_entry = ctk.CTkEntry(
            edit_expense_frame,
            text_color="black",
            font=("Bold", 53),
            fg_color="#D9D9D9",
            width=726,
            height=74
        )
        new_amount_entry.insert(0, old_amount)
        new_amount_entry.pack(pady=10)

        status_label = ctk.CTkLabel(
            edit_expense_frame,
            text="",
            font=("Bold", 20),
            text_color="red"
        )
        status_label.pack(pady=10)

        confirm_btn = ctk.CTkButton(
            edit_expense_frame,
            text="confirm",
            font=("Bold", 40),
            text_color="black",
            width=293,
            height=51,
            fg_color="#D9D9D9",
            command=lambda: self.update_expense(old_name, new_name_entry, new_amount_entry, status_label)
        )
        confirm_btn.pack(padx=50, pady=10)

        return_btn = ctk.CTkButton(
            edit_expense_frame,
            text="return",
            font=("Bold", 40),
            text_color="black",
            width=293,
            height=51,
            fg_color="#D9D9D9",
            command=self.load_dashboard
        )
        return_btn.pack(padx=50, pady=10)

    def update_expense(self, old_name, new_name_entry, new_amount_entry, status_label):
        """
        Handles the logic for updating an expense.

        Args:
            old_name (str): The original name of the expense.
            new_name_entry (ctk.CTkEntry): The entry widget for the new expense name.
            new_amount_entry (ctk.CTkEntry): The entry widget for the new expense amount.
            status_label (ctk.CTkLabel): The label to display status messages.
        """
        new_name = new_name_entry.get().strip()
        new_amount = new_amount_entry.get()

        if not all([new_name, new_amount]):
            status_label.configure(text="Fill in all fields")
            return

        if not new_amount.isdigit():
            status_label.configure(text="Amount must be a number")
            return
        
        success, message = edit_expense(self.username, old_name, new_name, float(new_amount))

        if success:
            self.load_dashboard()
        else:
            status_label.configure(text=message, text_color="red")

    def delete_expense(self, expense_name):
        """
        Deletes an expense.

        Args:
            expense_name (str): The name of the expense to be deleted.
        """
        success, message = delete_expense(self.username, expense_name)
        
        if success:
            self.load_dashboard()
        else:
            status_message = message
            status_color = "red"
            if hasattr(self, 'dashboard_status_label'):
                self.dashboard_status_label.configure(text=status_message, text_color=status_color)
            if hasattr(self, 'add_expense_feedback_label'):
                self.add_expense_feedback_label.configure(text=status_message, text_color=status_color)
            if hasattr(self, 'set_expense_feedback_label'):
                self.set_expense_feedback_label.configure(text=status_message, text_color=status_color)

    def update_dashboard_labels(self):
        """Updates the labels on the dashboard with the latest user data."""
        data = get_user_data(self.username)

        if not data:
            self.balance_label.configure(text="No budget")
            self.goal_name_label.configure(text="No goal")
            self.goal_amount_label.configure(text="")
            self.progess_bar.set(0)
            self.goal_status_label.configure(text="No goal set.", text_color="black")
            return

        if data["budget"]:
            budget_data = data["budget"][0]
            name = budget_data.get("name", "Budget")
            balance = budget_data.get("balance", 0)
            self.balance_label.configure(text=f"${balance}")
            self.budget_name_label.configure(text=name)
        else:
            self.balance_label.configure(text="No budget")
            balance = 0

        if data["goals"]:
            goal_data = data["goals"][0]
            goal_name = goal_data.get("name", "")
            goal_amount = goal_data.get("amount", 0)
            self.goal_name_label.configure(text=goal_name)
            self.goal_amount_label.configure(text=f"${goal_amount}")
            if goal_amount > 0:
                progress = max(0, min(balance / goal_amount, 1.0))
                self.progess_bar.set(progress)
                if balance >= goal_amount:
                    self.goal_status_label.configure(text="Goal Reached!", text_color="green")
                else:
                    remaining = goal_amount - balance
                    self.goal_status_label.configure(text=f"${remaining} to go!", text_color="red")
            else:
                self.progess_bar.set(0)
                self.goal_status_label.configure(text="No goal set.", text_color="black")
        else:
            self.goal_name_label.configure(text="No goal")
            self.goal_amount_label.configure(text="")
            self.progess_bar.set(0)
            self.goal_status_label.configure(text="No goal set.", text_color="black")
    
    def perform_logout(self):
        """Performs the actual logout by destroying the current window and opening the login menu."""
        self.destroy()
        from Login import LoginMenu
        LoginMenu().mainloop()
       
if __name__ == "__main__":
    pass
