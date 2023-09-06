import random
import csv
import os
import re
import string
import pickle
from random import randint, choice


besede_nagajivke_nepravilne = ['golop', 'vrak', 'hrip', 'blaš', 'poglet', 'grat', 'drobiš', 'krok', 'mras', 'zemljevit', 'paris', 'matevš', 'predlok', 'nahrptnik', 'vrapci', 'retko', 'nagopčnik', 'obras', 'tomaš', 'labot', 'sladolet', 'matjaš', 'moš', 'andraš', 'glazba', 'negdo', 'negdaj', 'rizba', 'gdo', 'gdaj', 'negdaj', 'gdor', 'napisav', 'napisau', 'domou', 'domol', 'beu', 'rou', 'lou', 'kupiu', 'nou', 'miseu', 'siu', 'žouna', 'oseu', 'učitel', 'kluka', 'učitelica', 'kegel', 'lubezniv', 'kniga', 'kon', 'zadni', 'sosedni', 'češna', 'bližnica', 'prijatelica', 'škoren', 'čevel', 'fotel', 'uhel', 'hmel', 'savinski', 'ravnatel', 'tulnje', 'tjulne', 'tjulni', 'tjulen', 'metul', 'knižničar', 'polje', 'ragla', 'reditel', 'zdroblen', 'bradla', 'prejšni', 'žemle', 'razsvetlava', 'zemelski', 'mravla', 'obluba', 'cinglati', 'von', 'čebelnak', 'življenski']
besede_nagajivke_pravilne = ['golob', 'vrag', 'hrib', 'blaž', 'pogled', 'grad', 'drobiž', 'krog', 'mraz', 'zemljevid', 'pariz', 'matevž', 'predlog', 'nahrbtnik', 'vrabci', 'redko', 'nagobčnik', 'obraz', 'tomaž', 'labod', 'sladoled', 'matjaž', 'mož', 'andraž', 'glasba', 'nekdo', 'nekdaj', 'risba', 'kdo', 'kdaj', 'nekdaj', 'kdor', 'napisal', 'napisal', 'domov', 'domov', 'bel', 'rov', 'lov', 'kupil', 'nov', 'misel', 'siv', 'žolna', 'osel', 'učitelj', 'kljuka', 'učiteljica', 'kegelj', 'ljubezniv', 'knjiga', 'konj', 'zadnji', 'sosednji', 'češnja', 'bližnjica', 'prijateljica', 'škorenj', 'čevelj', 'fotelj', 'uhelj', 'hmelj', 'savinjski', 'ravnatelj', 'tjuljnje', 'tjulnje', 'tjuljni', 'tjulenj', 'metulj', 'knjižnjičar', 'polje', 'raglja', 'reditelj', 'zdrobljen', 'bradlja', 'prejšnji', 'žemlje', 'razsvetljava', 'zemeljski', 'mravlja', 'obljuba', 'cingljati', 'vonj', 'čebelnjak', 'življenjski']
slovenian_alphabet_uppercase = ['A', 'B', 'C', 'Č', 'Ć', 'D', 'Đ', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'NJ', 'O', 'P', 'R', 'S', 'Š', 'T', 'U', 'V', 'Z', 'Ž', '_', '/']
slovenian_alphabet_lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'lj', 'm', 'n', 'nj', 'o', 'p', 'r', 's', 't', 'u', 'v', 'z']
linking_words = ["in", "kot", "ali", "oziroma", "ter", "le", "čeprav", "tudi", "vendar", "vključno", "kjer", "ki", "kateri", "a", "ne", "niti"]
filler_words = ["pa"]
link_sentences_filler = ["in"]

valid_chars = "abcčdefghijklmnoprsštuvzž"

lemma_dict = {}
count_lemma_dict = {}
root_lemma_dict = {}

#all_words = {}

with open('root_lemma_dict.pkl', 'rb') as f:
    root_lemma_dict = pickle.load(f)
    #print(root_lemma_dict)
    
# with open('lemma_dict.pkl', 'rb') as f:
#     lemma_dict = pickle.load(f)
#     #print(lemma_dict)
    
# with open('count_lemma_dict.pkl', 'rb') as f:
#     count_lemma_dict = pickle.load(f)
    
# with open('ssks_besede.txt', 'r') as file:
#     for line in file:
#         word = line.strip()
#         if word not in all_words:
#             all_words[word] = 1


def take_with_prob(probability=0.5):
    return random.random() < probability

