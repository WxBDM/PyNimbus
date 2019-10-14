from pynimbus import get_nhc_past_cyclone
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

dorian = get_nhc_past_cyclone("dorian", 2019, 24, extract_dir = "/Users/Brandon/Desktop")
lat, lon = dorian.polygon.lat_lon_to_plot()

ax = plt.axes(projection=ccrs.PlateCarree())
ax.coastlines()
plt.scatter(lat, lon)
plt.show()









