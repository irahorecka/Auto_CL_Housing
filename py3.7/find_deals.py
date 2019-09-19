#Look for all sublets and rooms in sfbay craigslist, sort out statistically significant pricings, i.e. mean - 1sd after outlier removal
#Afterwards, only sort out districts of interest, e.g. berkeley, oakland, fremont.

import pandas as pd
import os
import csv
import datetime
from craigslist_information import Filters as clsd #make better abbreviation later
from user_information import SelectionKeys as sk
import copy
pd.options.mode.chained_assignment = None

base_dir = os.getcwd()
os.chdir(f'{base_dir}/housing_csv/CL Files')

class StatAnalysis:
    def __init__(self, dtfm):
        self.dtfm = dtfm
    
    def omit_outlier(self):
        Q1 = self.dtfm['Price'].quantile(0.25)
        Q3 = self.dtfm['Price'].quantile(0.75)
        IQR = Q3 - Q1
        self.dtfm = self.dtfm.loc[self.dtfm['Price'] <= Q3 + 1.5*IQR]
        self.dtfm = self.dtfm.loc[self.dtfm['Price'] >= Q1 - 1.5*IQR]
        #a trimmed mean will cut too much data from either tail, those this can be adjusted
        #consult whether an outlier excision or trimmed mean should be used for negating outliers

    #try a price_area analysis with price - if price is high, are you getting a good deal per square foot?
    def stat_significant(self, sd_val, val_type):
        mean_price, mean_price_area = self.dtfm['Price'].mean(), self.dtfm['Price_Area'].mean()
        sd_price, sd_price_area = self.dtfm['Price'].std(), self.dtfm['Price_Area'].std()
        if val_type == 0:
            self.dtfm = self.dtfm.loc[self.dtfm['Price'] <= (mean_price - sd_val*sd_price)]
            print('%.2f' % (mean_price - sd_val*sd_price), '%.2f' % (mean_price_area - 1*sd_price_area))
        else:
            self.dtfm = self.dtfm.loc[self.dtfm['Price'] >= (mean_price + sd_val*sd_price)]
            print('%.2f' % (mean_price + sd_val*sd_price), '%.2f' % (mean_price_area - 1*sd_price_area))
        #Search low price/area
        self.dtfm = self.dtfm.loc[self.dtfm['Price_Area'] <= (mean_price_area + 1*sd_price_area)] #watch for hardcoded val

    def select_districts(self, dist_list):
        return_dtfm = pd.DataFrame()
        self.dtfm.loc[:,'Location'] = self.dtfm['Location'].str.lower()
        if len(dist_list) == 0:
            return_dtfm = self.dtfm
        else:
            for i in dist_list:
                return_dtfm = return_dtfm.append(self.dtfm.loc[self.dtfm['Location'].str.contains(i.lower())])
        self.dtfm = return_dtfm

    def curate_dtfm(self, housing_dist, sd, val_type):
        self.omit_outlier()
        self.stat_significant(sd, val_type)
        self.select_districts(housing_dist)
    
    def return_dtfm(self):
        return self.dtfm

        
class DataPrep: #does this need to be a class?
    def __init__(self, dtfm):
        self.dtfm = dtfm
    
    def title_key(self):
        def cut_time():
            append_list = list()
            for index,row in self.dtfm.iterrows():
                if len(row['Time Posted']) == 5:
                    append_list.append(int(row['Time Posted'][:2]))
                elif len(row['Time Posted']) == 4:
                    append_list.append(int(row['Time Posted'][:1]))
            return append_list
        dtfm = copy.deepcopy(self.dtfm)
        dtfm['Title Key'] = dtfm['Title'] + ' _ ' + dtfm['Location']
        dtfm['Num Time'] = pd.Series(cut_time())
        dtfm = dtfm.sort_values(by = ['Date Posted', 'Num Time'], ascending = [False, False], inplace = False, kind = 'quicksort')
        return dtfm


#should the functions below be made into classes?
def compile_dtfm():
    dtfm = pd.DataFrame()
    for filename in os.listdir():
        if filename[-4:] == '.csv':
            concat_dtfm = pd.read_csv(filename, sep = ',')
            concat_dtfm = concat_dtfm.loc[concat_dtfm['Area'].str[-3:] == 'ft2']
            #make key for title + location and remove duplicates
            concat_dtfm['Title Key'] = concat_dtfm['Title'] + ' _ ' + concat_dtfm['Location']
            concat_dtfm['Price'] = concat_dtfm['Price'].str[1:].astype(float)
            concat_dtfm['Area'] = concat_dtfm['Area'].str[:-3].astype(float)
            concat_dtfm['Price_Area'] = concat_dtfm['Price'] / concat_dtfm['Area']
            dtfm = dtfm.append(concat_dtfm, ignore_index=True, sort = False)
            #remove generated CL filenames to save space
            os.remove(filename)
        else:
            pass
    dtfm = dtfm.drop_duplicates(subset = ['Title Key'], keep = False)
    dtfm = dtfm.drop(['Post ID', 'Repost of (Post ID)', 'Post has Image', 'Post has Geotag', 'Title Key'], axis = 1)
    return dtfm

def drop_and_sort(dtfm1, dtfm2):
    dtfm = dtfm1.append(dtfm2, ignore_index = True, sort = False)
    dtfm = dtfm.drop_duplicates(subset = ['Title Key'], keep = False)
    dtfm = dtfm.drop(['Title Key', 'Num Time'], axis = 1)
    return dtfm

def find_rooms(dtfm, sd, val_type):
    cat_val = [clsd.cat_dict[i] for i in sk.selected_cat]
    reg_list = dtfm['CL District'].unique()
    for_export = pd.DataFrame()
    for i in cat_val:
        if i == 'apts & housing for rent' or i == 'vacation rentals': #find categories where bedrooms will be important
            bed_list = dtfm['Bedrooms'].unique()
        else:
            bed_list = []
        if len(bed_list) != 0:
            for j in bed_list:
                temp_dtfm = dtfm.loc[(dtfm['Housing Category'] == i) & (dtfm['Bedrooms'] == j)]
                for k in reg_list:    
                    temp_dtfm_curate = StatAnalysis(temp_dtfm.loc[temp_dtfm['CL District'] == k])
                    temp_dtfm_curate.curate_dtfm(sk.district_list, sd, val_type)
                    for_export = for_export.append(temp_dtfm_curate.return_dtfm(), ignore_index=True, sort = False)
        else:
            temp_dtfm = dtfm.loc[dtfm['Housing Category'] == i]
            for k in reg_list:    
                temp_dtfm_curate = StatAnalysis(temp_dtfm.loc[temp_dtfm['CL District'] == k])
                temp_dtfm_curate.curate_dtfm(sk.district_list, sd, val_type)
                for_export = for_export.append(temp_dtfm_curate.return_dtfm(), ignore_index=True, sort = False)
            
    os.chdir(f'{base_dir}/housing_csv/Significant Deals')
    old_file = pd.read_csv('significant posts.csv')
    parse_old_file = DataPrep(old_file).title_key()
    parse_for_export = DataPrep(for_export).title_key()
    concat_file = drop_and_sort(parse_for_export, parse_old_file)
 
    ref_file = concat_file.append(old_file, ignore_index = True, sort = False)
    ref_file.to_csv('significant posts.csv', index = False)
    concat_file.to_csv('new_post.csv', index = False)
    return concat_file