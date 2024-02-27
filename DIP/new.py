from abc import ABC, abstractmethod

# Abstração para a lâmpada
class LightBulb(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

# Implementação concreta da lâmpada
class IncandescentBulb(LightBulb):
    def turn_on(self):
        print("Lâmpada incandescente ligada.")

    def turn_off(self):
        print("Lâmpada incandescente desligada.")

# Abstração para o interruptor
class Switch(ABC):
    @abstractmethod
    def operate(self, bulb: LightBulb):
        pass

# Implementação concreta do interruptor
class ToggleSwitch(Switch):
    def operate(self, bulb: LightBulb):
        # Lógica do interruptor
        print("Operando o interruptor.")
        bulb.turn_on() if not bulb.is_on() else bulb.turn_off()

# Cliente
class HomeAutomation:
    def __init__(self, switch: Switch, bulb: LightBulb):
        self.switch = switch
        self.bulb = bulb

    def operate_home_devices(self):
        self.switch.operate(self.bulb)

# Exemplo de uso
incandescent_bulb = IncandescentBulb()
toggle_switch = ToggleSwitch()
home_automation = HomeAutomation(toggle_switch, incandescent_bulb)

home_automation.operate_home_devices()