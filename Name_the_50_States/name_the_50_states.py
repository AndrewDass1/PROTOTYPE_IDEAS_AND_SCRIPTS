the_50_states = ["Alaska", "Texas", "California", "Montana", "New Mexico", "Arizona", "Nevada", "Colorado", "Oregon", "Wyoming", "Michigan", "Minnesota", "Utah", "Idaho", "Kansas", "Nebraska", "South Dakota", "Washington", "North Dakota", "Florida", "Oklahoma", "Missouri", "Georgia", "Wisconsin", "Illinois", "Iowa", "New York", "North Carolina", "Virginia", "Arkansas", "Alabama", "Louisana", "Mississippi", "Pennsylvania", "Ohio", "Tennessee", "Kentucky", "Maine", "Indiana", "South Carolina", "West Virginia", "Maryland", "Hawaii", "Massachusetts", "Vermont", "New Hampshire", "New Jersey", "Connecticut", "Delaware", "Rhode Island"]

the_50_states_abbreviations = ["AK", "TX", "CA", "MT", "NM", "AZ", "NV", "CO", "OR", "WY", "MI", "MN", "UT", "ID", "KS", "NE", "SD", "WA", "ND", "FL", "OK", "MO", "GA", "WI", "IL", "IA", "NY", "NC", "VA", "AR", "AL", "LA", "MS", "PA", "OH", "TN", "KY", "ME", "IN", "SC", "WV", "MD", "HA", "MA", "VT", "NH", "NJ", "CT", "DE", "RI"]

the_50_capitals = ["Juneau", "Austin", "Sacramento", "Helena", "Santa Fe", "Pheonix", "Carson City", "Denver", "Salem", "Cheyenne", "Lansing", "St. Paul", "Salt Lake City", "Boise", "Topeka", "Lincoln", "Pierre", "Olympia", "Bismarck", "Tallahassee", "Oklahoma City", "Jefferson City", "Atlanta", "Madison", "Springfield", "Des Moines", "Albany", "Raleigh", "Richmond", "Little Rock", ]


correct_state_counter = 0
correct_state_list = []

correct_capital_counter = 0
correct_capital_list = []


while correct_state_counter !=50 and correct_capital_counter !=50:
    entry = input("Enter a state or capital:")

    if entry in the_50_states and entry not in correct_state_list:
        print(entry + " is a state!")
        correct_state_counter += 1
        correct_state_list.append(entry)

    if entry in the_50_capitals and entry not in correct_capital_list:
        print(entry + " is a capital!")
        correct_capital_counter += 1
        correct_capital_list.append(entry)


for i in range(0, 50):
    num_increment = 0
    print(the_50_states[num_increment])
    print(the_50_states[num_increment])

for i in range(0, 50):
    num_increment_2 = 0
    print(correct_state_list[num_increment_2])
    print(correct_capital_list[num_increment_2])
