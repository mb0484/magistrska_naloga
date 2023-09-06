import os
import csv
#import use_tagger
#import random
import make_text_incorrect_functions

general_model = False
general_model_2 = False
general_mask_model = False
general_mask_model_2 = True

convert_to_lower = False
add_spaces_before_punctuation = True

word_order = False
word_zapis = False
split_concat = False
character_level_word_zapis = False
just_mark_false_words = True

write_mask_row = False

make_target_for_bert = False

# Open the CSV file in write mode
with open("bert_data.txt", "w") as bert_file:
  with open("bert_data_masks.txt", "w") as bert_masks_file:
    with open("data.csv", "w", newline="") as csv_file:
      # Change to the directory containing the text files
      os.chdir("aug_16_ucne_mnozice")
      #os.chdir("testne_mnozice/jul_23_testne_mnozice")

      # Get a list of all the text files in the directory
      text_files = [f for f in os.listdir() if f.endswith(".txt")]
      
      print("text_files: ", text_files)
      
      file_counter = 0;
      write_row_counter = 0;
      
      # Create a CSV writer object
      writer = csv.writer(csv_file)
      
      # Write the header row
      writer.writerow(["Input", "Target"])
      
      # Open each text file and print its contents
      for file in text_files:
          file_counter += 1;
          
          #if counter > 1:
          #    break;
          # Open the text file in read mode
          with open(file, "r") as file:
            print("file is: ", file, "write_row_counter is: ", write_row_counter)
            print("working on file num: ", file_counter, " of: ", len(text_files))

            # Iterate through each line in the file
            for line in file:
              
              if len(line.split(" ")) > 3:
                  
                #if swo_structure:
                #  new_line = use_tagger.mix_word_order(new_line, 0.4)
                
                if add_spaces_before_punctuation:
                  line = make_text_incorrect_functions.add_spaces_before_and_after_punctuation(line)
                
                if just_mark_false_words:
                  
                  line = make_text_incorrect_functions.add_spaces_before_and_after_punctuation(line)
                  
                  line = make_text_incorrect_functions.preprocess_line(line)
                  
                line = make_text_incorrect_functions.replace_new_lines_and_double_Spaces(line)
                
                new_line = line
                
                if convert_to_lower:
                  new_line = make_text_incorrect_functions.convert_to_lower_case(new_line)
                  line = make_text_incorrect_functions.convert_to_lower_case(line)
                
                if False:
                  
                  #new_line = use_tagger.replace_random_linking_words_in_text(new_line, 0.1)
                  new_line = make_text_incorrect_functions.replace_random_linking_words_in_text(new_line, 0.05)

                if general_model:

                  new_line = make_text_incorrect_functions.split_random_words(new_line, 0.01)
                  
                  new_line = make_text_incorrect_functions.concat_random_words(new_line, 0.01)
                  
                  new_line = make_text_incorrect_functions.change_word_endings(new_line, 0.2)
                  
                  new_line = make_text_incorrect_functions.zamenjaj_besede_nagajivke(new_line, 0.14)
                  
                  new_line = make_text_incorrect_functions.replace_nj(new_line, 0.14)
                  
                  new_line = make_text_incorrect_functions.replace_lj(new_line, 0.14)
                  
                  #new_line = make_text_incorrect_functions.replace_v_na(new_line, 0.2)
                  
                  new_line = make_text_incorrect_functions.replace_konec_besed_v_l(new_line, 0.14)
                  
                  new_line = make_text_incorrect_functions.replace_all_ž_š_č_characters(new_line, 0.05)
                  
                  new_line = make_text_incorrect_functions.replace_random_chars_in_text(new_line, 0.35, 0.3)
                  
                if general_model_2:
                      
                  #new_line = make_text_incorrect_functions.split_random_words(new_line, 0.02)
                  
                  #new_line = make_text_incorrect_functions.concat_random_words(new_line, 0.02)
                  
                  new_line = make_text_incorrect_functions.zamenjaj_besede_nagajivke(new_line, 0.1)
                  
                  new_line = make_text_incorrect_functions.replace_some_predefined_characters(new_line, 0.7, 4)
                  
                  new_line = make_text_incorrect_functions.replace_all_ž_š_č_characters(new_line, 0.07)
                  
                  new_line = make_text_incorrect_functions.replace_random_chars_in_text_2(new_line)
                  
                if general_mask_model:
                  
                  new_line = make_text_incorrect_functions.split_random_words(new_line, 0.01)
                  
                  new_line = make_text_incorrect_functions.concat_random_words(new_line, 0.01)
                  
                  new_line = make_text_incorrect_functions.zamenjaj_besede_nagajivke(new_line, 0.1)
                  
                  new_line = make_text_incorrect_functions.replace_nj(new_line, 0.05)
                  
                  new_line = make_text_incorrect_functions.replace_lj(new_line, 0.05)
                  
                  new_line = make_text_incorrect_functions.replace_konec_besed_v_l(new_line, 0.05)
                  
                  new_line = make_text_incorrect_functions.replace_all_ž_š_č_characters(new_line, 0.05)
                  
                  new_line = make_text_incorrect_functions.replace_random_chars_in_text(new_line, 0.46, 0.35)
                  
                if general_mask_model_2:
                  
                  new_line = make_text_incorrect_functions.split_random_words(new_line, 0.04)
                  
                  new_line = make_text_incorrect_functions.concat_random_words(new_line, 0.04)
                  
                  new_line = make_text_incorrect_functions.zamenjaj_besede_nagajivke(new_line, 0.1)
                  
                  new_line = make_text_incorrect_functions.replace_some_predefined_characters(new_line, 0.6, 3)
                  
                  new_line = make_text_incorrect_functions.replace_all_ž_š_č_characters(new_line, 0.04)
                  
                  new_line = make_text_incorrect_functions.replace_random_chars_in_text_2(new_line)
                
                if word_order:
                  #new_line = make_text_incorrect_functions.change_word_endings(new_line, 0.2)    
                      
                  new_line = make_text_incorrect_functions.mix_word_order_in_sentence(new_line, 0.6)
                  
                  #new_line = make_text_incorrect_functions.mix_sentences(new_line, 0.04)
                  
                if word_zapis:
                  
                  #new_line = make_text_incorrect_functions.replace_random_chars_in_text(new_line, 0.3, 0.27)
                  
                  new_line = make_text_incorrect_functions.change_word_endings(new_line, 0.4)
                  
                if character_level_word_zapis:
                  
                  new_line = make_text_incorrect_functions.split_and_replace(new_line, not just_mark_false_words)
                  
                  new_line = make_text_incorrect_functions.replace_random_chars_by_word(new_line, 0.03)
                  
                  new_line = make_text_incorrect_functions.remove_random_chars_by_word(new_line, 0.01, not just_mark_false_words)
                  
                  new_line = make_text_incorrect_functions.insert_random_chars_by_word(new_line, 0.002)
                  
                  #new_line = make_text_incorrect_functions.duplicate_random_chars(new_line, 0.5)
                  
                  #new_line = make_text_incorrect_functions.insert_random_chars(new_line, 0.4)
                  
                  #new_line = make_text_incorrect_functions.replace_random_char(new_line, 0.9)
                
                #new_line = make_text_incorrect_functions.remove_spaces_before_punctuation(new_line)
                
                original_line = line #add_spaces_before_punctuation(line)
                incorrect_line = new_line #add_spaces_before_punctuation(new_line) "slovnica: " +
                
                if just_mark_false_words and character_level_word_zapis:
                  incorrect_line = make_text_incorrect_functions.de_split(incorrect_line)
                
                if just_mark_false_words:
                  incorrect_line, original_line = make_text_incorrect_functions.mark_false_words(incorrect_line, original_line)
                else:
                  incorrect_line = make_text_incorrect_functions.remove_concated_splited_word_indicators(incorrect_line)
              
                  
                if character_level_word_zapis and not just_mark_false_words:
                  original_line = make_text_incorrect_functions.remove_double_spaces(original_line)
                  original_line = make_text_incorrect_functions.split_and_replace(original_line)
                  
                  #incorrect_line = make_text_incorrect_functions.de_split(incorrect_line)
                  #original_line = make_text_incorrect_functions.de_split(original_line)
                
                if make_target_for_bert:
                      
                  original_line = make_text_incorrect_functions.replace_all_ž_š_č_characters(original_line)    
                  
                  bert_masked_line, bert_line = make_text_incorrect_functions.make_bert_mask_row(original_line)
                  
                  if bert_masked_line != None:
                    bert_file.write(bert_line + '\n')
                    bert_masks_file.write(bert_masked_line + '\n')

                
                original_line = make_text_incorrect_functions.make_T5_row(original_line)

                if not(incorrect_line == None or incorrect_line == ""):
                  #print("incorrect_line: ", incorrect_line)
                  write_row_counter += 1
                
                  writer.writerow([incorrect_line, original_line])
                  #print("write row")