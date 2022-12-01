# Date:         December/1/2022
# Author:       Ahmed Al Ghafri

def get_3max_cal(path, n):
    # Start Time:   11:05AM
    # Finish Time:  11:10AM
    elf_bags = []
    curr_cal = 0
    with open(path, 'r') as f:
        for line in f:
            if line == '\n':
                elf_bags.append(curr_cal)
                curr_cal = 0
            else:
                curr_cal += int(line)
    elf_bags.sort(reverse=True)
    # print((elf_bags[:3]))
    return (sum(elf_bags[:n]))

def get_max_cal(path):
    # Start Time:   10:54AM
    # Finish Time:  11:04AM
    max_cal = curr_cal = 0
    with open(path, 'r') as f:
        for line in f:
            if line == '\n':
                max_cal = curr_cal if max_cal<curr_cal else max_cal
                curr_cal = 0
            else:
                curr_cal += int(line)
    return max_cal


if __name__=='__main__':
    path = 'Inputs/01.txt'
    pathTest = 'Inputs/01test.txt'
    # First Quest:
    print(f"TestCase >> Top elf calorie-wise: {get_max_cal(pathTest)}")
    print(f"ActualCase >> Top elf calorie-wise: {get_max_cal(path)}")
    # Second Quest:
    print(f"TestCase >> Top 3 elves calorie-wise: {get_3max_cal(pathTest, 3)}")
    print(f"ActualCase >> Top 3 elves calorie-wise: {get_3max_cal(path, 3)}")
    print(f"THERE IS AN ALTERNATIVE TO FIRST ANSWER NOW!!\nAlternateCase >> Top 1 elf calorie-wise using 2nd answer: {get_3max_cal(path, 1)}")
    
