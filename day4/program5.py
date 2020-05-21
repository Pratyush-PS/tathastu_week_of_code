voters = int(input("Enter number of voters:"))

votes=[]

for i in range(voters):
    name = input("Enter candidate name:")
    votes.append(name)

cand_dict={}

for i in votes:
    cand_dict[i] = cand_dict.get(i,0)+1

sorted_dict =sorted(cand_dict.items(), key= lambda x:x[0], reverse=True)


win_cand = list(sorted(sorted_dict, key = lambda x:x[1]))

print("\nCandidate with highest votes is:", win_cand[-1][0])
