# *-* coding:utf-8 *-*
def check (st_reg_number):

	DIVISOR = 11
	
	weights = [2, 9, 8, 7, 6, 5, 4, 3, 2]

	if len(st_reg_number)>10:
		return False
	
	if len(st_reg_number)<10:
		return False

	sum = 0
	for i in range(len(st_reg_number)-1):
		sum = sum + int(st_reg_number[i]) * weights[i]

	rest_division = sum % DIVISOR
	digit = DIVISOR - rest_division		

	if digit == 10 or digit == 11:
		digit = 0

	return digit == int(st_reg_number[len(st_reg_number)-1])

	
