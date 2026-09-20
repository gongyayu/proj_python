from py_mod import line_print, st_print, st_code

### StartofFunc###


def py_basic():
    def pyvrf():
        line_print(f"pyvrf() {'-' * 30}")

        class vrf:
            def __init__(self):
                self.uid = 100
                self.name = ''
        # create a class object
        vrfObj = vrf()
        vrfObj.uid = 10
        vrfObj.name = 'backup'
        line_print(f"{vars(vrfObj)}")
        line_print(f"vrfObj.uid -> {vrfObj.uid}, vrfObj.name -> {vrfObj.name}")
        st_print(line_print(f''))

    def pyemployees():
        line_print(f"pyemployees() {'-' * 30}")

        class employee:
            def __init__(self, name, age, salary):  # __init__ allocates memory for E1
                self.name = name
                self.age = age
                self.salary = 20000

            def employee_print(self):
                self.salary = self.salary * 2
                line_print(
                    f"self.name -> {self.name}, self.age -> {self.age}, self.salary -> {self.salary}")

            def employee_info(self):
                return '{} {} {}'.format(self.name, self.age, self.salary)

        #  E1 is the instance of class Employee.
        E1 = employee("XYZ", 23, 20000)
        line_print(
            f"E1 -> {E1}, E1.name -> {E1.name}, E1.age -> {E1.age}, E1.salary -> {E1.salary}")
        E1.employee_print()

        line_print(f"vars(E1) -> {vars(E1)}, E1 -> {E1}")
        st_print(line_print(f''))
    pyvrf()
    pyemployees()
### EndofCodeSection###


def py_dynamic_attr():
    class student:
        school = 'Forward Thinking'
        address = '2626/Z Overlook Drive, COLUMBUS'
    student1 = student()
    student2 = student()
    student3 = student()

    student1.student_id = "V11"
    student1.student_name = "Ernesto Mendez"

    student2.student_id = "V12"
    student2.marks_language = 85
    student2.marks_science = 93
    student2.marks_math = 95

    student2.student_id = "V13"
    student3.test = 100

    students = [student1, student2, student3]
    for student in students:
        for attr in student.__dict__:
            line_print(f'{attr}->{getattr(student, attr)}')
    st_print(line_print(f''))
### EndofCodeSection###


def py_dynamic_set_get():
    class person():
        pass
    person_obj = person()
    person_obj.first = "Corey"
    # dynamic class attribute
    person_obj.second = "Schafer"
    line_print(
        f"person_obj.first -> {person_obj.first}, person_obj.second -> {person_obj.second}")

    first_key = 'first'
    first_val = 'Corey'
    setattr(person_obj, first_key, first_val)
    # person_obj.first_val -> {getattr(person_obj,first_val)}")
    line_print(f"person_obj.first_key -> {getattr(person_obj, first_key)}")

    person_info = {'first': 'Corey', 'last': 'Schafer', 'city': 'Seattle'}
    for key, value in person_info.items():
        setattr(person_obj, key, value)

    for key in person_info.keys():
        # getattr(person_obj,value) -> {getattr(person_obj,value)}")
        line_print(f"getattr(person_obj,key) -> {getattr(person_obj, key)}")
    st_print(line_print(f''))
### EndofCodeSection###


def py_class_inherirance():
    def pychef():
        line_print(f"pychef() {'-' * 30}")

        class chef:
            def make_chicken(self):
                line_print("The chef makes a chicken")

            def make_salads(self):
                line_print("The chef makes a salad")

            def make_special_dish(self):
                line_print("The chef makes bbq ribs")

        class ChineseChef(chef):                          # inheritance
            def make_fried_rice(self):
                line_print("The chef makes fried rice")

        chefA = ChineseChef()
        chefA.make_chicken()
        chefA.make_fried_rice()
        st_print(line_print(f''))
    pychef()

    def pyanimal():
        line_print(f"pyanimal() {'-' * 30}")

        class Animal:
            def __init__(self, name):
                self.name = name
                self.is_pet = True

        class Dog(Animal):
            def __init__(self, name, breed):
                super().__init__(name)                   # Pass name to parent's __init__
                self.breed = breed                       # Dog-specific attribute

            def describe(self):
                return f"{self.name} is a {self.breed}"

        # Create dogs with breeds - positional arguments
        golden = Dog("Buddy", "Golden Retriever")
        # Or with named arguments (clearer)
        poodle = Dog(name="Max", breed="Poodle")

        # Buddy is a Golden Retriever
        line_print(golden.describe())
        # True (inherited from Animal)
        line_print(f"golden.is_pet: {golden.is_pet}")
        st_print(line_print(f''))
    pyanimal()
