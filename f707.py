l = [int(x) for x in input().split()]
l.pop()
mod_7_list, non_mod_7_list = [], []
for i in l:
    if i % 7 == 0:
        mod_7_list.append(i)
    else:
        non_mod_7_list.append(i)

if mod_7_list:
    print(max(mod_7_list, key=lambda x: (x % 70, -x)))
elif non_mod_7_list:
    print(min(non_mod_7_list, key=lambda x: (x % 77, x)))