def randomize_spaces_in_pomisljaj_characters(line_in: str, probability=0.5) -> str:
    line = re.sub(r'\s*-\s*', '-', line_in)
    new_line = []
    for char in line:
        if char == '-':
            if random.random() > probability:
                new_line.append(' ')
            new_line.append(char)
            if random.random() > probability:
                new_line.append(' ')
        else:
            new_line.append(char)
    return ''.join(new_line)

def randomly_change_word_cases(text: str, probability=0.3) -> str:
    words = text.split()

    new_words = []
    for word in words:
        if random.random() < probability:
            if word[0].isupper():
                new_word = word[0].lower() + word[1:]
                new_words.append(new_word)
            elif word[0].islower():
                new_words.append(word.capitalize())
            else:
                new_words.append(word.capitalize())
        else:
            new_words.append(word)
    
    return " ".join(new_words)

def split_word_random(word):
    if len(word) <= 1:
        return [word]

    split_point = random.randint(1, len(word) - 1)
    return [word[:split_point], word[split_point:]]

def split_random_words(text: str, probability: 0.06) -> str:
    words = text.split()

    new_words = []
    for word in words:
        if random.random() < probability and can_modify(word) and len(word) > 1:
            word1, word2 = split_word_random(word)
            new_words.append(word1 + "<splited_word>" + word2)
            #new_words.append("<splited_word>" + word2)
        else:
            new_words.append(word)
    
    return " ".join(new_words)

def concat_random_words(text: str, probability: 0.04) -> str:
    words = text.split()

    new_words = []
    
    for word in words:
        if random.random() < probability and len(new_words) > 0 and "<splited_word>" not in word and "<splited_word>" not in new_words[-1] and word not in string.punctuation and new_words[-1] not in string.punctuation and not new_words[-1].startswith("<concated_word>"):
            if new_words[-1].startswith("<concated_word>"):
                new_words[-1] = new_words[-1] + word
            else:
                new_words[-1] = "<concated_word>" + new_words[-1] + word
        else:
            new_words.append(word)
    
    return " ".join(new_words)

def replace_random_s_z_characters_in_string(text: str, probability=0.5) -> str:
    words = text.split()

    modified_words = []
    for word in words:
        if word == "s" or word == "z":
            if random.random() > probability:
                modified_words.append("s")
            else:
                modified_words.append("z")
        else:
            modified_words.append(word)

    return " ".join(modified_words)

def replace_random_k_h_characters_in_string(text: str, probability=0.5) -> str:
    words = text.split()

    modified_words = []
    for word in words:
        if word == "k" or word == "h":
            if random.random() > probability:
                modified_words.append("k")
            else:
                modified_words.append("h")
        else:
            modified_words.append(word)

    return " ".join(modified_words)

def replace_random_chars(input_string: str) -> str:
    words = input_string.split()
    
    modified_words = []
    
    for word in words:
        new_word = word

        while random.random() < 0.1:
            index_to_replace = random.randint(0, len(new_word) - 1)
            
            chars = list(new_word)
            
            chars[index_to_replace] = random.choice(chars)
            
            new_word = ''.join(chars)
        
        modified_words.append(new_word)
    
    return ' '.join(modified_words)

def switch_characters(word, idx1, idx2):

    chars = list(word)

    chars[idx1], chars[idx2] = chars[idx2], chars[idx1]

    return ''.join(chars)

def replace_random_chars_in_word_2(word, charSubselection, charReplaceProb=0.15) -> str:
    while random.random() < charReplaceProb and len(word) > 1:
        index_to_replace = random.randint(1, len(word) - 1)
        
        chars = list(word)
        
        char_to_replace = ''
        
        if chars[index_to_replace].lower() in charSubselection:
            chars[index_to_replace] = random.choice(charSubselection)
            
        word = ''.join(chars)
    
    return word

def insert_random_chars_in_word_2(word, charSubselection, charReplaceProb=0.1) -> str:
    while random.random() < charReplaceProb and len(word) > 1:
        index_to_insert = random.randint(1, len(word) - 1)
        
        chars = list(word)
        
        char_to_insert = ''

        if chars[index_to_insert].lower() in charSubselection:
            char_to_insert = random.choice(charSubselection)
            
            chars.insert(index_to_insert, char_to_insert)
            
        word = ''.join(chars)
    
    return word

def remove_random_chars_in_word_2(word, charRemoveProb=0.1) -> str:
    while random.random() < charRemoveProb and len(word) > 1:
        index_to_remove = random.randint(1, len(word) - 1)
        
        chars = list(word)
        
        chars[index_to_remove] = ''
            
        word = ''.join(chars)
    
    return word            
        

