import pandas as pd


if __name__ == "__main__":
    model_list = ['CNN_LSTM_20201103-181740_0.4408.50', 'CNN_LSTM_20201103-181740_0.4408.50', 'CNN_LSTM_20201103-181044_0.4284.50', 'CNN_LSTM_20201103-174348_0.4127.70', 'CNN_LSTM_20201103-163042_0.4303.60', 'CNN_LSTM_20201103-160026_0.4157.65', 'CNN_LSTM_20201103-150358_0.4101.70']
    folder = './predict/'
    predict = [0] * 227         # 227: test size
    for idx, model_name in enumerate(model_list):
        df = pd.read_csv(folder + model_name + '.csv').sort_values(['ID']).Label.to_list()
        predict = [a + b for a, b in zip(predict, df)]
    predict = [sum_value / len(model_list) for sum_value in predict]
    id = [_+1 for _ in range(len(predict))]

    ensemble_df = pd.DataFrame({'ID': id, 'Label': predict})
    ensemble_df.to_csv(folder + 'ensemble.csv', index=False)