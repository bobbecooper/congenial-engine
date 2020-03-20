# main input loop

def update_cycle(cycles, user_input):
    pass


def print_new_idea(cycles):
    pass


def print_options(cycles):
    pass


cycles = []

print("Welcome to Mom's emotional stuff")
print("Enter a number to go somewhere; 0 to quit")
user_input = int(input())

while user_input != 0:
    update_cycles(cycles, user_input)
    print_new_idea(cycles)
    print_options(cycles)
    user_input = int(input())
