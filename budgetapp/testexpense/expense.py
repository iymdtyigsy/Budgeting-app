class Expense:

    def __init__(self, name, catergory, amount) -> None:
        self.name = name
        self.catergory = catergory
        self.amount = amount

    def __repr__(self):
        return f"<Expense: {self.name}, {self.catergory}, ${self.amount:.2f} >"