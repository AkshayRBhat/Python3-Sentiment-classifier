punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


def strip_punctuation(str):
    for c in punctuation_chars:
        str = str.replace(c, "")
    return str

def get_pos(str):
    str = strip_punctuation(str)
    str = str.lower()
    count = 0
    str_w = str.split()
    for i in str_w:
        if i in positive_words:
            count += 1
    return count

def get_neg(str):
    str = strip_punctuation(str)
    str = str.lower()
    count = 0
    str_w = str.split()
    for i in str_w:
        if i in negative_words:
            count += 1
    return count


main_data = open("project_twitter_data.csv").readlines()
with open("resulting_data.csv","w") as f:
    f.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
    f.write("\n")
    for line in main_data[1:]:
        text,retweets,replies = line.split(',')
        pos_count = get_pos(text)
        neg_count = get_neg(text)
        netscore = pos_count - neg_count
        f.write(str(retweets).strip()+","+str(replies).strip()+","+str(pos_count).strip()+","+str(neg_count).strip()+","+str(netscore).strip())
        f.write("\n")
