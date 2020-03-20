from Cycle import Cycle

my_cycle = Cycle()

# main input loop
my_cycle.print_options()
user_input = int(input())

while user_input != 0:
    my_cycle.update_cycle(user_input)
    my_cycle.print_new_idea()
    my_cycle.print_options()
    user_input = int(input())
