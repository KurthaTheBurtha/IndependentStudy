import string
#Use this to store the word - value pairs
sentiment_value_dictionary = {}


# Takes a String and returns the overall sentiment value of that String
def get_total_sentiment(user_input):
    total = 0
    list = user_input.split(" ")
    for i in list:
        if not i.isalpha():
            i = remove_punctuation(i)
        if i.lower() in sentiment_value_dictionary:
            total += float(sentiment_value_dictionary[i.lower()])
    return total

# Takes a String and returns that String without any punctuation or non-alphanumeric characters
def remove_punctuation(word):
    word = word.translate(str.maketrans('','',string.punctuation))
    return word

#open a file using the open function
file = open("sentiment_values.csv")

for line in file:
    #this creates a list at each blank space
    line_list = line.split(",")
    line_list[1] = line_list[1][:len(line_list[1])-1]
    sentiment_value_dictionary[line_list[0]] = line_list[1]
# print(sentiment_value_dictionary)
print(get_total_sentiment("This is absurd!"))