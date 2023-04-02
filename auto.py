import ctypes
import time

# 获取日出日落时间
sunrise = '06:00:00'  # 假设每天早上6点日出
sunset = '18:00:00'  # 假设每天晚上6点日落

# 设置壁纸
def sunrise_sw():
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0,r"C:\Users\10497\OneDrive\图片\壁纸\sunrise_2.jpg", 0)

# 设置壁纸
def sunset_sw():
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0,r"C:\Users\10497\OneDrive\图片\壁纸\sunset_2.jpg", 0)


# 定时更换壁纸
while True:
    now = time.strftime('%H:%M:%S', time.localtime())
    print(now)
    if now >= sunrise and now < sunset:
        sunrise_sw()
        print("sunrise")
    else:
        sunset_sw()
        print("sunset")
    time.sleep(3600)  # 每隔一个小时检查一次时间