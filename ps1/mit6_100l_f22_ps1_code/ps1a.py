## 6.100A PSet 1: Part A
## Name:
## Time Spent:
## Collaborators:

##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################
while True:
    yearly_salary = input("Enter your yearly salary: ")
    try:
        x = float(yearly_salary)
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################


###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################
