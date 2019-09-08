#ALL CL FILTERS AND STATES' CRAIGSLIST REGIONS IN DICTIONARY

class Filters:
    #A file to store room filters, rooming categories, and state keys in dictionaries
    room_filters = {'private_room' : True, #bool
        'private_bath' : None, #bool
        'cats_ok' : None, #bool
        'dogs_ok' : None, #bool
        'min_price' : 500,
        'max_price' : 1200,
        'min_ft2' : None,
        'max_ft2' : None,
        'min_bedrooms' : None,
        'max_bedrooms' : None,
        'min_bathrooms' : None,
        'max_bathrooms' : None,
        'no_smoking' : None, #bool
        'is_furnished' : None, #bool
        'wheelchair_acccess' : None, #bool
        'has_image' : True #bool
    }

    cat_dict = {'apa':'apts/housing for rent',
        'swp':'housing swap',
        'off':'office & commercial',
        'prk':'parking & storage',
        'reb':'real estate - by broker',
        'reo':'real estate - by owner',
        'roo':'rooms & shares',
        'sub':'sublets & temporary',
        'vac':'vacation rentals',
        'hou':'wanted: apts',
        'rew':'wanted: real estate',
        'sha':'wanted: room/share',
        'sbw':'wanted: sublet/temp'}

    apa_dict = {'aap':'apts/housing for rent',
        'swp':'housing swap',
        'off':'office & commercial',
        'prk':'parking & storage',
        'reb':'real estate - by broker',
        'reo':'real estate - by owner',
        'roo':'rooms & shares',
        'sub':'sublets & temporary',
        'vac':'vacation rentals',
        'hou':'wanted: apts',
        'rew':'wanted: real estate',
        'sha':'wanted: room/share',
        'sbw':'wanted: sublet/temp'}


