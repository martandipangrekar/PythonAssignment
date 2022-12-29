list_a = ["car", "place", "tree", "under", "grass", "price"]

remove_items_containing_a_or_A = lambda x: 'a' not in x and 'A' not in x


filtered_list = filter(remove_items_containing_a_or_A, list_a)

filtered_list = list(filtered_list)
print(filtered_list)
