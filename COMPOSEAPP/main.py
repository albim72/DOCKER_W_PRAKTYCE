import pandas as pd
import numpy as np

def funkcja3():
    data = {'Kolumna1': [1, 2, 3, 4, 5], 'Kolumna2': [10, 20, 30, 40, 50]}
    df = pd.DataFrame(data)
    arr = np.array([1, 2, 3, 4, 5])
    srednia = np.mean(arr)
    
    df['Średnia'] = srednia
    print(df)

if __name__ == "__main__":
    funkcja3()
