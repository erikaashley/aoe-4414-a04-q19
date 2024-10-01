# ecef_to_eci.py
#
# Usage:  python3 ecef_to_eci.py year month day hour minute second ecef_x_km ecef_y_km ecef_z_km
#  
# Parameters:
# inputs date year, month, day, hour, minute, second and ECEF position ecef_x_km ecef_y_km ecef_z_km in km
# Output:
# outputs ecef coordinates eci_x_km eci_y_km eci_z_km in km 
#
# Written by Erika Ashley
# Other contributors: None
#


# import Python modules
# e.g., import math # math module
import sys # argv
import math 

# "constants"
R_E_KM = 6378.137
E_E    = 0.081819221456
w      = 7.292115*10**-5
# helper functions

## function description
# def calc_something(param1, param2):
#   pass

# initialize script arguments
yr = float('nan') # year
mth = float('nan') # month
day = float('nan') # day
hr = float('nan') # hour
min = float('nan') # minute
sec = float('nan') # second
ecef_x_km=float('nan') # ECI x position in km
ecef_y_km=float('nan') # ECI y position in km
ecef_z_km=float('nan') # ECI z position in km

# parse script arguments
if len(sys.argv)==10:
  yr = float(sys.argv[1])
  mth = float(sys.argv[2])
  day = float(sys.argv[3])
  hr = float(sys.argv[4])
  min = float(sys.argv[5])
  sec = float(sys.argv[6])
  ecef_x_km=float(sys.argv[7])
  ecef_y_km=float(sys.argv[8])
  ecef_z_km=float(sys.argv[9]) 
else:
  print(\
   'Usage: '\
   ' python3 ecef_to_eci.py year month day hour minute second ecef_x_km ecef_y_km ecef_z_km'\
  )
  exit()

# write script below this line
JD=(day-32075)+int(1461*(yr+4800+int((mth-14)/12))/4)+int(367*(mth-2-int((mth-14)/12)*12)/12)-int(3*int((int(yr+4900+(mth-14)/12)/100))/4)
JDmid=JD-0.5
Dfrac=(sec+60*(min+60*hr))/86400
jd_frac=JDmid+Dfrac
T_uti=(jd_frac-2451545.0)/36525
gmsta=67310.54841+(876600*60*60+8640184.812866)*T_uti+0.093104*(T_uti**2)-(6.2*10**-6)*(T_uti**3)
gmst1=gmsta%86400
gmstrad=-w*gmst1


ecef_vect=[ecef_x_km,ecef_y_km,ecef_z_km]
zrotatinv=[[math.cos(gmstrad),math.sin(gmstrad),0],[-math.sin(gmstrad),math.cos(gmstrad),0],[0,0,1]]

eci_vect=[0,0,0]
for i in range(3):
    for j in range(3):
        eci_vect[i]+=zrotatinv[i][j]*ecef_vect[j]

print(eci_vect[0])
print(eci_vect[1])
print(eci_vect[2])
