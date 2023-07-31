from minhas_classes import Data
from datetime import datetime
# Testando...
hoje = Data(datetime.today().day, datetime.today().month, datetime.today().year)
print(hoje.data_formatada())
