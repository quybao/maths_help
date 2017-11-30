import sys

'''
This is a helper function to determine how many times
an n th box is worked on given certain number of passes
'''
def times_box_worked_on(box_num, pass_num):
    # if box_num is divisible by a number, it will be 
    # worked on during that pass. For example,
    # if we go through the boxes 5 times(or 5 passes)
    # box number 6 will be worked on during pass 1, pass 2
    # and pass 3
    # Since everything is divisible by 1, we do not 
    # check for that and start our counter at 1
    counter = 1

    # range function will stop before the upper  limit
    # ie range(2,5) will give us [2,3,4] so we need to 
    # add 1 to the upper limit
    for i in range(2, pass_num + 1):
        if box_num % i == 0:
            counter += 1;

    # the % (module) operator gives us the remainder
    # of a division. So if the remainder is 0 (==,the equal operator),
    # then box_num is divisible by i

    return counter

# Just a few quick unit tests to make sure 
# our helper function works correctly. Let's use box number 12

# if we do 1 pass, box 12 will be worked on once.
assert(times_box_worked_on(12, 1) == 1)

# if we do 2 passes, box 12 will be worked on during pass 1 and 2
assert(times_box_worked_on(12, 2) == 2)

# if we do 3 passes, box 12 will be worked on during pass 1,2, and 3
assert(times_box_worked_on(12, 3) == 3) 

# if we do 5 passes, box 12 will be worked on during pass 1,2,3 and 4
assert(times_box_worked_on(12, 5) == 4) 

# if we do 10 passes, box 12 will be worked on during pass 1,2,3,4 and 6
assert(times_box_worked_on(12, 10) == 5)


# Main program starts here

# First we read in the parameters from command line
# They will be in a list with starting index of 0
params = sys.argv

# params[0] contains program name
# params[1] contains number of boxes
# params[2] contains number of passes that we work on the boxes

if len(params) != 3:
    print("Usage: python puzzle.py <number_of_boxes> <number_of_passes>")

# parameters will be of type "string", we need to convert them to 
# numbers so we can use math operations.
num_boxes = int(params[1])
num_passes = int(params[2])

# Use a counter to keep track of number of open boxes
open_box_count = 0;

# Assuming the boxes are initially closed, if a box is worked on
# an even number of times, it will remain closed. If it is worked on
# an odd number of times, it will be open.
for box_num in range(1, num_boxes + 1):
    time_worked_on = times_box_worked_on(box_num, num_passes)
    if time_worked_on % 2 == 0:
        print("Box %s is closed" % box_num)
    else:
        print("Box %s is open" % box_num)
        open_box_count += 1

print("Total of opened boxes is: %s" % open_box_count)
