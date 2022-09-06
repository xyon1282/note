import argparse

# Accept command line arguments for note title and contents
parser = argparse.ArgumentParser(description='Process values for note title and contents.')
#T us for title of the note
parser.add_argument("-t", type=str)
# B is for body of the note
parser.add_argument("-b", type=str)
#F for filename. Note to self: make this optional, and if user does not specify, default to title
#parser.add_argument("-f", type=str)

args = parser.parse_args()


def note():
    f = open(args.t, "a")
    f.write("\n" + args.b)


note()
