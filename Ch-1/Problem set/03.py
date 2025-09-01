# Install an external module and use it to perform an operation of your interest.

# Import numpy library
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(np.mean(arr)) # Calculate the mean

import pyttsx3
engine = pyttsx3.init()
engine.say("Hey I am good")
engine.runAndWait()