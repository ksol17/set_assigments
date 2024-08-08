# Task 1:  Flight Route Comparison

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

while True:
    print("\nFlight Route Comparison Menu:")
    print("1. Show destinations both airlines fly to")
    print("2. Show destinations unique to our airline")
    print("3. Show all destinations that neither airline shares")
    print("4. Exit the program")

    choice = input("Please enter the number of your choice: ").strip()

    if choice == "1":
        # 1. Destinations that both airlines fly to
        common_destinations = our_routes.intersection(competitor_routes)
        print("Destinations both airlines fly to:", common_destinations)
    elif choice == "2":
        # 2. Destinations unique to our airline
        unique_our_routes = our_routes.difference(competitor_routes)
        print("Destinations unique to our airline:", unique_our_routes)
    elif choice == "3":
        # 3. Destinations that neither airline shares
        all_destinations = our_routes.union(competitor_routes)
        unique_to_both = all_destinations.difference(our_routes.intersection(competitor_routes))
        print("Destinations that neither airline shares:", unique_to_both)
    elif choice == "4":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")
