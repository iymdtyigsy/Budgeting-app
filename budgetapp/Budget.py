import tkinter as tk
import customtkinter as ctk

class BudgetMenu(ctk.CTk):
    
    def __init__(self):

        super().__init__()

        self.title("Budget app")
        self.geometry("844x844")
        self.minsize(951, 951)
        self.maxsize(951, 951)

        self.mainframe = ctk.CTkFrame(
            self, 
            fg_color="black", 
            width=744, 
            height=744)
        self.mainframe.pack(fill="both", expand=True)

        self.mainframe_holder = ctk.CTkFrame(
            self.mainframe, 
            fg_color="#D9D9D9", 
            width=644, 
            height=644)
        self.mainframe_holder.pack(padx=10, pady=10, fill="both", expand=True)

        self.load_set_expense()


    def delete_current(self):
        """Delete the current menu."""
        for widget in self.mainframe_holder.winfo_children():
            widget.forget()

    def load_create_budget(self):
        
        self.create_budget_frame = ctk.CTkFrame(
            self.mainframe_holder, 
            fg_color="white", 
            width=707, 
            height=585)
        self.create_budget_frame.pack(padx=10, pady=10, expand=True)
        self.create_budget_frame.pack_propagate(False)

        self.create_budget_label = ctk.CTkLabel(
            self.create_budget_frame, 
            text=
        """
looks like you don't 
have a budget.
Would you like to 
create one? 
        """ , 
            text_color="black", 
            fg_color="white", 
            font=("Bold", 55), 
            corner_radius=5)
        self.create_budget_label.pack(padx=10, pady=5)

        self.yes_btn = ctk.CTkButton(
            self.create_budget_frame, 
            text="yes", 
            font=("Bold", 20), 
            text_color="black", 
            width=200, 
            height= 50, 
            fg_color="#D9D9D9", 
            command=None)
        self.yes_btn.pack(padx=50, pady=10)

        self.return_btn = ctk.CTkButton(
            self.create_budget_frame, 
            text="return", 
            font=("Bold", 20), 
            text_color="black", 
            width=200, 
            height= 50, 
            fg_color="#D9D9D9", 
            command=None)
        self.return_btn.pack(padx=50, pady=10)

    def load_set_budget(self):
        
        self.set_budget_frame = ctk.CTkFrame(
            self.mainframe_holder, 
            fg_color="white", 
            width=810, 
            height=780)
        self.set_budget_frame.pack(padx=10, pady=10, expand=True)
        self.set_budget_frame.pack_propagate(False)

        self.set_budget_label = ctk.CTkLabel(
            self.set_budget_frame, 
            text="Create Budget", 
            text_color="black", 
            fg_color="white", 
            font=("Bold", 96))
        self.set_budget_label.pack(padx=10, pady=40)

        self.set_budget_label_2 = ctk.CTkLabel(
            self.set_budget_frame, 
            text="(Monthly)", 
            text_color="black", 
            fg_color="white", 
            font=("Bold", 50))
        self.set_budget_label_2.pack(padx=10, pady=20)

        self.budget_name_entry = ctk.CTkEntry(
            self.set_budget_frame, 
            placeholder_text="Budget name", 
            placeholder_text_color="black",
            text_color="black", 
            font=("Bold", 40), 
            fg_color="#D9D9D9", 
            width=726, 
            height=74)
        self.budget_name_entry.pack(padx=50, pady=30)

        self.budget_balance_entry = ctk.CTkEntry(
            self.set_budget_frame,
            placeholder_text="Budget balance", 
            placeholder_text_color="black",
            text_color="black", 
            font=("Bold", 40), 
            fg_color="#D9D9D9", 
            width=726, 
            height=74)
        self.budget_balance_entry.pack(padx=50)

        self.budget_income_entry = ctk.CTkEntry(
            self.set_budget_frame, 
            placeholder_text="Budget income", 
            placeholder_text_color="black",
            text_color="black", 
            font=("Bold", 40), 
            fg_color="#D9D9D9", 
            width=726, 
            height=74)
        self.budget_income_entry.pack(padx=50, pady=30)

        self.confirm_btn = ctk.CTkButton(
            self.set_budget_frame, 
            text="confirm", 
            font=("Bold", 40), 
            text_color="black", 
            width=293, 
            height= 51, 
            fg_color="#D9D9D9", 
            command=None)
        self.confirm_btn.pack(padx=50, pady=10)

        self.return_btn = ctk.CTkButton(
            self.set_budget_frame, 
            text="return", 
            font=("Bold", 40), 
            text_color="black", 
            width=293, 
            height= 51, 
            fg_color="#D9D9D9", 
            command=None)
        self.return_btn.pack(padx=50, pady=10)
    
    def load_set_expense_catergorie(self):
        
        self.set_expense_catergorie_frame = ctk.CTkFrame(
            self.mainframe_holder, 
            fg_color="white", 
            width=810, 
            height=780)
        self.set_expense_catergorie_frame.pack(padx=10, pady=10, expand=True)
        self.set_expense_catergorie_frame.pack_propagate(False)

        self.set_expense_catergorie_label = ctk.CTkLabel(
            self.set_expense_catergorie_frame, 
            text="Set Expense Catergories", 
            text_color="black", 
            fg_color="white", 
            font=("Bold", 64))
        self.set_expense_catergorie_label.pack(padx=10, pady=40)

        self.set_expense_catergorie_label_2 = ctk.CTkLabel(
            self.set_expense_catergorie_frame, 
            text="(Monthly)", 
            text_color="black", 
            fg_color="white", 
            font=("Bold", 50))
        self.set_expense_catergorie_label_2.pack(padx=10, pady=20)

        self.expense_name_entry = ctk.CTkEntry(
            self.set_expense_catergorie_frame, 
            placeholder_text="Expense name", 
            placeholder_text_color="black",
            text_color="black", 
            font=("Bold", 53), 
            fg_color="#D9D9D9", 
            width=726, 
            height=74)
        self.expense_name_entry.pack(pady=10)

        self.expense_amount_entry = ctk.CTkEntry(
            self.set_expense_catergorie_frame, 
            placeholder_text="Expense amount", 
            placeholder_text_color="black",
            text_color="black", 
            font=("Bold", 53), 
            fg_color="#D9D9D9", 
            width=726, 
            height=74)
        self.expense_amount_entry.pack(pady=10)

        self.confirm_btn = ctk.CTkButton(
            self.set_expense_catergorie_frame, 
            text="confirm", 
            font=("Bold", 40), 
            text_color="black", 
            width=293, 
            height= 51, 
            fg_color="#D9D9D9", 
            command=None)
        self.confirm_btn.pack(padx=50, pady=10)

        self.return_btn = ctk.CTkButton(
            self.set_expense_catergorie_frame, 
            text="return", 
            font=("Bold", 40), 
            text_color="black", 
            width=293, 
            height= 51, 
            fg_color="#D9D9D9", 
            command=None)
        self.return_btn.pack(padx=50, pady=10)

    def load_set_expense(self):
        """plus_image = ctk.CTkImage(
            size=(1,1),
            light_image="/images/plus.png",
            dark_image="/images/plus.png",
        )

        ctk.CTkButton(
            image=plus_image
        )"""

        self.set_expense_frame = ctk.CTkFrame(
            self.mainframe_holder, 
            fg_color="white", 
            width=810, 
            height=780)
        self.set_expense_frame.pack(padx=10, pady=10, expand=True)
        self.set_expense_frame.pack_propagate(False)

        self.set_expense_label = ctk.CTkLabel(
            self.set_expense_frame, 
            text="Set Expense Catergories", 
            text_color="black", 
            fg_color="white", 
            font=("Bold", 64))
        self.set_expense_label.pack(padx=10, pady=30)

        self.contain_scroll_frame = ctk.CTkFrame(
            self.set_expense_frame,
            width=757,
            height=411)
        self.contain_scroll_frame.pack()
        
        self.add_btn = ctk.CTkButton(
            self.contain_scroll_frame,
            text="add",
            font=("bold",20),
            width=86,
            height=83,
            fg_color="#3EA428",
            command=None)
        self.add_btn.grid(row=0,)

        self.scrollable_frame = ctk.CTkScrollableFrame(
            self.contain_scroll_frame,
            width=675,
            height=311)
        self.scrollable_frame.pack()

        self.confirm_btn = ctk.CTkButton(
            self.set_expense_frame, 
            text="confirm", 
            font=("Bold", 40), 
            text_color="black", 
            width=293, 
            height= 51, 
            fg_color="#D9D9D9", 
            command=None)
        self.confirm_btn.pack(padx=50, pady=10)

        self.return_btn = ctk.CTkButton(
            self.set_expense_frame, 
            text="return", 
            font=("Bold", 40), 
            text_color="black", 
            width=293, 
            height= 51, 
            fg_color="#D9D9D9", 
            command=None)
        self.return_btn.pack(padx=50, pady=10)

    def load_set_goal(self):
        None

    def load_dashboard(self):
        None

    def load_edit_budget(self):
        None
    
    def load_edit_expense_catergorie(self):
        None

    def load_edit_expense(self):
        None
    
    def load_edit_goal(self):
        None
    def log_out(self):
        None


if __name__ == "__main__":
    BudgetMenu().mainloop()