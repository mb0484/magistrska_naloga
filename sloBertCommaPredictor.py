import re

from transformers import CamembertTokenizer, CamembertForMaskedLM
import string

import torch

device = "cuda:0" if torch.cuda.is_available() else "cpu"

tokelineer = CamembertTokenizer.from_pretrained('finetuned_slobert_model/')
output_dir = 'finetuned_slobert_model/'
model = CamembertForMaskedLM.from_pretrained(output_dir).to(device)

tokelineer_dots = CamembertTokenizer.from_pretrained('finetuned_slobert_model_dots/')
output_dir_dots = 'finetuned_slobert_model_dots/'
final_punct = ['!', '.', '?', ':', ';']
quote_sign = ['"', '\'', '`', '»', '«', '”', '“']
mask_token_id = 32004
saved_spaces_before_quotes = {}
counter_saved_spaces = -1

saved_double_spaces = {}
double_spaces_counter = 0

saved_double_dots = {}
double_dots_counter = 0

model_dots = CamembertForMaskedLM.from_pretrained(output_dir_dots).to(device)

model.eval()
model_dots.eval()

# markedCommaType, 0 -> comma, which is predicted and original text, 1 -> comma, which isn't in predicted, but is in original text, 2 -> comma, which is in predicted, but isn't in original text
def markUpWord(word, markedCommaType):
    if markedCommaType == 1:
        return "<mark class='markVejicaPrejJaZdejNe'>" + word + "</mark>"
    elif markedCommaType == 2:
        return "<mark class='markVejicaPrejNeZdejJa'>" + word + "</mark>"
    return word

def fill_double_spaces_with_special_characters(line):
    replaced_spaces_string = " "

    for i in range(len(line.group(0)) - 1):
        replaced_spaces_string += '&nbsp;'
    
    return replaced_spaces_string

def mark_up_placed_text(origin_sentences, placed_sentences):
    newly_placed_sentences = ""
    split_origin_sentences = origin_sentences.split(" ")
    split_placed_sentences = placed_sentences.split(" ")

    assert len(split_origin_sentences) == len(split_placed_sentences)

    for i in range(0, len(split_origin_sentences)):
        if i != 0:
            newly_placed_sentences += " "
        if (not split_origin_sentences[i].endswith(",") and split_placed_sentences[i].endswith(",")) or (not split_origin_sentences[i].endswith(",\"") and split_placed_sentences[i].endswith(",\"")) or (not split_origin_sentences[i].endswith(",”") and split_placed_sentences[i].endswith(",”")) or (not split_origin_sentences[i].endswith(",«") and split_placed_sentences[i].endswith(",«")):
            newly_placed_sentences += markUpWord(split_placed_sentences[i], 1)
        elif (split_origin_sentences[i].endswith(",") and not split_placed_sentences[i].endswith(",")) or (split_origin_sentences[i].endswith(",\"") and not split_placed_sentences[i].endswith(",\"")) or (split_origin_sentences[i].endswith(",”") and not split_placed_sentences[i].endswith(",”")) or (split_origin_sentences[i].endswith(",«") and not split_placed_sentences[i].endswith(",«")):
            newly_placed_sentences += markUpWord(split_placed_sentences[i], 2)
        else:
            newly_placed_sentences += split_placed_sentences[i]

    newly_placed_sentences = re.sub('\n', '<br>', newly_placed_sentences)
    newly_placed_sentences = re.sub(' +', fill_double_spaces_with_special_characters, newly_placed_sentences)

    return newly_placed_sentences

