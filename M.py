import pandas as p
import statistics as s

df = p.read_csv("SOCR-HeightWeight.csv")
height = df['Height(Inches)'].tolist()
median = s.median(height)
mode = s.mode(height)
mean = s.mean(height)

print('median of height: ', median)
print('mode of height: ', mode)
print('mean of height: ', mean)

weight = df['Weight(Pounds)'].tolist()
median = s.median(weight)
mode = s.mode(weight)
mean = s.mean(weight)

print('median of weight: ', median)
print('mode of weight: ', mode)
print('mean of weight: ', mean)