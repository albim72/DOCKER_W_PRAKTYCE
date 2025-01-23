import pandas as pd
import numpy as np

def create_dataframe():
    data = {
        'A': np.random.rand(10),
        'B': np.random.randint(1, 100, 10)
    }
    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
