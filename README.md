# Naive Predictions of Electric Load Demand in Germany

This project aims to analyze and forecast electric load demand in Germany using naive forecasting models. The main objective is to transform raw electric load data into a manageable hourly resolution and compute forecasts based on historical values. The results are evaluated using Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE).

## Project Overview

The project involves the following key steps:
1. Download electric load demand data for Germany.
2. Transform the data to an hourly resolution.
3. Implement three naive forecasting models to predict future demand.
4. Evaluate the models using MAE and RMSE metrics.
5. Visualize the forecasts against actual values for a selected period.

## Data

The electric load demand data can be downloaded from the course web page. The dataset includes values recorded at 15-minute intervals (in MW) and needs to be processed to derive hourly averages.

## Methodology

The methodology followed in this project includes:

1. **Data Transformation**:
   - Average the four 15-minute values for each hour to create an hourly dataset.
   - Fill in any missing values in March with the average of the neighboring hours.

2. **Naive Forecasting Models**:
   - **Naive Model #1**: Predicts demand based on the same hour from the same day in the previous week.
   - **Naive Model #2**: Uses the same hour from the previous week for weekdays (Monday, Saturday, Sunday) and the previous day for other days.
   - **Naive Model #3**: Predicts demand based solely on the same hour from the previous day.

3. **Evaluation**:
   - Compute MAE and RMSE for the three naive models for each hour of the day, as well as jointly for all hours.

4. **Visualization**:
   - Select a 7-day period and plot forecasts from the three naive models alongside actual values.

## Results

The evaluation metrics (MAE and RMSE) for the naive models will be printed in the console output. Additionally, graphical visualizations comparing the forecasts and actual demand will be generated.
