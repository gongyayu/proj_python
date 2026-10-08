from py_mod import st_code, code_print, st_print, st_markline

### StartofFunc###

def py_decorator():
    def pydecorator(func):
        def log_function_called():
            st_code('The decorator is called')
            func()
            st_code('The decorator is called')
        return log_function_called

    @pydecorator
    def py_decorated():
        st_code('py_decorated is called')
    py_decorated()
    st_markline()

    # with func input parameters
    def add_sprinkles(func):
        def wrapper(*args, **kwargs):
            st_code(f' *You add sprinkle *')
            func(*args, **kwargs)
        return wrapper

    def add_fudge(func):
        def wrapper(*args, **kwargs):
            st_code(f' *You add fudge *')
            func(*args, **kwargs)
        return wrapper

    @add_sprinkles
    @add_fudge
    def get_ice_cream(flavor):
        st_code(f'Here is your {flavor} ice cream ')
    get_ice_cream('vanilla')
### EndofCodeSection###

def py_static_decorator():
    #
    # In Python, @staticmethod is a decorator used to define a method inside a class that doesn't need access to the instance (self) or the class (cls). 
    # It behaves like a normal function, but belongs to the class's namespace.
    #
    def demo1():
        class UserModel:
            def __init__ (self, uid:int, name:str, email:str):
                self.uid = uid
                self.name = name
                self.email = email
            def to_dict(self):
                return{"uid":self.uid, "name":self.name, "email": self.email}

            @staticmethod
            def from_dict(d:dict):
                return UserModel(d["uid"],d["name"],d["email"])

        u1 = UserModel(1001,'tom','tom@test.com')
        d = u1.to_dict()
        u2 = UserModel.from_dict(d)
        st_code(f"d: {d}, u2.name: {u2.name}")
    demo1()
    st_markline()

    def demo2():
        # Key benefits:
        # 1. Organizes utility functions inside relevant classes.
        # 2. Improves code readability and performance (slightly) by avoiding passing unnecessary self/cls arguments.

        class MathUtils:

            @staticmethod
            def add(a, b):
                return a + b

        # Call directly from the class (no instance needed)
        st_code(f"{MathUtils.add(5, 3)}")  # Output: 8
    demo2()
### EndofCodeSection###