from matplotlib import pyplot
from skimage import data, io, filters, color

#programa para manipular imagenes

imagen=data.imread('uniforme.jpg')

imagen_gris=color.rgb2gray(imagen)

imagen2=data.chelsea()

mascara1=(imagen_gris > 0.82) & (imagen_gris < 0.83)
mask=imagen_gris <87
imagen_gris[mask]

reddish = imagen[:, :, 0] < 180
imagen[reddish] = [255, 255, 0]

#reddish = imagen_gris[0] > 160
imagen_gris[reddish] = [255]

pyplot.imshow(imagen)
pyplot.show()
