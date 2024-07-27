subject = input("Please enter the subject of the vote: ");
pro_count = 0
against_count = 0
avoid_count = 0
all_votes=[]
veto_vote = False
first_pro_country = None
first_against_country = None
for i in range (1 , 45):
    if veto_vote:
        break
    while True:
        try:
            vote:int = int(input("Please enter your vote. Pro -1 Against -2 Avoid-3 Veto-4 "))
            if vote == 4:
                print (f"Country {i} has voted Veto");
                all_votes.append(vote)
                veto_vote = True
                break
            elif vote == 3:
                avoid_count += 1
                all_votes.append(vote)
                break
            elif vote == 2:
                against_count += 1
                all_votes.append(vote)
                if first_against_country is None:
                    first_against_country = i
                break
            elif vote == 1:
                pro_count += 1
                all_votes.append(vote)
                if first_pro_country is None:
                    first_pro_country = i
                break
            else:
                print ("Please enter a number between 1 - 4");
        except:
            print("Invalid input, please enter a number");

print(f"Vote results for the subject: {subject}");
print (f"The number of countries who are Pro {subject} is {pro_count} ");
print (f"The number of countries who are Against {subject} is {against_count} ");
print (f"The number of countries who Avoid {subject} is {avoid_count} ");
print(f"The first country to vote pro {subject} is country number {first_pro_country}.")
print(f"The first country to vote against {subject} is country number {first_against_country}.")

