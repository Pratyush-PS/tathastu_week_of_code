run1= int(input("Enter runs of 1st batsman:"))
run2= int(input("Enter runs of 2nd batsman:"))
run3= int(input("Enter runs of 3rd batsman:"))

rate1= run1/60*100
rate2= run2/60*100
rate3= run3/60*100
print('\n')
print("Run rate of 1st batsman:",rate1)
print("Run rate of 2nd batsman:",rate2)
print("Run rate of 3rd batsman:",rate3)

tot_runs1 = int(rate1*120/100)
tot_runs2 = int(rate2*120/100)
tot_runs3 = int(rate3*120/100)

print("\nTotal Runs scored by each batsman if they played 60 more balls(Total of 120 balls):")
print("Batsman 1:",tot_runs1)
print("Batsman 2:",tot_runs2)
print("Batsman 3:",tot_runs3)

max1= tot_runs1//6
max2= tot_runs2//6
max3= tot_runs3//6

print("\nMaximum six possible for 1st batsman:",max1)
print("Maximum six possible for 2nd batsman:",max2)
print("Maximum six possible for 3rd batsman:",max3)
