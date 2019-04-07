import math
import requests

# ROOT x, y, z, lon and lat parameters for loaction.
ROOT_X = 3429
ROOT_Y = 1676
ZOOM = 12
ROOT_ULLON = 121.376953125
ROOT_ULLAT = 31.05293398570515
ROOT_LRLON = 121.46484375
ROOT_LRLAT = 30.97760909334868

# x = 3429 + 1
# y = 1676 + 1
# z = 12


# the transformation is from openstreetmap wiki
# link:https://wiki.openstreetmap.org/wiki/Slippy_map_tilenames#X_and_Y
# convert the lon and lat to tile x, y coordinate.
# lon: the longitude in degrees
# lat: the latitude in degrees
# z: the zoom level
def convertToXY(lon, lat, z):
	n = math.pow(2, z)
	x = n * ((lon + 180) / 360)
	the = lat * math.pi / 180
	y = n / 2 * (1 - (math.log(math.tan(the) + 1 / math.cos(the))) / math.pi)
	return round(x), round(y)



# print the Lon and Lat
# z: the zoom level
# x: the tile x coordinate
# y: the tile y coordinate
def printLonLat(z, x, y):
	lon = x / math.pow(2, z) * 360 - 180
	print("longitude is {}".format(lon))
	lat_rad = math.atan(math.sinh(math.pi*(1 - 2*y/math.pow(2, z))))
	lat = lat_rad * 180.0 / math.pi
	print("latitude is {}".format(lat))


# save the picture
# z: the zoom level
# x: the tile x coordinate
# y: the tile y coordinate
# zRoot: zoom of the first tile in this level
# xRoot: x of the first tile in this level
# yRoot: y of the first tile in this level
def savePic(z, x, y, zR, xR, yR):
	img_url = "https://c.tile.openstreetmap.org/{}/{}/{}.png".format(z, x, y)
	img = requests.get(img_url)
	f = open("imgs/d{}_x{}_y{}.png".format(z - zR, x - xR, y - yR), "ab")
	f.write(img.content)
	f.close()
	print("d{}_x{}_y{}.png is downloaded".format(z - zR, x - xR, y - yR))


# main function
# get use of these functions to save the specific images
def main():
	zRoot = ZOOM
	z = 12
	while z <= 19:
		levels = int(math.pow(2, z - zRoot))
		xRoot, yRoot = convertToXY(ROOT_ULLON, ROOT_ULLAT, z)
		for i in range(levels):
			for j in range(levels):
				x = xRoot + i
				y = yRoot + j
				print("x:{}, y:{}".format(x, y))
				printLonLat(z, x, y)
				savePic(z, x, y, zRoot, xRoot, yRoot)
		print("******* z = {} finished *******".format(z))
		z += 1
	print("======= all done =======")

if __name__=="__main__":
	main()
