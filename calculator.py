import math

def word_value(name):
    counter = 0
    name = name.lower()
    for i in name:
        counter += ord(i)-96
        # print (counter)
    return counter

# print(word_value("Demi"))
def dict_value(file):
    dictionary = {}
    fin = open(file)
    for line in fin:
        word = line.strip()
        word = word.replace('-','')
        if word not in dictionary:
            dictionary[word] = dictionary.get(word, word_value(word))
    return dictionary

# print(dict_value("roster.txt"))

def most_value(dictionary):
    highest = max(dictionary.values())
    for i in dictionary:
        if dictionary[i] == highest:
            return i

# print(most_value(dict_value("roster.txt")))

def same_value(name):
    dictionary = dict_value('positive-words.txt')
    same_value = {}
    value = word_value(name)
    same_value[name] = same_value.get(name,[])
    for i in dictionary:
        if dictionary[i] == value:
            same_value[name].append(i)
    if same_value[name] == []:
        return None
    else:
        return same_value[name]

def process_file(file_name):
    """
    Given a file name, returns a list of lists [name, gender, births]

    :param file_name: a string
    :return: a list of lists, [[name1, gender1, births1], [name2, gender2, births2]...]

    Example:
    process_file('babynames/yob1880.txt')
        will return
    [["Mary","F",7065], ["Anna","F",2604],...]

    """
    fin = open(file_name)
    lis = []
    for line in fin:
        line = line.strip()
        # print(line)
        line = line.split(',')
        # print (line)
        line[2] = int(line[2])
        # name, gender, birth = line[0],line[1],line[2]
        # line = [name,gender,int(birth)]
        lis.append(line)

    return lis
# print(process_file('babynames/yob1880.txt'))

def total_births(year):
    """
    :param year: an integer, between 1880 and 2010
    :return: an integer, the total births of all the babies in that year
    """
    file_name = f'babynames/yob{year}.txt'
    # print (file_name)
    lis = process_file(file_name)
    counter = 0
    for i in lis:
        counter += i[2]
    return counter
        
# print(total_births(1880))

def proportion(name, gender, year):
    """

    :param name: a string, first name
    :param gender: a string, "F" or "M"
    :param year: an integer, between 1880 and 2010
    :return: a float number, the proportion of babies with the given name and given gender to total births in given year
    """
    file_name = f'babynames/yob{year}.txt'
    lis = process_file(file_name)
    total = total_births(year)
    for i in lis:
        if i[0] == name and i[1] == gender:
            return i[2]/total*100


# print(proportion('Gregory','M',1962))

def highest_year(name, gender):
    """

    :param name: a string
    :param gender: a string, "F" or "M"
    :return: an integer, the year when the given name has the highest proportion over the years (among all the
    proportions of the same name with same gender in all years)
    """
    dictionary = {}
    for i in range(1880,2011):
        num = proportion(name,gender,i)
        if num:
            dictionary[i] = dictionary.get(i, int(num*1000000)) #Multiplied to get rid of the floating numbers problem. Cannot sort or max with floating numbers
    # print (dictionary)
    highest = max(dictionary.values())
    for i in dictionary:
        if dictionary[i] == highest:
            return i

def main():
    a = input('please enter a name:')
    print('Results are:', same_value(a))


if __name__ == '__main__':
    main()