def replace_random_chars_in_word(word, charReplaceProb=0.15, checkLower=False) -> str:
    while random.random() < charReplaceProb and len(word) > 1:
        index_to_replace = random.randint(1, len(word) - 1)
        
        chars = list(word)
        
        if chars[index_to_replace].isdigit() or chars[index_to_replace] in string.punctuation:
            continue
        
        char_to_replace = ''
        
        if checkLower and not chars[index_to_replace].islower():
            print("not lower: ", chars[index_to_replace])
            continue
        
        if chars[index_to_replace].isupper():
            char_to_replace = random.choice(slovenian_alphabet_uppercase)
        else:
            char_to_replace = random.choice(slovenian_alphabet_lowercase)

        random_value = random.random()
        
        if random_value < 0.35:
            chars[index_to_replace] = ''
        elif random_value < 0.55:
            char_to_replace = random.choice(slovenian_alphabet_lowercase)
            if char_to_replace != '/':
                len_chars_prej = len(chars)
                chars.insert(index_to_replace, char_to_replace)
                assert len(chars) == len_chars_prej + 1
        elif random_value < 0.8:
            #switch random two chars that stand together
            index_to_switch = index_to_replace
            if index_to_switch == len(word) - 1:
                index_to_switch -= 1
            
            #print("before chars: ", chars)
            chars[index_to_switch - 1], chars[index_to_switch] = chars[index_to_switch], chars[index_to_switch - 1]
            #print("after chars: ", chars)
        else:
            assert random_value >= 0.80 and random_value <= 1.0
            
            chars[index_to_replace] = char_to_replace
            
        word = ''.join(chars)
        
    return word

def replace_random_chars_in_text(input_string: str, word_pick_prob=0.10, char_replace_prob=0.2) -> str:
    words = input_string.split()
    
    modified_words = []
    
    itr_index = 0
    for word in words:
        new_word = word
        
        #if itr_index >= 0 and itr_index < len(words) and not word.isdigit() and not word in string.punctuation and not word in linking_words and len(word) > 1:
        if itr_index >= 0 and itr_index < len(words) and not word.isdigit() and not word in string.punctuation and can_modify(word):
            if take_with_prob(word_pick_prob):
                new_word = replace_random_chars_in_word(word, char_replace_prob)
        
        modified_words.append(new_word)
        itr_index += 1
    
    return ' '.join(modified_words)

def replace_random_chars_in_text_2(input_string: str) -> str:
    words = input_string.split()
    
    modified_words = []
    
    for itr_index, word in enumerate(words):
        new_word = word
        
        if not word.isdigit() and not word in string.punctuation and can_modify(word):
            new_word = replace_random_chars_in_word_2(word, 'aeiou', 0.05)
            
            new_word = replace_random_chars_in_word_2(new_word, 'bcčdfghjklmnprsštvzž', 0.05)
            
            new_word = replace_random_chars_in_word_2(new_word, 'abcčdevghijklmnoprsštuvzž', 0.02)
            
            new_word = remove_random_chars_in_word_2(new_word, 0.04)
            
            new_word = insert_random_chars_in_word_2(new_word, 'abcčdevghijklmnoprsštuvzž', 0.03)
        
        modified_words.append(new_word)
    
    return ' '.join(modified_words)

def replace_random_linking_words_in_text(input_string: str, linking_word_replacement_prob=0.2) -> str:
    words = input_string.split()
    
    modified_words = []
    
    itr_index = 0
    for word in words:
        new_word = word
        
        if itr_index > 0 and itr_index < len(words) - 1 and not word.isdigit() and not word in string.punctuation and word in linking_words and take_with_prob(linking_word_replacement_prob):
            new_word = random.choice(linking_words)
        
        modified_words.append(new_word)
        itr_index += 1
    
    return ' '.join(modified_words)

def can_modify(word):
    return "<splited_word>" not in word and "<concated_word>" not in word
    

def zamenjaj_besede_nagajivke(input_string: str, probability=0.6) -> str:
    words = input_string.split()

    for i, word in enumerate(words):
        for j, w in enumerate(besede_nagajivke_pravilne):
            if take_with_prob(probability) and can_modify(word):
                if word.startswith(w):
                    words[i] = word.replace(w, besede_nagajivke_nepravilne[j], 1)
                elif word.startswith(w[:-1]):
                    words[i] = word.replace(w[:-1], besede_nagajivke_nepravilne[j][:-1], 1)

    return " ".join(words)

def replace_nj(text, prob=0.3):
    words = text.split()
    new_words = []
    for word in words:
        new_word = word
        if take_with_prob(prob) and can_modify(word):
            new_word = word.replace('nj', 'n')
        new_words.append(new_word)
    return ' '.join(new_words)

