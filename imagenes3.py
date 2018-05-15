from matplotlib import pyplot
from skimage import data, io, filters, color

imagen=data.imread('uniforme.jpg')

imagen_gris=color.rgb2gray(imagen)

pyplot.hist(imagen_gris)
pyplot.xlabel('ejex')
pyplot.ylabel('ejey')
pyplot.xlabel('Distr')
