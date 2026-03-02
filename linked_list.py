from abc import ABC, abstractmethod

class LinkedList(ABC):
    @abstractmethod
    def toString(self): pass
    
    @abstractmethod
    def addFirst(self, value): pass
    
    @abstractmethod
    def remove(self, value): pass
    
    @abstractmethod
    def smallest(self): pass
    
    @abstractmethod
    def sortSimple(self): pass

    @abstractmethod
    def isEmpty(self): pass

class EmptyLinkedList(LinkedList):
    def toString(self):
        return ""
    
    def addFirst(self, value):
        return PopulatedLinkedList(value, self)
    
    def remove(self, value):
        return self # Waarde niet gevonden
    
    def smallest(self):
        return float('inf') # Oneindig groot om vergelijking niet te storen
    
    def sortSimple(self):
        return self
    
    def isEmpty(self):
        return True

class PopulatedLinkedList(LinkedList):
    def __init__(self, value, tail):
        self.value = value
        self.tail = tail # De rest van de lijst

    def toString(self):
        return f"{self.value} {self.tail.toString()}"
    
    def addFirst(self, value):
        return PopulatedLinkedList(value, self)
    
    def remove(self, value):
        if self.value == value:
            return self.tail
        else:
            return PopulatedLinkedList(self.value, self.tail.remove(value))
    
    def smallest(self):
        tail_smallest = self.tail.smallest()
        return self.value if self.value < tail_smallest else tail_smallest
    
    def sortSimple(self):
        s = self.smallest()
        rest = self.remove(s)
        return PopulatedLinkedList(s, rest.sortSimple())
    
    def isEmpty(self):
        return False
