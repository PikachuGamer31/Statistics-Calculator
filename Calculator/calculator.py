import statistics

print("Made By b9803bd23b22b214707ab49402510c57b6dcbb684155b183b7d94d31a840c3a3")
print("Put in your numbers with spaces between them")
print("They no not have to be in order")
print("\n")

def main():  
    str_input = input(": ")
    lst = str_input.split()
    data = [int(x) for x in lst]
    int_min = int(min(data))
    int_max = int(max(data))

    print("\n")
    print("Data: " + str_input)
    print("Mean: " + str(statistics.mean(data)))
    print("Mode: " + str(statistics.multimode(data)))
    print("Median: " + str(statistics.median(data)))
    print("Range: " + str(int_max - int_min))
    print("\n")

while True:
    main()
