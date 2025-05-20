def create_headers():
    # create a list of all headers
    part1 = ['unit_number', 'time_in_cycle']
    part2 = []
    for i in range(1, 4):
        part2.append(f"op_setting_{i}")
    part3 = []
    for i in range(1, 22):
        part3.append(f"sensor_{i}")
    columns = part1 + part2 + part3
    return columns
headers_listed = create_headers()



