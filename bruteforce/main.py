import random
import pyautogui

# สร้างชุดตัวอักษรที่ใช้เดารหัสผ่าน
character = "0123456789abcdefghijklmnopqrstuvwxyz"
character_list = list(character)

# รับรหัสผ่านจากผู้ใช้
pass_word = pyautogui.password("Enter password here:")

# เริ่มต้นตัวแปรสำหรับการเดารหัสผ่าน
guess_password = ""

while guess_password != pass_word:
    # สุ่มรหัสผ่านที่เป็นไปได้
    guess_password = "".join(random.choices(character_list, k=len(pass_word)))

    print(">>>>" + guess_password + "<<<<<")

    if guess_password == pass_word:
        print("Your Password is: " + guess_password)
        break
