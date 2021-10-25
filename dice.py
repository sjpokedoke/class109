import random
import statistics
import plotly.figure_factory as ff

result = []

for i in range(0,1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    result.append(dice1+dice2)

mean = sum(result)/len(result)
median = statistics.median(result)
mode = statistics.mode(result)
stdev = statistics.stdev(result)

firststdevstart, firststdevend = mean-stdev, mean+stdev
twostdevstart, twostdevend = mean-2*stdev, mean+2*stdev
threestdevstart, threestdevend = mean-3*stdev, mean+3*stdev

listofdatafirststdev = [res for res in result if res > firststdevstart and res < firststdevend]
listofdatatwostdev = [res for res in result if res > twostdevstart and res < twostdevend]
listofdatathreestdev = [res for res in result if res > threestdevstart and res < threestdevend]

print("{}% of data lies within one standard deviation".format(len(listofdatafirststdev)*100.0/len(result)))
print("{}% of data lies within two standard deviation".format(len(listofdatatwostdev)*100.0/len(result)))
print("{}% of data lies within three standard deviation".format(len(listofdatathreestdev)*100.0/len(result)))

#fig = ff.create_distplot([result], ["Result"], show_hist = False)
#fig.show()