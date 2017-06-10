import pandas

def describeIt(filename):

    baseball = pandas.read_csv(filename)
    print baseball.describe()

describeIt('Master.csv')