def replace_lj(text, prob=0.3):
    words = text.split()
    new_words = []
    for word in words:
        new_word = word
        if take_with_prob(prob) and can_modify(word):
            new_word = word.replace('lj', 'l')
        new_words.append(new_word)
    return ' '.join(new_words)

def replace_v_na(text, prob=0.4):
    words = text.split()
    new_words = []
    for word in words:
        new_word = word
        if take_with_prob(prob):
            if word == 'v':
                new_word = word.replace('v', 'na')
        elif take_with_prob(prob):
            if word == 'na':
                new_word = word.replace('na', 'v')
        new_words.append(new_word)
    return ' '.join(new_words)

def replace_konec_besed_v_l(text, prob=0.4):
    words = text.split()
    new_words = []
    for word in words:
        new_word = word
        if take_with_prob(prob) and can_modify(word):
            if new_word[-1] == 'l' and len(new_word) > 3:
                new_word = new_word[:-1] + 'v'
            elif new_word[-1] == 'v' and len(new_word) > 3:
                new_word = new_word[:-1] + 'l'
        new_words.append(new_word)
    return ' '.join(new_words)

def replace_some_predefined_characters(text, prob=0.7, num_repeats=4):
    words = text.split()
    new_words = []
    for word in words:
        new_word = word
        if take_with_prob(prob) and can_modify(word):
            for num_repeat in range(0, num_repeats):
                random_number = random.randint(1, 30)
                
                if random_number == 1:
                    new_word = word.replace('nj', 'n')
                elif random_number == 2:
                    new_word = word.replace('n', 'nj')
                elif random_number == 3:
                    new_word = word.replace('l', 'lj')
                elif random_number == 4:
                    new_word = word.replace('lj', 'l')
                elif random_number == 5:
                    new_word = word.replace('t', 'd')
                elif random_number == 6:
                    new_word = word.replace('d', 't')
                elif random_number == 7:
                    new_word = word.replace('v', 'u')
                elif random_number == 8:
                    new_word = word.replace('u', 'v')
                elif random_number == 9:
                    new_word = word.replace('u', 'el')
                elif random_number == 10:
                    new_word = word.replace('el', 'u')
                elif random_number == 11:
                    new_word = word.replace('i', 'j')
                elif random_number == 12:
                    new_word = word.replace('j', 'i')
                elif random_number == 13:
                    new_word = word.replace('k', 'kj')
                elif random_number == 14:
                    new_word = word.replace('kj', 'k')
                elif random_number == 15:
                    new_word = word.replace('k', 'h')
                elif random_number == 16:
                    new_word = word.replace('h', 'k')
                elif random_number == 17:
                    new_word = word.replace('k', 'g')
                elif random_number == 18:
                    new_word = word.replace('g', 'k')
                elif random_number == 19:
                    new_word = word.replace('s', 'z')
                elif random_number == 20:
                    new_word = word.replace('z', 's')
                elif random_number == 21:
                    new_word = word.replace('p', 'b')
                elif random_number == 22:
                    new_word = word.replace('b', 'p')
                elif random_number == 23:
                    new_word = word.replace('š', 'ž')
                elif random_number == 24:
                    new_word = word.replace('ž', 'š')
                elif random_number == 25:
                    new_word = word.replace('v', 'l')
                elif random_number == 26:
                    new_word = word.replace('l', 'v')
                elif random_number == 27:
                    new_word = word.replace('u', 'l')
                elif random_number == 28:
                    new_word = word.replace('l', 'u')
                elif random_number == 29:
                    new_word = word.replace('t', 'tj')
                elif random_number == 30:
                    new_word = word.replace('tj', 't')
                    
                if new_word != word:
                    #print('NOT EQUAL')
                    break
        new_words.append(new_word)
    return ' '.join(new_words)

def zamenjaj_koncna_locila(text, prob=0.4):
    punc = '!?:;"\'?.'
    if take_with_prob(prob):
        return ''.join([random.choice(punc) if char in punc else char for char in text])
    return text

def add_spaces_before_and_after_punctuation(text):
    punctuation = set(string.punctuation)

    # Initialize an empty string to store the modified text
    modified_text = ""

    # Loop through each character in the text
    for char in text:
        # If the character is a punctuation mark
        if char in punctuation:
            # Add a space before and after the punctuation mark
            modified_text += " " + char + " "
        else:
            # Otherwise, just add the character to the modified text
            modified_text += char

    # Return the modified text
    return modified_text

def remove_spaces_before_punctuation(text):
    return re.sub(r'\s+([,.!?;])', r'\1', text)

