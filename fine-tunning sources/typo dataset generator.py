import random
import string
import json
#  introduces a typo by swapping two random characters in a word
def introduce_typo(word):
    # randomly change location
    if len(word) < 2:
        return word
    word = list(word)# Convert the word string into a list of characters for manipulation
    i, j = random.sample(range(len(word)), 2)# Pick two random indices from the word's length
    word[i], word[j] = word[j], word[i]# Swap the characters at those two indices
    return ''.join(word)# Join the list back into a string and return it

#generate a dataset of sentences with typos, defaulting to 100 samples
def generate_typo_dataset(num_samples=100):
    sample_sentences = [# List of clean sample sentences to base the dataset on
        "The quick brown fox jumps over the lazy dog.",
        "She sells seashells by the seashore.",
        "A journey of a thousand miles begins with a single step."
    ]
    
    typo_dataset = []# Initialize an empty list to store the typo-filled sentences
    
    for _ in range(num_samples):
        sentence = random.choice(sample_sentences)# Randomly pick one of the sample sentences
        words = sentence.split()# Split the sentence into a list of words
        typo_sentence = ' '.join([introduce_typo(word) for word in words])# Apply introduce_typo to each word and join back with spaces
        typo_dataset.append(typo_sentence)# Add the typo-filled sentence to the dataset
        
    return typo_dataset

# genrate 100 
typo_dataset = generate_typo_dataset(100)
print(typo_dataset)
 #save to json file
file_path =r'C:\Users\Tzara911\hwks\Lect19-RMI\coding  hwk2\fine-tunning sources\typo_dataset.json'
with open(file_path,'w') as f:
    json.dump(typo_dataset,f)
print(f"Dataset saved to {file_path}")    