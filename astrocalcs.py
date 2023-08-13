
from math import modf

def easter_date(year):
    _, a = divmod(year,19)
    b, c = divmod(year,100)
    d, e = divmod(b,4)
    f, _ = divmod(b+8,25)
    g, _ = divmod(b-f+1,3)
    _, h = divmod(19*a + b - d - g + 15,30)
    i, k = divmod(c,4)
    _, l = divmod(32 + 2*e + 2*i - h - k,7)
    m, _ = divmod(a + 11*h + 22*l, 451)
    n, p = divmod(h + l - 7*m + 114,31)
    month = n
    day = p + 1
    return month, day

def divmod(dividend, divisor):
    d = dividend/divisor
    return int(d), dividend-int(d)*int(divisor)

def hoursToHMS(hours):
    frachour, hours = modf(hours)
    fracmin, minutes = modf(frachour * 60)
    seconds = round(fracmin * 60, 7)
    return hours, minutes, seconds

def hmsToHours(hh,mm,ss):
    return hh + (mm + ss / 60) / 60

def julianDate(y,m,d,hh,mm,ss):
    yp = y
    mp = m
    d = d + hmsToHours(hh,mm,ss) / 24
    if m==1 or m==2:
        yp = y - 1
        mp = m + 12
    a, b, c = 0, 0, 0
    if int(y)*10000+int(m)*100+int(d) >= 15821015:
        a = int(yp/100)
        b = 2 - a + int(a/4)
    if yp < 0:
        c = int(365.25 * yp - 0.75)
    else:
        c = int(365.25 * yp)
    D = int(30.6001 * (mp + 1))
    return round(b + c + D + d + 1_720_994.5,4)

def modifiedJulianDate(y,m,d,hh,mm,ss):
    return round(julianDate(y,m,d,hh,mm,ss) - 2_400_000.5,4)




