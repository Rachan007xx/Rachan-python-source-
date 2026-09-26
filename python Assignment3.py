def deposit(money):
    wallet = 1000
    print(f"ยอดเงินเริ่มต้น: {wallet} บาท")
    try:
        amount = float(money)
        if amount <= 0:
            raise ValueError("จำนวนเงินฝากต้องมากกว่า 0")
    except ValueError as e:
        print(f"\nเกิดข้อผิดพลาด: {e}")
    except:
        print("\nเกิดข้อผิดพลาด: กรุณากรอกตัวเลขเท่านั้น")
    else:
        wallet += amount
        print("\nฝากเงินสำเร็จ")
        print(f"ยอดเงินคงเหลือ: {wallet:.2f} บาท")
    finally:
        print("สิ้นสุดรายการฝากเงิน")

# ทดลองเรียกใช้งาน
deposit_money = input("กรอกจำนวนเงินที่ต้องการฝาก: ")
deposit(deposit_money)
