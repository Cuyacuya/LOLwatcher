from riotwatcher import LolWatcher
from datetime import datetime, timedelta
import time

lol_watcher = LolWatcher('RGAPI-4b994acc-8e38-4a43-9372-7a0121615648')

my_region = 'kr'

me = lol_watcher.summoner.by_name(my_region, 'air wings cuya')

spectator = None

while True:
    print('[*] Checking...', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    try:
        spectator = lol_watcher.spectator.by_summoner(my_region, me['id'])

        start_time = datetime.fromtimestamp(spectator['gameStartTime'] / 1000)

        if datetime.now() - start_time < timedelta(minutes=5):
            print('[!]지금 게임을 시작했어요!', start_time.strftime('%Y-%m-%d %H:%M:%S'))
    except:
        pass

    time.sleep(5)
