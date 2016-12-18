import numpy as np

def solve_any_system(numpy_matrix):

	column_index = 0
	base_row_index = 0
	while column_index < numpy_matrix.shape[1] - 2: # will return a tuple (m, n), where m is the number of rows, and n is 
													 # the number of columns

		################################################################################################
		# method in which you divide all rows by item in top row won't work if item in top row is zero
		# in this case, will probably have to draw from another row
		# if there is no other row with non-zero then system is not solvable?
		################################################################################################

		solved_row_index = base_row_index + 1 # solved_row_index is the index of the row for which we are canceling out a variable
		while solved_row_index != numpy_matrix.shape[0]: # run until solved_row_index is number of rows in matrix

			# in line below, calculate a multiplier that will be used to cancel out the variable at the solved place in the matrix
			multiplier = -numpy_matrix[solved_row_index].item(column_index) / numpy_matrix[base_row_index].item(column_index)
			# in line below, use the multiplier to cancel out the variable at the solved place in the matrix
			numpy_matrix[solved_row_index] = numpy_matrix[solved_row_index] + (numpy_matrix[base_row_index] * multiplier)

			solved_row_index += 1

		column_index += 1
		base_row_index += 1


	solution_vector = np.zeros( (numpy_matrix.shape[0], 1) ) # zero vector with same # of rows as system matrix
	reverse_counter = numpy_matrix.shape[0] - 1 # start at index of last row

	while reverse_counter >= 0: # go through index zero
		for i in range(numpy_matrix.shape[0] - 1, reverse_counter, -1): # run 0 times for last row, 1 time for second 
																		# to last... n-1 times for first, where n is number of rows

			numpy_matrix[reverse_counter].itemset(-1, numpy_matrix[reverse_counter].item(-1) # set the last item in the subject row to that 
				- numpy_matrix[reverse_counter].item(i) * solution_vector[i])                # item minus the solved chi times its coefficient
			
	
		solution_vector[reverse_counter] = numpy_matrix[reverse_counter].item(-1) / numpy_matrix[reverse_counter].item(reverse_counter)
		reverse_counter -=1

	return solution_vector
