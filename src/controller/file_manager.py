from typing import List
import csv


class FileManager:
    @staticmethod
    def get_csv_to_list() -> List[dict]:
        years = [2020, 2021]
        list_from_csv = []
        for year in years:
            with open(f'data_files/extratos/extrato_{year}.csv', encoding='utf8') as file:
                list_from_csv.extend(csv.DictReader(file))
        return list_from_csv

    @staticmethod
    def get_brokerage_balance() -> float:
        with open('data_files/balance.txt') as file:
            return float(file.read())
