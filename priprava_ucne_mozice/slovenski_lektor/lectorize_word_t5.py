import string
from happytransformer import HappyTextToText
from happytransformer import TTSettings

from transformers import BertTokenizer, BertForMaskedLM
import torch

import support_functions
import pickle

from classla import Pipeline

# Initialize the pipeline
nlp = Pipeline('sl')

from transformers import T5ForConditionalGeneration, T5Tokenizer

# Load the pretrained T5 model and tokenizer
model_name = "t5-base"
model = T5ForConditionalGeneration.from_pretrained("./general_model_aug_9/")
tokenizer = T5Tokenizer.from_pretrained("./general_model_aug_9/")


#load T5 model
#happy_tt = HappyTextToText("T5", "t5-sl-small", load_path="./predict_masks_model")

# Load the pretrained T5 masks model and tokenizer
model_name = "t5-base-masks"
masks_model = T5ForConditionalGeneration.from_pretrained("./maksed_model_aug_7/")
masks_tokenizer = T5Tokenizer.from_pretrained("./maksed_model_aug_7/")

model_name = "t5-base-sklanjanje"
sklanjanje_model = T5ForConditionalGeneration.from_pretrained("./sklanjanje_aug_2/")
sklanjanje_tokenizer = T5Tokenizer.from_pretrained("./sklanjanje_aug_2/")

model_name = "t5-base-vrstni-red"
wo_model = T5ForConditionalGeneration.from_pretrained("./word_order_aug_2/")
wo_tokenizer = T5Tokenizer.from_pretrained("./word_order_aug_2/")


beam_settings =  TTSettings(num_beams=5, min_length=1, max_length=400)
print_debug = False

sloleks_root_dict = {}
root_lemma_dict = {}

special_character_map = []

#all_words = {}

with open('./root_lemma_dict.pkl', 'rb') as f:
    root_lemma_dict = pickle.load(f)

with open('./sloleks_root_dict.pkl', 'rb') as f:
    sloleks_root_dict = pickle.load(f)
    
#happy_tt_word_shape = HappyTextToText("T5", "t5-sl-small", load_path="./sklanjanje_aug_2/")
    
new_sloleks_root_dict = {}
predictionNum = 0

for key in list(sloleks_root_dict.keys()):
    new_sloleks_root_dict[key] = key
    
    new_key = key.replace('š', 's')
    new_key = key.replace('č', 'c')
    new_key = key.replace('ž', 'z')
    if new_key != key:
        new_sloleks_root_dict[new_key] = new_sloleks_root_dict.pop(key)
        
def namedEntityIndexes(text_input):
    text = text_input
    doc = nlp(text)
    conll_output = doc.to_conll()
    
    lines = conll_output.strip().split('\n')
    word_data = [line.split('\t') for line in lines]
    
    namedEntityIndexes = []

    # Loop through each word and check NER tag
    for idx, word_info in enumerate(word_data):
        if len(word_info) >= 9:
            word = word_info[1]
            ner_tag = word_info[9]

            if ner_tag.startswith('NER=B-PER') or ner_tag.startswith('NER=I-PER'):
                #print(f"'{word}' is a named entity.")
                namedEntityIndexes.append(idx - 3)
            #else:
                #print(f"'{word}' is not a named entity.")
                
    return namedEntityIndexes

def addOptions(optionsList, predictionWord, optionNum):
    if len(optionsList) == 0:
        return predictionWord
    
    endString = '<div id="selectContainer&' + str(optionNum) +'" class="select-container">'
    endString += '<div class="optionText" id="text&' + str(optionNum) + '" contenteditable="true">' + predictionWord + '</div>'
    endString += '<div id="select-options&' + str(optionNum) + '" class="select-options">'
    
    for optionidx, optionWord in enumerate(optionsList):
        if optionidx == 0:
            endString += '<div class="select-option"><s>' + optionWord + '</s></div>'
        else:
            endString += '<div class="select-option">' + optionWord + '</div>'
        
    endString += '</div>'
    endString += '</div>'
    
    return endString

def correct_word_mistakes(input_text, markUp=False, sklanjaj=False, wo=False, names=False):
    #print("input_text: ", input_text)
    
    input_text = input_text.replace('\r\r', '\n')
    
    input_text = input_text.replace('\r', '')
    
    sections = input_text.split("\n")
    
    #print("sections: ", sections)
    
    new_text = ""
    
    for section in sections:
        new_section, napaka = correct_word_mistakes_big_sections(section, markUp, sklanjaj, wo, names)
        
        if napaka != 0:
            return (new_text, napaka)
        
        if new_text != "":
            new_text += "</br>"
            
        new_text += new_section
    
    if markUp:    
        return ("<div>" + new_text + "</div>", 0)
    else:
        return (new_text, 0)

