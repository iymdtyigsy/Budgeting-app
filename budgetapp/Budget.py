import customtkinter as ctk
from Database import add_budget, check_budget, add_expenses, add_goal, get_expense, get_user_data

class BudgetMenu(ctk.CTk):
    def __init__(self, username):
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
        """Delete the current menu."""
        for widget in self.mainframe_holder.winfo_children():
            widget.forget()

    def load_create_budget(self):

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

        self.create_expense_card(self.scrollable_frame)

    def load_set_your_expenses(self):

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

        self.expense_name_entry = ctk.CTkEntry(
            self.set_expense_frame,
            placeholder_text="Expense name",
            placeholder_text_color="black",
            text_color="black",
            font=("Bold", 53),
            fg_color="#D9D9D9",
            width=726,
            height=74
        )
        self.expense_name_entry.pack(pady=10)

        self.expense_amount_entry = ctk.CTkEntry(
            self.set_expense_frame,
            placeholder_text="Expense amount",
            placeholder_text_color="black",
            text_color="black",
            font=("Bold", 53),
            fg_color="#D9D9D9",
            width=726,
            height=74
        )
        self.expense_amount_entry.pack(pady=10)

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
            command=self.create_expense("set_expense")
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
            height=36
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

        self.expense_scroll_frame = ctk.CTkScrollableFrame(
            self.dashboard_frame,
            width=673,
            height=320,
            fg_color="#D9D9D9"
        )
        self.expense_scroll_frame.place(relx=0.07, rely=0.53)

        self.create_expense_card(self.expense_scroll_frame)
        self.update_dashboard_labels()

    def load_edit_budget(self):

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
            command=None
        )
        self.edit_budget_btn.pack(pady=50)

        self.edit_expense_btn = ctk.CTkButton(
            self.edit_budget_frame,
            text="edit expense",
            font=("Bold", 40),
            text_color="black",
            width=293,
            height=51,
            fg_color="#D9D9D9",
            command=None
        )
        self.edit_expense_btn.pack(pady=50)

        self.edit_goal_btn = ctk.CTkButton(
            self.edit_budget_frame,
            text="edit goal",
            font=("Bold", 40),
            text_color="black",
            width=293,
            height=51,
            fg_color="#D9D9D9",
            command=None
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

    def log_out(self):

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
            command=None
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

        self.create_expense_card(self.scrollable_frame)

    def load_add_your_expenses(self):

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

        self.expense_name_entry = ctk.CTkEntry(
            self.set_expense_frame,
            placeholder_text="Expense name",
            placeholder_text_color="black",
            text_color="black",
            font=("Bold", 53),
            fg_color="#D9D9D9",
            width=726,
            height=74
        )
        self.expense_name_entry.pack(pady=10)

        self.expense_amount_entry = ctk.CTkEntry(
            self.set_expense_frame,
            placeholder_text="Expense amount",
            placeholder_text_color="black",
            text_color="black",
            font=("Bold", 53),
            fg_color="#D9D9D9",
            width=726,
            height=74
        )
        self.expense_amount_entry.pack(pady=10)

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
            command=self.create_expense("add_expense")
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

    def check_if_budget_exist(self):
        exist = check_budget(self.username)

        if exist:
            self.load_dashboard()
        else:
            self.load_create_budget()

    def create_budget(self):
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

        if income.isdigit() is False:
            self.set_budget_status_label.configure(
                text="Income must be a number/positive numbers")
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
            self.load_set_goal()
            return
        else:
            self.set_goal_status_label.configure(text=message)
            return

    def create_expense(self, location):
        name = self.expense_name_entry.get().strip()
        amount = self.expense_amount_entry.get()
        username = self.username

        if not all([name, amount]):
            self.set_expense_status_label.configure(
                text="Fill in name and amount")
            return
        
        if name.isdigit() or not name.isalpha():
            self.set_expense_status_label.configure(
                text="Name must be in letters")
            return
        
        if amount.isdigit() is False:
            self.set_expense_status_label.configure(
                text="Amount must be a number/positive numbers")
            return
        
        if amount.isdigit() and int(amount) <= 0:
            self.set_expense_status_label.configure(
                text="Amount must be greater than 0")
            return
        
        success, message = add_expenses(username, name, amount)
        if success:
            if location == "set_expense":
                self.set_expense_status_label.configure(
                    text=message, text_color="green")
                self.load_set_your_expenses()
                return
            elif location == "add_expense":
                self.set_expense_status_label.configure(
                    text=message, text_color="green")
                self.load_add_your_expenses()
                return
        else:
            self.set_expense_status_label.configure(text=message)
            return

    def create_expense_card(self, scrollable_frame):

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
                height=300,
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
            name_label.pack(side="left", fill="x", expand=True)

            amount_label = ctk.CTkLabel(
                expense_frame,
                text=f"-${amount}",
                font=("Arial", 20),
                anchor="e",
                fg_color="white",
                text_color="black"
            )
            amount_label.pack(side="right")

    def update_dashboard_labels(self):
        data = get_user_data(self.username)

        if not data:
            self.balance_label.configure(text="No budget")
            self.goal_name_label.configure(text="No goal")
            self.goal_amount_label.configure(text="")

        if data["budget"]:
            budget_data = data["budget"][0]
            name = budget_data.get("name", "Budget")
            amount = budget_data.get("amount", 0)
            self.balance_label.configure(text=f"${amount}")
            self.budget_name_label.configure(text=name)
        else:
            self.balance_label.configure(text="No budget")

        if data["goals"]:
            goal_data = data["goals"][0]
            self.goal_name_label.configure(text=goal_data.get("name", ""))
            self.goal_amount_label.configure(
                text=f"${goal_data.get('amount', 0)}")
        else:
            self.goal_name_label.configure(text="No goal")
            self.goal_amount_label.configure(text="")
       
if __name__ == "__main__":
    BudgetMenu("testuser").mainloop()
