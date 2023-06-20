import statistics
import pandas


def convert_data(file_name, data_type):
    input_df = pandas.read_excel(io='input_files/' + file_name, header=[0], engine='openpyxl')      # input data frame
    unique_date = input_df['date'].unique()                                                         # unique data
    headers = list(input_df.keys())                                                                 # get columns name

    output_df = pandas.DataFrame(columns=headers)

    for date in unique_date:
        raw_data_df = input_df.loc[input_df['date'] == date]

        raw_date = raw_data_df['date'].iloc[0]
        raw_time = str(raw_data_df['time'].iloc[0]) + ' - ' + str(raw_data_df['time'].iloc[-1])
        raw_time_zone = raw_data_df['time_zone'].iloc[0]

        if data_type == "Temp":
            raw_id = str(raw_data_df['id'].iloc[0]) + ' - ' + str(raw_data_df['id'].iloc[-1])
            raw_avg_t1 = round(statistics.mean(raw_data_df['T1']), 2)
            raw_avg_t2 = round(statistics.mean(raw_data_df['T2']), 2)
            raw_avg_t3 = round(statistics.mean(raw_data_df['T3']), 2)
            raw_avg_average = round(statistics.mean(raw_data_df['Average']), 2)

            output_df = output_df.append({'date': raw_date,
                                          'time': raw_time,
                                          'time_zone': raw_time_zone,
                                          'id': raw_id,
                                          'T1': raw_avg_t1,
                                          'T2': raw_avg_t2,
                                          'T3': raw_avg_t3,
                                          'Average': raw_avg_average}, ignore_index=True)
        elif data_type == "BMP":
            raw_id = str(raw_data_df['id'].iloc[0]) + ' - ' + str(raw_data_df['id'].iloc[-1])
            raw_avg_t = round(statistics.mean(raw_data_df['T']), 2)
            raw_avg_h = round(statistics.mean(raw_data_df['H']), 2)
            raw_avg_p = round(statistics.mean(raw_data_df['P']), 2)

            output_df = output_df.append({'date': raw_date,
                                          'time': raw_time,
                                          'time_zone': raw_time_zone,
                                          'id': raw_id,
                                          'T': raw_avg_t,
                                          'H': raw_avg_h,
                                          'P': raw_avg_p}, ignore_index=True)
        elif data_type == "Soil":
            raw_latitude = round(statistics.mean(raw_data_df['latitude']), 2)
            output_df = output_df.append({'date': raw_date,
                                          'time': raw_time,
                                          'time_zone': raw_time_zone,
                                          'latitude': raw_latitude}, ignore_index=True)
        else:
            print(f'Wrong data type!')

    output_df.to_excel('output_files/output_' + file_name)


convert_data(file_name='Soil.xlsx', data_type='Soil')
