import csv

def fix_turnstile_data(filenames):
    '''
    Filenames is a list of MTA Subway turnstile text files. A link to an example
    MTA Subway turnstile text file can be seen at the URL below:
    http://web.mta.info/developers/data/nyct/turnstile/turnstile_110507.txt

    As you can see, there are numerous data points included in each row of the
    a MTA Subway turnstile text file.

    You want to write a function that will update each row in the text
    file so there is only one entry per row. A few examples below:
    A002,R051,02-00-00,05-28-11,00:00:00,REGULAR,003178521,001100739
    A002,R051,02-00-00,05-28-11,04:00:00,REGULAR,003178541,001100746
    A002,R051,02-00-00,05-28-11,08:00:00,REGULAR,003178559,001100775

    Write the updates to a different text file in the format of "updated_" + filename.
    For example:
        1) if you read in a text file called "turnstile_110521.txt"
        2) you should write the updated data to "updated_turnstile_110521.txt"

    The order of the fields should be preserved. Remember to read through the
    Instructor Notes below for more details on the task.

    In addition, here is a CSV reader/writer introductory tutorial:
    http://goo.gl/HBbvyy

    You can see a sample of the turnstile text file that's passed into this function
    and the the corresponding updated file by downloading these files from the resources:

    Sample input file: turnstile_110528.txt
    Sample updated file: solution_turnstile_110528.txt
    '''

    # I don't take credit for this one. But I finally understand what it is doing:
    for name in filenames:
        # your code here
        # 'with' allows us to open these objects as a block in one go. Very Python
            with open(name, 'r') as f_in, open(''.join(['updated_',name]), 'w') as f_out:
                reader = csv.reader(f_in)
                writer = csv.writer(f_out)
                # Loop throuh each row
                for row in reader:
                    # Walk the row. Start at the third element, stop at the length
                    # of the row, jump by five.
                    for i in range(3, len(row), 5):
                        # Write the first 3 elements. Then, write the next one;
                        # remember that we jumped by 5. SO, for example, if i = 4
                        # then write row[4:4+5] of start at 4 end at nine and so on
                        # VERY ELEGANT
                        writer.writerow(row[0:3] + row[i:i+5])
