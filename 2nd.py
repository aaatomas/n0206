class Animal(object):
    def __init__(self, sound):
        self.sound = sound

    def make_sound(self):
        print(f"Animal making sound '{self.sound}'")

cat = Animal('mow')
cat.make_sound()