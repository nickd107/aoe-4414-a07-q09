# max_bitrate.py
#
# Usage: python3 max_bitrate.py tx_w tx_gain_db freq_hz dist_km rx_gain_db n0_j bw_hz
# Calculates for maximum achievable bitrate

# Parameters:
#tx_w: transimtter power in Watts
#tx_gain_db: transmitter gain in db
#freq_hz: frequency in hz
#dist_km: transmission distance in km
#rx_gain_db: receiver gain in db
#n0_j: spectral density in joules
#bw_hz: bandwidth in hz

# Output:
#r_max: maximum bitrate

# Written by Nick Dickson

# import Python modules
import math # math module
import sys # argv

# constants
c = 2.99792458e8

# initialize script arguments
tx_w = float('nan') 
tx_gain_db = float('nan') 
freq_hz = float('nan') 
dist_km = float('nan')
rx_gain_db = float('nan')
n0_j = float('nan')
bw_hz = float('nan')

# parse script arguments
if len(sys.argv) == 8:
  tx_w = float(sys.argv[1])
  tx_gain_db = float(sys.argv[2])
  freq_hz = float(sys.argv[3])
  dist_km = float(sys.argv[4])
  rx_gain_db = float(sys.argv[5])
  n0_j = float(sys.argv[6])
  bw_hz = float(sys.argv[7])
else:
  print(\
    'Usage: '\
    'python3 max_bitrate.py tx_w tx_gain_db freq_hz dist_km rx_gain_db n0_j bw_hz'\
  )
  exit()

G_t=10**(tx_gain_db/10)
G_r=10**(rx_gain_db/10)
L_l=10**(-1/10)
L_a=10**(0/10)

N= n0_j*bw_hz
WL = c/freq_hz
C=tx_w * L_l * G_t * (WL/(4*math.pi*dist_km*1000))**2 * L_a * G_r

r_max = bw_hz * math.log(1 + C/N, 2)

print(math.floor(r_max))

