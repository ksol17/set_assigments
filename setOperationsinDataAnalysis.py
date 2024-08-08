# Task 1: Duplicate Entries Cleanup
# List of customer IDs with duplicates
customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

# Convert the list to a set to remove duplicates
unique_customer_ids = set(customer_ids)

# Display the set of unique customer IDs
print("Unique customer IDs:", unique_customer_ids)
