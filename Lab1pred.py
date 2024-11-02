import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df1 = pd.read_csv('Total Load_DE_timestamped.csv', delimiter=';', index_col=False, header=0, names=['time', 'MW'])
print(df1)

#pierwszy sposób
df2 = pd.DataFrame()
df2['time'] = df1['time'][::4].reset_index(drop=True)
print(df2)
df2['MW'] = df1.MW.groupby(np.arange(len(df1.MW))//4).mean()
print(df2)

#drugi sposób
#group_index = df1.index // 4
#df2 = df1.groupby(group_index).agg({'time': 'first', 'MW': 'mean'})
#print(df2)

nan_rows = df2[df2['MW'].isnull()].index.tolist()
print(nan_rows)

df2.loc[nan_rows[0], 'MW'] = np.mean([df2.loc[nan_rows[0]-1, 'MW'], df2.loc[nan_rows[0]+1, 'MW']])

#task 2
df2['Naive forecast 1'] = df2['MW'].shift(7*24)
print(df2.loc[168:, :])

#task 3
df2['time'] = pd.to_datetime(df2['time'], format='%d.%m.%Y %H:%M')

df2['day_of_week'] = df2['time'].dt.day_name()

df2['Naive forecast 2'] = df2['MW'].shift(1*24)  #domyślnie

included_days = ['Monday', 'Saturday', 'Sunday']
df2.loc[df2['day_of_week'].isin(included_days), 'Naive forecast 2'] = df2['Naive forecast 1']

print(df2.loc[48:,:])
print(df2.loc[72:,:])
print(df2.loc[216:,:])

#task 4
df2['Naive forecast 3'] = df2['MW'].shift(1*24)

# TASK 5: Calculate MAE and RMSE for each hour
mae_results_naive1 = []
rmse_results_naive1 = []
mae_results_naive2 = []
rmse_results_naive2 = []
mae_results_naive3 = []
rmse_results_naive3 = []
df2['Hour'] = df2['time'].dt.hour

grouped_df = df2.iloc[168:].copy() #aby pozbyć się pierwszych wartości NaN

for hour, group in grouped_df.groupby('Hour'):
    errors_naive1 = group['MW'] - group['Naive forecast 1']
    #print(errors_naive1)
    mae_naive1 = np.abs(errors_naive1).mean()
    #print(mae_naive1)
    rmse_naive1 = np.sqrt((errors_naive1 ** 2).mean())

    errors_naive2 = group['MW'] - group['Naive forecast 2']
    mae_naive2 = np.abs(errors_naive2).mean()
    rmse_naive2 = np.sqrt((errors_naive2 ** 2).mean())

    mae_results_naive1.append(mae_naive1)
    rmse_results_naive1.append(rmse_naive1)
    mae_results_naive2.append(mae_naive2)
    rmse_results_naive2.append(rmse_naive2)

errors_total_naive1 = grouped_df['MW'] - grouped_df['Naive forecast 1']
mae_total_naive1 = np.abs(errors_total_naive1).mean()
rmse_total_naive1 = np.sqrt((errors_total_naive1 ** 2).mean())

errors_total_naive2 = grouped_df['MW'] - grouped_df['Naive forecast 2']
mae_total_naive2 = np.abs(errors_total_naive2).mean()
rmse_total_naive2 = np.sqrt((errors_total_naive2 ** 2).mean())

for hour, group in grouped_df.groupby('Hour'):
    errors_naive3 = group['MW'] - group['Naive forecast 3']
    mae_naive3 = np.abs(errors_naive3).mean()
    rmse_naive3 = np.sqrt((errors_naive3 ** 2).mean())

    mae_results_naive3.append(mae_naive3)
    rmse_results_naive3.append(rmse_naive3)


errors_total_naive3 = grouped_df['MW'] - grouped_df['Naive forecast 3']
mae_total_naive3 = np.abs(errors_total_naive3).mean()
rmse_total_naive3 = np.sqrt((errors_total_naive3 ** 2).mean())


print("MAE for naive_forecast_1 (separately for each hour):", mae_results_naive1)
print("RMSE for naive_forecast_1 (separately for each hour):", rmse_results_naive1)
print("MAE for naive_forecast_2 (separately for each hour):", mae_results_naive2)
print("RMSE for naive_forecast_2 (separately for each hour):", rmse_results_naive2)
print("MAE for naive_forecast_3 (separately for each hour):", mae_results_naive3)
print("RMSE for naive_forecast_3 (separately for each hour):", rmse_results_naive3)

print("MAE for naive_forecast_1 (jointly for all hours):", mae_total_naive1)
print("RMSE for naive_forecast_1 (jointly for all hours):", rmse_total_naive1)
print("MAE for naive_forecast_2 (jointly for all hours):", mae_total_naive2)
print("RMSE for naive_forecast_2 (jointly for all hours):", rmse_total_naive2)
print("MAE for naive_forecast_3 (jointly for all hours):", mae_total_naive3)
print("RMSE for naive_forecast_3 (jointly for all hours):", rmse_total_naive3)

print(df2)

start_date = '2022-03-04 00:00:00'
end_date = '2022-03-11 00:00:00'
selected_data = df2[(df2['time'] >= start_date) & (df2['time'] <= end_date)]

plt.figure(figsize=(12, 6))
plt.plot(selected_data['time'], selected_data['MW'], label='Actual')
plt.plot(selected_data['time'], selected_data['Naive forecast 1'], label='Naive Forecast 1')
plt.plot(selected_data['time'], selected_data['Naive forecast 2'], label='Naive Forecast 2')
plt.plot(selected_data['time'], selected_data['Naive forecast 3'], label='Naive Forecast 3')
plt.xlabel('Time')
plt.ylabel('MW')
plt.title('Actual vs. Forecasted Values for a 7-day Period')
plt.legend()
plt.grid(True)
plt.show()