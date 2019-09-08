#2019-08-22 A refined single bedroom search on craigslist for actual housing help
#Goal: move away from creating .csv files, rather make a pandas dataframe to pipe to data analysis file

#ADDITION TO BE MADE: The file crashes when reading. I blieve it has to do with an incorrect or empty district_list.
# If district_list == 'all', do not filter district
# If district_list is incorrect, write 'could not find {district}'
'''
  File "/Users/irahorecka/Desktop/Harddrive_Desktop/Python/Auto_CL_Housing/pandas_single_bedroom.py", line 108, in find_rooms
    for_export = DataPrep(for_export).title_key()
  File "/Users/irahorecka/Desktop/Harddrive_Desktop/Python/Auto_CL_Housing/pandas_single_bedroom.py", line 54, in title_key
    self.dtfm['Title Key'] = self.dtfm['Title'] + ' _ ' + self.dtfm['Location']'''
import os
import csv
from craigslist import CraigslistHousing
import datetime
import time
import logging
import cl_search_dict as clsd
import state_reg as sr
import selection_key as sk
import copy
#os.chdir('/Users/irahorecka/Desktop/Harddrive_Desktop/Python/Craigslist_project/Data/From Python/Single rooms')
date_time = str(datetime.datetime.now())[:-10]
date = datetime.date.today()

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
        title = f'{date} rooms and sublets in {inst_site_name}_{inst_state_name.title()}.csv'
        with open(title, 'w', newline = '') as rm_csv:
            writer = csv.writer(rm_csv, delimiter = ',')
            writer.writerows([i.split(self.code_break) for i in write_list])
        rm_csv.close()


def my_logger(func):
    logging.basicConfig(filename=f'{func.__name__}.log', level = logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(
            f'Ran with filters: {clsd.room_filters} at {date_time}')
        return func(*args, **kwargs)

    return wrapper


class ExecSearch:
    def __init__(self, states, regions, subregions, house_filter):
        self.states = states
        self.regions = regions
        self.subregions = subregions
        self.filter = house_filter
        self.code_break = ';n@nih;'
        self.header = [f'CL State{self.code_break}CL Region{self.code_break}CL District{self.code_break}Housing Category{self.code_break}Post ID{self.code_break}Repost of (Post ID){self.code_break}Title{self.code_break}URL{self.code_break}Date Posted{self.code_break}Time Posted{self.code_break}Price{self.code_break}Location{self.code_break}Post has Image{self.code_break}Post has Geotag{self.code_break}Bedrooms{self.code_break}Area']

    @my_logger
    def cl_search(self):
        t0 = time.time()
        housing_dict = clsd.cat_dict
        search_state = sr.States

        for state in self.states:
            focus_list = [] 
            if 'focus_dist' in eval(f'search_state.{state}'):
                for reg, reg_name in eval(f'search_state.{state}')["focus_dist"].items():
                    if reg in self.regions:
                        if reg == 'newyork' or reg == 'boston':
                            housing_dict = clsd.apa_dict
                        for sub_reg in reg_name:
                            header_list = copy.deepcopy(self.header)
                            for cat, cat_name in housing_dict.items():
                                if cat in self.filter:
                                    housing_result = CL_Housing_Select(reg, cat, clsd.room_filters)
                                    large_region = housing_result.large_region(sub_reg)
                                    header_list.extend([f"{state.title()}{self.code_break}{reg}{self.code_break}{sub_reg}{self.code_break}{cat_name}{self.code_break}{i['id']}{self.code_break}{i['repost_of']}{self.code_break}{i['name']}{self.code_break}{i['url']}{self.code_break}{i['datetime'][0:10]}{self.code_break}{i['datetime'][11:]}{self.code_break}{i['price']}{self.code_break}{i['where']}{self.code_break}{i['has_image']}{self.code_break}{i['geotag']}{self.code_break}{i['bedrooms']}{self.code_break}{i['area']}" for i in large_region.get_results(sort_by='newest')])
                                    print(state, sub_reg, cat)
                            housing_result.write_to_file(header_list, sub_reg, state)
                            focus_list.append(reg)
            for reg, reg_name in eval(f'search_state.{state}').items():
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
                                    header_list.extend([f"{state.title()}{self.code_break}{reg}{self.code_break}{reg_name}{self.code_break}{cat_name}{self.code_break}{i['id']}{self.code_break}{i['repost_of']}{self.code_break}{i['name']}{self.code_break}{i['url']}{self.code_break}{i['datetime'][0:10]}{self.code_break}{i['datetime'][11:]}{self.code_break}{i['price']}{self.code_break}{i['where']}{self.code_break}{i['has_image']}{self.code_break}{i['geotag']}{self.code_break}{i['bedrooms']}{self.code_break}{i['area']}" for i in small_region.get_results(sort_by='newest')])
                                    print(state, reg, cat)
                            housing_result.write_to_file(header_list, reg_name, state)
                        except ValueError:
                            print('focus_dict encountered')
                            pass
            t1 = time.time()
            print(f"Run time: {'%.2f' % (t1 - t0)} sec")