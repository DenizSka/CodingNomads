# Description:
# Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.
# Rules for a smiling face:
# -Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
# -A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
# -Every smiling face must have a smiling mouth that should be marked with either ) or D.
# No additional characters are allowed except for those mentioned.
# Valid smiley face examples:
# :) :D ;-D :~)
# Invalid smiley faces:
# ;( :> :} :]


def count_smileys(arr):
    count = 0
    list_eyes = [':', ';']
    list_smiles = [')', 'D']
    list_nose = ['-', '~']
    # I can make a list of tuple of all smile variations in a list comprehension
    # loop each and join each tuple to one string
    # check if it exist in the list
    list1_ = ['{}{}'.format(x, y) for x in list_eyes for y in list_smiles]
    list2_ = ['{}{}{}'.format(x, y, z) for x in list_eyes for y in list_nose for z in list_smiles]
    list3_ = list1_ + list2_
    # print(list3_)
    for one in arr:
        if one in list3_:
            # print(one)
            # print(one in list3_)
            count += 1
    return count


print(count_smileys([';]', ':[', ';*', ':$', ';-D']))
print(count_smileys([':D', ':~)', ';~D', ':)']))
