from matplotlib import pyplot
from skimage import data, io, filters, color, img_as_ubyte
import ctypes
import numpy

imagen=io.imread('uniforme.jpg')

print("--------------------------------------------------------")
print("Tipo de Imagen real: ",type(imagen[0][0][0]))

#imagen2=int(imagen)

imagen_gris=color.rgb2gray(imagen)

print("Tipo de Imagen en Gris: ", type(imagen_gris[0][0]))

mascaraAmarillo=(imagen_gris > 0.82) & (imagen_gris < 0.83)

imagenUint=imagen_gris.astype(numpy.uint8)

imagenUint2=img_as_ubyte(imagen_gris)

print("Tipo de Imagen en Gris Convertida 2: ",type(imagenUint2[0][0]))

mask=imagen_gris <87
imagen_gris[mask]
print("--------------------------------------------------------")
print("valor minimo Imagen Real: ",imagen.min())
print("valor minimo Imagen en Gris: ",imagen_gris.min())
print("valor minimo Imagen Convertida: ", imagenUint.min())
print("--------------------------------------------------------")
print("valor minimo Imagen Real: ",imagen.max())
print("valor minimo Imagen en Gris: ",imagen_gris.max())
print("valor minimo Imagen Convertida: ", imagenUint.min())
print("valor minimo Imagen Convertida : ", imagenUint.max())
print("valor minimo Imagen Convertida 2: ", imagenUint2.min())
print("valor minimo Imagen Convertida 2: ", imagenUint2.max())
print("--------------------------------------------------------")
print("pixel (0,0)",imagenUint2[0,0])
print("pixel (514,638)",imagenUint2[514,638])

reddish = imagen[:, :, 0] < 140
imagen[reddish] = [255, 255, 0]

reddish = imagen_gris[0] > 160
#imagen_gris[reddish] = [255]


#pyplot.imshow(imagenUint2, cmap='gray')

pyplot.hist(imagenUint2)
pyplot.xlabel('ejex')
pyplot.ylabel('ejey')
pyplot.xlabel('Distr')

pyplot.show()
