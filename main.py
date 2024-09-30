from bs4 import BeautifulSoup
import math
import os

if __name__ == '__main__':
    names = {}
    total = 0

    # Count the number of messages for each person
    for (root, dirs, files) in os.walk('./facebook_data/your_facebook_activity/messages/inbox'):
        for file in files:
            if file.endswith('.html'):
                with open(root + '/' + file, 'r') as f:
                    soup = BeautifulSoup(f, 'html.parser')
                    for item in soup.find_all('div', {'class': '_2ph_ _a6-h _a6-i'}):
                        if item.text not in names:
                            names[item.text] = 1
                        else:
                            names[item.text] += 1
                        total += 1

    # Sort by value
    names = dict(sorted(names.items(), key=lambda item: item[1]))
        
    # Labeling the names
    def convert_key(key: str):
        words = key.split()  # Split the key into words
        new_words = []
        for word in words:
            if len(word) > 1:
                new_word = word[0] + 'x' * (len(word) - 1)
            else:
                new_word = word[0]  # If it's a single character, keep it as is
            new_words.append(new_word)
        return ' '.join(new_words)  # Join the processed words back
    
    # Print the result
    for key, value in names.items():
        print(f'{convert_key(key):<10}\t:{value:<7}, {"#" * math.ceil(value / total * 100)}')
