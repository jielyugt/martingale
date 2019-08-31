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



# ===================================================================================
# Useful links 

# project 1 Homepage
# http://quantsoftware.gatech.edu/Fall_2019_Project_1:_Martingale

# matplotlib.pyplot API overview
# https://matplotlib.org/3.1.1/api/pyplot_summary.html 	  

# bionomial probability calculator
# https://www.stattrek.com/online-calculator/binomial.aspx



# ===================================================================================
# Libaraies and caller functions 

import numpy as np
import matplotlib.pyplot as plt
  		   	  			  	 		  		  		    	 		 		   		 		  
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
	win_prob = 9/19		   	  			  	 		  		  		    	 		 		   		 		  
	np.random.seed(gtid())  
	bank_roll = 256   	  			  	 		  		  		    	 		 		   		 		  
	
	#exp1_figure1(win_prob)	  	 		  		  		    	 		 		   		 		  
	#exp1_figure2_and_figure3(win_prob)
	exp2_figure4_and_figure5(win_prob, bank_roll)


# ===================================================================================
# The game simulator

# returns a 1d array of length 1001
def simulator(win_prob, has_bankroll, bankroll):

	# init the array with 80 so that after we win early, we don't need to populate the rest
	result_array = np.full((1001),80)	
	episode_winnings = 0

	count = 0
	while episode_winnings < 80:
		won = False
		bet_amount = 1
		while not won:
			if count >= 1001:
				return result_array
			result_array[count] = episode_winnings
			count += 1
			won = get_spin_result(win_prob)
			if won:
				episode_winnings += bet_amount
			else:
				episode_winnings -= bet_amount
				bet_amount *= 2

				if has_bankroll:

					# if last round went all in
					if episode_winnings == -bankroll:
						# populate the rest of array
						result_array[count:] = episode_winnings
						return result_array

					if episode_winnings - bet_amount < -bankroll:
						# all in the left
						bet_amount = bankroll + episode_winnings
	
	return result_array



# ===================================================================================
# Make figure 1 to 6 

def exp1_figure1(win_prob):

	# run simulator 10x and plot winnings 
		# starting from 0
		# 10 arrays needed for graph
	# plot all 10 runs on one chart using matplotlib functions
		# horizontal axis should range from 0 to 300, vertical axis from -256 to +100
		# 10 lines in total

	plt.axis([0, 300, -256, 100])
	plt.title("Figure 1 - 10 trials w/ infinite bankroll")
	plt.xlabel("Number of Trials")
	plt.ylabel("Total Winnings")

	for index in range(10):
		curr_episode = simulator(win_prob, False, None)
		plt.plot(curr_episode)
		#result_array[index] = curr_episode
	
	plt.savefig("figure1.png")
	plt.clf()
	#return result_array

def exp1_figure2_and_figure3(win_prob):
	
	# run simulator 1000x and plot the mean value of winnings
		# starting from 0
		# 3 arrays (mean, mean +sd, mean -sd) needed for graph
	# plot all 1000 runs and +- sd on one chart using matplotlib functions
		# horizontal axis should range from 0 to 300, vertical axis from -256 to +100
		# three lines in total
		
	result_array = np.zeros((1000, 1001))
	for index in range(1000):
		curr_episode = simulator(win_prob, False, None)
		result_array[index] = curr_episode
	
	# print the last element of every episode
	print(result_array[:, -1])

	
	### plot figure 2

	# 1. calculations
	mean_array = np.mean(result_array, axis = 0)
	std = np.std(result_array, axis = 0)
	mean_plus_array = mean_array + std
	mean_minus_array = mean_array - std

	# 2. plot setup
	plt.axis([0, 300, -256, 100])
	plt.title("Figure 2 - means of 1000 trials w/ infinite bankroll")
	plt.xlabel("Number of Trials")
	plt.ylabel("Total Winnings")

	# 3. plotting!
	plt.plot(mean_array, label = "mean")
	plt.plot(mean_plus_array, label = "mean+std")
	plt.plot(mean_minus_array, label = "mean-std")

	# 4. saving and clearing
	plt.legend()
	plt.savefig("figure2.png")
	plt.clf()


	### plot figure 3
	
	median_array = np.median(result_array, axis = 0)
	std = np.std(result_array, axis = 0)
	median_plus_array = median_array + std
	median_minus_array = median_array - std

	plt.axis([0, 300, -256, 100])
	plt.title("Figure 3 - medians of 1000 trials w/ infinite bankroll")
	plt.xlabel("Number of Trials")
	plt.ylabel("Total Winnings")

	plt.plot(median_array, label = "median")
	plt.plot(median_plus_array, label = "median+std")
	plt.plot(median_minus_array, label = "median-std")
	plt.legend()
	plt.savefig("figure3.png")
	plt.clf()

def exp2_figure4_and_figure5(win_prob, bank_roll):
	result_array = np.zeros((1000, 1001))
	for index in range(1000):
		curr_episode = simulator(win_prob, True, bank_roll)
		result_array[index] = curr_episode
	
	print(result_array[:, -1])

	### plot figure 4
	mean_array = np.mean(result_array, axis = 0)
	std = np.std(result_array, axis = 0)
	mean_plus_array = mean_array + std
	mean_minus_array = mean_array - std

	plt.axis([0, 300, -256, 100])
	plt.title("Figure 4 - means of 1000 trials w/ $" + str(bank_roll) + " bankroll")
	plt.xlabel("Number of Trials")
	plt.ylabel("Total Winnings")

	plt.plot(mean_array, label = "mean")
	plt.plot(mean_plus_array, label = "mean+std")
	plt.plot(mean_minus_array, label = "mean-std")

	plt.legend()
	plt.savefig("figure4.png")
	plt.clf()

	### plot figure 5
	median_array = np.median(result_array, axis = 0)
	std = np.std(result_array, axis = 0)
	median_plus_array = median_array + std
	median_minus_array = median_array - std

	plt.axis([0, 300, -256, 100])
	plt.title("Figure 5 - medians of 1000 trials w/ $" + str(bank_roll) + " bankroll")
	plt.xlabel("Number of Trials")
	plt.ylabel("Total Winnings")

	plt.plot(median_array, label = "median")
	plt.plot(median_plus_array, label = "median+std")
	plt.plot(median_minus_array, label = "median-std")
	plt.legend()
	plt.savefig("figure5.png")
	plt.clf()


if __name__ == "__main__":

	# print the whole matrix without scientific formatting
	np.set_printoptions(threshold = 10000000000000, suppress = True)
		   	  			  	 		  		  		    	 		 		   		 		  
	test_code()  		   	  			  	 		  		  		    	 		 		   		 		  
