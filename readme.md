# Lidia test

## Analysis

The data were analyzed to start the construction of the intended predictor, but there was no time to carry out exploratory analysis of the data, since I was summoned by the Ministry of Health to contribute with planning public health actions for Covid-19 and also the test required skills programming and data analysis in python. 
I had a lot of difficulty to accomplish the task.

## How to analyse data (step by step)

To start exploring the data, I would clean and standardize the bank. 
Afterwards, I would do the descriptive analysis to characterize the sample and calculate the prevalence of each variable in the sample. 
It would also be possible to perform bivariate analysis with chi-square (Pearson's correlation) for linear trend (significance of 5%). 
To register the presence of combinations between factors, it would be possible to create agglomeration scores and, finally, perform a logistic regression (unconditional), with reference to individuals without the presence of a risk variable for heart disease. 
I would use an Odds-Ratio (OR) (95% CI; p <0.05) for all tests.

## Graphs

- x; y

## How to install

```bash
 - python3 -m venv venv
 - source venv/bin/activate
 - pip install -r requirements.txt
 - python3 sex_predictor.py --inputfile test_item.csv
```

## How to run

For sex prediction

- Just run: `python3 sex_predictor.py --inputfile <csv file>`

For graphs generation

- Run `python3 analysis.py`

## Requirements

- Python 3.6
