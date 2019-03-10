## TODO: import all necessary packages and functions


## Filenames
chicago = 'chicago.csv'
new_york_city = 'new_york_city.csv'
washington = 'washington.csv'


def get_city():
    '''Asks the user for a city and returns the filename for that city's bike share data.
    Args:
        none.
    Returns:
        (str) Filename for a city's bikeshare data.
    '''
    city_set = ["chicago", "new york city", "washington"]
    while true:
      city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                   'Would you like to see data for Chicago, New York, or Washington?\n').lower()
 	  if city_input in city_set:
      	break
      else:
        print("Please enter a valid name from the three city choices.")
        
        
	if city == "chicago":
      filename = "chicago.csv"
  	elif city == "new york city":
      filename = "new_york_city.csv"
    elif city == "washington":
      filename = "washington.csv"
      
    return filename
      
def get_time_period():
    '''Asks the user for a time period and returns the specified filter.
    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
  months = ['january', 'february', 'march', 'april', 'may', 'june', all]
  days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'] 
  
  while true:
      month = input("\n\n\nPlease input a month to investigate January through June. Input all, if you wish to include all months").lower()
 		if month in months:
          break
        else:
          Print("Please input a correct month, or all.")
  while true:
      day_input = input("\n\n\nPlease input a day of the week to investigate, Monday through Sunday. Input all if you do not \
      wish to filter by day.").lower()
      
      	if day in days:
          break
        elif:
          Print("Please input a correct day, or all.")





