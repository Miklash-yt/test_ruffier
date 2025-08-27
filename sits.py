from kivy.uix.label import Label
class Sits(Label):
    
    def __init__(self, total, **kwargs):
        self.quantity_sits = 0
        self.total_sits = total
        myy_text = 'Осталось приседаний:'+str(self.total_sits)
        super().__init__(text=myy_text, **kwargs)

    def next(self, *args):
        self.quantity_sits += 1
        remain = max(self.total_sits - self.quantity_sits, 0)
        self.text = 'Осталось приседаний:' + str(remain)