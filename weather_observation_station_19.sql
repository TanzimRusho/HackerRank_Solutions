select round(sqrt((min(lat_n) - max(lat_n))*(min(lat_n) - max(lat_n)) + (min(long_w) - max(long_w))*(min(long_w) - max(long_w))), 4) 
from station;
