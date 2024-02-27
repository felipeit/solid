class IncandescentBulbWithoutDIP:
    def turn_on(self):
        print("Lâmpada incandescente ligada.")

    def turn_off(self):
        print("Lâmpada incandescente desligada.")

    def is_on(self):
        # Lógica para verificar se a lâmpada está ligada
        return True

class ToggleSwitchWithoutDIP:
    def operate(self, bulb: IncandescentBulbWithoutDIP):
        # Lógica do interruptor
        print("Operando o interruptor.")
        bulb.turn_on() if not bulb.is_on() else bulb.turn_off()

class HomeAutomationWithoutDIP:
    def __init__(self, switch: ToggleSwitchWithoutDIP, bulb: IncandescentBulbWithoutDIP):
        self.switch = switch
        self.bulb = bulb

    def operate_home_devices(self):
        self.switch.operate(self.bulb)

incandescent_bulb_without_dip = IncandescentBulbWithoutDIP()
toggle_switch_without_dip = ToggleSwitchWithoutDIP()
home_automation_without_dip = HomeAutomationWithoutDIP(toggle_switch_without_dip, incandescent_bulb_without_dip)

home_automation_without_dip.operate_home_devices()
