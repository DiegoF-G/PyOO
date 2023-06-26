from myClasses import Data
from datetime import datetime
d = Data(datetime.today().day, datetime.today().month, datetime.today().year)
print(d.data_formatada())
