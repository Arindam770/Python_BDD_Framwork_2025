import csv

class CSV_Handler:
    def __init__(self, file_path):
        self.file_path = file_path

    def write_csv_dict(self, data):
        all_columns = data[0].keys()
        with open(self.file_path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=all_columns)
            writer.writeheader()
            for row in data:
                writer.writerow(row)

    def read_csv_dict(self):
        listofData = []
        with open(self.file_path, mode='r') as file:
            all_data = csv.reader(file)
            # Get the first row as the header
            all_columns = next(all_data)
            if all_columns:
                for row in all_data:
                    # Skip empty rows
                    is_empty = True
                    for cell in row:
                        if cell.strip() != "":
                            is_empty = False
                            break
                    if is_empty:
                        continue

                    row_dict={}
                    for i in range(len(all_columns)):
                        row_dict[all_columns[i]] = row[i]
                    listofData.append(row_dict)
        return listofData
    
if __name__ == '__main__':
    csv_handler = CSV_Handler('Python_BDD_Framwork\\TestData\\testData_Ecom.csv')
    #print(csv_handler.read_csv_dict())
    data = csv_handler.read_csv_dict()
    print(data)
    #csv_handler.write_csv_dict(data)
    print("-----------------------------------------")
    