def correct_word_mistakes_big_sections(cur_section, markUp=False, sklanjaj=False, wo=False, names=True):
    final_text = ""
    
    while (len(cur_section) > 0):
        
        #dot_pos = support_functions.pos_last_dotin_text(cur_section[:400], 400)
        dot_pos = len(cur_section) -1
        
        if markUp:
            dot_pos = support_functions.pos_last_dotin_text(cur_section, 250)
        
        #print("cur_section:", cur_section)
        #print("dot_pos: ", dot_pos)
        #dot_pos = support_functions.pos_second_dotin_text(cur_section, 200)
        
        start_with = 0
        while cur_section[start_with] == ' ':
            start_with += 1
            
        new_section = cur_section[start_with:dot_pos + 1]
            
        addedDot = False
        
        if len(new_section) > 0 and new_section[-1] != '.' and new_section[-2] != '.':
            new_section += '. '
            addedDot = True
        
        if wo:
            new_section = popraviVrstniRed(new_section)
            napaka = 0
        else:
            new_section, napaka = correct_word_mistakes_section(new_section, markUp, sklanjaj, names)
        
        if addedDot:
            addedDot = False
            while new_section[-1] != '.':
                new_section = new_section[:-1]
            new_section = new_section[:-1]
            
        while start_with > 0:
            new_section = ' ' + new_section
            start_with -= 1
        
        if napaka != 0:
            return (new_section, napaka)
        
        #if len(final_text) > 0 and final_text[-1] != ' ':
        #    final_text += ' '
        
        final_text += new_section
        
        if dot_pos < len(cur_section) and len(cur_section) > 3:
            cur_section = cur_section[dot_pos + 1:]
        else:
            break
        
    return (final_text, 0)    
    

