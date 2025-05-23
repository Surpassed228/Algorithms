import random as rd
from MaxSubAr_nlogn import MaxSub



def MAXSUB(A):
	N = len(A)
	if N == 1:
		return A

	ind = 0
	main_ind = 0
	main_sum = A[ind]
	current_el = A[ind]
	while current_el < 0 and ind < N-1:
		ind += 1
		current_el = A[ind]

		if main_sum <= current_el:
			main_sum = current_el
			main_ind = ind

	if main_ind == N - 1:
		return main_ind,main_ind,main_sum

	else:
		start = main_ind 
		end = main_ind 

		max_sum = A[main_ind]
		total_sum = A[main_ind]

		new_ind = main_ind + 1

		while new_ind < N:
			if A[new_ind] >= 0:
				diff = total_sum-max_sum
				abs_diff = abs(diff)
				# print(diff)
				# print(abs_diff)
				if diff < 0 and abs_diff > max_sum:
					old_ind = new_ind
					pos_sum = 0
					while old_ind < N and pos_sum >= 0:
						if pos_sum >= max_sum:
							break
						else:
							pos_sum += A[old_ind]
							old_ind += 1
					old_ind -= 1

					if pos_sum >= max_sum:
						start = new_ind 
						end = old_ind
						max_sum = pos_sum
						total_sum = pos_sum
						new_ind = old_ind + 1
					else:
						new_ind = old_ind + 1
						total_sum += pos_sum
				else:
					if total_sum + A[new_ind] >= max_sum:
						end = new_ind
						max_sum = total_sum
						max_sum += A[new_ind]
						total_sum += A[new_ind]

					else:
						total_sum += A[new_ind]
					#update index
					new_ind += 1
			else:
				total_sum += A[new_ind]
				#update index
				new_ind += 1

		return start,end,max_sum



# some_ar = [-34, -1, -1, 25, -29, -28, 42, -20, 37, -31]
# print(some_ar)
# print(MAXSUB(some_ar))
# print(MaxSub(some_ar,0,len(some_ar)-1))

def test(N = 10):
	for _ in range(N):
		R = rd.randint(1,25)
		some_rand = [rd.randint(-50,50) for _ in range(R)]
		t1 = MAXSUB(some_rand)
		t2 = MaxSub(some_rand,0,len(some_rand)-1)
		if t1[-1] == t2[-1]:
			print(f'TEST #{_+1} PASSED')
		else:
			print('\n\n###WRONG###')
			print(some_rand)
			print(t1,t2,end = '\n\n')
			break
test(1_000)