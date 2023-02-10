def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """

    a=data.split('\n')
    s=a[0]
    x=s.split(',')
    
    return len(x)
data=open("data.csv").read()
print(find_number_of_columns(data))

# Read the csv file