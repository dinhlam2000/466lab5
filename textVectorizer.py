import sys
import os


# returns tokens found from string text
def tokenizer(text):
    tokens = text.split(' ').strip()
    return tokens


# main function to iterate through each .txt file in the input directory
def textVectorizer(dirname):
    # list of lines to add to the groundtruth file
    ground_truth = []
    # set of words found to avoid duplicates
    words = set()

    for authorname in os.listdir(dirname):
        folderdir = ''.join((dirname, '/', authorname))
        for filename in os.listdir(folderdir):
            # building ground_truth list
            truth_line = ','.join((filename, authorname))
            ground_truth.append(truth_line)

            # list of tokens in current .txt file
            filetokens = []
            filedir = ''.join((folderdir, '/', filename))
            with open(filedir, 'r') as f:
                filetokens = tokenizer(f.read())
                #filetokens = list(f)
                #filetokens = f.read().strip().split(' ')
                print(filetokens)
                exit()
                # for line in f:
                #     filetokens = list()
                #     print(line)
                #     exit()

    # add ground truth list to a file and output the groundtruth.csv
    #print(len(ground_truth))
    with open ('groundtruth.csv', 'w') as f:
        for line in ground_truth:
            f.write(line)
            f.write('\n')


if __name__ == '__main__':
    dirname = sys.argv[1]
    textVectorizer(dirname)

