# Take marks of three subjects as input (as strings), convert them to integers, calculate total marks and percentage.
math = input("Enter your marks in Mathematics:")
biology = input("Enter your marks in Biology:")
chemistry = input("Enter your marks in Chemistry:")
math = int(math)
biology = int(biology)
chemistry = int(chemistry)
tot_mar = math + biology + chemistry
print("Total Marks:", tot_mar)
perc = (tot_mar/300)*100
print("Percentage:", perc)
