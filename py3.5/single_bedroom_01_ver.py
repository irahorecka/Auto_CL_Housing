#2019-08-22 A refined single bedroom search on craigslist for actual housing help
#Goal: move away from creating .csv files, rather make a pandas dataframe to pipe to data analysis file

#ADDITION TO BE MADE: The file crashes when reading. I blieve it has to do with an incorrect or empty district_list.
# If district_list == 'all', do not filter district
# If district_list is incorrect, write 'could not find {district}'

import os
import csv
from craigslist import CraigslistHousing
import datetime
import time
import logging
from craigslist_information import Filters as clsd #make better abbreviation later
from craigslist_information import States as sr #make better abbreviation later
from user_information import SelectionKeys as sk
import copy

class CL_Housing_Select:
    def __init__(self, inst_site, inst_category, inst_filters):
        self.inst_site = inst_site
        self.inst_category = inst_category
        self.inst_filters = inst_filters
        self.code_break = ';n@nih;'

    def small_region(self):
        #make this into another method and add small_region addition below as its native method function
        return CraigslistHousing(site=self.inst_site,category=self.inst_category,filters=self.inst_filters)

    def large_region(self, inst_area):
        return CraigslistHousing(site=self.inst_site,category=self.inst_category,filters=self.inst_filters,area=inst_area)

    def write_to_file(self, write_list, inst_site_name, inst_state_name):
        date = datetime.date.today()
        title = '{} rooms and sublets in {}_{}.csv'.format(date,inst_site_name,inst_state_name.title())
        with open(title, 'w', newline = '') as rm_csv:
            writer = csv.writer(rm_csv, delimiter = ',')
            writer.writerows([i.split(self.code_break) for i in write_list])
        rm_csv.close()


def my_logger(func):
    logging.basicConfig(filename='{}.log'.format(func.__name__), level = logging.INFO)

    def wrapper(*args, **kwargs):
        date_time = str(datetime.datetime.now())[:-10]
        logging.info(
            'Ran with filters: {} at {}'.format(clsd.room_filters,date_time))
        return func(*args, **kwargs)

    return wrapper


class ExecSearch:
    def __init__(self, states, regions, subregions, house_filter):
        self.states = states
        self.regions = regions
        self.subregions = subregions
        self.filter = house_filter
        self.code_break = ';n@nih;'
        self.header = ['CL State{}CL Region{}CL District{}Housing Category{}Post ID{}Repost of (Post ID){}Title{}URL{}Date Posted{}Time Posted{}Price{}Location{}Post has Image{}Post has Geotag{}Bedrooms{}Area'.format(self.code_break,self.code_break,self.code_break,self.code_break,self.code_break,self.code_break,self.code_break,self.code_break,self.code_break,self.code_break,self.code_break,self.code_break,self.code_break,self.code_break,self.code_break)]

    

    @my_logger
    def cl_search(self):
        t0 = time.time()
        housing_dict = clsd.cat_dict

        for state in self.states:
            focus_list = [] 
            if 'focus_dist' in eval('sr.{}'.format(state)):
                for reg, reg_name in eval('sr.{}'.format(state))["focus_dist"].items():
                    if reg in self.regions:
                        if reg == 'newyork' or reg == 'boston':
                            housing_dict = clsd.apa_dict
                        for sub_reg in reg_name:
                            header_list = copy.deepcopy(self.header)
                            for cat, cat_name in housing_dict.items():
                                if cat in self.filter:
                                    housing_result = CL_Housing_Select(reg, cat, clsd.room_filters)
                                    large_region = housing_result.large_region(sub_reg)
                                    header_list.extend(["{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}".format(state.title(),self.code_break,reg,self.code_break,sub_reg,self.code_break,cat_name,self.code_break,i['id'],self.code_break,i['repost_of'],self.code_break,i['name'],self.code_break,i['url'],self.code_break,i['datetime'][0:10],self.code_break,i['datetime'][11:],self.code_break,i['price'],self.code_break,i['where'],self.code_break,i['has_image'],self.code_break,i['geotag'],self.code_break,i['bedrooms'],self.code_break,i['area']) for i in large_region.get_results(sort_by='newest')])
                                    print(state, sub_reg, cat)
                            housing_result.write_to_file(header_list, sub_reg, state)
                            focus_list.append(reg)
            for reg, reg_name in eval('sr.{}'.format(state)).items():
                if reg in self.regions:
                    if reg in focus_list:
                        continue
                    else:
                        try:
                            header_list = copy.deepcopy(self.header)
                            for cat, cat_name in housing_dict.items():
                                if cat in self.filter:
                                    housing_result = CL_Housing_Select(reg, cat, clsd.room_filters)
                                    small_region = housing_result.small_region()
                                    header_list.extend(["{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}".format(state.title(),self.code_break,reg,self.code_break,reg_name,self.code_break,cat_name,self.code_break,i['id'],self.code_break,i['repost_of'],self.code_break,i['name'],self.code_break,i['url'],self.code_break,i['datetime'][0:10],self.code_break,i['datetime'][11:],self.code_break,i['price'],self.code_break,i['where'],self.code_break,i['has_image'],self.code_break,i['geotag'],self.code_break,i['bedrooms'],self.code_break,i['area']) for i in small_region.get_results(sort_by='newest')])                        
                                    print(state, reg, cat)
                            housing_result.write_to_file(header_list, reg_name, state)
                        except ValueError:
                            print('focus_dict encountered')
                            pass
            t1 = time.time()
            print("Run time: {} sec".format('%.2f' % (t1 - t0)))