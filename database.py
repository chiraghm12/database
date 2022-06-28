import json


def isfloat(num):
    """
    this method checks the vlue is float or not
    and its returns true if value is float otherwise returns false
    :param num: value for which we want to check it is float or not.
    :return: true or false
    """
    try:
        float(num)
        return True
    except ValueError:
        return False


def is_valid_string(st):
    """
    this method checks the given value is string or not
    this method returns true if value is valid string otherwise returns false
    :param st: value for which we want to check it is valid string or not
    :return: true or false
    """
    try:
        float(st)
        return False
    except ValueError:
        return True


def is_date(st):
    """
    this method checks the given value is valid for date or not, checks all constraints for date
    and returns true if value os valid date otherwise return s false
    :param st: vale for which e=we want to check it is valid date or not
    :return: true or false
    """
    # dd/mm/yyyy
    # slicing the date string into parts DD, MM, YY
    dd = st[0:2]
    mm = st[3:5]
    yy = st[6:]

    # check for numeric values
    if dd.isdigit() and mm.isdigit() and yy.isdigit():
        dd = int(dd)
        mm = int(mm)
        yy = int(yy)

        # check date range and month range
        if 1800 <= yy < 2022:
            if 12 >= mm > 0:
                if mm in [1, 3, 5, 7, 8, 10, 12]:
                    if 0 < dd <= 31:
                        return True
                    else:
                        return False
                else:
                    if 0 < dd <= 30:
                        return True
                    else:
                        return False
            else:
                return False
        else:
            return False
    else:
        return False


def is_time(st):
    """
    this method checks given value or string is valid time or not, checks all constraints for valid time
    this method returns true if given value is valid time otherwise returns false
    :param st: value for which we want to check it is valid time or not
    :return: true or false
    """
    # slicing the time string for hour and minuted
    hh = st[:2]
    mm = st[3:]

    # check values is numeric or not
    try:
        hh = int(hh)
        mm = int(mm)
    except ValueError:
        return False

    # validating the range of hour and minute
    if 24 > hh >= 0:
        if 60 > mm >= 0:
            return True
        else:
            return False
    else:
        return False


# class database
class Database:
    """
    class for database, insert the entry to json file or read from json file
    in this class aa functions are handled
    """

    # constructor of class in which format of table is store in database
    def __init__(self, data):
        """
        this method is constructor for Database class,
        in this method we fetch the keys of dictionary and write them into file as a first row and store
            them into one list and fetch the values of dictionary and store them into a list
        :param data: Dictionary in which keys are column-name and values are their datatypes respectively
        """
        # lists for column_name, types of attributes,feilds for entry values and valid for validation results
        self.types_of_attributes = []
        self.feilds = []
        self.full_dictionary = {}
        self.n = int(0)
        self.serial_no = int(0)
        try:
            self.n = len(data)
            # with open("database.json", "w") as fp:
            #     json.dump(Dict, fp)
            self.types_of_attributes = list(data.values())
        except:
            print('Something Went Wrong..!!')

    # function for validate all the values and store in database

    def validation(self, data):
        """
        this method validate the all value for its datatypes and store the true false vale in valid named list
        :param data: Dictionary in which keys are column-name and values are entries(values) respectively
        :return: return nothing and validation results stored the valid named list
        """
        self.feilds = list(data.values())
        # print(self.feilds)
        if len(data) == self.n:
            for i in range(self.n):
                if self.types_of_attributes[i] == 'int':
                    if not self.feilds[i].isnumeric():
                        return False
                elif self.types_of_attributes[i] == 'float':
                    if not isfloat(self.feilds[i]):
                        return False
                elif self.types_of_attributes[i] == 'string':
                    if not is_valid_string(self.feilds[i]):
                        return False
                elif self.types_of_attributes[i] == 'date':
                    if not is_date(self.feilds[i]):
                        return False
                elif self.types_of_attributes[i] == 'time':
                    if not is_time(self.feilds[i]):
                        return False
            return True
        else:
            return False

    def insert(self, data):
        """
        this method insert the entry to the database
        if all constraints are satisfies then entry is stored in database file otherwise throw the exception
        :param data: Dictionary in which keys are column-name and values are entries(values) respectively
        :return: this is method not return true or false, in this method all constraints are satiesfies then
        entry stored in database otherwise raise exception
        """
        try:
            if self.validation(data):
                print(data)
                if self.serial_no == 0:
                    all_data = {self.serial_no + 1: data}
                else:
                    all_data = self.get_all()
                    print('all Data LEn : ',len(all_data))
                    all_data[self.serial_no+1] = data
                # self.full_dictionary[len(self.full_dictionary) + 1] = Dict
                # print(self.full_dictionary)
                # print(json_object)
                with open('database.json', 'w') as fp:
                    json.dump(all_data, fp)
                self.serial_no = self.serial_no + 1
        except:
            print('Something Went Wrong...!!')
        else:
            print('Stored Successfully..!!')

    def get_all(self):
        """
        this method give all data of the database json file
        :return: return json object which have all data of the jason file
        """
        a = self
        with open('database.json', 'r') as fp:
            json_obj = json.load(fp)
        return json_obj

    def get_one(self):
        """
        this method give the first data entry of the database json file
        :return: json object which have first data entry of the database
        """
        a = self
        with open('database.json', 'r') as fp:
            json_obj = json.load(fp)
        return json_obj


# main function
if __name__ == '__main__':
    index = {'id': 'int', 'name': 'string', 'date': 'date', 'time': 'time'}
    d = Database(index)
    data1 = {'id': '1', 'name': 'chirag', 'date': '02/07/2001', 'time': '13:45'}
    d.insert(data1)
    data2 = {'id': '2', 'name': 'rohan', 'date': '04/05/2003', 'time': '16:24'}
    d.insert(data2)

    print("\nFile's Full Content")
    print(d.get_all())
    print("\nFile's One Content")
    one_entry = d.get_one()
    print(one_entry['1'])