def mark_up_placed_text_2(origin_sentences, placed_sentences):
    changes_marks = []
    split_origin_sentences = origin_sentences.split(" ")
    split_placed_sentences = placed_sentences.split(" ")
    
    assert len(split_origin_sentences) == len(split_placed_sentences)

    for i in range(0, len(split_origin_sentences)):
        #if i != 0:
            #newly_placed_sentences += " "
        if (not split_origin_sentences[i].endswith(",") and split_placed_sentences[i].endswith(",")) or (not split_origin_sentences[i].endswith(",\"") and split_placed_sentences[i].endswith(",\"")) or (not split_origin_sentences[i].endswith(",”") and split_placed_sentences[i].endswith(",”")) or (not split_origin_sentences[i].endswith(",«") and split_placed_sentences[i].endswith(",«")):
            #newly_placed_sentences += markUpWord(split_origin_sentences[i] + ',', 1)
            changes_marks.append(1)
            changes_marks.append(1)
        elif (split_origin_sentences[i].endswith(",") and not split_placed_sentences[i].endswith(",")) or (split_origin_sentences[i].endswith(",\"") and not split_placed_sentences[i].endswith(",\"")) or (split_origin_sentences[i].endswith(",”") and not split_placed_sentences[i].endswith(",”")) or (split_origin_sentences[i].endswith(",«") and not split_placed_sentences[i].endswith(",«")):
            #newly_placed_sentences += markUpWord(split_origin_sentences[i][:-1], 2)
            changes_marks.append(2)
        else:
            #newly_placed_sentences += split_origin_sentences[i]
            changes_marks.append(0)
            
            for znak in split_origin_sentences[i]:
                if znak in string.punctuation:
                    changes_marks.append(0)

            
    #newly_placed_sentences = re.sub('\n', '<br>', newly_placed_sentences)
    #newly_placed_sentences = re.sub(' +', fill_double_spaces_with_special_characters, newly_placed_sentences)

    return changes_marks

def classify_sentences_based_on_dots_2(group_of_sentences): 
    group_of_sentences = re.sub('\n', '\r', group_of_sentences)
    
    split_sentences = group_of_sentences.split(".")
    
    cur_num_of_dropped_dots = 0
    
    final_sentences = ""
    
    for i in range(len(split_sentences)):
        if cur_num_of_dropped_dots == 0:
            if i <= len(split_sentences) - 3:
                origin_group_of_sentences = (split_sentences[i] + split_sentences[i + 1] + split_sentences[i + 2]).split(" ")
                tr_group_of_sentences = split_sentences[i] + ' <mask> ' + split_sentences[i + 1] + ' <mask> ' + split_sentences[i + 2] + ' <mask> '
            elif i == len(split_sentences) - 2:
                final_sentences += split_sentences[i] + '. ' + split_sentences[i + 1]
                break
            else:
                print("split_Sentences are: ", split_sentences)
                final_sentences += split_sentences[i]
                break
            
            tr_group_of_sentences = re.sub(" *<mask> *", " <mask> ", tr_group_of_sentences)

            tr_group_of_sentences = re.sub('[öó]', 'o', tr_group_of_sentences)
            tr_group_of_sentences = re.sub('[áä]', 'a', tr_group_of_sentences)
            tr_group_of_sentences = re.sub('ë', 'e', tr_group_of_sentences)
            tr_group_of_sentences = re.sub('í', 'i', tr_group_of_sentences)
            tr_group_of_sentences = re.sub('ü', 'u', tr_group_of_sentences)
            tr_group_of_sentences = re.sub('ć', 'c', tr_group_of_sentences)
            
            tr_group_of_sentences = "<s> " + tr_group_of_sentences + " </s>"
            
            print("tr_group_of_sentences: ", tr_group_of_sentences)
            
            input_ids = []
            attention_masks = []
            # For every sentence...
            encoded_dict = tokelineer.encode_plus(
                                tr_group_of_sentences,
                                add_special_tokens = False,
                                max_length = 200,
                                #pad_to_max_length = True,
                                padding='max_length',
                                truncation = True,
                                return_attention_mask = True,
                                return_tensors = 'pt',
                            )


            input_ids.append(encoded_dict['input_ids'])

            attention_masks.append(encoded_dict['attention_mask'])
            
            input_ids = torch.cat(input_ids, dim=0)
            attention_masks = torch.cat(attention_masks, dim=0)

            outputs = model_dots(input_ids, attention_mask=attention_masks)
            
            logits = outputs[0]

            input_ids = input_ids[0].numpy()

            mask_index = 0

            origin_counter_sentence = 0

            predicted_sentence = ""
            
            for token in tr_group_of_sentences.split(" "):
                if token != "<s>" and token != "</s>":
                    if token == "<mask>":
                        while input_ids[mask_index] != mask_token_id:
                            mask_index = mask_index + 1
                        if torch.argmax(logits[0, mask_index]).item() == 1:
                            predicted_sentence += ".\n"
                            break
                        else:
                            predicted_sentence += "."
                            cur_num_of_dropped_dots += 1
                        mask_index += 1
                    else:
                        if len(predicted_sentence) > 0:
                            predicted_sentence += " "
                        if origin_counter_sentence < len(origin_group_of_sentences):
                            predicted_sentence += origin_group_of_sentences[origin_counter_sentence]
                            origin_counter_sentence += 1
                        else:
                            break
                        
            final_sentences += predicted_sentence
            
        else:
            cur_num_of_dropped_dots -= 1
    return final_sentences
        
    

