day_time = int (input ('How much time (in minutes) has passed since the beginning of the day? \n'))
minutes = day_time // 60 #// - это целочисленное деление
hours = day_time % 60 # % - остаток от деления
print (f'Time now:{hours:0>2}:{minutes:0>2}')