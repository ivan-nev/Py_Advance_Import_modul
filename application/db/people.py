from datetime import datetime, timedelta

def get_employees():
    print("Все уволены")

def Lion():
    dn = datetime.now()
    dz = dn.strftime('%H:%M:%S')
    print(f'сейчас {dz}')
    # dn = datetime(2022, 9, 5, 21, 0, 0, 456)
    dc = datetime(dn.year, dn.month, dn.day, 23, 00, 00)
    do = datetime(dn.year, dn.month, dn.day, 8, 00, 00)
    delta = (dc - dn)
    if delta.seconds > (8 * 60 * 60):
        print(f"До открытия Лиона {(do - dn)/1000000*1000000}")
    else:
        print(f'До закрытия Лиона {(dc - dn)/1000000*1000000}')