To automate the data scrapping by setting jobs via Terminal by 'crontab -e'
- Open terminal
- Type 'crontab -e' and i to Insert jobs
- */1 * * * * /usr/local/bin/python location_of_the_py_file #minutes(0-59), hours(0-23), day(1-31), month(1-12), day of week(0-7)
- e.g. */1 * * * * /usr/local/bin/python /Users/username/foldername/jp_yen_rate.py
- After the insert is done, press esc key then type in ':wq' to exit
- To double check if cron job is set up by running 'crontab -l' command
