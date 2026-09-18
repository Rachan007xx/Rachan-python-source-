try:
     num1 = float(input("ตัวเลขที่ 1: "))
     num2 = float(input("ตัวเลขที่ 2: "))
     operators = input("เครื่องหมาย(+,-,*,/):")


     result = 0
     if  operators == "+":
      result = num1 + num2
     elif operators == "+":
      result = num1 - num2
     elif operators == "+":
      result = num1 * num2
     elif operators == "+":
      result = num1 / num2


     print(f"{num1} {operators} {num2} = {result}")
except ValueError:
    print("กรุณากรอกตัวเลขเท่านั้น")

except ZeroDivisionError:
    print("ไม่สามารถหารด้วยศูนย์ได้")

else:
  print("ทํางานได้สมบูรณ์")

finally:
  print("จบการทํางาน")

    



