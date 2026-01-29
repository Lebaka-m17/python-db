#
# 

def print_order(name, chai_type):
    print(f"{name} orderded {chai_type} chai!")
print_order("Aman", "masala")
print_order("Hitesh", "Ginger")
print_order("Jia", "Tulsi")
#hiding
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