import twint
from datetime import date
from datetime import timedelta
#TODO Should look into twitter-scrapper also.

# c = twint.Config()
# c.Search = "#JohnnyDepp"
# #c.Verified = True
# c.Show_hashtags = True
# c.Count = True
# c.Profile_full = True
# c.Lang = "en"
# c.Since = "2022-03-01"
# c.Until = "2022-04-01"
# c.Output = "JohhnyTweets.csv"
# c.Store_csv = True

# twint.run.Search(c)

#"2022-04-01"
def tweetSeach(_since:str, _until:str):
    ''' Searches the related topic between related dates.'''
    c = twint.Config()
    c.Search = "#JohnnyDepp"
    #c.Verified = True
    c.Show_hashtags = True
    c.Count = True
    c.Profile_full = True
    c.Lang = "en"
    c.Since = _since
    c.Until = _until
    c.Output = "data/JohhnyTweets" + _since + ".csv"
    c.Store_csv = True
    twint.run.Search(c)

if __name__ == "__main__":
    for month in range(1,6):#From January to May
        day_number = (date(2022,month+1, 1) - date(2022, month, 1) ).days
        for day in range(1,day_number + 1):
            tweetSeach(date(2022, month, day).strftime("%Y-%m-%d"), (date(2022, month, day) + timedelta(days=1)).strftime("%Y-%m-%d"))