def classify_sentences_based_on_dots(sentences):
    global mask_token_id

    final_sentences = ""

    for group_of_sentences in sentences.split('\n'):

        if final_sentences != "":
            final_sentences += '\r'

        split_sentences = group_of_sentences.split(".")

        cur_num_of_dropped_dots = 0

        for i in range(len(split_sentences)):
            if cur_num_of_dropped_dots == 0:
                if i <= len(split_sentences) - 3:
                    origin_group_of_sentences = (split_sentences[i] + split_sentences[i + 1] + split_sentences[i + 2]).split(" ")
                    tr_group_of_sentences = split_sentences[i] + ' <mask> ' + split_sentences[i + 1] + ' <mask> ' + split_sentences[i + 2] + ' <mask> '
                elif i == len(split_sentences) - 2:
                    final_sentences += split_sentences[i] + '. ' + split_sentences[i + 1]
                    break
                else:
                    final_sentences += split_sentences[i]
                    break

                tr_group_of_sentences = re.sub(" *<mask> *", " <mask> ", tr_group_of_sentences)

                tr_group_of_sentences = re.sub('[öó]', 'o', tr_group_of_sentences)
                tr_group_of_sentences = re.sub('[áä]', 'a', tr_group_of_sentences)
                tr_group_of_sentences = re.sub('ë', 'e', tr_group_of_sentences)
                tr_group_of_sentences = re.sub('í', 'i', tr_group_of_sentences)
                tr_group_of_sentences = re.sub('ü', 'u', tr_group_of_sentences)
                tr_group_of_sentences = re.sub('ć', 'c', tr_group_of_sentences)

                tr_group_of_sentences = "<s> " + tr_group_of_sentences + " </s>"

                input_ids = []
                attention_masks = []
                # For every sentence...
                encoded_dict = tokelineer.encode_plus(
                                    tr_group_of_sentences,
                                    add_special_tokens = False,
                                    max_length = 200,
                                    #pad_to_max_length = True,
                                    padding='max_length',
                                    truncation = True,
                                    return_attention_mask = True,
                                    return_tensors = 'pt',
                                )


                input_ids.append(encoded_dict['input_ids'])

                attention_masks.append(encoded_dict['attention_mask'])


                input_ids = torch.cat(input_ids, dim=0)
                attention_masks = torch.cat(attention_masks, dim=0)

                outputs = model_dots(input_ids, attention_mask=attention_masks)

                logits = outputs[0]

                input_ids = input_ids[0].numpy()

                mask_index = 0

                origin_counter_sentence = 0

                predicted_sentence = ""

                for token in tr_group_of_sentences.split(" "):
                    if token != "<s>" and token != "</s>":
                        if token == "<mask>":
                            while input_ids[mask_index] != mask_token_id:
                                mask_index = mask_index + 1
                            if torch.argmax(logits[0, mask_index]).item() == 1:
                                predicted_sentence += ".\n"
                                break
                            else:
                                predicted_sentence += "."
                                cur_num_of_dropped_dots += 1
                            mask_index += 1
                        else:
                            if len(predicted_sentence) > 0:
                                predicted_sentence += " "
                            if origin_counter_sentence < len(origin_group_of_sentences):
                                predicted_sentence += origin_group_of_sentences[origin_counter_sentence]
                                origin_counter_sentence += 1
                            else:
                                break

                final_sentences += predicted_sentence
            
            else:
                cur_num_of_dropped_dots -= 1

    return final_sentences

