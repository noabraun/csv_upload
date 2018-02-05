import csv

def read_csv():
    
    with open('example.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile)
      
        for row in spamreader:
            print row #array
            #should loop through the row and push elements of the array into the DB
            print row[0]
            row_list = ', '.join(row)
            print row_list #create string out of the different elements in the array (elements seperated by comma)




