"""*************************************
Created By Vecsei Gabor
Blog: https://gaborvecsei.wordpress.com/
Email: vecseigabor.x@gmail.com
https://github.com/gaborvecsei
*************************************"""

"""**************SUMMARY****************
With this code you can train a Perceptron and
classify data with it. (only linearly separable).

Here you can find about the background and math:
https://en.wikipedia.org/wiki/Perceptron
http://lcn.epfl.ch/tutorial/english/perceptron/html/learning.html
*************************************"""

from pylab import rand,norm
import matplotlib.pyplot as plt
import time


def Perceptron(data):
	#Weights
	w = [0,0]
	print "Init weights of the perceptron: " + str(w)
	#Learning rate
	lr = 0.1
	print "Learning rate of the perceptron:" + str(lr)

	#Training
	trained = False
	startTime = time.clock()
	while not trained:
		error = 0.0
		for x in data:
			#Dot product, this is the response
			y = x[0]*w[0]+x[1]*w[1]
			if y >= 0:
				y = 1
			else:
				y = -1
			#This is the iteration error for each data
			epsilon = x[2] - y
			if epsilon != 0:
				#Update the weights: w(k+1) = w(k) + learningRate * epsilon * x
				w[0] = w[0] + lr * epsilon * x[0]
				w[1] = w[1] + lr * epsilon * x[1]
				error += abs(epsilon)
			#We have to stop with the training
		if error == 0.0:
			trained = True
			print "Training is done"
			print "The correct weights: " + str(w)
			print "Training is completed in: " +  str(time.clock() - startTime) + " secs!"
			return w

#Linearly separable datasets
data_one = [[-1,-1,-1],
			[1,1,1],
			[0.5,1,1],
			[1,0.5,1]]

data_two = [[1,1,1],
			[-1,1,-1],
			[1,0,1],
			[-0.5,0.5,-1],
			[-1,0,-1]]

def main():
	#First we train the classifier to get the correct weights
	w = Perceptron(data_two)

	for x in data_two:
		#Get the responses with the correct weights
		y = x[0]*w[0]+x[1]*w[1]
		if y >= 0:
			y = 1
		else:
			y = -1

		if y == 1:
			plt.plot(x[0],x[1],'xb')
		else:
			plt.plot(x[0],x[1],'or')

	#Setting the range of the plot
	plt.ylim(-2, 2)
	plt.xlim(-2, 2)
	plt.show()

if __name__ == "__main__":
    main()