def change_word_endings(text, probability=0.1):
    words = text.split()
    
    array_of_words = []
    
    for word in words:
        if word not in string.punctuation and word in root_lemma_dict and not word.isdigit() and take_with_prob(probability) and can_modify(word):
            lemma = root_lemma_dict[word.lower()]
            
            arr = count_lemma_dict[lemma]
            
            weights = [num / sum(arr) for num in arr]
            chosen_idx = random.choices(range(len(arr)), weights=weights)[0]
            
            array_of_words.append(lemma_dict[lemma][chosen_idx])
        else:
            array_of_words.append(word)
            
    return ' '.join(array_of_words)

def shuffle_n_words(words, n):
    if len(words) != len(set(words)):
        return words
    
    if len(words) == 0:
        return words
    
    if n > len(words):
        print("vecja dolzina besed as it should be")
        n = len(words)
    
    words_to_shuffle = random.sample(words, n)
    random.shuffle(words_to_shuffle)
    shuffled_words = []
    i = 0
    #print("n je: ", n)
    #print("words_to_shuffle: ", words_to_shuffle)
    #print("words: ", words)
    for word in words:
        if word in words_to_shuffle:
            shuffled_words.append(words_to_shuffle[i])
            i += 1
        else:
            shuffled_words.append(word)
    return shuffled_words

def weighted_random(max_number):
    if max_number < 2:
        raise ValueError("max_number should be greater than or equal to 2")

    choices = list(range(2, max_number + 1))
    weights = list(reversed(range(1, len(choices) + 1)))

    return random.choices(choices, weights, k=1)[0]

def mix_word_order_in_sentence(text, probability=0.1, change_verbs=False):
    words = text.split()
    
    array_of_words = []
    keep_shuffle_array = []
    
    for word in words:
        if word in linking_words or word in string.punctuation or ',' in word:
            keep_shuffle_array.append(0)
        else:
            keep_shuffle_array.append(1)
        array_of_words.append(word)
        
    found_something_or_beginning = True
    
    while found_something_or_beginning:
        found_something_or_beginning = False
        just_shuffle_array = []
        
        for index in range(0, len(array_of_words)):
            if keep_shuffle_array[index] == 1:
                found_something_or_beginning = True
                just_shuffle_array.append(array_of_words[index])
            elif found_something_or_beginning:
                break
        
        #print("before just_shuffle_array: ", just_shuffle_array)
        
        # rand_int = random.randint(0, 100)
        # how_many_to_shuffle = 5
        # if rand_int < 40:
        #     how_many_to_shuffle = 2
        # elif rand_int < 70:
        #     how_many_to_shuffle = 3
        # elif how_many_to_shuffle < 90:
        #     how_many_to_shuffle = 4
        
        max_number = 10
        if len(just_shuffle_array) >= 2:
            how_many_to_shuffle = weighted_random(len(just_shuffle_array))
            
            #random.shuffle(just_shuffle_array)
            just_shuffle_array = shuffle_n_words(just_shuffle_array, how_many_to_shuffle)
        
        #print("after just_shuffle_array: ", just_shuffle_array)
        
        #shuffle_section = (len(just_shuffle_array) <= 5 and random.random() < probability) or (len(just_shuffle_array) > 5 and random.random() < (probability / len(just_shuffle_array)))
        shuffle_section = random.random() < probability
        
        shuffled_array_index = 0
        for index in range(0, len(array_of_words)):
            if keep_shuffle_array[index] == 1:
                if shuffle_section:
                    array_of_words[index] = just_shuffle_array[shuffled_array_index].lower()
                shuffled_array_index += 1
                keep_shuffle_array[index] = 0
            elif shuffled_array_index > 0:
                break
            
    return " ".join(array_of_words)

