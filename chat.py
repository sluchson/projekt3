import smbus2

class XL9535:
    def __init__(self, bus_number, device_address):
        self.bus = smbus2.SMBus(bus_number)
        self.address = device_address

    def write_register(self, register, value):
        self.bus.write_byte_data(self.address, register, value)

    def read_register(self, register):
        return self.bus.read_byte_data(self.address, register)

    def set_pin(self, pin, value):
        current_value = self.read_register(0x01)  # Przykładowy rejestr pinu
        if value:
            current_value |= (1 << pin)
        else:
            current_value &= ~(1 << pin)
        self.write_register(0x01, current_value)

# Przykładowe użycie
expander = XL9535(bus_number=1, device_address=0x20)
expander.set_pin(3, 1)  # Ustawienie pinu 3 na wysoki poziom
