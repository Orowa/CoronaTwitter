import GetOldTweets3 as got
import subprocess
import datetime

start_date = datetime.datetime.strptime("2020-03-15", "%Y-%m-%d")
end_date = datetime.datetime.today()
dates_list = [start_date + datetime.timedelta(days=x) for x in range(0, (end_date-start_date).days)]

running_processes = list()
for date in dates_list:
    e_date = date + datetime.timedelta(days=1)
    
    
    
    query_search = 'corona'
    near = "England"
    lang = "en"
    max_tweets = 10000
    
    out_file = f'./tweets/{date.date()}_{query_search}.csv'

    str_to_run = f'GetOldTweets3 --querysearch "{query_search}" --near "{near}" --since {date.date()} --until {e_date.date()} --lang {lang} --output {out_file} --maxtweets {max_tweets}'
    print(str_to_run)
    process = subprocess.Popen(str_to_run, shell=True)
    
    running_processes.append(process)
    
for process in running_processes:
    process.wait()