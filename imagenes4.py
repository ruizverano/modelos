import skimage.color as askcolor
grayimage=skcolor.rgb2gray(image)
plt.imshow(grayimage)
plt.title('1 channel image')
