# Узнать какая максимальная households в зоне минимального значения population

df[df['population']==df['population'].min()]['households'].agg(['max'])
max    4.0
Name: households, dtype: float64