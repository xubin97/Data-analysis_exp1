import time
import pandas as pd
import numpy as np
#
CITY_DATA = { 'Chicago': 'D:\\Uda_data\\bikeshare\\chicago.csv',
              'New york city': 'D:\\Uda_data\\bikeshare\\new_york_city.csv',
              'Washington': 'D:\\Uda_data\\bikeshare\\washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    print('Would you like to see data for Chicago,New york city,or Washington?')
    city=input(' You input:').title()
    while city!='Chicago'and city!='New York City'and city!='Washington':
        print('\nError!')
        city=input('input your select again:')
        
    


    # TO DO: get user input for month (all, january, february, ... , june)
    print('Which month? all,january,february,march,april,may,or june?')
    month=input('You input:').title()
    while month!='All' and month!='January' and month!='February' and month!='March' and month!='April' and month!='May' and month!='June':
        print('\nError!')
        month=input('input your select again:')


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print('Which day?Please type your response as an integer(e.g.monday,..,sunday)')
    day=input('You input:').title()
    while day!='All'and day!='Monday' and day!='Tuesday' and day!='Wednesday' and day!='Thursday' and day!='Friday' and day!='Saturday' and day!='Sunday':
        print('\nError!')
        day=input('input your select again:')

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
# load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'All':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df,city,month,day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    common_month=df['month'].value_counts().head(1)
    print("\ncommon month and count:   %s ."%(common_month))
    print("filter:    %s ,%s ,%s"%(city,month,day))

    # TO DO: display the most common day of week
    
    common_day=df['day_of_week'].value_counts().head(1)
    print("\ncommon day and count:   %s"%(common_day))
    print("filter:    %s ,%s ,%s"%(city,month,day))
    
    # TO DO: display the most common start hour
    
    df['hour']=df['Start Time'].dt.hour
    common_hour=df['hour'].value_counts().head(1)
    print("\ncommon hour and cout:   %s"%(common_hour))
    print("filter:    %s ,%s ,%s"%(city,month,day))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df,city,month,day):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station=df['Start Station'].value_counts().head(1)
    print("\ncommon start station and count:   %s"%(common_start_station))
    print("filter:    %s ,%s ,%s"%(city,month,day))

    # TO DO: display most commonly used end station
    common_end_station=df['End Station'].value_counts().head(1)
    print("\ncommon start station and count:   %s"%(common_end_station))
    print("filter:    %s ,%s ,%s"%(city,month,day))


    # TO DO: display most frequent combination of start station and end station trip
    df_group=df['Start Station']+df['End Station']
    frequent_combination=df_group.value_counts().head(1)
    print("\nthe most frequent combination:%s"%(frequent_combination))
    print("filter:    %s ,%s ,%s"%(city,month,day))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df,city,month,day):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    
    total_time=df['Trip Duration'].sum()
    print("\ntotal travel time:%s's"%(total_time))
    print("filter:    %s ,%s ,%s"%(city,month,day))

    # TO DO: display mean travel time
    
    mean_time=df['Trip Duration'].mean()
    print("\nmean travel time:%s's"%(mean_time))
    print("filter:    %s ,%s ,%s"%(city,month,day))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def user_stats(df,city,month,day):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    user_types=df['User Type'].value_counts()
    print("counts of user types:%s"%(user_types))
    print("filter:    %s ,%s ,%s"%(city,month,day))
    # TO DO: Display counts of gender
    
    count_gender=df['Gender'].value_counts()
    print("\n counts of gender:%s"%(count_gender))
    print("filter:    %s ,%s ,%s"%(city,month,day))

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest=df['Birth Year'].min()
    most_recent=df['Birth Year'].max()
    most_commmon=df['Birth Year'].mode()

    print("\nthe earliest year:%s"%(earliest))
    print("the most recent year:%s"%(most_recent))
    print("the most common year:%s"%(most_commmon))
    print("filter:    %s ,%s ,%s"%(city,month,day))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        
        
        time_stats(df,city,month,day)
        station_stats(df,city,month,day)
        trip_duration_stats(df,city,month,day)
        user_stats(df,city,month,day)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()

