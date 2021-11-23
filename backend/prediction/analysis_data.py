import numpy as np

class AnalysisData():
    def __init__(self):


    def create_sequences(data, seq_length):
        xs = []
        ys = []
        for i in range(len(data)-seq_length):
            x = data.iloc[i:(i+seq_length)]
            y = data.iloc[i+seq_length]
            xs.append(x)
            ys.append(y)
        return np.array(xs), np.array(ys)

    seq_length = 5
    X, y = create_sequences(daily_cases, seq_length)