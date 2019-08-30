"""Assess a betting strategy.  		   	  			  	 		  		  		    	 		 		   		 		  
  		   	  			  	 		  		  		    	 		 		   		 		  
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		   	  			  	 		  		  		    	 		 		   		 		  
Atlanta, Georgia 30332  		   	  			  	 		  		  		    	 		 		   		 		  
All Rights Reserved  		   	  			  	 		  		  		    	 		 		   		 		  
  		   	  			  	 		  		  		    	 		 		   		 		  
Template code for CS 4646/7646  		   	  			  	 		  		  		    	 		 		   		 		  
  		   	  			  	 		  		  		    	 		 		   		 		  
Georgia Tech asserts copyright ownership of this template and all derivative  		   	  			  	 		  		  		    	 		 		   		 		  
works, including solutions to the projects assigned in this course. Students  		   	  			  	 		  		  		    	 		 		   		 		  
and other users of this template code are advised not to share it with others  		   	  			  	 		  		  		    	 		 		   		 		  
or to make it available on publicly viewable websites including repositories  		   	  			  	 		  		  		    	 		 		   		 		  
such as github and gitlab.  This copyright statement should not be removed  		   	  			  	 		  		  		    	 		 		   		 		  
or edited.  		   	  			  	 		  		  		    	 		 		   		 		  
  		   	  			  	 		  		  		    	 		 		   		 		  
We do grant permission to share solutions privately with non-students such  		   	  			  	 		  		  		    	 		 		   		 		  
as potential employers. However, sharing with other current or future  		   	  			  	 		  		  		    	 		 		   		 		  
students of CS 7646 is prohibited and subject to being investigated as a  		   	  			  	 		  		  		    	 		 		   		 		  
GT honor code violation.  		   	  			  	 		  		  		    	 		 		   		 		  
  		   	  			  	 		  		  		    	 		 		   		 		  
-----do not edit anything above this line---  		   	  			  	 		  		  		    	 		 		   		 		  
  		   	  			  	 		  		  		    	 		 		   		 		  
Student Name: Jie Lyu		   	  			  	 		  		  		    	 		 		   		 		  
GT User ID: jlyu31	   	  			  	 		  		  		    	 		 		   		 		  
GT ID: 903329676	   	  			  	 		  		  		    	 		 		   		 		  
"""  		   	  			  	 		  		  		    	 		 		   		 		  
		   	  			  	 		  		  		    	 		 		   		 		  
import numpy as np

# print the whole matrix without scientific formatting
np.set_printoptions(threshold = np.nan, suppress = True)		   	  			  	 		  		  		    	 		 		   		 		  
  		   	  			  	 		  		  		    	 		 		   		 		  
def author():  		   	  			  	 		  		  		    	 		 		   		 		  
        return 'jlyu31' 		   	  			  	 		  		  		    	 		 		   		 		  
  		   	  			  	 		  		  		    	 		 		   		 		  
def gtid():  		   	  			  	 		  		  		    	 		 		   		 		  
	return 903329676  		   	  			  	 		  		  		    	 		 		   		 		  
  		   	  			  	 		  		  		    	 		 		   		 		  
def get_spin_result(win_prob):  		   	  			  	 		  		  		    	 		 		   		 		  
	result = False  	
	if np.random.random() <= win_prob:  		   	  			  	 		  		  		    	 		 		   		 		  
		result = True  		   	  			  	 		  		  		    	 		 		   		 		  
	return result  		   	  			  	 		  		  		    	 		 		   		 		  
  		   	  			  	 		  		  		    	 		 		   		 		  
def test_code():  		   	  			  	 		  		  		    	 		 		   		 		  
	win_prob = 9/19 # set appropriately to the probability of a win  		   	  			  	 		  		  		    	 		 		   		 		  
	np.random.seed(gtid()) # do this only once  		   	  			  	 		  		  		    	 		 		   		 		  
	#print(get_spin_result(win_prob)) # test the roulette spin     

	print(exp1_1(win_prob))
	  			  	 		  		  		    	  			  	 		  		  		    	 		 		   		 		  
		    	 		 		   		 		     	  			  	 		  		  		    	 		 		   		 		  
	# add your code here to implement the experiments

# for exp1 bankroll will be None
# returns a 1d array of length 300
def simulator(win_prob, has_bankroll, bankroll):
	result_array = np.zeros((301))
	episode_winnings = 0

	count = 0
	while episode_winnings < 80:
		won = False
		bet_amount = 1
		while not won:
			if count > 301:
				return result_array
			result_array[count] = episode_winnings
			count += 1
			#print(episode_winnings, bet_amount)
			won = get_spin_result(win_prob)
			if won:
				episode_winnings += bet_amount
			else:
				episode_winnings -= bet_amount
				bet_amount *= 2

				if has_bankroll:

					# if last round went all in
					if episode_winnings == -bankroll:
						return episode_winnings

					if episode_winnings - bet_amount < -bankroll:
						# all in the left
						bet_amount = bankroll + episode_winnings

	# print the final winning
	if episode_winnings >= 80 and count <= 301:
		result_array[count] = episode_winnings

	return result_array
				
			

def exp1_1(win_prob):
	result_array = np.zeros((10, 301))

	for index in range(10):
		result_array[index] = simulator(win_prob, False, None)

	return result_array

	# run simulator 10x and plot winnings 
		# starting from 0
		# 10 arrays needed for graph
	# plot all 10 runs on one chart using matplotlib functions
		# horizontal axis should range from 0 to 300, vertical axis from -256 to +100
		# 10 lines in total

"""
def exp1_2():
	# run simulator 1000x and plot the mean value of winnings
		# starting from 0
		# 3 arrays (mean, mean +sd, mean -sd) needed for graph
	# plot all 1000 runs and +- sd on one chart using matplotlib functions
		# horizontal axis should range from 0 to 300, vertical axis from -256 to +100
		# three lines in total

def exp1_3():
	# run simulator 10x and track winnings 
		# starting from 0
	# plot all 10 runs on one chart using matplotlib functions
		# horizontal axis should range from 0 to 300, vertical axis from -256 to +100
"""

if __name__ == "__main__":  		   	  			  	 		  		  		    	 		 		   		 		  
    test_code()  		   	  			  	 		  		  		    	 		 		   		 		  
