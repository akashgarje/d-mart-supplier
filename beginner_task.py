import json
import pandas as pd


class CsvToJson:
    data_file = r'data.csv'

    def main(self, csv_file):

        data = pd.read_csv(csv_file)
        data = data.dropna()
        # print(data.head())
        final_data = []

        """ Base URL """
        data_df = data.groupby(["Base URL"])
        # df_dct = {}
        for name, group in data_df:
            dct = {}
            dct['Base URL'] = name
            dct['children'] = group
            final_data.append(dct)

        """ Level 1 """
        df2 = final_data[0]['children'].groupby(['Level 1 - Name', 'Level 1 - ID', 'Level 1 - URL'])
        final_data[0]['children'] = []
        for name, group in df2:
            dct1 = {
                'Level 1 - ID': name[1],
                'Level 1 - Name': name[0],
                'Level 1 URL': name[2],
                'children': group
            }
            final_data[0]['children'].append(dct1)

        """ Level 2 """
        df3 = final_data[0]['children'][0]['children'].groupby(['Level 2 - Name', 'Level 2 - ID', 'Level 2 URL'])
        final_data[0]['children'][0]['children'] = []
        for name, group in df3:
            # print(name)
            # print(group)
            dct2 = {
                'Level 2 - ID': name[1],
                'Level 2 - Name': name[0],
                'Level 2 URL': name[2],
                'children': group
            }
            final_data[0]['children'][0]['children'].append(dct2)

        """ Level 3 """
        for temp_df in final_data[0]['children'][0]['children']:
            df4 = temp_df['children'].groupby(['Level 3 - Name', 'Level 3 - ID', 'Level 3 URL'])
            temp_df['children'] = []
            for name, group in df4:
                dct3 = {
                    'Level 3 - ID': name[1],
                    'Level 3 - Name': name[0],
                    'Level 3 URL': name[2]
                }
                temp_df['children'].append(dct3)

        # print(json.dumps(final_data, indent=2))

        f = open("output.json", "w")
        f.write(json.dumps(final_data, indent=2))
        f.close()


if __name__ == '__main__':
    csvtojson = CsvToJson()
    csvtojson.main(csv_file=csvtojson.data_file)