def correct_word_mistakes_section(input_text, markUp=False, sklanjaj=False, names=True):
    global predictionNum
    
    predictions_all = {}
    local_prediction_num = 0
    splits = []
    
    orig_input_text = input_text
    
    #input_text = input_text.replace('\r', '\n')
    
    #input_text = support_functions.add_dot_to_sentence(input_text)
    
    #added_dot = False
    
    #print("ZACETEK")
    #print("input_text: ", input_text)
    
    changed_positions = []
    
    input_text = support_functions.replace_multiple_occurrences_of_punctuation(input_text)
    input_text = support_functions.add_spaces_before_and_after_punctuation(input_text)
    input_text = support_functions.remove_double_spaces(input_text)
    
    #new_line_indexes = support_functions.find_indexes_of_character(input_text, '\n')
    
    #print("new_line_indexes: ", new_line_indexes)
    
    #input_text = input_text.replace('\n', '')
    
    if len(input_text) < 3:
        return (orig_input_text, 0)
    
    input_text = support_functions.remove_double_spaces(input_text)
    
    #print("input_text: ", input_text)

    othrPredictions = []
    
    has_masks = True
    repeats_counter = 0
    
    while has_masks:
        has_masks = False
        repeats_counter += 1

        #result = happy_tt.generate_text(input_text.lower(), args=beam_settings)
        
        # Tokenize the input text
        input_ids = masks_tokenizer.encode(input_text, return_tensors="pt")

        # Generate the text using beam search
        masks_beam_outputs = masks_model.generate(
            input_ids,
            num_beams=10,
            num_return_sequences=1,
            max_length=400,
            early_stopping=True
        )
        
        masked_result_split_orig = []
        
        for i, masks_beam_output in enumerate(masks_beam_outputs):
        
            resultText = tokenizer.decode(masks_beam_output, skip_special_tokens=True)
            
            resultText = support_functions.add_spaces_before_and_after_punctuation(resultText)
            resultText = support_functions.remove_double_spaces(resultText)

            masked_result_split = resultText.split(' ')
            
            if masked_result_split_orig == []:
                masked_result_split_orig = masked_result_split
            else:
                for idx_mask_word, mask_word in enumerate(masked_result_split):
                    if mask_word == '<mask>':
                        masked_result_split_orig[idx_mask_word] = '<mask>'
                    
            input_split = input_text.split(' ')
            
            masked_result_split = masked_result_split_orig
            
            if print_debug:
                print("masked_result_split: ", masked_result_split)
                print("input_split: ", input_split)

            if len(masked_result_split) != len(input_split):
                #print("masked_result_split: ", masked_result_split)
                #print("input_split: ", input_split)
                print("NAPAK 1")
                return (orig_input_text, 2)

        result_split = []

        new_predicted_text = ""
        
        input_text = " ".join(input_split)
                
        # Tokenize the input text
        input_ids = tokenizer.encode(input_text, return_tensors="pt")

        # Generate the text using beam search
        beam_outputs = model.generate(
            input_ids,
            num_beams=15,
            num_return_sequences=4,
            max_length=400,
            early_stopping=True
        )
        
        indexCountRepair = 0
        prevSplit = False
        spremenilRepairCounterPos = False
        
        #print("masked_result_split: ", masked_result_split)
        
        idxesToExclude = []
        
        if not names:
            idxesToExclude = namedEntityIndexes(input_text)
            #print("idxesToExclude: ", idxesToExclude)
        
        for idx, (predicted_word, word) in enumerate(zip(masked_result_split, input_split)):
            
            #print("predicted_word: ", predicted_word)
            #if (len(word) > 1 and (predicted_word == '<mask>' or  word.lower() not in sloleks_root_dict)): # or (len(predicted_word) > 1 and predicted_word not in root_lemma_dict):
            #if len(predicted_word) > 1 and word.lower() not in sloleks_root_dict:
            #if (predicted_word == '<splited_mask>' or predicted_word == '<concated_word>' or predicted_word == '<mask>' or word.lower() not in sloleks_root_dict or word.lower() not in root_lemma_dict) and (len(word) > 1 or word.isalpha()) and not word.isnumeric():
            if (predicted_word == '<mask>') and (len(word) > 1 or word.isalpha()) and not idx in idxesToExclude:
            #if (predicted_word == '<splited_mask>' or predicted_word == '<concated_word>' or predicted_word == '<mask>') and (len(word) > 1 or word.isalpha()):
                has_masks = True
                shouldBreak = False
                othrPredictions = [word]
                
                if prevSplit:
                    prevSplit = False
                    continue
                
                count1Lavenstein = 0
                count2Lavenstein = 0
                count3Lavenstein = 0
                countOverallLavenstein = 0
                
                prediction_1 = {
                    'word': '',
                    'position': -1
                }
                prediction_2 = {
                    'word': '',
                    'position': -1
                }
                prediction_3 = {
                    'word': '',
                    'position': -1
                }
                prediction = ""
                
                #print("trying prediction")
                
                generatedTextIdx = idx + indexCountRepair
                spremenilRepairCounterPos = False

                # Decode and print the generated text
                for i, beam_output in enumerate(beam_outputs):
                    
                    generated_text = tokenizer.decode(beam_output, skip_special_tokens=True)
                    
                    generated_text = support_functions.replace_multiple_occurrences_of_punctuation(generated_text)
                    generated_text = support_functions.add_spaces_before_and_after_punctuation(generated_text)
                    generated_text = support_functions.remove_double_spaces(generated_text)
                    #print(f"Beam {i+1}: {generated_text}")
                    
                    generated_text_split = generated_text.split(' ')
                    
                    if idx >= len(generated_text_split):
                        print("index too long, generated_text: ", generated_text_split, " idx: ", idx)
                        break
                    
                    # if predicted_word == '<concated_word>' and idx < len(generated_text_split) - 1:
                    #     predicted_word = generated_text_split[generatedTextIdx] + ' ' + generated_text_split[generatedTextIdx + 1]
                    # elif predicted_word == '<splited_mask>':
                    #     word = input_split[idx] + ' ' + input_split[idx + 1]
                    #     predicted_word = generated_text_split[generatedTextIdx]
                    #     prevSplit = True
                    # else:    
                    predicted_word = generated_text_split[support_functions.get_most_probable_position(generated_text_split, input_split, masked_result_split, generatedTextIdx)]
                        
                    
                    #Check ce zapisati skupaj
                    if idx < len(masked_result_split) - 1 and masked_result_split[idx] == '<mask>' and masked_result_split[idx + 1] == '<mask>' and generated_text_split[generatedTextIdx] == input_split[idx] + input_split[idx + 1]:
                        word = input_split[idx] + ' ' + input_split[idx + 1]
                        predicted_word = generated_text_split[generatedTextIdx]
                        if not spremenilRepairCounterPos:
                            indexCountRepair -= 1
                            spremenilRepairCounterPos = True
                        prevSplit = True
                    
                    if (len(predicted_word.split(' ')) > 0 and predicted_word[0] in sloleks_root_dict) or ((predicted_word in sloleks_root_dict or predicted_word.lower() in sloleks_root_dict) and (predicted_word in root_lemma_dict or predicted_word.lower() in root_lemma_dict)):
                        
                        calculated_lavenshtein_distance = support_functions.levenshtein_distance(word, predicted_word)
                        
                        if not shouldBreak:
                            if calculated_lavenshtein_distance <= 1:
                                # if masked_result_split[idx] == '<concated_word>' and not spremenilRepairCounterPos:
                                #     indexCountRepair += 1
                                #     spremenilRepairCounterPos = True
                                # elif masked_result_split[idx] == '<splited_mask>' and not spremenilRepairCounterPos:
                                #     indexCountRepair -= 1
                                #     spremenilRepairCounterPos = True
                                #print(word + " -> " + predicted_word)
                                
                                prediction_1['word'] = predicted_word
                                
                                if word != predicted_word:
                                    #changed_positions.append(idx);
                                    prediction_1['position'] = generatedTextIdx
                                
                                    shouldBreak = True;
                                    
                                if prevSplit:
                                    splits.append({ 'predicted_word': predicted_word, 'word': word })
                            
                            if i < 1 and calculated_lavenshtein_distance == 2 and prediction_2['position'] == -1:
                                prediction_2['word'] = predicted_word
                                
                                prediction_2['position'] = generatedTextIdx
                                    
                            if i < 1 and calculated_lavenshtein_distance == 3 and prediction_3['position'] == -1:
                                prediction_3['word'] = predicted_word
                                
                                prediction_3['position'] = generatedTextIdx
                            
                        
                        if markUp:
                            
                            if count1Lavenstein < 3 and calculated_lavenshtein_distance == 1:
                            
                                if word != predicted_word and predicted_word not in othrPredictions:
                                    count1Lavenstein += 1
                                    
                                    othrPredictions.append(predicted_word)
                            
                            elif count2Lavenstein < 2 and calculated_lavenshtein_distance == 2:
                                
                                if word != predicted_word and predicted_word not in othrPredictions:
                                    count2Lavenstein += 1
                                    
                                    othrPredictions.append(predicted_word)
                                    
                            elif count3Lavenstein < 2 and calculated_lavenshtein_distance == 3:
                                
                                if word != predicted_word and predicted_word not in othrPredictions:
                                    count3Lavenstein += 1
                                    
                                    othrPredictions.append(predicted_word)
                                
                            elif countOverallLavenstein < 2:
                                
                                if word != predicted_word and predicted_word not in othrPredictions:
                                    countOverallLavenstein += 1
                                    
                                    othrPredictions.append(predicted_word)
                                
                            
                            
                            
                if prediction_1['position'] != -1:
                    prediction = prediction_1['word']
                    changed_positions.append(prediction_1['position']);
                    
                    print("1: " + word + " -> " + prediction)
                    
                elif prediction_2['position'] != -1:
                    prediction = prediction_2['word']
                    changed_positions.append(prediction_2['position']);
                    
                    print("2: " + word + " -> " + prediction)
                    
                elif prediction_3['position'] != -1:
                    prediction = prediction_3['word']
                    changed_positions.append(prediction_3['position']);
                    
                    print("3: " + word + " -> " + prediction)
                    
                else:
                    print("0: " + word + " -> " + prediction)
                    
                    prediction = word
                    
                if markUp:
                    # if prediction != word:
                    #     prediction = "<mark class='markVejicaPrejJaZdejNe'>" + addOptions(othrPredictions, prediction, predictionNum) + "</mark>"
                    # else:
                    #     prediction = "<mark class='markVejicaPrejNeZdejJa'>" + addOptions(othrPredictions, prediction, predictionNum) + "</mark>"
                    
                    # predictionNum += 1
                    
                    predictions_all[idx] = { 'othrPredictions': othrPredictions, 'prediction': prediction, 'predictionNum': predictionNum }
                    
                    predictionNum += 1
                    local_prediction_num += 1
                        

                if prediction == "":
                    assert 2 == 0
                else:
                    result_split.append(prediction)
            
            elif (predicted_word == '<splited_mask>' or predicted_word == '<concated_word>') and (len(word) > 1 or word.isalpha()):
                predictions_all[idx] = { 'othrPredictions': [], 'prediction': word, 'predictionNum': predictionNum }
                    
                predictionNum += 1
                local_prediction_num += 1
                
                result_split.append(word)
                  
            else:
                result_split.append(word)
        
                    
        input_text = " ".join(result_split)
        
        #print("resultText: ", input_text)
        
        if repeats_counter >= 1 and has_masks:
            #input_text = lectorize_word.correct_word_mistakes(input_text)
            
            has_masks = False

    #SKLANJATVE-START
    local_prediction_num = 0

    result_text_split = []
    
    #print("input_ids: ", input_ids)

    # Generate the text using beam search
    if sklanjaj:
        input_ids = sklanjanje_tokenizer.encode(input_text, return_tensors="pt")
        
        sklanjanje_beam_output = sklanjanje_model.generate(
            input_ids,
            num_beams=10,
            num_return_sequences=1,
            max_length=400,
            early_stopping=True
        )
        
        input_text = tokenizer.decode(sklanjanje_beam_output[0], skip_special_tokens=True)
        
        input_text = support_functions.replace_multiple_occurrences_of_punctuation(input_text)
        input_text = support_functions.add_spaces_before_and_after_punctuation(input_text)
        input_text = support_functions.remove_double_spaces(input_text)
    
    #print("input_text: ", input_text)
    #print("input_split: ", input_split)
    if markUp:
        new_text = []
        
        for split in splits:
            orig_input_text = orig_input_text.replace(split['word'], split['predicted_word'])
        
        orig_text_split = orig_input_text.split(" ")
        orig_text_split_idx = -1
        
        #print("orig_text_split: ", orig_text_split)
            
        
        for idx, (word, orig_word) in enumerate(zip(input_text.split(' '), input_split)):
            prediction = word
            
            if idx in predictions_all:
                
                if predictions_all[idx]['prediction'] != orig_word:
                    prediction = "<mark class='markVejicaPrejJaZdejNe'>" + addOptions(predictions_all[idx]['othrPredictions'], predictions_all[idx]['prediction'], predictions_all[idx]['predictionNum']) + "</mark>"
                else:
                    prediction = "<mark class='markVejicaPrejNeZdejJa'>" + addOptions(predictions_all[idx]['othrPredictions'], predictions_all[idx]['prediction'], predictions_all[idx]['predictionNum']) + "</mark>"
                    
                #if idx < len(input_split) - 1 and predictions_all[idx]['prediction'] == (input_split[idx] + input_split[idx + 1]):
                #    print("MAMO SPLIT")
            elif word.isalpha() and word != orig_word:
                othrPredictionsIn = []
                othrPredictionsIn.append(orig_word)
                othrPredictionsIn.append(word)
                
                prediction = "<mark class='sklanjanaBeseda'>" + addOptions(othrPredictionsIn, word, predictionNum) + "</mark>"
                
                predictionNum += 1
            
            while not orig_word in orig_text_split[orig_text_split_idx]:
                
                orig_text_split_idx += 1
            
            
            if prediction != word:
                orig_text_split[orig_text_split_idx] = orig_text_split[orig_text_split_idx].replace(orig_word, prediction)
            #print("after orig_text_split[orig_text_split_idx]: ", orig_text_split[orig_text_split_idx])
        
        input_text = " ".join(orig_text_split)
    
    #print("input_text: ", input_text)
    
    
    #input_text = support_functions.reasignDotsAndCommas(orig_input_text, input_text)
    
    #input_text = support_functions.remove_spaces_before_some_characters(input_text)
    
    
    #input_text = input_text.replace('\r', '\n')
    
    #input_text = support_functions.place_character_at_indexes(input_text, '\n', new_line_indexes)
    
    return (input_text, 0)


def popraviVrstniRed(input_text):
    input_text = support_functions.convert_to_lower_case(input_text)
    
    input_ids = wo_tokenizer.encode(input_text, return_tensors="pt")
    
    input_text = support_functions.replace_multiple_occurrences_of_punctuation(input_text)
    input_text = support_functions.add_spaces_before_and_after_punctuation(input_text)
    input_text = support_functions.remove_double_spaces(input_text)
        
    wo_beam_output = wo_model.generate(
        input_ids,
        num_beams=10,
        num_return_sequences=1,
        max_length=400,
        early_stopping=True
    )
    
    input_text = wo_tokenizer.decode(wo_beam_output[0], skip_special_tokens=True)
    
    return input_text

    
if __name__=="__main__":
    print_debug = True
    #while True:
        #work_mode = input("Način delovanja (my_annotation) (auto_annotation): ")
        
        #if work_mode == "auto_annotation":
    while True:
        #input_text = "enotnost družine je vrednota, ki jo morajo verniki spodnujati s svojim živlenjskim pričevanjem, ne le z zakonsko prisilo."
        input_text = input("Vaše besedilo: ")
        
        if input_text == "exit":
            break
        
        corrected_input_text = correct_word_mistakes(input_text)
        
        print(corrected_input_text)
                

