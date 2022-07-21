# example of loading the cifar10 dataset
from matplotlib import pyplot
from keras.datasets import cifar10



# load train and test dataset
def load_dataset():
	# load dataset
	(trainX, trainY), (testX, testY) = cifar10.load_data()

	# one hot encode target values
	trainY = to_categorical(trainY)
	testY = to_categorical(testY)
    
	return trainX, trainY, testX, testY


if __name__ == "__main__":
    # load dataset
    trainX, trainy, testX, testy = load_dataset()

    # summarize loaded dataset
    print('Train: X=%s, y=%s' % (trainX.shape, trainy.shape))
    print('Test: X=%s, y=%s' % (testX.shape, testy.shape))

    # plot first few images
    for i in range(9):
        # define subplot
        pyplot.subplot(330 + 1 + i)
        # plot raw pixel data
        pyplot.imshow(trainX[i])

    # show the figure
    pyplot.show()
