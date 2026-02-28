def part_b(yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise):
	#########################################################################
	portion_down_payment = 0.25
	r = 0.05
	amount_saved = 0
	down_payment = cost_of_dream_home*portion_down_payment
	months = 0
	
	
	###############################################################################################
	## Determine how many months it would take to get the down payment for your dream home below ## 
	###############################################################################################
	while amount_saved < down_payment:
	    months += 1
	    monthly_salary = yearly_salary/12
	    saving_of_month = monthly_salary * portion_saved    
	    amount_saved += saving_of_month + amount_saved *(r/12)
	    if months%6 == 0: 
	        yearly_salary += yearly_salary*semi_annual_raise
	
	print(f"Number of months: {months}")
	return months