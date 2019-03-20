## open street map images crawler in Python3

- this crawler is for downloading the map images from the [open steet map](https://www.openstreetmap.org).
- it is based on Python3 and requests module.
- the transformation of the image tilename and its longitude and latitude is based on [osm wiki](https://wiki.openstreetmap.org/wiki/Slippy_map_tilenames#X_and_Y).
- in this project the crawler is only for the distribution which is covered by another project of mine, and if you want to assign another area, just change the ROOT_XXX parameters if you like, but make sure you have checked the spot's longitude and latitude are correct, otherwise the transformation would give you a wrong tilename which would be illegal for querying the open street map server.
- make sure you have well known about the open street map parameters, like zoom level, tilename before using this crawler to download another area's map images.
- the downloaded images are 256x256 pixels, and will be named as "dXX_xXX_yXX.png", which is for differrent zoom levels and blocks.
- the other .xml file in this repository is the open street map data file corresponding to the area I need to query, it can be downloaded from [this](https://download.bbbike.org/osm/).