import csv
from datetime import datetime
from time import sleep

with open('rows_300.csv', mode='w', encoding='utf-8') as file:
    file_writer = csv.writer(file, delimiter = ' ', lineterminator = '\r')
    file_writer.writerow(['№', "Секунда", "Микросекунда"])
    for i in range(300):
        file_writer.writerow([i+1, datetime.now().second, datetime.now().microsecond])
        sleep(0.01)