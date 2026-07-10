print("2. Time Converter:")


#input
second = int(input("Tnsert second:"))

#process
hours = second // 3600
secod_remain = second %3600

minute = second_remain // 60
second_remain = secod % 60

#output

print(second, "seconds =", hour,"hour, ",minute, "minute," ,second_remain, "second")
print(f"{second} second = {hour} hour, {minute}minute, {second_remain}second")