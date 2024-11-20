def sponge_case(sentence):

    # itterate through all the letters in the sentence untill end and make it lower case
    # step each letter and convert it to upper untill you reach end 
    result = ""

    for i in range(len(sentence)):
        if i % 2 == 0:
            result += sentence[i].lower()
        else:
            result += sentence[i].upper()

    return result







# sponge_case("spongebob") --  sPoNgEbOb"
# sponge_case(("Who are YOU calling A Pinhead")) -- "wHo aRe yOu cAlLiNg a pInHeAd"
sponge_case("WHAT is UP my dude") 
# sponge_case("E") --- Should return "e"












    # Write your solution here!
    
   
    # turn the sentence into an array of individual words
    # words = sentence.split()

    # # create a new array of sponge-case words using our helper function
    # new_words = []
    # for word in words:
    #     new_words.append(sponge_single_word(word))

    # # Join the new spongy words with spaces
    # return " ".join(new_words)


# Helper function that converts a single word to sponge-case 
# def sponge_single_word(word):
#     new_word = ""
#     # Instructions say the word must start with a lowercase letter
#     # We will toggle this variable to alternate between lower and upper case
#     lower = True 

#     for letter in word:
#     # if our toggle is set to lowercase, add a lowercase version of the letter
#         if lower:
#             new_word += letter.lower()
#         # if our toggle is set to lowercase, add a uppercase version of the letter
#         else:
#             new_word += letter.upper()
#         # flip our toggle
#         lower = not lower
    
#     return new_word



# Test cases
assert sponge_case("spongebob") == "sPoNgEbOb"
assert sponge_case("Who are YOU calling A Pinhead") == "wHo aRe yOu cAlLiNg a pInHeAd"
assert sponge_case("WHAT is UP my dude") == "wHaT iS uP mY dUdE"
assert sponge_case("E") == "e"
assert sponge_case("e") == "e"

print("All tests passed!")
print("Discuss time and space complexity if there's time remaining")