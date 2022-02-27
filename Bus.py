class Bus:
    def __init__(self, bus_num, route, driver):
        self.bus_num = bus_num
        self.route = route
        self.driver = driver

bus_list = []

bus1 = Bus("2010","Y","Greg")
bus2 = Bus("2011","P","Bob")
bus3 = Bus("2012","130","Baker")

for bus in bus_list:
    print(f"Bus number: {bus.bus_num}"
          f"on route: {bus.route}"
          f"with driver: {bus.driver}")
