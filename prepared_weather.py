from functools import reduce
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
import time


def weather_exctract(input_file, output_file, header: bool = False, verbose: bool = False,
                     start_time: datetime = None, duration: int = None, columns: list = None):
    '''
    This function exctract the air_temp, humidity, leaf, leaf_dry, leaf_wet columns from the weather_data.csv
    :param input_file: Which weather data file has to exctract the column
    :param output_file: Out put file name
    :param header: Header of the extract data set
    :param verbose:
    :param start_time: start time of the data set
    :param duration: Time gap
    :param columns:air_temp, humidity, leaf, leaf_dry, leaf_wet
    :return:
    '''
    with output_file as output:
        if header:
            output_file.write("AirTemp,Humidity,Leaf,LeafDry,LeafWet\n")
        with input_file as f:
            data = f.readlines()

            for i, line in enumerate(data):
                if i < 7:
                    continue
                line = line.strip()
                data = line.split(",")

                air_temp, humidity, leaf, leaf_dry, leaf_wet, = data[2], data[4], data[11], data[12], data[13]

                if start_time is not None and duration is None:
                    data_time = datetime.strptime(data[1], "%H:%M:%S")
                    start = datetime.strptime(start_time, "%H:%M:%S")

                    if data_time >= start:
                        for column in columns:
                            if column == 'air_temp':
                                col = data[2]
                            if column == 'humidity':
                                col = data[4]
                            if column == 'leaf':
                                col = data[11]
                            if column == 'leaf_dry':
                                col = data[12]
                            if column == 'leaf_wet':
                                col = data[13]
                            output_line = f"{col}"
                            output_file.write(output_line)
                            print(output_line, end="")
                            if column != columns[len(columns) - 1]:
                                output_line = f","
                                print(output_line, end="")
                                output_file.write(output_line)
                        output_line = f"\n"
                        output_file.write(output_line)
                        print()
                elif start_time is not None and duration is not None:
                    data_time = datetime.strptime(data[1], "%H:%M:%S")
                    start = datetime.strptime(start_time, "%H:%M:%S")
                    end = start + timedelta(seconds=duration)
                    if start <= data_time <= end:
                        for column in columns:
                            if column == 'air_temp':
                                col = data[2]
                            if column == 'humidity':
                                col = data[4]
                            if column == 'leaf':
                                col = data[11]
                            if column == 'leaf_dry':
                                col = data[12]
                            if column == 'leaf_wet':
                                col = data[13]
                            output_line = f"{col}"
                            output_file.write(output_line)
                            print(output_line, end="")
                            if column != columns[len(columns) - 1]:
                                output_line = f","
                                print(output_line, end="")
                                output_file.write(output_line)
                        output_line = f"\n"
                        output_file.write(output_line)
                        print()

                elif start_time == None and duration == None:

                    for column in columns:
                        if column == 'air_temp':
                            col = data[2]
                        if column == 'humidity':
                            col = data[4]
                        if column == 'leaf':
                            col = data[11]
                        if column == 'leaf_dry':
                            col = data[12]
                        if column == 'leaf_wet':
                            col = data[13]
                        output_line = f"{col}"
                        output_file.write(output_line)
                        print(output_line, end="")
                        if column != columns[len(columns) - 1]:
                            output_line = f","
                            print(output_line, end="")
                            output_file.write(output_line)
                    output_line = f"\n"
                    output_file.write(output_line)
                    print()
            output_file.close()
    return output_file

if __name__ == "__main__":
    print("This is a test of weather_data.csv module !")
