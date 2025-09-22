import pandas as pd

import numpy as np

def Pan():
    df2 = pd.DataFrame(

        {
            "Name": "Aron",
            "B": pd.Timestamp("20130102"),
            "C": pd.Series(1, index=list(range(4)), dtype="float32"),
            "D": np.array([3] * 4, dtype="int32"),
            "E": pd.Categorical(["test", "train", "test", "train"]),
        }
    )

    print(df2)
    print(df2.dtypes)
    print(df2.head(1))
    print(df2.columns)
    #print(df2.to_numpy)
    print(df2.loc[:, ["B","C"]])



Pan()