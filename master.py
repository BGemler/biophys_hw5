import random
import numpy as np
import matplotlib.pyplot as plt

random.seed(2021)

def initiate_walk(num_steps_for_walk):
	"""
	this function simulates a single walk in 3D
	"""
	position = [0, 0, 0] # x y z plane

	# simulate each step of the walk
	for i in range(num_steps_for_walk):
		# decide if step will be in x y or z direction
		direction = random.sample([0, 1, 2], 1)[0]

		# decide if step is postiive or negative 
		step_pos_neg = random.sample([-1, 1], 1)[0]

		position[direction] += step_pos_neg

	# calculate squared end to end distance
	r2 = position[0]**2 + position[1]**2 + position[2]**2

	if position[0] == 0 and position[1] == 0 and position[2] == 0:
		returned_to_zero = True
	else:
		returned_to_zero = False

	return r2, returned_to_zero


def initiate_walk_2d(num_steps_for_walk):
	"""
	this function simulates a single walk in 2D
	"""
	position = [0, 0] # x y plane

	# simulate each step of the walk
	for i in range(num_steps_for_walk):
		# decide if step will be in x y or z direction
		direction = random.sample([0, 1], 1)[0]

		# decide if step is postiive or negative 
		step_pos_neg = random.sample([-1, 1], 1)[0]

		position[direction] += step_pos_neg

	return position[0], position[1]


def write_out_walk(plot_x, plot_y, num_walks):
	"""
	"""
	out_img = "results/num_step_vs_r2.png"

	plt.scatter(plot_x, plot_y)
	plt.xlabel("Number of Steps (N)")
	plt.ylabel("Average <R^2>")

	plt.title("<R^2> at N Ranging from 0:1000" + "\n" + 
							"Number of Simulations at Each N: " + str(num_walks))

	plt.savefig(out_img, bbox_inches='tight')
	plt.close()

	return


def write_out_final_walk_poses(plot_x, plot_y, num_walks, walk_size):
	"""
	"""
	out_img = "results/end_walk_poses_size=" + str(walk_size) + ".png"

	plt.scatter(plot_x, plot_y)
	plt.xlabel("X Axis")
	plt.ylabel("Y Axis")

	plt.title("Number of Steps: " + str(walk_size) + "\n" + 
							"Number of Simulations: " + str(num_walks))

	plt.savefig(out_img, bbox_inches='tight')
	plt.close()

	return


def write_out_fracts(plot_x, plot_y, num_walks, max_step_size):
	"""
	"""
	out_img = "results/fract_returned_zero.png"

	plt.loglog(plot_x, plot_y)
	plt.xlabel("Number of Steps (N)")
	plt.ylabel("Probability of Returning to 0")

	plt.title("P0 at N Ranging from 0:" + str(max_step_size) + "\n" + 
							"Number of Simulations at Each N: " + str(num_walks))

	plt.savefig(out_img, bbox_inches='tight')
	plt.close()

	return


def prob_10():
	"""
	"""
	num_steps_for_walk_array = [1000]
	num_walks = 1000
	max_step_size = max(num_steps_for_walk_array)
	tasks = [
		#"part_a", \
		#"part_b", \
		"part_c"
	]

	if "part_a" in tasks:
		plot_x, plot_y = [], []
		for num_steps_for_walk in num_steps_for_walk_array:
			all_r2s = []
			for i in range(num_walks):
				r2, _ = initiate_walk(num_steps_for_walk)
				all_r2s.append(r2)

			# get average value
			avg_r2 = np.average(all_r2s)

			plot_x.append(num_steps_for_walk)
			plot_y.append(avg_r2)

		write_out_walk(plot_x, plot_y, num_walks)

	if "part_b" in tasks:
		plot_x, plot_y = [], []
		for num_steps_for_walk in num_steps_for_walk_array:
			all_fracts = []
			for i in range(num_walks):
				_, returned_to_zero = initiate_walk(num_steps_for_walk)
				if returned_to_zero == True:
					all_fracts.append(1)
				else:
					all_fracts.append(0)

			avg_fract = sum(all_fracts) / num_walks

			if num_steps_for_walk % 2 == 0:
				plot_x.append(num_steps_for_walk)
				plot_y.append(avg_fract)

		write_out_fracts(plot_x, plot_y, num_walks, max_step_size)

		for i in range(len(plot_x)):
			print(plot_x[i], plot_y[i])

	if "part_c" in tasks:
		plot_x, plot_y = [], []
		for num_steps_for_walk in num_steps_for_walk_array:
			for i in range(num_walks):
				x, y = initiate_walk_2d(num_steps_for_walk)

				plot_x.append(x)
				plot_y.append(y)

		write_out_final_walk_poses(plot_x, plot_y, num_walks, num_steps_for_walk_array[0])


	return

prob_10()