import random
import csv
import os
import re
import string
import datetime
from random import randint, choice

data_folder = "./prepared_data/data.csv"

# Read the CSV file
with open(data_folder, 'r') as input_file:
    reader = csv.reader(input_file)
    rows = list(reader)

# Count the number of rows
num_rows = len(rows)

print(f'Number of rows: {num_rows}')

# Read the CSV file
with open(data_folder, 'r') as input_file:
    reader = csv.reader(input_file)
    rows = list(reader)

# Split the rows into two lists
n = 5  # Number of rows to write to the first file
first_rows = rows[:num_rows-2000]
second_rows = rows[num_rows-2000:num_rows]

# Write the first rows to a CSV file
with open('train.csv', 'w') as first_file:
    writer = csv.writer(first_file)
    # Write the header row
    writer.writerow(["input", "target"])
    writer.writerows(first_rows)

# Write the second rows to a CSV file
with open('eval.csv', 'w') as second_file:
    writer = csv.writer(second_file)
    # Write the header row
    writer.writerow(["input", "target"])
    writer.writerows(second_rows)
    
import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration

# Load the pre-trained T5 model and tokenizer
model_name = "./t5-sl-small/"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

import pandas as pd
from torch.utils.data import DataLoader, Dataset

class CustomDataset(Dataset):
    def __init__(self, file_path, tokenizer):
        self.data = pd.read_csv(file_path)
        self.tokenizer = tokenizer

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        input_text = self.data.iloc[idx]['input']
        target_text = self.data.iloc[idx]['target']

        input_tokens = self.tokenizer.encode_plus(input_text, padding='max_length', max_length=90, return_tensors='pt', truncation=True)
        target_tokens = self.tokenizer.encode_plus(target_text, padding='max_length', max_length=90, return_tensors='pt', truncation=True)

        return {
            'input_ids': input_tokens['input_ids'].squeeze(),
            'attention_mask': input_tokens['attention_mask'].squeeze(),
            'labels': target_tokens['input_ids'].squeeze(),
            'decoder_attention_mask': target_tokens['attention_mask'].squeeze()
        }

def collate_fn(batch):
    return {key: torch.stack([sample[key] for sample in batch]) for key in batch[0]}

# Load your training data from a CSV file
train_file_path = "train.csv"
train_dataset = CustomDataset(train_file_path, tokenizer)
train_dataloader = DataLoader(train_dataset, batch_size=85, collate_fn=collate_fn, shuffle=True)

import torch.optim as optim

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

optimizer = optim.AdamW(model.parameters(), lr=5e-5)
num_epochs = 3

counter = 0
counter_all = len(train_dataloader) * num_epochs

model.train()
for epoch in range(num_epochs):
    total_loss = 0

    for batch in train_dataloader:
        counter += 1

        input_ids = batch['input_ids'].to(device)
        attention_mask = batch['attention_mask'].to(device)
        labels = batch['labels'].to(device)
        decoder_attention_mask = batch['decoder_attention_mask'].to(device)

        # print("input_ids: ", input_ids)
        # print("attention_mask: ", attention_mask)
        # print("labels: ", labels)
        # print("decoder_attention_mask: ", decoder_attention_mask)

        optimizer.zero_grad()

        outputs = model(input_ids=input_ids, attention_mask=attention_mask, labels=labels, decoder_attention_mask=decoder_attention_mask)

        loss = outputs.loss
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

        if counter % 50 == 0:
          avg_loss = total_loss / len(train_dataloader)
          print(f"Korak {counter} od {counter_all}. Epoch {epoch + 1}/{num_epochs}, Loss: {loss.item()}, time: {datetime.datetime.now()}")

    avg_loss = total_loss / len(train_dataloader)
    print(f"Epoch {epoch + 1}/{num_epochs}, Loss: {avg_loss}")

# Save the trained model
output_dir = "./general_model_aug_22/"
model.save_pretrained(output_dir)
tokenizer.save_pretrained(output_dir)