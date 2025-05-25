class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device Name: {self.name}, Connected by: {self.connected_by}, Connected: {self.connected}"
    
    def discionnect(self):
        self.connected = False
        print(f"{self.name} has been disconnected.")


# printer = Device("Printer", "USB")
# print(printer)
# printer.discionnect()
# print(printer)

class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity

    def __str__(self):
        return super().__str__() + f", Capacity: {self.capacity} pages"
    

printer = Printer("HP LaserJet", "USB", 500)
print(printer)
printer.discionnect()