from locale import normalize
import os
import re
class IdMap:

    term = []
    dictionary = dict()
    posting_list = dict()
    final_data = []
    dockIds = []
    count_labels = 0

    # yy = r'/13800711-txt-0073631_utf.txt'

    # xx = open('information_retrieval/1.txt' , 'r').read()



    # ere = xx.split(' ')
    # print(ere)
 
    str = r'information_retrieval/Train/'
    dirs = os.listdir(str)
    i = 1
    for dir in dirs :
        for f in os.listdir(str + dir):
            i = 1
            x = open(str + dir + '/' + f, encoding='utf8').read()
            count_labels = count_labels + 1


            y = x.split(' ')
            for aa in range(len(y)):
                
                posting_list[y[aa]] = count_labels
            # # print (y)
            term.append(y)

    for arrays in term:
        final_data = arrays+final_data

        


    for word in final_data:
        
        # posting_list[y] = count_labels
        if word not in dictionary: 
            dictionary[word] = i
            i = i+1

    # for term in final_data:

    #     for doc in range(count_labels):
    #         posting_list[y] = count_labels

    
    print(posting_list)

    







#     """Helper class to store a mapping from strings to ids."""

#     def __init__(self):
#         self.str_to_id = {}
#         self.id_to_str = []

#     def __len__(self):
#         """Return number of terms stored in the IdMap"""
#         return len(self.id_to_str)

#     def _get_str(self, i):
#         """Returns the string corresponding to a given id (`i`)."""
#         ### Begin your code

        
        

#         ### End your code

#     def _get_id(self, s):
#         """Returns the id corresponding to a string (`s`).
#         If `s` is not in the IdMap yet, then assigns a new id and returns the new id.
#         """
#         ### Begin your code

#         ### End your code

#     def __getitem__(self, key):
#         """If `key` is a integer, use _get_str;
#            If `key` is a string, use _get_id;"""
#         if type(key) is int:
#             return self._get_str(key)
#         elif type(key) is str:
#             return self._get_id(key) 
#         else:
#             raise TypeError

# if __name__ == '__main__':
#     testIdMap = IdMap()
#     assert testIdMap['a'] == 0, "Unable to add a new string to the IdMap"
#     assert testIdMap['bcd'] == 1, "Unable to add a new string to the IdMap"
#     assert testIdMap['a'] == 0, "Unable to retrieve the id of an existing string"
#     assert testIdMap[1] == 'bcd', "Unable to retrive the string corresponding to a\
#                                     given id"
#     try:
#         testIdMap[2]
#     except IndexError as e:
#         assert True, "Doesn't throw an IndexError for out of range numeric ids"
#     assert len(testIdMap) == 2