class States:
    alabama = {'auburn':'Auburn',
        'bham':'Birmingham',
        'columbusga':'Columbus, GA',
        'dothan':'Dothan',
        'shoals':'Florence-Muscle Shoals',
        'gadsden':'Gadsden-Anniston',
        'huntsville':'Huntsville-Decatur',
        'mobile':'Mobile',
        'montgomery':'Montgomery',
        'tuscaloosa':'Tuscaloosa'
        }

    arizona = {'flagstaff':'Flagstaff-Sedona',
        'mohave':'Mohave County',
        'phoenix':'Phoenix',
        'prescott':'Prescott',
        'showlow':'Show Low',
        'sierravista':'Sierra Vista',
        'tucson':'Tucson',
        'yuma':'Yuma'
        }
        
    arkansas = {'fayar':'Fayetteville',
        'fortsmith':'Fort Smith',
        'jonesboro':'Jonesboro',
        'littlerock':'Little Rock',
        'memphis':'Memphis, TN',
        'texarkana':'Texarkana'}

    california = {'bakersfield':'Bakersfield',
        'chico':'Chico',
        'fresno':'Fresno & Madera',
        'goldcountry':'Gold Country',
        'hanford':'Hanford-Corcoran',
        'humboldt':'Humboldt County',
        'imperial':'Imperial County',
        'inlandempire': 'Inland Empire',
        'losangeles':'Los Angeles',
        'mendocino':'Mendocino County',
        'merced':'Merced',
        'modesto':'Modesto',
        'monterey':'Monterey',
        'orangecounty':'Orange County',
        'palmsprings':'Palm Springs',
        'redding':'Redding',
        'reno':'Reno & Tahoe',
        'sacramento':'Sacramento',
        'sandiego':'San Diego',
        'slo':'San Luis Obispo',
        'santabarbara':'Santa Barbara',
        'santamaria':'Santa Maria',
        'sfbay':'SF Bay Area',
        'siskiyou':'Siskiyou County',
        'stockton':'Stockton',
        'susanville':'Susanville',
        'ventura':'Ventura County',
        'visalia':'Visalia-Tulare',
        'yubasutter':'Yuba-Sutter',
        'focus_dist':{'sfbay': ['eby',#east bay
                'nby',#north bay
                'sby',#south bay
                'pen',#peninsula
                'sfc',#san francisco county
                'scz'],#santa cruz
                'losangeles': ['wst',
                'sfv',
                'lac',
                'sgv',
                'lgb',
                'ant'],
                'sandiego': ['csd',
                'nsd',
                'esd',
                'ssd']}
        } 

    colorado = {'boulder':'Boulder',
        'cosprings':'Colorado Springs',
        'denver':'Denver',
        'eastco':'Eastern CO',
        'fortcollins':'Fort Collins-North CO',
        'pueblo':'Pueblo',
        'rockies':'High Rockies',
        'westslope':'Western Slope'
        }

    connecticut = {'hartford':'Hartford',
        'newhaven':'New Haven',
        'newlondon':'Eastern CT',
        'newyork':'Fairfield County',
        'nwct':'Northwest CT',
        'focus_dist':{'newyork':['fct']}}

    delaware = {'delaware':'Delaware'}

    district_of_columbia = {'washingtondc':'Washington DC'}

    florida = {'cfl':'Heartland Florida',
        'daytona':'Daytona Beach',
        'fortmyers':'Ft. Myers-SW Florida',
        'gadsden':'Gadsden',
        'gainesville':'Gainesville',
        'jacksonville':'Jacksonville',
        'keys':' Florida Keys',
        'lakecity':'North Central Florida',
        'lakeland':'Lakeland',
        'miami':'South Florida',
        'ocala':'Ocala',
        'okaloosa':'Okaloosa-Walton',
        'orlando':'Orlando',
        'panamacity':'Panama City',
        'pensacola':'Pensacola',
        'sarasota':'Sarasota-Bradenton',
        'spacecoast':'Space Coast',
        'staugustine':'St. Augustine',
        'tallahassee':'Tallahassee',
        'tampa':'Tampa Bay Area',
        'treasure':'Treasure Coast',
        'focus_dist':{'miami': ['mdc',
            'brw',
            'pbc'],
            'tampa':['hdo',
            'hil',
            'psc',
            'pnl'],
            'fortmyers':['lee',
            'chl',
            'col']
        }
    }

    georgia = {'albanyga':'Albany',
        'athensga':'Athens',
        'atlanta':'Atlanta',
        'augusta':'Augusta',
        'brunswick':'Brunswick',
        'columbusga':'Columbus',
        'macon':'Macon-Warner Robins',
        'nwga':'Northwest GA',
        'savannah':'Savannah-Hinesville',
        'statesboro':'Statesboro',
        'valdosta':'Valdosta',
        'focus_dist':{'atlanta': ['atl',
            'nat',
            'eat',
            'sat',
            'wat']}
    }

    idaho = {'boise':'Boise',
        'eastidaho':'East Idaho',
        'lewiston':'Lewiston-Clarkston',
        'pullman':'Pullman-Moscow',
        'spokane':"Spokane-Coeur d'Alene",
        'twinfalls':'Twin Falls'}

    illinois =  {'bn':'Bloomington-Normal',
        'carbondale':'Southern Illinois',
        'chambana':'Champaign Urbana',
        'chicago':'Chicago',
        'decatur':'Decatur',
        'lasalle':'Lasalle',
        'mattoon':'Mattoon',
        'peoria':'Peoria',
        'quadcities':'Quad Cities, IA-IL',
        'quincy':'Western IL',
        'rockford':'Rockford',
        'springfieldil':'Springfield',
        'stlouis':'St. Louis MO',
        'focus_dist':{'chicago': ['chc',
            'nch',
            'wcl',
            'sox',
            'nwi',
            'nwc']}           
    }

    indiana = {'bloomington':'Bloomington',
        'chicago':'Chicago',
        'evansville':'Evansville',
        'fortwayne':'Fort Wayne',
        'indianapolis':'Indianapolis',
        'kokomo':'Kokomo',
        'muncie':'Muncie-Anderson',
        'richmondin':'Richmond',
        'southbend':'South Bend-Michiana',
        'terrehaute':'Terre Haute',
        'tippecanoe':'Lafayette-West Lafayette',
        'focus_dist':{'chicago': ['nwi']}
    }

    iowa = {'ames':'Ames',
        'cedarrapids':'Cedar Rapids',
        'desmoines':'Des Moines',
        'dubuque':'Dubuque',
        'fortdodge':'Fort Dodge',
        'iowacity':'Iowa City',
        'masoncity':'Mason City',
        'omaha':'Omaha-Council Bluffs',
        'ottumwa':'Southeast IA',
        'quadcities':'Quadcities, IA-IL',
        'siouxcity':'Sioux City',
        'waterloo':'Waterloo-Cedar Falls',
    }

    kansas = {'kansascity':'Kansas City, MO',
        'ksu':'Manhattan',
        'lawrence':'Lawrence',
        'nwks':'Northwest KS',
        'salina':'Salina',
        'seks':'Southeast KS',
        'swks':'Southwest KS',
        'topeka':'Topeka',
        'wichita':'Wichita'
    }

    kentucky = {'bgky':'Bowiling Green',
        'cincinnati':'Cincinnati, OH',
        'eastky':'Eastern Kentucky',
        'huntington':'Huntington-Ashland',
        'lexington':'Lexington',
        'louisville':'Louisville',
        'owensboro':'Owensboro',
        'westky':'Western Kentucky'}

    louisiana = {'batonrouge':'Baton Rouge',
        'cenla':'Central Louisiana',
        'houma':'Houma',
        'lafayette':'Lafayette',
        'lakecharles':'Lake Charles',
        'monroe':'Monroe',
        'neworleans':'New Orleans',
        'shreveport':'Shreveport'
    }

    maine = {'maine':'Maine'}

    maryland = {'annapolis':'Annapolis',
        'baltimore':'Baltimore',
        'chambersburg':'Cumberland Valley',
        'easternshore':'Eastern Shore',
        'frederick':'Frederick',
        'smd':'South Maryland',
        'washingtondc':'MD suburbs of DC',
        'westmd':'Western Maryland'}

    massachusetts = {'boston':'Boston',
        'capecod':'Cape Cod-Islands',
        'southcoast':'South Coast',
        'westernmass':'Western Massachusetts',
        'worcester':'Worcester-Central MA',
        'focus_dist':{'boston': ['gbs',
            'nwb',
            'bmw',
            'nos',
            'sob']}
    }

    michigan = {'annarbor':'Ann Arbor',
        'battlecreek':'Battle Creek',
        'centralmich':'Central Michigan',
        'detroit':'Detroit Metro',
        'flint':'Flint',
        'grandrapids':'Grand Rapids',
        'holland':'Holland',
        'jxn':'Jackson',
        'kalamazoo':'Kalamazoo',
        'lansing':'Lansing',
        'monroemi':'Monroe',
        'muskegon':'Muskegon',
        'nmi':'North Michigan',
        'porthuron':'Port Huron',
        'saginaw':'Saginaw-Midland-Baycity',
        'swmi':'Soutwest Michigan',
        'thumb':'The Thumb',
        'up':'Upper Peninsula',
        'focus_dist':{'detroit': ['mcb',
            'wyn',
            'okl']}
    }

    minnesota = {'bemidji':'Bemidji',
        'brainerd':'Brainerd',
        'duluth':'Duluth-Superior',
        'fargo':'Fargo-Moorhead',
        'mankato':'Mankato',
        'marshall':'Southwest MN',
        'minneapolis':'Minneapolis-St. Paul',
        'rmn':'Rochester',
        'stcloud':'St. Cloud',
        'focus_dist':{'minneapolis': ['hnp',
            'ram',
            'ank',
            'wsh',
            'dak',
            'csw']}
    }

    mississippi = {'gulfport':'Gulfport-Biloxi',
        'hattiesburg':'Hattiesburg',
        'jackson':'Jackson',
        'memphis':'Memphis, TN',
        'meridian':'Meridian',
        'natchez':'Southwest MS',
        'northmiss':'North Mississippi'}

    missouri = {'columbiamo':'Columbia-Jeff City',
        'joplin':'Joplin',
        'kansascity':'Kansas City',
        'kirksville':'Kirksville',
        'loz':'Lake of the Ozarks',
        'semo':'Southeast Missouri',
        'springfield':'Springfield',
        'stjoseph':'St. Joseph',
        'stlouis':'St. Louis'}

    montana = {'billings':'Billings',
        'bozeman':'Bozeman',
        'butte':'Butte',
        'greatfalls':'Great Falls',
        'helena':'Helena',
        'kalispell':'Kalispell',
        'missoula':'Missoula',
        'montana':'Eastern Montana'}

    nebraska = {'grandisland':'Grand Island',
        'lincoln':'Lincoln',
        'northplatte':'North Platte',
        'omaha':'Omaha-Council Bluffs',
        'scottsbluff':'Scottsbluff-Panhandle',
        'siouxcity':'Sioux City, IA'}

    nevada = {'elko':'Elko',
        'lasvegas':'Las Vegas',
        'reno':'Reno-Tahoe'}

    new_hampshire = {'nh':'Nh'}

    new_jersey = {'cnj':'Central New Jersey',
        'jerseyshore':'Jersey Shore',
        'newjersey':'North Jersey',
        'southjersey':'South Jersey',
        'newyork':'New Jersey',
        'focus_dist':{'newyork': ['jsy']}
    }

    new_mexico = {'albuquerque':'Albuquerque',
        'clovis':'Clovis-Portales',
        'farmington':'Farmington',
        'lascruces':'Las Cruces',
        'roswell':'Roswell-Carlsbad',
        'santafe':'Santa Fe-Taos'}

    new_york = {'albany':'Albany',
        'binghamton':'Binghamton',
        'buffalo':'Buffalo',
        'catskills':'Catskills',
        'chautauqua':'Chautauqua',
        'elmira':'Elmira-Corning',
        'fingerlakes':'Finger Lakes',
        'glensfalls':'Glens Falls',
        'hudsonvalley':'Hudson Valley',
        'ithaca':'Ithaca',
        'longisland':'Long Island',
        'newyork':'New York City',
        'oneonta':'Oneonta',
        'plattsburgh':'Plattsburgh-Adirondacks',
        'potsdam':'Potsdam-Canton-Massena',
        'rochester':'Rochester',
        'syracuse':'Syracuse',
        'twintiers':'Twin Tiers NY-PA',
        'utica':'Utica-Rome-Oneida',
        'watertown':'Watertown',
        'focus_dist':{'newyork': ['mnh',
            'brk',
            'que',
            'brx',
            'stn',
            'jsy',
            'lgi',
            'wch',
            'fct']}
    }

    north_carolina = {'asheville':'Asheville',
        'boone':'Boone',
        'charlotte':'Charlotte',
        'eastnc':'Eastern NC',
        'fayetteville':'Fayetteville',
        'greensboro':'Greensboro',
        'hickory':'Hickory-Lenoir',
        'onslow':'Jacksonville',
        'outerbanks':'Outer Banks',
        'raleigh':'Raleigh-Durham-CH',
        'wilmington':'Wilmington',
        'winstonsalem':'Winston-Salem'}

    north_dakota = {'bismarck':'Bismarck',
        'fargo':'Fargo-Moorhead',
        'minneapolis':'Minneapolis',
        'grandforks':'Grand Forks',
        'nd':'North Dakota'}

    ohio = {'akroncanton':'Akron-Canton',
        'ashtabula':'Ashtabula',
        'athensohio':'Athens',
        'chillicothe':'Chillicothe',
        'cincinnati':'Cincinnati',
        'cleveland':'Cleveland',
        'columbus':'Columbus',
        'dayton':'Dayton-Springfield',
        'huntington':'Huntington-Ashland',
        'limaohio':'Lima-Findlay',
        'mansfield':'Mansfield',
        'parkersburg':'Parkersburg-Marietta',
        'sandusky':'Sandusky',
        'toledo':'Toledo',
        'tuscarawas':'Tuscarawas CO',
        'wheeling':'Northern Panhandle',
        'youngstown':'Youngstown',
        'zanesville':'Zanesville-Cambridge'}

    oklahoma = {'fortsmith':'Fort Smith, AR',
        'lawton':'Lawton',
        'nwks':'Northwest OK',
        'oklahomacity':'Oklahoma City',
        'stillwater':'Stillwater',
        'texoma':'Texoma',
        'tulsa':'Tulsa'}

    oregon = {'bend':'Bend',
        'corvallis':'Corvallis-Albany',
        'eastoregon':'East Oregon',
        'eugene':'Eugene',
        'klamath':'Klamath Falls',
        'medford':'Medford-Ashland',
        'oregoncoast':'Oregon Coast',
        'portland':'Portland',
        'roseburg':'Roseburg',
        'salem':'Salem',
        'focus_dist':{'portland': ['mlt',#multnomah county
                'wsc',#washington county
                'clk',#clark-cowlitz washington
                'clc',#clackamas county
                'nco',#north coast
                'yam',#yamhill co,
                'grg']}#columbia gorge
            }

    pennsylvania = {'allentown':'Allentown-Johnstown',
        'altoona':'Altoona',
        'chambersburg':'Cumberland Valley',
        'erie':'Erie',
        'harrisburg':'Harrisburg',
        'lancaster':'Lancaster',
        'meadville':'Meadville',
        'pennstate':'State College',
        'philadelphia':'Philadelphia',
        'pittsburgh':'Pittsburgh',
        'poconos':'Poconos',
        'reading':'Reading',
        'scranton':'Scranton-Wilkes-barre',
        'twintiers':'Twin Tiers NY-PA',
        'williamsport':'Williamsport',
        'york':'York'}

    rhode_island = {'providence':'Rhode Island'}

    south_carolina = {'charleston':'Charleston',
        'columbia':'Columbia',
        'florencesc':'Florence',
        'greenville':'Greenville-Upstate',
        'hiltonhead':'Hilton Head',
        'myrtlebeach':'Myrtle Beach'}

    south_dakota = {'nesd':'Northeast SD',
        'csd':'Pierre-Central SD',
        'nd':'North Dakota',
        'rapidcity':'Rapidcity',
        'siouxfalls':'Sioux Falls-SE SD',
        'sd':'South Dakota'}

    tennessee = {'chattanooga':'Chattanooga',
        'clarksville':'Clarksville',
        'cookeville':'Cookeville',
        'jacksontn':'Jackson',
        'knoxville':'Knoxville',
        'memphis':'Memphis',
        'nashville':'Nashville',
        'tricities':'Tricities'}

    texas = {'abilene':'Abilene',
        'amarillo':'Amarillo',
        'austin':'Austin',
        'beaumont':'Beaumont-Port Arthur',
        'bigbend':'Southwest TX',
        'brownsville':'Brownsville',
        'collegestation':'College Station',
        'corpuschristi':'Corpus Christi',
        'dallas':'Dallas-Fort Worth',
        'delrio':'Del Rio-Eagle Pass',
        'easttexas':'Tyler-East Texas',
        'elpaso':'El Paso',
        'galveston':'Galveston',
        'houston':'Houston',
        'killeen':'Killeen-Temple-Ft. Hood',
        'laredo':'Laredo',
        'lubbock':'Lubbock',
        'mcallen':'Mcallen-Edinburg',
        'nacogdoches':'Deep East Texas',
        'odessa':'Odessa-Midland',
        'sanangelo':'San Angelo',
        'sanantonio':'San Antonio',
        'sanmarcos':'San Marcos',
        'texarkana':'Texarkana',
        'texoma':'Texoma',
        'victoriatx':'Victoria',
        'waco':'Waco',
        'wichitafalls':'Wichita Falls',
        'focus_dist':{'dallas': ['dal',
            'ftw',
            'mdf',
            'ndf',
            'sdf']}
        }

    utah = {'logan':'Logan',
        'ogden':'Ogden-Clearfield',
        'provo':'Provo-Orem',
        'saltlakecity':'Salt Lake City',
        'stgeorge':'St. George'}

    vermont = {'vermont':'Vermont'}

    virginia = {'blacksburg':'New River Valley',
        'charlottesville':'Charlottesville',
        'danville':'Danville',
        'easternshore':'Eastern Shore',
        'fredericksburg':'Fredericksburg',
        'harrisonburg':'Harrisonburg',
        'lynchburg':'Lynchburg',
        'norfolk':'Norfolk-Hampton Roads',
        'richmond':'Richmond',
        'roanoke':'Roanoke',
        'swva':'Southwest VA',
        'washingtondc':'Northern Virginia',
        'winchester':'Winchester'}

    washington = {'bellingham':'Bellingham',
        'kpr':'Kennewick-Pasco-Richland',
        'lewiston':'Lewiston-Clarkston',
        'moseslake':'Moses Lake',
        'olympic':'Olympic Peninsula',
        'pullman':'Pullman-Moscow',
        'seattle':'Seattle-Tacoma',
        'skagit':'Skagit-Island-SJI',
        'spokane':"Spokane-Coeur d'Alene",
        'wenatchee':'Wenatchee',
        'yakima':'Yakima',
        'focus_dist':{'seattle': ['see',
            'est',
            'sno',
            'kit',
            'tac',
            'oly',
            'skc'],
            'portland': ['mlt',
            'wsc',
            'clk',
            'clc',
            'nco',
            'yam',
            'grg']}
        }

    west_virginia = {'charlestonwv':'Charleston',
        'huntington':'Huntington-Ashland',
        'martinsburg':'Eastern Panhandle',
        'morgantown':'Morgantown',
        'parkersburg':'Parkersburg-Marietta',
        'swv':'Southern WV',
        'wheeling':'Northern Panhandle',
        'wv':'West Virginia (Old)'}

    wisconsin = {'appleton':'Appleton-Oshkosh-FDL',
        'duluth':'Duluth-Superior',
        'eauclaire':'Eau Claire',
        'greenbay':'Green Bay',
        'janesville':'Janesville',
        'lacrosse':'La Crosse',
        'madison':'Madison',
        'milwaukee':'Milwaukee',
        'northernwi':'Northern WI',
        'racine':'Kenosha-Racine',
        'sheboygan':'Sheboygan',
        'wausau':'Wausau'}

    wyoming = {'wyoming':'Wyoming'}