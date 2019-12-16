class Card:
    def __init__(self, suit_in, value_in):
        self.suit = suit_in
        self.value = value_in

    def get_val(self):
        if self.value == "JACK":
            return 11
        elif self.value == "QUEEN":
            return 12
        elif self.value == "KING":
            return 13
        elif self.value == "ACE":
            return 14
        return int(self.value)

    def get_suit_color(self):
        if self.suit == "SPADES" or self.suit == "CLUBS":
            return "BLACK"
        else:
            return "RED"

    def __gt__(self, other):
        return self.get_val() > other.get_val()

    def __str__(self):
        return self.suit + " " + self.value