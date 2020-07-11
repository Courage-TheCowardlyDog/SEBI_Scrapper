from crontab import CronTab
file_cron = CronTab(tabfile='Scheduler.tab')
job = file_cron.new(command='python SEBI_Scrapper.py')
job.minute.on(0)
job.hour.on(21)
job.enable()
file_cron.write()

