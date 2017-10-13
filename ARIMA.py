from __future__ import print_function
import pandas as pd
import numpy as np
from scipy import  stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.graphics.api import qqplot

# datafile= '../train/23/23_data.csv'
# data = pd.read_csv(datafile, encoding = 'utf-8')
# data['index'] = range(len(data.index))
# data = data.set_index(["index"])
# plot_lines = data.loc[1:250, ['int_tmp']]
# print (len(plot_lines))
# plot_lines.index = pd.Index(sm.tsa.datetools.dates_from_range('2001', '2250'))

start = 0
end = 999
gap = end - start +1
daily_payment = pd.read_csv('../train/23/23_data.csv', encoding='utf-8')
daily_payment = daily_payment.drop(['group', 'acc_y', 'acc_x', 'pitch1_ng5_DC', 'pitch1_speed', 'pitch2_speed',
                  'pitch3_speed', 'yaw_speed', 'wind_direction_mean', 'wind_direction',
                  'wind_speed', 'wind_speed'], axis=1)
test_data = daily_payment.loc[start:end, ['int_tmp']]
test_data.index = pd.date_range(start='20130101', periods=(end - start)+1)

diff1 = test_data.diff(1)
fig = plt.figure()
ax1 = fig.add_subplot(211)
# l1 = plt.axvline(x=7900, color='b')
# l2 = plt.axvline(x=7950, color='b')
fig = sm.graphics.tsa.plot_acf(test_data, lags=gap-3, ax=ax1)
# ax2 = fig.add_subplot(212)
# fig = sm.graphics.tsa.plot_pacf(test_data, lags=gap, ax=ax2)
plt.show()

#
# # arma_mod50 = sm.tsa.ARMA(plot_lines, (5, 0)).fit()
# # print(arma_mod50.aic, arma_mod50.bic, arma_mod50.hqic)
# arma_mod06 = sm.tsa.ARMA(plot_lines, (0, 6)).fit()
# print(arma_mod06.aic, arma_mod06.bic, arma_mod06.hqic)
# # arma_mod56 = sm.tsa.ARMA(plot_lines, (5, 5)).fit()
# # print(arma_mod56.aic, arma_mod56.bic, arma_mod56.hqic)
#
# # fig = plt.figure()
# # resid = arma_mod06.resid
# # ax1 = fig.add_subplot(211)
# # fig = sm.graphics.tsa.plot_acf(resid.values.squeeze(), lags=97, ax=ax1)
# # ax2 = fig.add_subplot(212)
# # fig = sm.graphics.tsa.plot_pacf(resid, lags=97, ax=ax2)
# # plt.show()
#
# # print(sm.stats.durbin_watson(arma_mod06.resid.values))
# #
# # fig1 = plt.figure()
# # ax = fig1.add_subplot(111)
# # fig = qqplot(resid, line='q', ax=ax, fit=True)
# # plt.show()
#
# predict_dta = arma_mod06.predict('2250', '2300', dynamic=True)
# print(predict_dta)
#
#
# origin_data_lines = data.loc[250:300, ['int_tmp']]
# origin_data_lines.index = pd.Index(sm.tsa.datetools.dates_from_range('2250', '2300'))
# print ('origin data:')
# print (origin_data_lines)
# fig, ax = plt.subplots(figsize=(12, 8))
# ax = plot_lines.ix['2000':].plot(ax=ax)
# origin_data_lines.plot(ax=ax)
# fig = arma_mod06.plot_predict('2250', '2300', dynamic=True, ax=ax, plot_insample=False)
# plt.show()









