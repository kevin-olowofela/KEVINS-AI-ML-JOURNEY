import csv
nyc_temp=[]
with open("nyc_weather.csv", 'r') as f:
    reader = csv.reader(f)
    next(reader)  
    for row in reader:
        nyc_temp.append(int(row[1]))
avg_temp=sum(nyc_temp[0:7])/len(nyc_temp[0:7])
print(f"The average temperature in NYC for the first 7 days of the month is: {avg_temp:.2f}°F")
max_temp=max(nyc_temp[0:7])
print(f"The maximum temperature in NYC for the first 7 days of the month is: {max_temp}°F")



nyc_temperature_dict = {}
with open("nyc_weather.csv", 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        nyc_temperature_dict[row['date']] = int(row['temperature(F)'])

jan9_temp=nyc_temperature_dict['Jan 9']
print(f"The temperature in NYC on Jan 9 is: {jan9_temp}°F")



with open("Poem.txt", "r") as f:
    poem=f.read()
    word_count={}
    words=poem.split()
    for word in words:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
print(word_count)


