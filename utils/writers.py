import csv


def csv_writer(fields: list, data: list, path: str):
    with open(path, 'w') as f:
        write = csv.writer(f)
        write.writerow(fields)
        write.writerows(data)
