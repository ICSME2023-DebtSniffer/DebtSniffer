import pandas as pd
from sklearn.model_selection import train_test_split
import pdb
from sklearn.model_selection import StratifiedKFold
import os
import subprocess
from sklearn.model_selection import KFold


df = pd.read_csv("data/satd-comments-manual-subclass-simple-preprocessed.csv")
print(len(df))
df = df.dropna()
print(len(df))

df = df.rename(columns={"debt": "label"})
# print(df.head())
# train, test = train_test_split(df, test_size=0.2)

number_of_folds = 5
kf = KFold(n_splits = number_of_folds, shuffle = True, random_state = 2)
fold = kf.split(df)


def get_dataset():
    result = next(fold, None)
    train = df.iloc[result[0]]
    test =  df.iloc[result[1]]
    # import pdb;pdb.set_trace()
    train.to_csv("train.csv")
    test.to_csv("test.csv")
    train['subset'] = 'train'
    test['subset'] = 'test'
    frames = [train, test]
    dataset = pd.concat(frames)

    #create file dataset.txt
    df_label = dataset[['subset', 'label']].copy()
    df_content = dataset[['comment']].copy()
    df_label.to_csv("data/SATD.txt", sep='\t', index=True, header=False)
    df_content.to_csv("data/corpus/SATD.clean.txt", sep=' ', index=False, header=False)

get_dataset()
print("DONE")