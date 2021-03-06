import random as rd
import matplotlib.pyplot as plt
import numpy as np

size_siml = 1000000
marble_data = ['R', 'R', 'R', 'R', 'R', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'G', 'G', 'G', 'G']
# The above array is an array of characters, 'R' representing the event of choosing a red marble, 'W' representing the event of choosing a white marble,
# 'G' representing the event of choosing a green marble. There are 5 'R's, 8 'W's, 4 'G's.
unique_marbles = ["Red", "White", "Not Green"]
numb_red = numb_white = numb_green = 0
#The above variables are going to store the number of red, white and green marbles we will be getting in the simulations 
#The for loop goes through 1000000 iterations. 
for i in range(size_siml):
  sim_itr = rd.randint(0, 16)
  if(marble_data[sim_itr] == 'R'):
    numb_red += 1
  elif(marble_data[sim_itr] == 'W'):
    numb_white += 1
  else:
    numb_green += 1
  
  
# The variables below store the probability values based on simulations  
prob_red = numb_red / size_siml
prob_white = numb_white / size_siml
prob_notGreen = 1 - (numb_green / size_siml)
#Creating an array to store the probabilities
probabilities_simu = [prob_red, prob_white, prob_notGreen]

print(" The following results are obtained from simulations")
print(f"(a) Choosing a red marble has a probability of : {probabilities_simu[0]}")
print(f"(b) Choosing a white marble has a probability of : {probabilities_simu[1]}")
print(f"(c) Choosing a not green has a probability of : {probabilities_simu[2]}")

print()
print("The following results are obtained theoretically")
print("(a) Choosing a red marble has a probability of : 0.294118")
print("(b) Choosing a white marble has a probability of : 0.470589")
print("(c) Choosing a not green has a probability of : 0.764706")


print("Drawing the comparison graphs with conditions on x-axis, probabilities on y-axis, blue bar representing simulations and orange bar representing theoretical value")
probabilities_theor = [0.294118, 0.470589, 0.764706]
x_axis = list(unique_marbles)
# Number of pairs of bars
N = 3
# Positions of bars on x-axis
ind = np.arange(N)
# Width of bars
width = 0.3
#Plotting two bar graphs 
plt.bar(ind, probabilities_simu , width, label="Simulations' data")
plt.bar(ind + width, probabilities_theor, width, label='Theoretical data')
#Labels on x-axis, y-axis and the title.
plt.xlabel('---Conditions---')
plt.ylabel('---Probabilities---')
plt.title('Comparison plot between simulated and theoretical estimations.')

plt.xticks(ind + width / 2, x_axis)
plt.legend(loc='best')
plt.show()
