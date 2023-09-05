from lectorize_word_t5 import correct_word_mistakes_section

from datasets import load_dataset
from transformers import pipeline

import re

# Load the dataset
dataset = load_dataset("cjvt/solar3", "paragraph_level")

TN = 0
TP = 0
FP = 0
FN = 0

skip_num = 3500

for row in dataset['train']:

  if row['is_manually_validated'] and len(row['src_tokens']) < 40:

    if skip_num > 0:
      skip_num -= 1
      continue
    src_text = " ".join(row['src_tokens'])

    plus_TN = len(row['src_tokens'])

    src_text = re.sub('[!@#$:;\'\"“”„•«»%&ø×¹]', '', src_text)
    src_text = re.sub('[öó]', 'o', src_text)
    src_text = re.sub('[áä]', 'a', src_text)
    #src_text = re.sub('[0123456789]', '1', src_text)
    src_text = re.sub('ë', 'e', src_text)
    src_text = re.sub('í', 'i', src_text)
    src_text = re.sub('ü', 'u', src_text)
    src_text = re.sub('ć', 'c', src_text)

    #orig_masked_text, masked_text = postavi_masks_v_text(src_text)
    
    #print("src_text: ", src_text)

    predictions, masked_text, izhod_text = correct_word_mistakes_section(src_text, False, True, True, [], True)
    
    if type(masked_text) == int or type(masked_text) == float or len(masked_text) < 2:
        continue
    
    #print("predictions: ", predictions)
            

    corrections_tgt_words = []

    corrections = []

    for correction in row['corrections']:
      if correction['corr_types'][0].startswith('Č'):
        #print("src_word: ", row['src_tokens'][correction['idx_src'][0]])
        #print("tgt_word: ", row['tgt_tokens'][correction['idx_tgt'][0]])
        if len(row['src_tokens'][correction['idx_src'][0]]) > 1:

          corrections.append(correction)

          corrections_tgt_words.append(row['tgt_tokens'][correction['idx_tgt'][0]])

    #print("src_text: ", src_text)
    #break
    
    orig_predictions = predictions.copy()

    for correction_tgt_word in corrections_tgt_words:
      new_word = correction_tgt_word

      new_word = new_word.replace('ž', 'z')
      new_word = new_word.replace('š', 's')
      new_word = new_word.replace('č', 'c')

      if new_word in predictions:
        TP += 1
        plus_TN -= 1

        predictions.remove(new_word)
      
      elif new_word.lower() in predictions:
        TP += 1
        plus_TN -= 1

        predictions.remove(new_word.lower())

      else:
        FN += 1

    FP += len(predictions)
    plus_TN -= len(predictions)

    TN += plus_TN

    if len(predictions) > 0 or len(corrections_tgt_words) > 0:
      print("---------------------------------------------")
      print("stavek: ", src_text)
      print("masked stavek: ", masked_text)
      print("izhodni stavek: ", izhod_text)
      print("predictions: ", orig_predictions)
      print("corrections_tgt_words: ", corrections_tgt_words)
      print("corrections: ", corrections)
      print("TP: ", TP, "FP: ", FP, "FN: ", FN, "TN: ", TN)