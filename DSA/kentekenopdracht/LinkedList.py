from abc import ABC, abstractmethod

class LinkedList(ABC):
    @abstractmethod
    def toString(self):
        pass

    @abstractmethod
    def addFirst(self, value):
        pass

    @abstractmethod
    def remove(self, value):
        pass

class LinkedListEmpty(LinkedList):
    def toString(self):
        # Basisgeval voor recursie: een lege lijst is een lege string.
        return ""

    def addFirst(self, value):
        # Wanneer je iets toevoegt aan een lege lijst, 
        # ontstaat er een 'Populated' lijst met 'self' (de lege lijst) als staart.
        return LinkedListPopulated(value, self)

    def remove(self, value):
        # Je kunt niets verwijderen uit een lege lijst, dus geef jezelf terug.
        return self

class LinkedListPopulated(LinkedList):
    def __init__(self, value, tail):
        self.value = value
        self.tail = tail # Dit is de volgende LinkedList (Empty of Populated)

    def toString(self):
        # Recursieve stap: neem de huidige waarde en plak daar de string van de rest achter.
        return str(self.value) + " " + self.tail.toString()

    def addFirst(self, value):
        # Maak een nieuwe lijst-node aan die naar de huidige lijst wijst.
        return LinkedListPopulated(value, self)

    def remove(self, value):
        # Als de huidige waarde de gezochte waarde is, 'skip' deze dan
        # door de rest van de lijst (de tail) terug te geven.
        if self.value == value:
            return self.tail
        
        # Zo niet, behoud de huidige waarde en zoek verder in de staart.
        # Let op: we maken een nieuwe Populated aan om de lijst intact te houden (immutability).
        return LinkedListPopulated(self.value, self.tail.remove(value))