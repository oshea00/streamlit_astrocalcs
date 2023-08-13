
from math import modf
import re

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

def reduceWithin(v,r):
    if v >= 0 and v <= r:
        return v
    
    if v > r:
        while v > r:
            v -= r
    else:
        while v < 0:
            v += r
    return v

def gmtToGST(y,m,d,hh,mm,ss):
    jd = julianDate(y,m,d,0,0,0)
    s = jd - 2_451_545.0
    t = s / 36_525.0
    t0 = 6.697_374_558 + (t * 2_400.051_336) + (t**2 * 0.000_025_862)
    t0Reduced = reduceWithin(t0,24)
    utDecimalHours = hmsToHours(hh,mm,ss)
    utByConstant = utDecimalHours * 1.002_737_909
    gst = reduceWithin(utByConstant + t0Reduced,24)
    gstHms = hoursToHMS(round(gst,6))
    return gstHms

def getTime(s):
  hour = 0
  minute = 0
  second = 0
  valid = False
  try:
    match = re.search("^[0-9]+\:[0-9]+\:[0-9]+\.?[0-9]*",s)
    if match:
        p = s.split(":")
        hour = int(p[0])
        minute = int(p[1])
        second = float(p[2])
        valid = True
    return hour, minute, second, valid
  except:
    return 0, 0, 0, False

def getInt(s):
  i = 0
  match = re.search("\-{0,1}[\d]+",s)
  if match:
    i = int(match[0])
  return i



