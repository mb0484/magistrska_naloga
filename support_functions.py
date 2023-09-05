
import string
import re

def add_spaces_before_and_after_punctuation(text):
    punctuation = set(string.punctuation)

    # Initialize an empty string to store the modified text
    modified_text = ""

    # Loop through each character in the text
    for char in text:
        # If the character is a punctuation mark
        if char in punctuation or char == '„' or char == '”' or char == '»' or char == '«':
            # Add a space before and after the punctuation mark
            if modified_text != "":
                modified_text += " " + char + " "
            else:
                modified_text += char + " "
        else:
            # Otherwise, just add the character to the modified text
            modified_text += char

    modified_text = modified_text.replace("< mask >", "<mask>")
    
    modified_text = modified_text.replace("< concated _ word >", "<concated_word>")
    
    modified_text = modified_text.replace("< splited _ mask >", "<splited_mask>")
    
    # Return the modified text
    return modified_text

def remove_double_spaces(text):
    # pattern = r'\s{2,}'
    # return re.sub(pattern, ' ', text)
    return re.sub(r"\s+", " ", text)

def word_splited(orig_word, new_word_1, new_word_2):
    if levenshtein_distance(orig_word, new_word_1 + new_word_2) <= 1:
        return True
    return False

def put_back_pa_s_and_one_char_words(orig, corrected):
    for idx, word in enumerate(orig):
        if idx >= len(corrected):
            return orig
        
        if word == 'pa' and corrected[idx] != 'pa':
            corrected.insert(idx, 'pa')
            
        if word == ',' and corrected[idx].lower() != word.lower():
            corrected.insert(idx, word)
            
    return corrected

def convert_to_lower_case(input_string):
    return input_string.lower()

def replace_multiple_occurrences_of_punctuation(text):
    pattern = r'\.+'
    text = re.sub(pattern, '.', text)
    
    pattern = r'\?+'
    text = re.sub(pattern, '?', text)
    
    pattern = r'\!+'
    text = re.sub(pattern, '!', text)
    
    #text = re.sub('…', '.', text)
    
    return text

def construct_word(tokens):
    word = ""

    for token in tokens:
        if token.startswith("##"):
            word += token[2:]
        elif token == '[UNK]':
            word += ""
        else:
            word += token
        
    return word

all_combination_strings = []

def combined_distance(splited_text, orig_splited_text, idx, idx_orig):
    return levenshtein_distance(splited_text[idx - 1], orig_splited_text[idx_orig - 1]) + levenshtein_distance(splited_text[idx], orig_splited_text[idx_orig]) + levenshtein_distance(splited_text[idx + 1], orig_splited_text[idx_orig + 1])

def get_most_probable_position(splited_text, orig_splited_text, masked_text, idx):
    if "<concated_word>" in masked_text or "<splited_mask>" in masked_text:
        #print("zaznal za menjavo idx")
        if idx == 0:
            return idx
        elif idx == len(splited_text):
            return idx
        else:
            # print("splited_text: ", splited_text)
            # print("orig_splited_text: ", orig_splited_text)
            # print("idx: ", idx)
            
            combined_distance_0 = combined_distance(splited_text, orig_splited_text, idx - 1, idx)
            
            combined_distance_1 = combined_distance(splited_text, orig_splited_text, idx, idx)
            
            combined_distance_2 = combined_distance(splited_text, orig_splited_text, idx + 1, idx)
            
            #print("combined_distance_0: ", combined_distance_0)
            #print("combined_distance_1: ", combined_distance_1)
            #print("combined_distance_2", combined_distance_2)
            
            if combined_distance_0 < combined_distance_1 and combined_distance_0 < combined_distance_2:
                return idx - 1
            elif combined_distance_2 < combined_distance_0 and combined_distance_2 < combined_distance_1:
                return idx + 1
            else:
                return idx
    return idx
        

def get_all_combinations(array_of_arrays, depth=0, cur_combination=[]):

    if depth >= len(array_of_arrays):
        all_combination_strings.append(construct_word(cur_combination))
        return

    for token in array_of_arrays[depth]:
        new_array = cur_combination.copy()
        new_array.append(token)

        #if (token != '[UNK]'):
        get_all_combinations(array_of_arrays, depth + 1, new_array)
        
def get_all_combinations_2(array_of_arrays):
    memo = {}

    def helper(depth, cur_combination):
        if depth >= len(array_of_arrays):
            return [construct_word(cur_combination)]

        if depth in memo and tuple(cur_combination) in memo[depth]:
            return memo[depth][tuple(cur_combination)]

        all_combinations = []
        for token in array_of_arrays[depth]:
            new_array = cur_combination + [token]

            all_combinations += helper(depth + 1, new_array)

        if depth not in memo:
            memo[depth] = {}
        memo[depth][tuple(cur_combination)] = all_combinations
        return all_combinations

    return helper(0, [])

def levenshtein_distance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize the first row and column
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    # Compute the distances
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if word1[i - 1] == word2[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + cost)
    
    return dp[m][n]

def edit_step(word):
    letters = 'abcčdefghijklmnoprsštuvzž'
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edit_step_2(word):
    return (e2 for e1 in edit_step(word)
            for e2 in edit_step(e1))
    
def write_all_possible_corrections(word):
    all_edits = edit_step(word)
    
    valid_edits = []
    
    #print(words)
    
    for word_edit in all_edits:
        #if word_edit in all_words:
        if word_edit not in valid_edits:
            valid_edits.append(word_edit)
                
    #valid_edits.append(word)
    #random.shuffle(valid_edits)
            
    return valid_edits

