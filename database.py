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

    # lists for column_name, types of attributes,feilds for entry values and valid for validation results
    types_of_attributes = []
    feilds = []
    full_dictionary = {}
    n = int(0)

    # constructor of class in which format of table is store in database
    def __init__(self, Dict):
        """
        this method is constructor for Database class,
        in this method we fetch the keys of dictionary and write them into file as a first row and store
            them into one list and fetch the values of dictionary and store them into a list
        :param Dict: Dictionary in which keys are column-name and values are their datatypes respectively
        """
        try:
            self.n = len(Dict)
            # with open("database.json", "w") as fp:
            #     json.dump(Dict, fp)
            self.types_of_attributes = list(Dict.values())
        except:
            print('Something Went Wrong..!!')

    # function for validate all the values and store in database

    def validation(self, Dict):
        """
        this method validate the all value for its datatypes and store the true false vale in valid named list
        :param Dict: Dictionary in which keys are column-name and values are entries(values) respectively
        :return: return nothing and validation results stored the valid named list
        """
        self.feilds = list(Dict.values())
        # print(self.feilds)
        if len(Dict) == self.n:
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

    def insert(self, Dict):
        """
        this method insert the entry to the database
        if all constraints are satisfies then entry is stored in database file otherwise throw the exception
        :param Dict: Dictionary in which keys are column-name and values are entries(values) respectively
        :return: this is method not return true or false, in this method all constraints are satiesfies then
        entry stored in database otherwise raise exception
        """
        try:
            if self.validation(Dict):
                print(Dict)
                # self.full_dictionary[len(self.full_dictionary) + 1] = Dict
                # print(self.full_dictionary)
                # print(json_object)
                with open('database.json', 'w') as fp:
                    json.dump(Dict, fp)
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
        print("\nFile's Full Content")
        with open('database.json', 'r') as fp:
            json_obj = json.load(fp)
        return json_obj

    def get_one(self):
        """
        this method give the first data entry of the database json file
        :return: json object which have first data entry of the database
        """
        a = self
        print("\nFile's One Content")
        with open('database.json', 'r') as fp:
            json_obj = json.load(fp)

        return json_obj


# main function
if __name__ == '__main__':
    dict = {'id': 'int', 'name': 'string', 'date': 'date', 'time': 'time'}
    d = Database(dict)
    dict1 = {'id': '1', 'name': 'chirag', 'date': '02/07/2001', 'time': '13:45'}
    d.insert(dict1)
    # dict2 = {"id": "2", "name": "abcd", "date": "02/04/2011", "time": "15:12"}
    # d.insert(dict2)
    # dict3 = {"id": "3", "name": "hello", "date": "05/04/2011", "time": "18:12"}
    # d.insert(dict3)
    print(d.get_all())
    print(d.get_one())
