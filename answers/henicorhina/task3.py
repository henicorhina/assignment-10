# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
BIOL7800 assignment 10
Oscar Johnson 28 February 2016
"""


def ExaML_to_dict(string):
    """
    Processes ExaML run data as string and returns a dictionary
    of run name as key and log-likelihood as value
    """
    st = string.replace('Likelihood of best tree:\t', '').replace('\t', '\n').split('\n')
    keys = [st[2::2]]
    values = [st[3::2]]
    # the string editting above returned a list with the first two indices blank
    # if run data starts at list[0], use the code below for keys and values
    #keys = [st[0::2]]
    #values = [st[1::2]]
    my_dict = dict(zip(keys[0], values[0]))
    return(my_dict)


def print_runs(d):
    """
    takes dictionary of ExaML run names and the log-likelihood value 
    and prints them in a two column format
    """
    for key, value in d.items():
        print(key, '\t', value)


def max_like(d):
    """
    takes dictionary of ExaML run names and the log-likelihood value 
    and prints the maximum log-likelihood value and assocated run name
    and then returns those data
    """
    count_of_words = [] 
    for key, value in d.items():
        # add words and values to list in form of tuples
        count_of_words.append((value, key))
    count_of_words.sort() #sort words in descending abundance    
    print('\n', 'maximized -log likelihood value: ', count_of_words[0][0], 
    ', and run name: ', count_of_words[0][1])
    return(count_of_words[0][0], count_of_words[0][1])



def main():
    my_string = """
ExaML_info.T6\tLikelihood of best tree:\t-82924194.67
ExaML_info.T5\tLikelihood of best tree:\t-82924194.71
ExaML_info.T9\tLikelihood of best tree:\t-82924194.73
ExaML_info.T7\tLikelihood of best tree:\t-82924252.98
ExaML_info.T2\tLikelihood of best tree:\t-82924253.01
ExaML_info.T1\tLikelihood of best tree:\t-82924354.95
ExaML_info.T8\tLikelihood of best tree:\t-82924354.98
ExaML_info.T15\tLikelihood of best tree:\t-82924366.58
ExaML_info.T0\tLikelihood of best tree:\t-82924366.59
ExaML_info.T4\tLikelihood of best tree:\t-82924397.48
ExaML_info.T16\tLikelihood of best tree:\t-82924424.87
ExaML_info.T3\tLikelihood of best tree:\t-82924424.89
ExaML_info.T14\tLikelihood of best tree:\t-82924426.52
ExaML_info.T12\tLikelihood of best tree:\t-82924426.53
ExaML_info.T13\tLikelihood of best tree:\t-82924426.54
ExaML_info.T19\tLikelihood of best tree:\t-82924465.57
ExaML_info.T17\tLikelihood of best tree:\t-82924707.69
ExaML_info.T10\tLikelihood of best tree:\t-82925366.65
ExaML_info.T18\tLikelihood of best tree:\t-82925393.89
ExaML_info.T11\tLikelihood of best tree:\t-82925447.6"""
    vals = ExaML_to_dict(my_string)
    print_runs(vals)
    max_like(vals)

if __name__ == '__main__':
    main()