range_input=int(input("Enter range input:"))
largest_no=0
smallest_no=0
for each in range(1,range_input,5):
    if each>largest_no:
        largest_no=each
for each in range(1,range_input,5):
    if each<smallest_no:
        smallest_no=each
print(largest_no,"is a Largest Number")
print(smallest_no,"is a Smallest Number")


# input=[20,40,60,80,90,100]
# largest_no=0
# for each in input:
#     if each>largest_no:
#         largest_no=each
# print(largest_no,"is a largest number")