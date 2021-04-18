import pandas as pd 
import plotly.figure_factory as ff 
import statistics

data = pd.read_csv("StudentsPerformance.csv")

percentageList = data["math score"].tolist()

mean = statistics.mean(percentageList)
mode = statistics.mode(percentageList)
median = statistics.median(percentageList)
sd = statistics.stdev(percentageList)


p1_sd_start,p1_sd_end = mean - sd, mean+sd
p2_sd_start,p2_sd_end = mean -(2*sd), mean+ (2*sd)
p3_sd_start,p3_sd_end = mean -(3*sd), mean+ (3*sd)


percentage_list_within_sd_1 = [r for r in percentageList if r > p1_sd_start and r< p1_sd_end]
percentage_list_within_sd_2 = [r for r in percentageList if r > p2_sd_start and r< p2_sd_end]
percentage_list_within_sd_3 = [r for r in percentageList if r > p3_sd_start and r< p3_sd_end]

print("{}% of data lies within 1 sd".format(len(percentage_list_within_sd_1)*100/len(percentageList)))
print("{}% of data lies within 2 sd".format(len(percentage_list_within_sd_2)*100/len(percentageList)))
print("{}% of data lies within 3 sd".format(len(percentage_list_within_sd_3)*100/len(percentageList)))