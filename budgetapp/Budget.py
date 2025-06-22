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
        self, fg_color="black", width=744, height=744)
        self.mainframe.pack(fill="both", expand=True)

        self.mainframe_holder = ctk.CTkFrame(
        self.mainframe, fg_color="#D9D9D9", width=644, height=644)
        self.mainframe_holder.pack(padx=10, pady=10, fill="both", expand=True)

        self.load_set_budget()


    def delete_current(self):
        """Delete the current menu."""
        for widget in self.mainframe_holder.winfo_children():
            widget.forget()

    def load_create_budget(self):
        
        self.create_budget_frame = ctk.CTkFrame(
        self.mainframe_holder, fg_color="white", width=707, height=585,)
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
        """ , text_color="black", fg_color="white", 
        font=("Bold", 55), corner_radius=5)
        self.create_budget_label.pack(padx=10, pady=5)

        self.yes_btn = ctk.CTkButton(
        self.create_budget_frame, text="yes", font=("Bold", 20), 
        text_color="black", width=200, height= 50, fg_color="#D9D9D9", command=None)
        self.yes_btn.pack(padx=50, pady=10)

        self.return_btn = ctk.CTkButton(
        self.create_budget_frame, text="return", font=("Bold", 20), 
        text_color="black", width=200, height= 50, fg_color="#D9D9D9", command=None)
        self.return_btn.pack(padx=50, pady=10)

    def load_set_budget(self):
        
        self.set_budget_frame = ctk.CTkFrame(
        self.mainframe_holder, fg_color="white", width=810, height=780)
        self.set_budget_frame.pack(padx=10, pady=10, expand=True)
        self.set_budget_frame.pack_propagate(False)
    
    def load_set_expense_catergorie(self):
        None

    def load_set_expense(self):
        None
    
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