def mix_sentences(text, probability=0.1):
    words = text.split()
    
    array_of_words = []
    keep_shuffle_array = []
    
    arrays_of_sentences = []
    array_of_fillers = []
    sentences_index_array = []
    
    sentence_index = 0
    
    for word in words:
        if word in linking_words or word in string.punctuation or ',' in word:
            keep_shuffle_array.append(0)
            array_of_fillers.append(word)
        else:
            keep_shuffle_array.append(1)
        array_of_words.append(word)
        
    found_something_or_beginning = True
    
    while found_something_or_beginning:
        found_something_or_beginning = False
        just_shuffle_array = []
        
        for index in range(0, len(array_of_words)):
            if keep_shuffle_array[index] == 1:
                keep_shuffle_array[index] = 0
                found_something_or_beginning = True
                just_shuffle_array.append(array_of_words[index])
            elif found_something_or_beginning:
                break
        
        if len(just_shuffle_array) > 0:
            arrays_of_sentences.append(" ".join(just_shuffle_array))
            sentences_index_array.append(sentence_index)
            sentence_index += 1
        
    #print("arrays_of_sentences: ", arrays_of_sentences)
    #print("array_of_fillers: ", array_of_fillers)
    #print("sentences_index_array: ", sentences_index_array)
    
    rand_int = random.randint(0, 100)
    how_many_to_shuffle = 3
    if rand_int < 70:
        how_many_to_shuffle = 2
    
    #print("before just_shuffle_sentences_index_array: ", sentences_index_array)
    
    just_shuffle_sentences_index_array = shuffle_n_words(sentences_index_array, how_many_to_shuffle)
    
    #print("after just_shuffle_sentences_index_array: ", just_shuffle_sentences_index_array)
    
    final_sentence = ""
    
    filler_index = 0
    for sentence_index in just_shuffle_sentences_index_array:
        final_sentence += arrays_of_sentences[sentence_index]
        
        if filler_index < len(array_of_fillers):
            final_sentence += " " + array_of_fillers[filler_index] + " "
            
            filler_index += 1
            
    return final_sentence

def insert_random_filler_words(text, probability=0.05):
    words = text.split()
    
    new_words_array = []
    
    for word in words:
        new_words_array.append(word)
        
        if word not in linking_words and word not in string.punctuation and ',' not in word and take_with_prob(probability):
            new_words_array.append(random.choice(filler_words))
            
    return " ".join(new_words_array)

def convert_to_lower_case(input_string):
    return input_string.lower()

def replace_all_ž_š_č_characters(text, prob=1.0):
    if random.random() < prob:
        text = text.replace('ž', 'z')
        text = text.replace('š', 's')
        text = text.replace('č', 'c')
    
    return text










def split_and_replace(input_str, mark_othrs_with_hash=True):
    slovenian_alphabet = set('abcčdefghijklmnoprsštuvzž')
    output_str = ''
    for char in input_str:
        if char == ' ':
            output_str += '_'
        elif char.lower() not in slovenian_alphabet and mark_othrs_with_hash:
            output_str += '#'
        else:
            output_str += char
        output_str += ' '
    return output_str

def de_split(input_str):
    input_str = re.sub(' ', '', input_str)
    return re.sub('_', ' ', input_str)

def remove_random_characters_in_array(input_char_str, prob=0.3):
    input_str_array = input_char_str.split(' ')
    new_char_str = input_char_str
    
    if take_with_prob(prob):
        num_chars_to_remove = weighted_random(4) - 1

        # loop through the array and remove random characters
        for i in range(num_chars_to_remove):
            # get a random index from the array
            random_index = random.randint(0, len(input_str_array)-1)
            # remove the character at the random index
            
            if input_str_array[random_index] != '#':
                input_str_array.pop(random_index)

        new_char_str = " ".join(input_str_array)
        
        #print("popped_input_char_str: ", new_char_str)
        
    return new_char_str

def remove_random_chars_by_word(input_char_str, prob=0.05, do_not_remove_spaces=False, masked_words=False):
    input_str_array = input_char_str.split(' ')
    new_char_str = input_char_str
    
    for index in range(len(input_str_array) - 3):
        if index < len(input_str_array) -1 and take_with_prob(prob):
            
            if masked_words and input_str_array[index] in valid_chars and ((index == 0 or input_str_array[index - 1] != '_') or input_str_array[index + 1] != '_'):
                input_str_array.pop(index)
            elif (do_not_remove_spaces or input_str_array[index] != '_') and input_str_array[index] != '#' and ((index == 0 or input_str_array[index - 1] != '_') or input_str_array[index + 1] != '_'):
                input_str_array.pop(index)
                
    new_char_str = " ".join(input_str_array)
    
    return new_char_str

def duplicate_random_chars(input_char_str, prob=0.2):
    input_str_array = input_char_str.split(' ')
    new_char_str = input_char_str
    
    if take_with_prob(prob):
        
        num_chars_to_duplicate = weighted_random(3) - 1
    
        for i in range(num_chars_to_duplicate):
            
            random_index = random.randint(0, len(input_str_array)-1)
            
            if input_str_array[random_index] != '#' and input_str_array[random_index] != '_':
                input_str_array.insert(random_index, input_str_array[random_index])
            
        new_char_str = " ".join(input_str_array)
        
        #print("popped_input_char_str: ", new_char_str)
        
    return new_char_str


