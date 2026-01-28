# QRcode.py

import qrcode
import time
import cv2

url = 'http://www.google.com'
qr_img = qrcode.make(url)
qr_img.save(stream='./images/gg_QR.png') # stream= 생략가능

print('QRtesting~~ 저장성공') # 구글로 가는 QR코드 생성!
time.sleep(1)

image=cv2.imread('./images/gg_QR.png')
cv2.imshow('title',image)
cv2.waitKey(0) #키입력까지 대기(0)을 넣으면 무한대기
cv2.destroyAllWindows() # 모든 창 닫기

print('QRtesting~~ 열기성공')

# 에러발생 >>> ModuleNotFoundError: No module named 'qrcode'
# C:\Users\Donga\Desktop\donga AI\day0123> pip install qrcode 다운받아줘야함

# 에러발생 >>> ModuleNotFoundError: No module named ' cv2'
# C:\Users\Donga\Desktop\donga AI\day0123> pip install cv2 도 에러
# # C:\Users\Donga\Desktop\donga AI\day0123> pip install opencv-python 이것이 정답