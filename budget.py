class Category:

    def __init__(self, category):
        self.category = category
        self.ledger = []

    def __str__(self):
        # what comes when the budget object is printed
        receipt_list = []
        title = self.category.center(30, "*")
        receipt_list.append(title)

        # Loops through the ledger list and appends items to the receipt
        for i in self.ledger:
            round_amount_float = "{:.2f}".format(i.get("amount"))
            round_amount = str(round_amount_float)[:7]
            round_description = i.get("description")[:23]
            list_item = f"{round_description:<23}{round_amount:>7}"
            receipt_list.append(list_item)

        self.get_balance()
        formatted_balance = "{:.2f}".format(self.get_balance())
        balance = f"Total: {formatted_balance}"
        receipt_list.append(balance)

        receipt = "\n".join(receipt_list)

        return receipt

    # Deposit method that appends amounts and descriptions to the ledger
    def deposit(self, amount, description=""):

        if description:
            # deposit = {"amount": amount, "description": description}
            self.ledger.append({"amount": amount, "description": description})
        else:
            # deposit = {"amount": amount, "description": ""}
            self.ledger.append({"amount": amount, "description": ""})

    # method that checks if the current amount in the ledger is bigger than the withdrawal
    def check_funds(self, amount):
        if amount > self.ledger[0]["amount"]:
            return False
        else:
            return True

    # method that appends negative amounts to the ledger
    def withdraw(self, amount, description=""):

        result = self.check_funds(amount)

        if result:
            if description:
                neg_amount = -1 * amount
                # withdraw = {"amount": neg_amount, "description": description}
                self.ledger.append({"amount": neg_amount, "description": description})
                return True
            else:
                neg_amount = -1 * amount
                # withdraw = {"amount": neg_amount, "description": ""}
                self.ledger.append({"amount": neg_amount, "description": ""})
                return True
        else:
            return False

    # gets current balance in the ledger
    def get_balance(self):
        balance = 0

        for i in self.ledger:
            round_amount = i.get("amount")
            balance += round_amount

        return balance

    # method that deposits for one objects and withdraws for the other
    def transfer(self, amount, dif_category):

        result = self.check_funds(amount)

        if result:
            transfer_to = f"Transfer to {dif_category.category}"
            transfer_from = f"Transfer from {self.category}"
            self.withdraw(amount, transfer_to)
            dif_category.deposit(amount, transfer_from)
            return True
        else:
            return False


def create_spend_chart(categories_list):

    total_spending_list = []

    # loops through objects in object list
    for category in categories_list:

        spent_by_cat = 0
        # loops through object ledger and adds withdrawals to a var
        for i in category.ledger:
            withdrawal_amount = i.get("amount")
            if withdrawal_amount < 0:
                spent_by_cat += withdrawal_amount

        # adds withdrawal sum by each category to a list
        total_spending_list.append(spent_by_cat)

    # sum of all category spending
    total_spending = 0
    for category_spending in total_spending_list:
        total_spending += -1 * category_spending

    # percentage by category list
    total_spending_list_by_perc = []
    for category_spending in total_spending_list:
        perc_spent = (category_spending / total_spending) * 100 * -1

        # rounding the percentage to the nearest 10
        rounded_perc = (perc_spent // 10) * 10 / 10
        total_spending_list_by_perc.append(int(rounded_perc))

    # the len of every row in the chart
    len_of_row = 5 + (len(total_spending_list) * 3)
    num_of_lines = (len(total_spending_list) * 3) + 1

    # lines after the percentages
    lines = "-" * num_of_lines
    lines_row = "    " + lines

    # template chart list with strings for percentages
    percentage_part = ["100|", " 90|", " 80|", " 70|", " 60|", " 50|", " 40|", " 30|", " 20|", " 10|", "  0|"]

    for perc in total_spending_list_by_perc:
        for i in range(len(percentage_part) - 1, len(percentage_part) - (perc + 2), -1):
            percentage_part[i] += " o "

    # adds the lines and the title to the list
    percentage_part.append(lines_row)
    title = "Percentage spent by category"
    percentage_part = [title] + percentage_part

    # turns the list of strings into 1 string
    str_percentage_part = "\n".join(percentage_part)

    # list of categories by letters
    cat_letters_list = []
    for category in categories_list:
        cat_letters = list(category.category)
        cat_letters_list.append(cat_letters)

    # category names
    cat_names_list = []
    for category in categories_list:
        cat_names_list.append(category.category)

    max_len = max(len(category) for category in cat_names_list)

    # honestly, these 2 loops are hard to explain...
    cat_in_rows = []
    for cat_letters in cat_letters_list:
        happened = 0
        for index, letters in enumerate(cat_letters):

            if len(cat_in_rows) > index and cat_in_rows[index] is not None:
                cat_in_rows[index] += f"  {letters}"
                happened = 1
            else:
                if happened == 1:
                    row = f"        {letters}"
                    cat_in_rows.append(row)
                else:
                    row = f"     {letters}"
                    cat_in_rows.append(row)

    # turns the list of strings into 1 string
    str_cat_rows = "\n".join(cat_in_rows)

    chart = f"{str_percentage_part}\n{str_cat_rows}"

    return chart

        
