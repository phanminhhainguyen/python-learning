class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    def deposit(self, amount, description=''):
        self.ledger.append({
            'amount' : amount,
            'description' : description
        })
    def withdraw(self, amount, description=''):
        
        
        if self.check_funds(amount):
            self.ledger.append({
                'amount': -amount,
                'description':description
            })
            return True
        return False
    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item['amount']
        return balance
    def transfer(self, amount, other_category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {other_category.name}')
            other_category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False
    def check_funds(self, amount):
        return self.get_balance() >= amount
    def __str__(self):
        title = self.name.center(30, '*')
        lines = [title]
        for item in self.ledger:
            description = item["description"]
            amount = item["amount"]
            description = description[:23]
            lines.append(f"{description: <23}{amount: >7.2f}" )
        lines.append(f"Total: {self.get_balance()}")
        return "\n".join(lines)
def create_spend_chart(categories):
    
    # Tính tổng số tiền rút
    total_spent = 0
    spent_by_category = []

    for category in categories:
        spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spent += -item["amount"]
        spent_by_category.append(spent)
        total_spent += spent

    # Tính phần trăm (làm tròn xuống bội số của 10)
    percentages = []
    for spent in spent_by_category:
        percentage = int((spent / total_spent) * 100)
        percentages.append((percentage // 10) * 10)

    # Tiêu đề
    chart = "Percentage spent by category\n"

    # Vẽ cột phần trăm
    for i in range(100, -1, -10):
        chart += f"{i:>3}|"
        for percentage in percentages:
            if percentage >= i:
                chart += " o "
            else:
                chart += "   "
        chart += " \n"

    # Đường ngang
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Chiều dài tên dài nhất
    max_length = max(len(category.name) for category in categories)

    # In tên theo cột
    for i in range(max_length):
        chart += "     "
        for category in categories:
            if i < len(category.name):
                chart += category.name[i] + "  "
            else:
                chart += "   "
        if i != max_length - 1:
            chart += "\n"

    return chart