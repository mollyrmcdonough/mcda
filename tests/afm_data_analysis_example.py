import pySPM
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import os
from IPython import display

filenameB = "data/example_data/afm/MBE1-230404A-MS.0_00000.spm"
ScanB = pySPM.Bruker(filenameB)
ScanB.list_channels()
topoB = ScanB.get_channel('Height Sensor')

fig, ax = plt.subplots()
ScanB.get_channel('Height Sensor').show(ax=ax)
plt.show()

pixels = topoB.correct_plane().pixels
im = plt.imshow(pixels, cmap='afmhot')
plt.colorbar(im) 

# Show the figure
plt.show()

pixels = topoB.correct_plane().pixels

print("Shape of the data:", pixels.shape)
print("Min height:", np.min(pixels))
print("Max height:", np.max(pixels))
print("Mean height:", np.mean(pixels))

# fig1, ax1 = plt.subplots()
# img1 = ax1.imshow(topoB.pixels, cmap='afmhot', extent=[0, topoB.size['real']['x'], 0, topoB.size['real']['y']])
# cbar1 = plt.colorbar(img1, ax=ax1)
# cbar1.set_label('Height (nm)')
# ax1.set_xlabel('X (µm)')
# ax1.set_ylabel('Y (µm)')
# plt.show()

# topo1a = topoB.correct_lines(inline=False)
# fig3, ax3 = plt.subplots()
# img3 = ax3.imshow(topo1a.pixels,cmap='afmhot', extent=[0,topo1a.size['real']['x'],0,topo1a.size['real']['y']])
# cbar3 = plt.colorbar(img3,ax=ax3)
# cbar3.set_label('Height (nm)')
# ax3.set_xlabel('X (µm)')
# ax3.set_ylabel('Y (µm)')
# plt.show()

# filenameA= "Example Data/AFM Data/AFM2_MBE1-230404A-MS_23-414_Bi2Se3 on Al2O3 Se cap/MBE1-230404A-MS.0_00001.spm"
# ScanA = pySPM.Bruker(filenameA)
# ScanA.list_channels()
# topoA = ScanA.get_channel()

# fig2, ax2 = plt.subplots()
# img2 = ax2.imshow(topoA.pixels, cmap='afmhot', extent=[0, topoA.size['real']['x'], 0, topoA.size['real']['y']])
# cbar2 = plt.colorbar(img2, ax=ax2)
# cbar2.set_label('Height (nm)')
# ax2.set_xlabel('X (µm)')
# ax2.set_ylabel('Y (µm)')
# plt.show()

# topoB = ScanB.get_channel("Height Sensor")
# print(topoB.pixels)
# # Convert the height data to a numpy array
# height_data = np.array(topoB.pixels)

# # Calculate roughness parameters
# Ra = np.mean(np.abs(height_data))
# Rq = np.sqrt(np.mean(height_data**2))
# Rz = np.max(height_data) - np.min(height_data)

# print("Ra:", Ra, "nm")
# print("Rq:", Rq, "nm")
# print("Rz:", Rz, "nm")
