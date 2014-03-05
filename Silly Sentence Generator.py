import random

verb_list = ["runs","jumps","climbs","swims to","eats","spins"] #create a list of all your verbs
adjective_list = ["smelly","old","mean","young","big", "tall", "smart","red","blue","thick"]
noun_list = ["Statue of Liberty", "car", "table", "house","trash","building","dog","sunscreen"]
#this function is given a list of words and selects one at random
def random_word(list_of_words):
    number_of_words = len(list_of_words) #get the length of the words list
    random_word_number = random.randint(0,number_of_words - 1) #pick a random number up to the end of the list
    selected_word = list_of_words[random_word_number] #select the word at the number spot
    return selected_word #hand it back


for num in range(0,10):
    verb = random_word(verb_list)
    adj1 = random_word(adjective_list)
    adj2 = random_word(adjective_list)
    noun1 = random_word(noun_list)
    noun2 = random_word(noun_list)
    print "The",adj1, noun1,verb, "the", adj2, noun2 + "."
