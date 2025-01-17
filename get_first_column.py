def get_first_column(data):
    """
    Get the first column from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First column.
    """
    s=[]
    a=data.split('\n')
  
    for i in a[1:]:
        if i.isdigit:
            s.append(int(i.split(',')[0]))
    
    
    return s
data=open("data.csv").read()
print(get_first_column(data))
    
# Read the csv file