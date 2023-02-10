#Define function,Get coloumn names from a csv file
def get_column_names(data):
    """ 
    Get column names from a csv file
    Parameters:
        data(str): csv file
    Returns:
        column_names: list of column names
    """
    a=data.split('\n')
    s=a[0]
    x=s.split(',')
    return x
data=open("data.csv").read()
print(get_column_names(data))
    
# Read the csv file