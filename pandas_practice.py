
import pandas as pd
#Weekend Domestic Chart for October 28, 2022

df = pd.DataFrame({
    'Gross': [27472140, 9852430, 7185126, 5432387, 4059665, 2741834,2741100],
    'Weekends in Release': [2,2,1,5,3,3,4]
})

df.index = [
    'Black Adam', 'Ticket to Paradise', 'Prey for the Devil', 'Smile', 'Halloween Ends', 'Till', 'Lyle, Lyle, Crocodile',
]

#Select "Black Adam" information
df.loc['Black Adam']
df.iloc[0]

#Show the Gross for Ticket to Paradise, Prey for the Devil and Smile
df.loc['Ticket to Paradise': 'Smile', 'Gross']

#Filter out Lyle, Lyle, Crocodile
df.drop('Lyle, Lyle, Crocodile')

#What if next week is a holiday and more people go to the movies? add 5000000 to Gross to all movies
success = pd.Series([-5000000], index = ['Gross'])
df[['Gross']] + success

#Add new column "Per Theater"
theater = pd.Series(
    [6241, 2669, 2411, 1687, 1187, 1332, 874], name = 'Per Theater'
)
df['Per Theater'] = theater

#Capitalize movie titles
df.rename(index=str.upper)

#Add "The Woman King" to the df
df.append(pd.Series({
    'Gross' : 1127527, 'Weekends in Release' : 7, 'Per Theater' : 780
}, name = 'The Woman King'))

#Summary statistics for Gross
df.describe()
gross = df['Gross']
gross.sum(), gross.mean(), gross.std()
