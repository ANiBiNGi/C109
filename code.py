import pandas as pd
import statistics
import csv 


df = pd.read_csv("height-weight.csv")
height_list = df["Height(Inches)"].to_list()
weight_list = df["Weight(Pounds)"].to_list()

## -- MEAN FOR HEIGHT & WEIGHT -- ##

height_mean = statistics.mean(height_list)
weight_mean = statistics.mean(weight_list)

## -- MEDIAN FOR HEIGHT & WEIGHT -- ##

height_median = statistics.median(height_list)
weight_median = statistics.median(weight_list)

## -- MODE FOR HEIGHT & WEIGHT -- ##

height_mode = statistics.mode(height_list)
weight_mode = statistics.mode(weight_list)


## -- PRINTING MEAN, MEDIAN, AND MODE TO VALIDATE -- ##

print("Mean, Median, and Mode of Height is {}, {} and {} respectively".format(height_mean, height_median, height_mode))
print("Mean, Median, and Mode of Weight is {}, {} and {} respectively".format(weight_mean, weight_median, weight_mode))

## -- STANDARD DEVIATION FOR HEIGHT & WEIGHT -- ##

height_std_deviation = statistics.stdev(height_list)
weight_std_deviation = statistics.stdev(weight_list)

## -- 1, 2, 3 STANDARD DEVIATIONS FOR HEIGHT -- ##

height_first_std_deviation_start, height_first_std_deviation_end = height_mean - height_std_deviation, height_mean + height_std_deviation

height_second_std_deviation_start, height_second_std_deviation_end = height_mean - (2*height_std_deviation), height_mean + (2*height_std_deviation)

height_third_std_deviation_start, height_third_std_deviation_end = height_mean - (3*height_std_deviation), height_mean + (3*height_std_deviation)


## -- 1, 2, 3 STANDARD DEVIATIONS FOR WEIGHT -- ##

weight_first_std_deviation_start, weight_first_std_deviation_end = weight_mean - weight_std_deviation, weight_mean + weight_std_deviation

weight_second_std_deviation_start, weight_second_std_deviation_end = weight_mean - (2*weight_std_deviation), weight_mean + (2*weight_std_deviation)

weight_third_std_deviation_start, weight_third_std_deviation_end = weight_mean - (3*weight_std_deviation), weight_mean + (3*weight_std_deviation)

## -- PERCENTAGE OF DATA WITHIN 1, 2, 3, STAMDARD DEVIATION FOR HEIGHT -- ##

height_list_of_data_within_1_std_deviation = [result for result in height_list if result > height_first_std_deviation_start and result < height_first_std_deviation_end]

height_list_of_data_within_2_std_deviation = [result for result in height_list if result > height_second_std_deviation_start and result < height_second_std_deviation_end]

height_list_of_data_within_3_std_deviation = [result for result in height_list if result > height_third_std_deviation_start and result < height_third_std_deviation_end]

## -- PERCENTAGE OF DATA WITHIN 1, 2, 3, STAMDARD DEVIATION FOR WEIGHT -- ##

weight_list_of_data_within_1_std_deviation = [result for result in weight_list if result > weight_first_std_deviation_start and result < weight_first_std_deviation_end]

weight_list_of_data_within_2_std_deviation = [result for result in weight_list if result > weight_second_std_deviation_start and result < weight_second_std_deviation_end]

weight_list_of_data_within_3_std_deviation = [result for result in weight_list if result > weight_third_std_deviation_start and result < weight_third_std_deviation_end]

## -- DATA FOR HEIGHT & WEIGHT -- ##

print("{}% of data for height lies within 1 standard deviation".format(len(height_list_of_data_within_1_std_deviation)*100.0/len(height_list)))

print("{}% of data for height lies within 2 standard deviations".format(len(height_list_of_data_within_2_std_deviation)*100.0/len(height_list)))

print("{}% of data for height lies within 3 standard deviations".format(len(height_list_of_data_within_3_std_deviation)*100.0/len(height_list)))

print("{}% of data for weight lies within 1 standard deviation".format(len(weight_list_of_data_within_1_std_deviation)*100.0/len(weight_list)))

print("{}% of data for weight lies within 2 standard deviations".format(len(weight_list_of_data_within_2_std_deviation)*100.0/len(weight_list)))

print("{}% of data for weight lies within 3 standard deviations".format(len(weight_list_of_data_within_3_std_deviation)*100.0/len(weight_list)))




