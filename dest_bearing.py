from geographiclib.geodesic import Geodesic

def dest_bearing(ini_p, dest_p):
	lat1, lat2 = ini_p[0], dest_p[0]
	long1, long2 = ini_p[1], dest_p[1]
	brng = Geodesic.WGS84.Inverse(lat1, long1, lat2, long2)['azi1']
	return brng



ini_p = (23.211077764070467, 79.95616785156247)
dest_p = (23.211042345773805, 79.96337762939454)

# print(dest_bearing(ini_p, dest_p))