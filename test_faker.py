# test_facker.py

import qrcode
import cv2
from faker import Faker

# 에러발생 >>> ModuleNotFoundError: No module named 'faker'
# C:\Users\Donga\Desktop\donga AI\day0123> pip install faker 다운받아줘야함

my=Faker()
for k in range(10):
    print(my.name())

print()
for k in range(10):
    print(my.ipv4_private())

print()
data=Faker('ko_KR') # 한국어로 출력해줌
for k in range(20):
    print(data.address())