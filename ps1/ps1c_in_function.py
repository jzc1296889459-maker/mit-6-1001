def part_c(initial_deposit):
	#########################################################################
	cost_of_house = 800000
	down_payment = 800000*0.25
	##################################################################################################
	## Determine the lowest rate of return needed to get the down payment for your dream home below ##
	##################################################################################################
	tor = 100
	months = 36
	
	# Setting up upper and lower bounds and pathological cases
	a = 0.0
	b = 1.0
	steps = 0
	max_saving = initial_deposit*((1 + 1/12)**months)
	# Case 1: if initial_deposit is enough, we don't need to save, so r = 0
	if initial_deposit >= down_payment - tor:
	    r = 0.0
	# Case 2: if initial_deposit is not enough, see if we can save enough with r = 1
	# if even with r = 1, we can't save enough, then none of r works
	elif max_saving < down_payment - tor:
	    r = None
	# Case 3 (main case): we can implement bisection search
	else:
	    r = (a+b)/2
	    amount_saved = initial_deposit*(1 + r/12)**months
	    while abs(amount_saved - down_payment) >= tor:
	        steps += 1
	        # if save more than enough with current r, try smaller r
	        if amount_saved >= down_payment:
	            b = r
	        # else try larger r
	        else:
	            a = r
	        #update r and amount_saved
	        r = (a+b)/2
	        amount_saved = initial_deposit*(1 + r/12)**months
	
	
	if r is None:
	    print("Best savings rate: None")
	else:
	    print(f"Best savings rate: {r}, [or very close to this number]")
	print(f'Steps in bisection search: {steps} [May vary based on how you implemented your bisection search]')
	 
	    
	            
	   
	return r, steps