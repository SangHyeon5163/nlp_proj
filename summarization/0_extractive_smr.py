# Import Library
import pandas as pd
import numpy as np 

from gensim.summarization.summarizer import summarize

# Load Dataset 
df = pd.read_csv('Korean_NLP_Tutorial/dataset/BookSummarization/test_df/Book_test.csv')
df = df.iloc[0:150] 
df.reset_index(inplace=True)

# Extract Summarization
df['extract'] = df.passage.apply(lambda x : summarize(x, ratio=0.4))
df.head() 

random_number = np.random.randint(0,99, size=1)
print(random_number[0]) 

for i in range(0, 3):
    random_number = np.random.randint(0,150, size=1)
    print("=" * 120)
    print(f'{random_number[0]}' + " 번째 문장 \n")
    print('원문 내용: \n\n' + df['passage'][random_number[0]] + '\n\n')
    print('추출 요약 내용: \n\n' + df['extract'][random_number[0]] + '\n\n')
    print('라벨링된 요약 내용: \n\n' + df['summary'][random_number[0]] + '\n\n')