### EndofCodeSection###


def py_class_override():
    #
    # override
    #
    class animal:
        def __init__(self, name):
            self.name = name

        def make_sound(self):
            return f"{self.name} makes a sound"

    class dog(animal):
        def make_sound(self):  # Override parent method
            return f"{self.name} barks: Woof!"

    # Different animals, different sounds
    generic = animal(name="Something")
    mydog = dog(name="Buddy")

    # Something makes a sound
    line_print(generic.make_sound())
    # Buddy barks: Woof!
    line_print(mydog.make_sound())
    st_print(line_print(f''))
### EndofCodeSection###


def py_dunder_methods():
    #
    # __init__, __call__, __str__, __len__
    #
    class agent:
        def __init__(self, system=''):
            self.system = system
            self.messages = []
            if self.system:
                self.messages.append(self.system)

        def __call__(self, message):
            line_print(f'message into __call_ {message}')
            self.messages.append(message)
            result = self.execute()
            return result

        def execute(self):
            line_print(f"execute is called")
            return self.messages

    ret = '123'
    my_agent = agent('gongya')
    line_print(
        f"my_agent.system -> {my_agent.system}, my_agent.messages -> {my_agent.messages}, result -> {ret}")
    ret = my_agent('good morning')
    line_print(
        f"my_agent.system -> {my_agent.system}, my_agent.messages -> {my_agent.messages}, result = {ret}")

    my_agent.__dict__['response'] = 'Hello world!'
    line_print(f"my_agent.response -> {my_agent.response}")
    st_print(line_print(f''))
### EndofCodeSection###


def py_class_methods():
    ''' CoffeeShop class has an attribute, specialty, set to 'espresso' by default. 
        Each instance of CoffeeShop is initialized with an attribute coffee_price . 
        It also has 3 methods, an instance method, a static method and a class method.
    '''
    class CoffeeShop:
        specialty = 'espresso'

        def __init__(self, coffee_price):
            self.coffee_price = coffee_price

        # instance method
        def make_coffee(self):
            line_print(f'Making {self.specialty} for \\${self.coffee_price}')

        # static method
        @staticmethod
        def check_weather():
            line_print(f'Its sunny')

        # class method
        @classmethod
        def change_specialty(clear, specialty):
            clear.specialty = specialty
            line_print(f'Specialty changed to {specialty}')
    """ Let's initialize an instance of the coffee shop with a coffee_price of 5. 
        Then call the instance method make_coffee.
    """
    coffee_shop = CoffeeShop('5')
    # Making espresso for $5
    coffee_shop.make_coffee()

    """ Static methods can't modify class or instance state 
        so they're normally used for utility functions, for example, adding 2 numbers. 
    """
    coffee_shop.check_weather(
    )                                                            # Its sunny

    """use the class method to modify the coffee shop's specialty and then make_coffee.
    """
    coffee_shop.change_specialty(
        # Specialty changed to drip coffee
        'drip coffee')
    # Making drip coffee for $5
    coffee_shop.make_coffee()
    st_print(line_print(f''))
### EndofCodeSection###


def py_monkey_patch():
    # check monkey patching
    class old_service:
        def ad():
            line_print(f"This is an old service")

    def new_service():
        line_print(f"This is an updated service")

    service = old_service()
    service.ad = new_service
    service.ad()
    st_print(line_print(f''))
### EndofCodeSection###


def py_person_class():
    class Person():
        pass

    person = Person()
    person.first = "Corey"
    person.second = "Schafer"                           # dynamic class attribute
    st_code(f"person.first: {person.first}, person.second: {person.second}")

    first_key = 'first'
    first_val = 'Corey'
    setattr(person, first_key, first_val)
    first = getattr(person, first_key)
    st_code(f"person.first: {person.first}")

    person_info = {'first': 'Corey', 'last': 'Schafer', 'city': 'Seattle'}
    for key, value in person_info.items():
        setattr(person, key, value)
    st_code(
        f"person.first: {person.first}, person.last: {person.last}, person.city: {person.city}")

    for key in person_info.keys():
        st_code(f"getattr(person, key): {getattr(person, key)}")
### EndofCodeSection###
