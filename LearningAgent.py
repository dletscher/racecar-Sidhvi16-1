import pickle

class Agent:
	def __init__(self):
		self._values = {}
		self._Qvalues = {}
		
		# Constants
		self._learningRate = .1
		
	def load(self, filename):
		print('Loading data')
		with open(filename, 'rb') as dataFile:
			self._values = pickle.load(dataFile)
			self._Qvalues = pickle.load(dataFile)
		
	def save(self, filename):
		print('Saving data')
		with open(filename, 'wb') as dataFile:
			pickle.dump(self._values, dataFile)
			pickle.dump(self._Qvalues, dataFile)
		
	def chooseAction(self, observations, possibleActions):
		return possibleActions[0]
		
	def updateValues(self, observation1, action, observation2, reward):
		val = reward + self.getValue(observation2)
		self._Qvalues[self.getBin(observation1) + (action,)] = self._learningRate * val + (1-self._learningRate) * self._Qvalues[self.getBin(observation1) + (action,)]
		self._values[self.getBin(observation1)] = max([self._Qvalues[self.getBin(observation1) + a] for a in [-1,0,1]])

	def train(self, repetitions):
		pass
from MyData import load_data, save_data

class LearningAgent:
    def __init__(self):
        # Load saved coefficients or defaults at start
        self.coeffs = load_data()

    def update_coefficients(self, new_values: dict):
        # Update your coefficients with learned values
        self.coeffs.update(new_values)

    def save(self):
        # Save updated coefficients for next run
        save_data(self.coeffs)

    # Your agent logic here that updates self.coeffs as it learns...

