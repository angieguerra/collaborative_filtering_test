import sys
import numpy

def main(num):
    # Save account number
    account_num = num
    account_data = []
    comparison_num = ''
    comparison = []
    recommend = []

    # Create dictionary for data collection and analysis
    D = {}

    # Open data file
    data = open('./TTI Data.csv', 'r')

    # Collect headers for reference
    headers = data.readline().rstrip().split(',')

    # Parse data and put into dictionary
    for line in data:
        line_data = line.rstrip().split(',')
        D[line_data[0]] = line_data[1:]

    # Check that given account exists
    if account_num in D:
        account_data = D[account_num]
    else:
        print 'No account found with that account number'
        sys.exit()

    # Find closest other account based on euclidean distance
    a = numpy.array([ int(x) for x in account_data ])
    euclidean = float('inf')
    for data in D:
        if data != account_num:
            b = numpy.array([ int(x) for x in D[data] ])
            if numpy.linalg.norm(a-b) < euclidean:
                comparison = D[data]
                comparison_num = data
                euclidean = numpy.linalg.norm(a-b)

    # Pull out names of items to recommend from closest account
    for num in [ int(x) for x in D[comparison_num] ]:
        if num > 0:
            recommend.append(headers[D[comparison_num].index(str(num)) + 1])

    for item in recommend:
        if int(account_data[headers.index(item) - 1]) > 0:
            recommend.remove(item)

    # Print out recommendations
    print 'Based on your purchase history, we recommend you also purchase:'
    for item in recommend:
        print item

if __name__ == '__main__':
    # Require arguments
    if len(sys.argv) < 3 or sys.argv[1] != '-account':
        print 'Please use the \'-account\' flag and provide an account number.'
    else:
        # Pass account number and begin main
        main(sys.argv[2])