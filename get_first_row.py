def get_first_row(data):   
   """
   Get the first row from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First row.
   """
   a=data.split('\n')
   s=a[1]
   x=s.split(',')
   return x
data=open("data.csv").read()
print(get_first_row(data))

# Read the csv file