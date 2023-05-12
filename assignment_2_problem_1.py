
#   Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuple

# Take input from the user 

mine_list = []
n = int(input("Enter the number of tuples: "))
print("Enter the tuples in the format (x, y): ")
for i in range(n):
    tuple_input = input()
    tuple_values = tuple(map(int, tuple_input.strip('()').split(',')))
    mine_list.append(tuple_values)

# Sort the list 
for i in range(len(mine_list)):
    for j in range(len(mine_list) - i - 1):
        if mine_list[j][-1] > mine_list[j+1][-1]:
            mine_list[j], mine_list[j+1] = mine_list[j+1], mine_list[j]

# Print the sorted list
print("Sorted List in increasing order:", mine_list)