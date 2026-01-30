#
# reusabaility

def print_order(name, chai_type):
    print(f"{name} orderded {chai_type} chai!")
print_order("Aman", "masala")
print_order("Hitesh", "Ginger")
print_order("Jia", "Tulsi")
#complex
def fetch_sales():
    print("Fetching the sales data")
def filter_valid_sales():
    print("Filtering valid sales data")
def summarize_data():
    print("Summarizing sales data")
def generate_report():
    fetch_sales()
    filter_valid_sales()
    summarize_data()
    print("Report is ready")
generate_report()
#hiding
def get_input():
    print("Getting user input")
def validate_input():
    print("Validating the user info")
def save_to_db():
    print("saving to database")
def register_user():
    get_input()
    validate_input()
    save_to_db()
    print("User registration complete")
register_user()
#readability
def calculate_bill(cups, price_per_cup):
    return cups * price_per_cup
my_bill = calculate_bill(3, 15)
print(my_bill)
print("Order for table 2: ", calculate_bill(2, 50))
#trace
def add_vat(price, vat_rate):
    return price * (100 + vat_rate)/100
orders = [100, 150, 200]
for price in orders:
    final_amount = add_vat(price, 10)
    print(f"Original: {price}, Final with VAT: {final_amount}")