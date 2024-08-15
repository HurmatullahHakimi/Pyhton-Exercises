# 2. Add a method called greet to the Person class that prints a greeting message including the person's name
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def attributes(self):
        print(f"name is {self.name}")
        print(f"age is {self.age}")
        
    def greeting(self,greeting_message):
        print(greeting_message)
        print(f"my name is {self.name}")
        print(f"my age is {self.age}")
        
ahmad=person(name="ahmad",age=45)
ahmad.greeting("hello how are you")
    
        
