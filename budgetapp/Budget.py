import tkinter as tk
import customtkinter as ctk

class BudgetMenu(ctk.CTk):
    
    def __init__(self):

        super().__init__()

        self.title("Budget app")
        self.geometry("844x844")
        self.minsize(844, 844)
        self.maxsize(844, 844)

        self.mainframe = ctk.CTkFrame(
        self, fg_color="black", width=744, height=744)
        self.mainframe.pack(fill="both", expand=True)

        self.mainframe_holder = ctk.CTkFrame(
        self.mainframe, fg_color="#D9D9D9", width=644, height=644)
        self.mainframe_holder.pack(padx=10, pady=10, fill="both", expand=True)

    def load_create_budget(self):
        None

    def load_set_budget(self):
        None
    
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


if __name__ == "__main__":
    BudgetMenu().mainloop()