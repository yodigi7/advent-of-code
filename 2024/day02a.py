def is_all_increasing(lst):
    return all(x < y for x, y in zip(lst, lst[1:]))

def is_all_decreasing(lst):
    return all(x > y for x, y in zip(lst, lst[1:]))

def is_within_three(lst):
    return all(abs(x-y) <= 3 for x, y in zip(lst, lst[1:]))

if __name__ == "__main__":
    with open('day02.txt', 'r') as inputfile:
        safe_report_count = 0
        i = -1
        for line in inputfile.readlines():
            i += 1
            report = [int(x) for x in line.split(" ")]
            if (len(report) <= 1):
                print(f"{i}: {safe_report_count}")
                safe_report_count += 1
                continue
            if report[0] < report[1] and is_all_increasing(report) and is_within_three(report):
                print(f"{i}: {safe_report_count}")
                safe_report_count += 1
            elif report[0] > report[1] and is_all_decreasing(report) and is_within_three(report):
                print(f"{i}: {safe_report_count}")
                safe_report_count += 1
    print(f"Safe reports: {safe_report_count}")