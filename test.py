
# ===========================

print("\n=== TRAVERSING STRINGS ===")
message = "hello"
index = 0

print("Method 1: Using for loop with enumerate")
for i, char in enumerate(message):
    print(f"message[{i}] = {char}")

print("\nMethod 2: Manual indexing")
index = 0
for char in message:
    print(f"message[{index}] = {char}")
    index += 1



    
# เขียนโปรเเกรม นับจํานวนอักขระที่สนใจในข้อความที่กําหนดโดยผู้ใช้
# 1. รับข้อมูลที่กําหนดให้ผู้ใช้ (text)
# 2. รับอักขระที่สนใจจากผู้ใช้ (char)
# 3. เเสดงผลการนับอักขระที่สนใจในข้อความออกทางหน้า

# ตัวอย่างหน้าจอ
# Insert the text: Kasetsart sriracha
# Character to find: r
# 3 letters 'r' found in 'Kasetsart sriracha'

"""
print("\n=== ITERATING THROUGH STRING ===")
count = 0
text = input("Insert the text: ")
count = text = input("character to find: ")
for letter in text:
    if letter == char:
        count += 1
print(f"{count} letters '{char}' found in '{text}'")

"""
# เขียนโปรเเกรม ตรวจสอบความเเข็งเเรง password
# passworh ที่เเข็งเเรงคือ ยาวมากกว่า 8 ตัว เเละผสมกันระหว่างตัวเลข ตัวอักษร เเละอักขระพิเศษ 

# ตัวอย่างหน้อจอ
# Insert your password : Test123
# your password is not strong!

# Insert your password : Test124!
# your password is  strong!

password = input("Insert your password :")
lenght = len(password)
check = password.isalnum()

if lenght > 8 and check == False:
    print("your password is strong!")
else:
    print("your password is not strong!")


