def min_dis(lst):
    mx_ele = max(lst)
    mn_ele = min(lst)
    total=mx_ele - mn_ele
    return total
def main():
    lst=list(map(int, input().split()))
    print(min_dis(lst))
main()
