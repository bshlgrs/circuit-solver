# helpers

def difference(list1,list2):
    return sum(abs(list1[x]-list2[x]) for x in range(len(list1)))

def wait():
    raw_input("\nPress enter to continue")
    print "\n\n"
    return

rounding_length= 6

max_loop_length = 5
