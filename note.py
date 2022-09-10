import argparse
import datetime

date = datetime.datetime
timestamp = str(date.now())


# Accept command line arguments for note title and contents
parser = argparse.ArgumentParser(description='Process values for note title and contents.')
#T us for title of the note
parser.add_argument("-t", type=str)
# B is for body of the note
parser.add_argument("-b", type=str)

args = parser.parse_args()


def note():
    f = open(args.t, "a")
    f.write("\n" + "\n" + args.b + "\n" + "Time:" + timestamp)


note()



