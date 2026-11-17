listings = [
    {"listing_id": "L1", "city": "Pune",    "price": 4500000,  "agent": "Ravi Kumar"},
    {"listing_id": "L2", "city": "Mumbai",  "price": 12000000, "agent": "Anita Desai"},
    {"listing_id": "L3", "city": "Pune",    "price": 3200000,  "agent": "Ravi Kumar"},
    {"listing_id": "L2", "city": "Mumbai",  "price": 12000000, "agent": "Anita Desai"},
    {"listing_id": "L4", "city": "Chennai", "price": 6800000,  "agent": "Mohammed Irfan"},
    {"listing_id": "L5", "city": "Mumbai",  "price": 9500000,  "agent": "Sneha Rao"},
    {"listing_id": "L6", "city": "Chennai", "price": 6800000,  "agent": "Arjun Menon"},
    {"listing_id": "L7", "city": "Pune",    "price": 5100000,  "agent": "Priya Shah"},
]


def remove_duplicates(listings):
    # Task 1: Your code here
    return []


def get_unique_cities(listings):
    # Task 2: Your code here
    return []


def sort_by_price(listings):
    # Task 3: Your code here
    return []


def count_listings_per_city(listings):
    # Task 4: Your code here
    return {}


# Do not change the code below
if __name__ == "__main__":
    unique_listings = remove_duplicates(listings)
    print(", ".join(listing["listing_id"] for listing in unique_listings))
    print(", ".join(get_unique_cities(unique_listings)))
    print(", ".join(sort_by_price(unique_listings)))
    counts = count_listings_per_city(unique_listings)
    print(", ".join(f"{city}: {counts[city]}" for city in sorted(counts)))