def insert_random_chars(input_char_str, prob=0.1):
    input_str_array = input_char_str.split(' ')
    new_char_str = input_char_str
    
    if take_with_prob(prob):
    
        num_chars_to_insert = weighted_random(3) - 1
        
        # loop through the array and insert random characters
        for i in range(num_chars_to_insert):
            # get a random valid character
            random_char = random.choice(valid_chars)
            # get a random index from the array
            random_index = random.randint(0, len(input_str_array))
            # insert the random character into the array at the random index
            input_str_array.insert(random_index, random_char)
            
            new_char_str = " ".join(input_str_array)
    
    return new_char_str

def insert_random_chars_by_word(input_char_str, prob=0.05, masked_words=False):
    input_str_array = input_char_str.split(' ')
    new_char_str = input_char_str
    
    for index in range(len(input_str_array) - 1):
        if take_with_prob(prob):
            random_char = random.choice(valid_chars)
            
            if masked_words:
                if input_str_array[index] in valid_chars and (input_str_array[index - 1] != '_' or input_str_array[index + 1] != '_'):
                    input_str_array[index] = random_char
            elif input_str_array[index] != '#' and (input_str_array[index - 1] != '_' or input_str_array[index + 1] != '_'):     
                input_str_array.insert(index, random_char)
    
    new_char_str = " ".join(input_str_array)
    
    return new_char_str


def replace_random_char(input_char_str, prob=0.3):
    input_str_array = input_char_str.split(' ')
    new_char_str = input_char_str
    
    if take_with_prob(prob):
    
        num_chars_to_insert = weighted_random(5) - 1
        
        for i in range(num_chars_to_insert):
            
            random_index = random.randint(1, len(input_str_array)-2)
            
            random_char = random.choice(valid_chars)
            
            if input_str_array[random_index] != '#' and (input_str_array[random_index - 1] != '_' or input_str_array[random_index + 1] != '_'):
                input_str_array[random_index] = random_char
            
        new_char_str = " ".join(input_str_array)
        
    return new_char_str

def replace_random_chars_by_word(input_char_str, prob=0.05, masked_words=False):
    input_str_array = input_char_str.split(' ')
    new_char_str = input_char_str
    
    for index in range(len(input_str_array) - 1):
        if take_with_prob(prob):
            
            random_char = random.choice(valid_chars)
            
            if masked_words:
                if input_str_array[index] in valid_chars and (input_str_array[index - 1] != '_' or input_str_array[index + 1] != '_'):
                    input_str_array[index] = random_char
            elif input_str_array[index] != '_' and input_str_array[index] != '#' and (input_str_array[index - 1] != '_' or input_str_array[index + 1] != '_'):
                input_str_array[index] = random_char
                
    new_char_str = " ".join(input_str_array)
        
    return new_char_str

def remove_concated_splited_word_indicators(incorrect_line):
    #"<splited_word>" not in word and "<concated_word>" not in word
    
    incorrect_line = re.sub("<splited_word>", ' ', incorrect_line)
    incorrect_line = re.sub("<concated_word>", '', incorrect_line)
    
    return incorrect_line
    

def mark_false_words(incorrect_line, original_line):
    new_incorrect_line = []
    new_original_line  = []
    
    numConcat = incorrect_line.count("<concated_word>")
    
    incorrect_line = incorrect_line.strip()
    original_line = original_line.strip()
    
    incorrect_line = incorrect_line.split(' ')
    original_line = original_line.split(' ')
    
    if (len(incorrect_line) + numConcat) != len(original_line):
        print("incorrect_line: ", incorrect_line)
        print("original_line: ", original_line)
        print("incorrect_line length: ", len(incorrect_line))
        print("count: ", numConcat)
        print("len(original_line): ", len(original_line))
    
    assert (len(incorrect_line) + numConcat) == len(original_line)
    
    # print("incorrect_line: ", incorrect_line)
    # print("original_line: ", original_line)
    plus_orig_line_counter = 0
    
    for i in range(0, len(incorrect_line)):
        #new_incorrect_line.append(incorrect_line[i])
        
        if can_modify(incorrect_line[i]):
            new_incorrect_line.append(incorrect_line[i])
        
            if incorrect_line[i] == original_line[i + plus_orig_line_counter]:
                new_original_line.append(original_line[i + plus_orig_line_counter])
            else:
                new_original_line.append(original_line[i + plus_orig_line_counter] + "<mask>" + incorrect_line[i])
                #new_original_line.append("<mask>")
        else:
            if "<splited_word>" in incorrect_line[i]:
                word1, word2 = incorrect_line[i].split("<splited_word>")
                new_incorrect_line.append(word1)
                new_incorrect_line.append(word2)
                
                new_original_line.append("<splited_mask>")
                new_original_line.append("<splited_mask>")
            elif "<concated_word>" in incorrect_line[i]:
                plus_orig_line_counter += 1
                
                word0 = incorrect_line[i].split("<concated_word>")[1]
                
                new_incorrect_line.append(word0)
                new_original_line.append("<concated_word>")
            
    #print("new_incorrect_line: ", new_incorrect_line)
    #print("new_original_line: ", new_original_line)
            
    assert len(new_incorrect_line) == len(new_original_line)
    
    new_incorrect_line = " ".join(new_incorrect_line)
    new_original_line = " ".join(new_original_line)
    
    return (new_incorrect_line, new_original_line)

