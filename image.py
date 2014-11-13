import numpy
import matplotlib.pyplot as pyplot
import matplotlib.image

# A simple helper library for computer vision
# Note: image coordinates are (y, x) in (height, width)

def read(path):
	return numpy.array(matplotlib.image.imread(path), dtype = numpy.float32)

def write(path, image):

	dimensions = len(image.shape)

	if (dimensions == 2):
		matplotlib.image.imsave(path, image, cmap = pyplot.get_cmap('gray'))
	else:
		matplotlib.image.imsave(path, image)

def show(image, title = None, block = True):
	
	dimensions = len(image.shape)

	if title is not None:
		pyplot.title(title)

	if (dimensions == 2):
		pyplot.imshow(image, cmap = pyplot.get_cmap('gray'))
	else:
		pyplot.imshow(image)

	pyplot.show(block = block)

def normalize(image):

	image_min = numpy.min(image)
	image_max = numpy.max(image)
	image_range = image_max - image_min

	image -= image_min

	if (image_range > 0):
		image /= (image_max-image_min)

	return image

def greyscale(image):

	dimensions = len(image.shape)

	if (dimensions != 2):
		image = numpy.dot(image[..., range(3)], [0.299, 0.587, 0.144])

	return normalize(image)

def neighbours(image, yy, xx, size, roll = False):

	if roll:

		# Given an image
		# Return an NxN array whose "center" element is arr[y,x]

		image = numpy.roll(image, shift = 1-yy, axis = 0)
		image = numpy.roll(image, shift = 1-xx, axis = 1)

		span = 1 + 2*size

		return image[:span, :span]

	else:
		
		return numpy.transpose(image[range(yy-size, yy+size+1)])[range(xx-size, xx+size+1)]
