<<<<<<< Updated upstream

=======
"""
State names in a dictionary
"""
>>>>>>> Stashed changes
STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales",
               "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria",
               "TAS": "Tasmania"}
<<<<<<< Updated upstream
# print(STATE_NAMES)

for state in STATE_NAMES:
    print(state, "is", STATE_NAMES[state])
=======

for key, value in STATE_NAMES.items():
    print('{:<3} is {}'.format(key, value))
>>>>>>> Stashed changes

state = input("Enter short state: ").upper()
while state != "":
    if state in STATE_NAMES:
        print(state, "is", STATE_NAMES[state])
    else:
        print("Invalid short state")
    state = input("Enter short state: ").upper()
<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
