import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# data sets

apl_price = [93,112,104.88,144,169]
ms_price = [39, 50, 57, 69, 94]
year = [2014, 2015, 2016, 2017, 2018 ]

plt.plot(year,apl_price,'-.r',                              #will show in same subplot
         year,ms_price, ':g')
plt.scatter(year,ms_price)
plt.xlabel('year')                                          #label x-axis
plt.ylabel('Apple Stock')
plt.show()

"""Making subplots"""

sub_plot, plot = plt.subplots(2,2, figsize=(10,5))
plot[0,1].scatter(year,apl_price)
# apl_pri.set_major_locator(MaxNLocator(integer = True))
plot[1,1].plot(year,ms_price,':y')


"""For Only one row or column"""

sub_plot, plot2 = plt.subplots(1,2, figsize=(10,5))
plot2[0].scatter(year,apl_price)
plot2[1].plot(year,ms_price,':y')
plt.show()