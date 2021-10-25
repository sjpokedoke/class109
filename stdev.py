import csv
import pandas as pd
import statistics

df = pd.read_csv("data.csv")
heightlist = df["Height(Inches)"].to_list()
weightlist = df["Weight(Pounds)"].to_list()

heightmean = statistics.mean(heightlist)
heightmedian = statistics.median(heightlist)
heightmode = statistics.mode(heightlist)
heightstdev = statistics.stdev(heightlist)

weightmean = statistics.mean(weightlist)
weightmedian = statistics.median(weightlist)
weightmode = statistics.mode(weightlist)
weightstdev = statistics.stdev(weightlist)

print("Mean, Median and mode of height is {}, {} and {} respectively".format(heightmean, heightmedian, heightmode))
print("Mean, Median and mode of weight is {}, {} and {} respectively".format(weightmean, weightmedian, weightmode))

heightfirststdevstart, heightfirststdevend = heightmean-heightstdev, heightmean+heightstdev
weightfirststdevstart, weightfirststdevend = weightmean-weightstdev, weightmean+weightstdev

heightlistdataonestdev = [res for res in heightlist if res > heightfirststdevstart and res < heightfirststdevend]
weightlistdataonestdev = [res for res in weightlist if res > weightfirststdevstart and res < weightfirststdevend]

print("{}% of data for height lies within one standard deviation".format(len(heightlistdataonestdev)*100.0/len(heightlist)))
print("{}% of data for weight lies within one standard deviation".format(len(weightlistdataonestdev)*100.0/len(weightlist)))

heighttwostdevstart, heighttwostdevend = heightmean-2*heightstdev, heightmean+2*heightstdev
weighttwostdevstart, weighttwostdevend = weightmean-2*weightstdev, weightmean+2*weightstdev

heightlistdatatwostdev = [res for res in heightlist if res > heighttwostdevstart and res < heighttwostdevend]
weightlistdatatwostdev = [res for res in weightlist if res > weighttwostdevstart and res < weighttwostdevend]

print("{}% of data for height lies within two standard deviation".format(len(heightlistdatatwostdev)*100.0/len(heightlist)))
print("{}% of data for weight lies within two standard deviation".format(len(weightlistdatatwostdev)*100.0/len(weightlist)))

heightthreestdevstart, heightthreestdevend = heightmean-3*heightstdev, heightmean+3*heightstdev
weightthreestdevstart, weightthreestdevend = weightmean-3*weightstdev, weightmean+3*weightstdev

heightlistdatathreestdev = [res for res in heightlist if res > heightthreestdevstart and res < heightthreestdevend]
weightlistdatathreestdev = [res for res in weightlist if res > weightthreestdevstart and res < weightthreestdevend]

print("{}% of data for height lies within three standard deviation".format(len(heightlistdatathreestdev)*100.0/len(heightlist)))
print("{}% of data for weight lies within three standard deviation".format(len(weightlistdatathreestdev)*100.0/len(weightlist)))