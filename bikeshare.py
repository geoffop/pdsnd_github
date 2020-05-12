import time
import pandas as pd

CITY_DATA = {
    "chicago": "chicago.csv",
    "new york city": "new_york_city.csv",
    "washington": "washington.csv",
}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    city = ""
    month = ""
    day = ""
    print("Hello! Let's explore some US bikeshare data!")
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while city not in ["chicago", "new york city", "washington"]:
        print(
            "enter city you would like to look at (",
            "chicago",
            "new york city",
            "washington",
            ")",
        )
        city = input().lower()
    # TO DO: get user input for month (all, january, february, ... , june)
    while month not in ["all", "january", "february", "march", "april", "may", "june"]:
        print(
            "Enter month you would like to look at (",
            "all",
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            ")",
        )
        month = input().lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while day not in [
        "all",
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "Friday",
        "saturday",
        "sunday",
    ]:
        print(
            "enter day of the week you would like to look at (",
            "all",
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
            ")",
        )
        day = input().lower()

    print("-" * 40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    if city == "chicago":
        df = pd.read_csv("chicago.csv")
        if month != "all":
            df = df[
                pd.to_datetime(df["Start Time"]).dt.month_name() == month.capitalize()
            ]
        if day != "all":
            df = df[pd.to_datetime(df["Start Time"]).dt.day_name() == day.capitalize()]
    elif city == "washington":
        df = pd.read_csv("washington.csv")
        if month != "all":
            df = df[
                pd.to_datetime(df["Start Time"]).dt.month_name() == month.capitalize()
            ]
        if day != "all":
            df = df[pd.to_datetime(df["Start Time"]).dt.day_name() == day.capitalize()]
    else:
        df = pd.read_csv("new_york_city.csv")
        if month != "all":
            df = df[
                pd.to_datetime(df["Start Time"]).dt.month_name() == month.capitalize()
            ]
        if day != "all":
            df = df[pd.to_datetime(df["Start Time"]).dt.day_name() == day.capitalize()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print("\nCalculating The Most Frequent Times of Travel...\n")
    start_time = time.time()

    # TO DO: display the most common month
    print("most common month")
    print(pd.to_datetime(df["Start Time"]).dt.month_name().mode())

    # TO DO: display the most common day of week
    print("most common day of week")
    print(pd.to_datetime(df["Start Time"]).dt.day_name().mode())

    # TO DO: display the most common start hour
    print("most common start hour")
    print(pd.to_datetime(df["Start Time"]).dt.hour.mode())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print("\nCalculating The Most Popular Stations and Trip...\n")
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("most commonly used start station")
    print(df["Start Station"].mode())

    # TO DO: display most commonly used end station
    print("most commonly used end station")
    print(df["End Station"].mode())

    # TO DO: display most frequent combination of start station and end station trip
    print("most frequent combination of start station and end station trip")
    print(df[["Start Station", "End Station"]].mode())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print("\nCalculating Trip Duration...\n")
    start_time = time.time()

    # TO DO: display total travel time
    print("total travel time")
    print(df["Trip Duration"].sum())

    # TO DO: display mean travel time
    print("mean travel time")
    print(df["Trip Duration"].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print("\nCalculating User Stats...\n")
    start_time = time.time()

    # TO DO: Display counts of user types
    print("counts of user types")
    print(df["User Type"].value_counts())

    # TO DO: Display counts of gender
    print("counts of gender")
    print(df["Gender"].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    print("earliest year of birth")
    print(df["Birth Year"].min())
    print("most recent year of birth")
    print(df["Birth Year"].max())
    print("most common year of birth")
    print(df["Birth Year"].mode())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        if city in ["chicago", "new york city"]:
            user_stats(df)
        print("Would you like to see the raw data 5 rows at a time? (yes/no)")
        raw = input().lower()
        s = 0
        f = 5
        while raw == "yes":
            print(df[s:f])
            print("more? (yes/no)")
            if input().lower() == "yes":
                raw = "yes"
                s = s + 5
                f = s + 5
            else:
                raw = "no"
        restart = input("\nWould you like to restart? Enter yes or no.\n")
        if restart.lower() != "yes":
            break


if __name__ == "__main__":

    main()
