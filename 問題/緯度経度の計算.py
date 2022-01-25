# ある都市の緯度 latitude、経度 longitude が与えられるので、
# 赤道（equator）、本初子午線（prime meridian）を基準として、
# その都市が東西南北どこに位置しているかを文字列で返す、
# calculateLocation という関数を作成してください。
# 文字列は「緯度/経度」の順で表記してください。

def calculateLocation(latitude, longitude):
    print(f"{nort_or_south(latitude)}{west_or_east(longitude)}")

def nort_or_south(latitude):
    if latitude == 0:
      str = 'equator/'
    elif latitude > 0:
      str = 'north/'
    else :
      str = 'south/'
    return str


def west_or_east(longitude):
    if longitude == 0:
      str = 'prime meridian'
    elif longitude > 0:
      str = 'east'
    else:
      str = 'west'
    return str




# 入力のデータ型： double-float latitude, double-float longitude

# 出力のデータ型： string

calculateLocation(77.147489,0) #--> north/prime meridian
calculateLocation(-55.78774,0) #--> south/prime meridian
calculateLocation(-36.615626,68.130625) #--> south/east
calculateLocation(9.236204,-25.806614) #--> north/west
calculateLocation(-29.998979,-19.74947) #--> south/west
calculateLocation(0,0) #--> equator/prime meridian