saved_first_part_of_text = ""
def save_first_dots(line):
    global saved_first_part_of_text

    saved_first_part_of_text = line.group(0)
    return ""

saved_last_part_of_text = ""
def save_last_dots(line):
    global saved_last_part_of_text

    if len(line.group(0)) > 1:
        saved_last_part_of_text = line.group(0)[1:]
    return "."

def insert_spaces_before_quote(line):
    global final_punct, saved_spaces_before_quotes, counter_saved_spaces
    counter_saved_spaces += 1

    if not line.group(0)[0] in final_punct and line.group(0)[0] != " ":
        saved_spaces_before_quotes[counter_saved_spaces] = True
        return line.group(0)[0] + " " + line.group(0)[-1]
    saved_spaces_before_quotes[counter_saved_spaces] = False
    return line.group(0)

def remove_spaces_before_quote(line):
    global saved_spaces_before_quotes, counter_saved_spaces
    counter_saved_spaces += 1

    if saved_spaces_before_quotes[counter_saved_spaces]:
        return line.group(0)[-1]
    return line.group(0)

def save_double_single_spaces(line):
    global saved_double_spaces, double_spaces_counter

    double_spaces_counter += 1
    saved_double_spaces[double_spaces_counter] = line.group(0)
    return " "

def return_double_single_spaces(_):
    global saved_double_spaces, double_spaces_counter
    
    double_spaces_counter += 1
    return saved_double_spaces[double_spaces_counter]

def save_double_single_dots(line):
    global saved_double_dots, double_dots_counter

    double_dots_counter += 1
    saved_double_dots[double_dots_counter] = line.group(0)
    return ". "

def return_double_single_dots(_):
    global saved_double_dots, double_dots_counter
    
    double_dots_counter += 1
    return saved_double_dots[double_dots_counter]


numbers_dict = {}
def save_numbers_to_preserve_numbers_with_commas(tmp_token, token, i):
    global numbers_dict

    if tmp_token[0] in "(" and tmp_token[-2] in ")":
        if tmp_token[1:-2].isnumeric() and token != tmp_token:
            numbers_dict[tmp_token + str(i)] = token
            return tmp_token
        else:
            return token
    elif tmp_token[0] in "(" and tmp_token[-1] in ")":
        if tmp_token[1:-1].isnumeric() and token != tmp_token:
            numbers_dict[tmp_token + str(i)] = token
            return tmp_token
        else:
            return token
    elif tmp_token[0] in "(":
        if tmp_token[1:].isnumeric() and token != tmp_token:
            numbers_dict[tmp_token + str(i)] = token
            return tmp_token
        else:
            return token
    elif tmp_token[-1] in ")" or tmp_token[-1] in final_punct:
        if tmp_token[:-1].isnumeric() and token != tmp_token:
            numbers_dict[tmp_token + str(i)] = token
            return tmp_token
        else:
            return token
    else:
        if tmp_token.isnumeric() and token != tmp_token:
            numbers_dict[tmp_token + str(i)] = token
            return tmp_token
        else:
            return token