def remove_double_spaces(text):
    pattern = r'\s{2,}'
    return re.sub(pattern, ' ', text)

def de_split(input_str):
    input_str = re.sub(' ', '', input_str)
    return re.sub('_', ' ',  input_str)

def replace_new_lines_and_double_Spaces(line):
    line = re.sub(r"\s+", ' ', line)
    return re.sub('\n', '', line)

def make_bert_mask_row(line):
    row_has_mask = False
    
    end_words = []
    new_line = []
    
    new_masked_line = []
    #new_line.append('[CLS]')
    
    for word in line.split(' '):
        if "<mask>" in word:
            row_has_mask = True
            #end_words.append(word.split('<mask>')[1])
            end_word = word.split('<mask>')[1]
            new_line.append(word.split('<mask>')[0])
            new_masked_line.append('[MASK]')
            
            new_line.append('( ' + end_word + ' )')
            new_masked_line.append('( ' + end_word + ' )')
        else:
            new_line.append(word)
            new_masked_line.append(word)
            
    #new_line.append('[SEP]')
    
    output_line = " ".join(new_line)
    output_maked_line = " ".join(new_masked_line)
    
    for word in end_words:
        output_line += " " + word
        output_maked_line += " " + word
    
    if row_has_mask:
        return (output_maked_line, output_line)
    else:
        return (None, None)
    
def make_bert_mask_row_2(line):
    row_has_mask = False
    
    end_words = []
    new_line = []
    
    new_masked_line = []
    possible_words = []
    #new_line.append('[CLS]')
    
    for word in line.split(' '):
        if "<mask>" in word:
            if not row_has_mask:
                row_has_mask = True
                
                correct_word = word.split('<mask>')[0]
                
                possible_words = write_all_possible_corrections(correct_word)
                idx_of_correct_word = possible_words.index(correct_word)
                
                #end_words.append(word.split('<mask>')[1])
                end_word = word.split('<mask>')[1]
                new_line.append(str(idx_of_correct_word))
                new_masked_line.append('[MASK]')
                
                #new_line.append('( ' + end_word + ' )')
                #new_masked_line.append('( ' + end_word + ' )')
            else:
                correct_word = word.split('<mask>')[0]
                
                new_line.append(correct_word)
                new_masked_line.append(correct_word)
        else:
            new_line.append(word)
            new_masked_line.append(word)
    
    
         
    #new_line.append('[SEP]')
    new_line.append('(')
    new_masked_line.append('(')
    
    for idx, possible_word in enumerate(possible_words):
        new_line.append(str(idx) + ":" + possible_word)
        new_masked_line.append(str(idx) + ":" + possible_word)
        
    new_line.append(')')
    new_masked_line.append(')')
    
    output_line = " ".join(new_line)
    output_maked_line = " ".join(new_masked_line)
    
    for word in end_words:
        output_line += " " + word
        output_maked_line += " " + word
    
    if row_has_mask:
        return (output_maked_line, output_line)
    else:
        return (None, None)

def make_T5_row(line):
    new_line = []
    
    for word in line.split(' '):
        if "<mask>" in word:
            new_line.append('<mask>')
        else:
            new_line.append(word)
            
    
    return " ".join(new_line)

def preprocess_line(line):
    return re.sub('_', ' ', line)

def edit_step(word):
    """
    All edits that are one edit away from `word`.
    """
    letters = 'abcdefghijklmnopqrstuvwxyz'
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edit_step_2(word):
    """
    All edits that are two edits away from `word`.
    """
    return (e2 for e1 in edit_step(word)
            for e2 in edit_step(e1))

def write_all_possible_corrections(word):
    all_edits = edit_step(word)
    
    valid_edits = []
    
    #print(words)
    
    for word_edit in all_edits:
        if word_edit in all_words:
            if word_edit not in valid_edits:
                valid_edits.append(word_edit)
                
    valid_edits.append(word)
    random.shuffle(valid_edits)
            
    return valid_edits
    

#def mark_