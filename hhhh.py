class Person:
    def __init__(self, full_name, age, address, ID_card, position):
        self.full_name = full_name
        self.age = age
        self.address = address
        self.ID_card = ID_card
        self.position = position


class staff(Person):
    def __init__(self, full_name : str, age : int, address : str, ID_card : int, position : str, working_hours : int):
        super().__init__(full_name, age, address, ID_card, position)
        self.working_hours = working_hours

    def cal_bill(self, don_hang : dict):
        menu = {
            "cafe": 15000,
            "cafe_milk": 20000,
            "orange_juice": 30000
        }
        sum = 0
        try:
            for key, value in don_hang.items():
                sum += menu[key] * value
        except Exception as e:
            return 'Errors, Please check your settings'
        return sum

    def carry_drinks(self, drinks):
        return (f"{self.full_name} carry {drinks}")

    def reception_customer(self, quantity : int, drinks : str):
        return (f"Bill: {drinks}, {quantity}")

nhanvien = staff("Hoang1", 25, "123 Trường Chinh", 32467, "Nhanvien", 12)
nhanvien = staff("Hoang2", 36, "123 Bùi Viện", 53774, "Nhanvien", 6)
nhanvien = staff("Hoang3", 27, "123 Âu Cơ", 43798, "Nhanvien",8)


class manager(Person):
    def __init__(self, full_name, age, address, ID_card, position, working_hours):
        super().__init__(full_name, age, address, ID_card, position)
        self.working_hours = working_hours

    def manage_staffs(self, list_staffs : list):
        for staff in list_staffs:
            print(f"Name: {staff.full_name}")


    def cal_staff(self, list_staffs : list ):
        salary = {
            "staff" : 12.000,
            "bartender" : 20.000
        }
        for staff in list_staffs:
            staff.total_salary = salary[staff.position] * staff.working_hours



manager = manager("Hoang1", 25, "123 Trường Chinh", 32467, "quanly", 12)
nhanvien1 = staff("Hoang2", 36, "123 Bùi Viện", 53774, "bartender",15)
nhanvien2 = staff("Hoang3", 27, "123 Âu Cơ", 43798, "nhanvien", 15)
lst = [nhanvien1, nhanvien2]


class bartender(Person):
    def __init__(self, full_name, age, address, ID_card, position, working_hours):
        super().__init__(full_name, age, address, ID_card, position)
        self.working_hours = working_hours



    def prepare_drink(self, drinks):
        for drink in drinks:
            print(f"{drink['name']}:")
            for key, value in drink.items():
                print(f"{key}: {value} ml")

bartender = bartender("Hoang2", 36, "123 Bùi Viện", 53774, "bartender",15)
drinks = [
    {
        "name": "Cafe",
        "sugar": 10,
        "coffee": 50,
        "ice": 20
    },
    {
        "name": "Cafe_milk",
        "sugar": 15,
        "coffee": 40,
        "ice": 15,
        "milk": 30
    },
    {
        "name": "Orange_juice",
        "sugar": 20,
        "ice": 10,
        "orange_count": 4
    }
]
bartender.prepare_drink(drinks)

