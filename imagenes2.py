from matplotlib import pyplot
from skimage import data, io, filters, color

imagen=data.imread('uniforme.jpg')

imagen_gris=color.rgb2gray(imagen)

mask1 = (imagen_gris > 0.82) & (imagen_gris < 0.85)

mask2 = (imagen > 0.82) & (imagen < 0.85)


pyplot.imshow(imagen_gris, cmap='gray')
pyplot.show()
