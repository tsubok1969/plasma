class plasma():
    def __init__(self):
        from const import Const
        self.const = Const()

    def ev2vel(species, energy):
        if species == 0:
            mass = self.const.EMAS
        else:
            mass = self.const.PMAS
        return 
    
    def vel2ev(species, velocity):
        if species == 0:
            mass = self.const.EMAS
        else:
            mass = self.const.PMAS

