class Category:
  def __init__(self,category):
    self.category = category
    self.ledger = []
  def __str__(self):
    ## for the title
    start = round(len(self.category)/2)
    string = ""
    for i in range(15-start):
      string+="*"
    string+=self.category
    for i in range(15-abs(start-len(self.category))):
      string+="*"
    string+="\n"
    #for the items part
    padding = "                              "
    for item in self.ledger:
        amount_len = len("%.2f" % item["amount"])
        description_len = len(item["description"])
        if description_len > 30 - (amount_len+1):
          string+=item["description"][0:(30 - (amount_len+1))]
          string+=" "
        else:
          string+=item["description"]
          string+=padding[description_len:30-amount_len]
        string+="%.2f" % item["amount"]
        string+="\n"    
    string+="Total: "+str(self.get_balance())
    return string
    

  def deposit(self, amount, description=""):
    self.ledger.append({"amount":amount, "description":description})

  def withdraw(self, amount, description=""):
    have_funds = self.check_funds(amount)
    if have_funds == True:
      self.ledger.append({"amount":amount*-1, "description":description})
      return True
    else:
      return False

    
  def get_balance(self):
    total = 0
    for item in self.ledger:
      total += item["amount"]
    return total
    
  def transfer(self, amount, destination):
    have_funds = self.check_funds(amount)
    if have_funds == False:
      return False
    else:
      self.withdraw(amount, "Transfer to "+ destination.category)
      destination.deposit(amount, "Transfer from "+self.category)
      return True

  def check_funds(self, amount):
    return False if  amount > self.get_balance() else True
def create_spend_chart(categories):
  string = "Percentage spent by category\n"
  total_spent = 0
  spent_per_category = {}
  # calculation of total spent and spent per category
  for category in categories:
    spent_per_category[category.category] = 0 # create a dictionary for each spent by the category
    for i in range(len(category.ledger)):
      if category.ledger[i]["amount"] < 0:
        spent_per_category[category.category] += category.ledger[i]["amount"] * -1
    total_spent += spent_per_category[category.category] 
  percentage = {}
  for category in spent_per_category.keys():
    percentage[category] = round((spent_per_category[category]/total_spent)*100, -1)
  #creation of the chart
  for percent in range(100,-10,-10):
    if percent == 100:
      string += str(percent) + "| "
    elif percent < 100 and percent > 0:
      string += " " +str(percent) + "| "
    else:
      string += "  " +str(percent) + "| "      
    for category in percentage.keys():
      if percentage[category] >= percent:
        string += "o  "
      else:
        string += "   "
    string += "\n"
  padding = "----------------------------"
  string += "    "
  string += padding[0:(len(categories)*3)+1] + "\n"
  #creation of the labels
  for i in range(len(max(percentage.keys()))):
    string += "     "
    key = list(percentage.keys())
    for j in range(len(categories)):
      if i < len(key[j]) :
        string += key[j][i] + "  "
      else:
        string += "   "
    if i == len(max(percentage.keys())) -1:
      continue
    else:
      string += "\n"
  return string


food = Category("Food")
entertainment = Category("entertainment")
food.deposit(10.05, "deposit")
food.deposit(900, "deposit")
food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
food.transfer(20, entertainment)
entertainment.deposit(200)
entertainment.withdraw(200)
print(food.ledger)
print(food)
print(food.check_funds(20))
print(create_spend_chart([food,entertainment]))