def insert_commas(sentences, apiLevel=False):
    global saved_first_part_of_text, saved_last_part_of_text, numbers_dict, mask_token_id, counter_saved_spaces, saved_spaces_before_quotes, double_spaces_counter, saved_double_spaces, double_dots_counter, saved_double_dots

    saved_first_part_of_text = ""
    saved_last_part_of_text = ""
    saved_spaces_before_quotes = {}
    double_spaces_counter = 0
    saved_double_spaces = {}
    double_dots_counter = 0
    saved_double_dots = {}

    sentences = re.sub('\n *', '\n', sentences)
    #each tab is converted into a sequence of spaces
    sentences = re.sub('\t', '        ', sentences)

    sentences = re.sub("^(\.* *)* *", save_first_dots, sentences)
    sentences = re.sub("(\. *)+ *$", save_last_dots, sentences)
    sentences = re.sub(' +', save_double_single_spaces, sentences)
    sentences = re.sub('(\.+ *)+', save_double_single_dots, sentences)

    sentences = re.sub(',+', ',', sentences)
    sentences = re.sub('\r', '', sentences)
    sentences = re.sub(' *\.', '.', sentences)

    sentences = re.sub('.["\'»«”“`]', insert_spaces_before_quote, sentences)

    new_sentences = ""
    counter_saved_spaces = -1

    for i, token in enumerate(sentences.split(' ')):
        if new_sentences != "":
            new_sentences += " "

        if len(token) > 1:

            add_comma = False
            if token[-1] == ",":
                token = token[:-1]
                add_comma = True

            tmp_token = re.sub(',', '', token)

            new_sentences += save_numbers_to_preserve_numbers_with_commas(tmp_token, token, i)

            if add_comma:
                new_sentences += ","
        else:
            new_sentences += token

    sentences = re.sub(', *', ', ', new_sentences)

    origin_sentences = sentences
    
    print("printing sentences before")
    
    print(sentences)
    
    sentences = classify_sentences_based_on_dots_2(sentences)
    
    #sentences = classify_sentences_based_on_dots(sentences)
    
    print("printing sentences 2 after")
    
    #print(sentences2)

    #so i can include dots in numbers, that are written together
    sentences = re.sub('\0', '.', sentences)
    origin_sentences = re.sub('\0', '.', origin_sentences)

    predicted_sentences = ""

    for line in sentences.split("\n"):

        line = re.sub(',', '', line)
        
        line_for_origin = re.sub('\S\r', ' \r', line)

        originalen_line = line_for_origin.split(" ")

        line = re.sub('[öó]', 'o', line)
        line = re.sub('[áä]', 'a', line)
        line = re.sub('ë', 'e', line)
        line = re.sub('í', 'i', line)
        line = re.sub('ü', 'u', line)
        line = re.sub('ć', 'c', line)

        line = re.sub('[\'»«”“`]', '"', line)

        line = "<s> " + line + " </s>"
        
        #print("line is: ", re.sub('\r', '\n', line))

        maskedline = ""
        mimozacetka = False
        for token in line.split(" "):
            if token != "<s>" and token != "</s>" and token != "." and token != "?" and token != "!" and mimozacetka:
                maskedline += " <mask> "
            elif token != "<s>" and token != "</s>":
                mimozacetka = True
            if token == "</s>" or token == ".":
                maskedline += " "
            maskedline += token
            if token == "<s>":
                maskedline += " "

        input_ids = []
        attention_masks = []
        
        maskedline = re.sub('\S\r', ' <mask> \r', maskedline)
        
        #print("masked line is: ", re.sub('\r', '\n', maskedline))
        
        # For every sentence...
        encoded_dict = tokelineer.encode_plus(
                            maskedline,
                            add_special_tokens = False,
                            max_length = 256,
                            #pad_to_max_length = True,
                            padding='max_length',
                            truncation = True,
                            return_attention_mask = True,
                            return_tensors = 'pt',
                        )


        input_ids.append(encoded_dict['input_ids'].to(device))

        attention_masks.append(encoded_dict['attention_mask'].to(device))


        input_ids = torch.cat(input_ids, dim=0)
        attention_masks = torch.cat(attention_masks, dim=0)

        outputs = model(input_ids, attention_mask=attention_masks)

        logits = outputs[0]

        input_ids = input_ids.cpu()

        input_ids = input_ids[0].numpy()

        predicted_sentence = ""
        mask_index = 0

        origin_counter_sentence = 0

        for token in maskedline.split(" "):
            
            #print("\nprinting for token: ", re.sub('\r', '\n', token))
            #print("\npredicted sentence is: ", re.sub('\r', '\n', predicted_sentence))
            
            if mask_index >= len(input_ids):
                for i in range(origin_counter_sentence, len(originalen_line)):
                    predicted_sentence += " " + originalen_line[i]
                break
            if token != "<s>" and token != "</s>":
                if token == "<mask>":
                    while input_ids[mask_index] != mask_token_id:
                        mask_index = mask_index + 1
                    if torch.argmax(logits[0, mask_index]).item() == 1:
                        if predicted_sentence != "" and predicted_sentence[-1] not in final_punct and predicted_sentence[-1] != ',':
                            predicted_sentence += ","
                    mask_index += 1
                else:
                    if mask_index > 0 and token != ".":
                        predicted_sentence += " "
                    predicted_sentence += originalen_line[origin_counter_sentence]
                    origin_counter_sentence += 1
        
        #print("predicted sentence is: ", re.sub('\r', '\n', predicted_sentences))
        
        if len(predicted_sentences) > 0:
            predicted_sentences += " "
        predicted_sentences += predicted_sentence
    
    predicted_sentences = re.sub(' +', ' ', predicted_sentences)
    predicted_sentences = re.sub('\.+', '.', predicted_sentences)

    new_predicted_sentences = ""

    predicted_sentences = re.sub(' *\r', '\n', predicted_sentences)
    predicted_sentences = re.sub('\n,', '\n', predicted_sentences)
    origin_sentences = re.sub(' *\n', '\n', origin_sentences)

    origin_sentences_split = origin_sentences.split(" ")

    for i, token in enumerate(predicted_sentences.split(' ')):
        if new_predicted_sentences != "":
            new_predicted_sentences += " "
        
        if len(token) > 1:

            add_comma = False
            if token[-1] == ",":
                add_comma = True
                token = token[:-1]
            elif origin_sentences_split[i][-1] == ",":
                origin_sentences_split[i] = origin_sentences_split[i][:-1]

            if token + str(i) in numbers_dict:
                new_predicted_sentences += numbers_dict[token + str(i)]
            else:
                new_predicted_sentences += origin_sentences_split[i]

            if add_comma:
                if new_predicted_sentences[-1] not in final_punct and new_predicted_sentences[-1] != ',':
                    new_predicted_sentences += ","
        
        else:
            new_predicted_sentences += token

    predicted_sentences = new_predicted_sentences

    if predicted_sentences[-1] == " " and origin_sentences[-1] != " ":
        predicted_sentences = predicted_sentences[:-1]

    origin_sentences = re.sub('.["\'»«”“`]', remove_spaces_before_quote, origin_sentences)
    counter_saved_spaces = -1

    predicted_sentences = re.sub('.["\'»«”“`]', remove_spaces_before_quote, predicted_sentences)
    counter_saved_spaces = -1

    double_dots_counter = 0
    origin_sentences = re.sub('\. *', '. ', origin_sentences)
    origin_sentences = re.sub('\. ', return_double_single_dots, origin_sentences)

    double_dots_counter = 0
    predicted_sentences = re.sub('\. *', '. ', predicted_sentences)
    predicted_sentences = re.sub('\. ', return_double_single_dots, predicted_sentences)

    double_spaces_counter = 0
    origin_sentences = re.sub(' ', return_double_single_spaces, origin_sentences)

    double_spaces_counter = 0
    predicted_sentences = re.sub(' ', return_double_single_spaces, predicted_sentences)

    origin_sentences = saved_first_part_of_text + origin_sentences + saved_last_part_of_text
    predicted_sentences = saved_first_part_of_text + predicted_sentences + saved_last_part_of_text

    if apiLevel:
        return predicted_sentences
    else:
        #return predicted_sentences #mark_up_placed_text(origin_sentences, predicted_sentences)
        return (mark_up_placed_text_2(origin_sentences, predicted_sentences), predicted_sentences)



