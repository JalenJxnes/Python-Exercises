import pandas as pd

columns = ['name', 'city', 'age', 'exam-score']

df = pd.read_csv('data3.csv', names = columns)
print(df)
print ('\n')

#Add a row to dataframe
member = pd.Series(data = ['John', 'Boston', 34, 79], index = df.columns, name = 10)
df = pd.concat([df, pd.DataFrame([member])])
print(df)
print('\n')

#Delete rows
df = df.drop(10)

#Add column
df['midterm-score'] = [71, 72, 73, 74, 75, 76, 77, 78, 79, 50]
print(df)
print('\n')

#Insert column describing position
df.insert(loc=2, column='position', value=['dba', 'analyst', 'developer',
'dba', 'analyst', 'developer', 'dba', 'dba', 'analyst', 'analyst'])
print(df)
print('\n')

df = df.drop('age', axis = 1)
print(df)
print('\n')

#Perform data analysis
df['total'] = (df['exam-score'] + df['midterm-score']) / 2
print(df)
print('\n')