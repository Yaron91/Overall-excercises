movie: int = int (input("Please enter how long is the movie *in minutes*: "));
hours: int =  movie // 60
minutes: float = movie % 60
print (f"The length of the movie was {hours} hours and {minutes} minutes ");