def write_all_possible_corrections_2(word):
    all_edits = edit_step_2(word)
    
    valid_edits = []
    
    #print(words)
    
    for word_edit in all_edits:
        #if word_edit in all_words:
        if word_edit not in valid_edits:
            valid_edits.append(word_edit)
                
    #valid_edits.append(word)
    #random.shuffle(valid_edits)
            
    return valid_edits

def find_wrong_word(sent):
    wrong_words = []

    split_sent = sent.split(' ')

    for idx, token in enumerate(split_sent):
        if token == '[MASK]' and split_sent[idx + 1] != '[MASK]':
            wrong_words.append(split_sent[idx + 2])
    
    return wrong_words

def reasignDotsAndCommas(origText, newText):
    dotsCommasSpaces = []
    
    newCharText = ''
    
    for origCharIdx, origChar in enumerate(origText):
        #print("origChar: ", origChar)
        
        charDotCommaSpaceIdx = -1
        
        if origChar == '.' or origChar == ',':
            charDotCommaSpaceIdx = 0
            
            if origCharIdx > 0 and origText[origCharIdx - 1] == ' ' and origCharIdx < len(origText) - 1 and origText[origCharIdx + 1] != ' ':
                charDotCommaSpaceIdx = 1
                
            if origCharIdx > 0 and origText[origCharIdx - 1] != ' ' and origCharIdx < len(origText) - 1 and origText[origCharIdx + 1] == ' ':
                charDotCommaSpaceIdx = 2
                
            if origCharIdx > 0 and origText[origCharIdx - 1] == ' ' and origCharIdx < len(origText) - 1 and origText[origCharIdx + 1] == ' ':
                charDotCommaSpaceIdx = 3
                
            dotsCommasSpaces.append(charDotCommaSpaceIdx)
    
    commaDotIdx = 0
    continueTillNext = False
    
    #print(dotsCommasSpaces)
    
    for newCharIdx, newChar in enumerate(newText):

        if newCharIdx > 0 and newCharIdx < (len(newText) - 1):
            if newText[newCharIdx + 1] == '.' or newText[newCharIdx + 1] == ',':
                if commaDotIdx >= len(dotsCommasSpaces):
                    break
                
                if dotsCommasSpaces[commaDotIdx] == 0:
                    newCharText += newText[newCharIdx + 1]
                elif dotsCommasSpaces[commaDotIdx] == 1:
                    newCharText += ' '
                    newCharText += newText[newCharIdx + 1]
                elif dotsCommasSpaces[commaDotIdx] == 2:
                    newCharText += newText[newCharIdx + 1]
                    newCharText += ' '
                elif dotsCommasSpaces[commaDotIdx] == 3:
                    newCharText += ' '
                    newCharText += newText[newCharIdx + 1]
                    newCharText += ' '
                    
                continueTillNext = True
                commaDotIdx += 1
                    
            elif continueTillNext:
                if newChar != ' ' and newChar != ',' and newChar != '.':
                    newCharText += newChar
                    continueTillNext = False
                    
            else:
                newCharText += newChar
                
        else:
            newCharText += newChar
            
    return newCharText

def add_dot_to_sentence(sentence):
    # Check if the sentence ends with "!", "?", or "."
    if not sentence.endswith(("!", "?", ".")):
        # Add a dot at the end of the sentence
        sentence += "."

    return sentence

def find_indexes_of_character(text, character):
    return [index for index, char in enumerate(text) if char == character]

def place_character_at_indexes(text, character, indexes):
    result = list(text)

    for index in indexes:
        if 0 <= index < len(text):
            result[index] = character

    return ''.join(result)

# def pos_last_dotin_text(text, max_pos):
#     if len(text) < max_pos:
#         return -1
    
#     last_dot_pos = -1
    
#     for idx, char in enumerate(text):
#         if char == '.' or char == '?' or char == '!':
#             last_dot_pos = idx
            
#     if first_dot_pos == -1:
#         first_dot_pos = max_pos
            
#     return last_dot_pos

# def pos_first_dotin_text(text, max_dot_pos):
    
#     first_dot_pos = -1
#     last_space_idx = -1
    
#     for idx, char in enumerate(text):
#         if char == '.' or char == '?' or char == '!':
#             first_dot_pos = idx
#             break
#         if char == ' ':
#             last_space_idx = idx
        
#     if first_dot_pos > max_dot_pos:
#         first_dot_pos = max_dot_pos
    
#     if first_dot_pos == -1 and last_space_idx != -1:
#         first_dot_pos = last_space_idx
        
#     if first_dot_pos == -1:
#         first_dot_pos = max_dot_pos
            
#     return first_dot_pos

def pos_last_dotin_text(text, max_dot_pos):
    
    first_dot_pos = -1
    last_space_idx = -1
    
    for idx, char in enumerate(text):
        if idx >= max_dot_pos:
            break
        
        if char == '.' or char == '?' or char == '!' or char == ':' or char == ';':
            first_dot_pos = idx
        if char == ' ':
            last_space_idx = idx
        
    if first_dot_pos == -1 and last_space_idx != -1:
        first_dot_pos = last_space_idx  
    elif first_dot_pos == -1 and last_space_idx == -1:
        first_dot_pos = max_dot_pos
            
    return first_dot_pos

def remove_spaces_before_some_characters(text):
    # Replace spaces after ( and before )
    text = re.sub(r'\(\s+', '(', text)
    text = re.sub(r'\s+\)', ')', text)
    
    # Replace spaces after " (double quotes), ' (single quotes), : and ;
    text = re.sub(r'"\s+', '"', text)
    text = re.sub(r"'\s+", "'", text)
    text = re.sub(r':\s+', ':', text)
    text = re.sub(r';\s+', ';', text)
    
    return text


# plan da si bi nekam zabelezil vse presledke
# def fill_special_characters_and_spaces(orig_sentance, spaces_array):
#     cur_
    
#     for idx, char in enumerate(orig_sentance):
#         if char