class Student:
  def __init__(self, greet, hand):
    self.greet = greet
    self.hand = hand

  def printname(self):
    print(self.greet, self.hand)

class ChattyStudent(Student):
  def __init__(self, greet, hand, phrase):
    super().__init__(greet, hand)
    self.phrase = phrase

  def chattyphrase(self):
    print( self.greet)
    print(self.hand)
    print(self.phrase)
x = ChattyStudent("Hey there! I'm so excited to learn stuff.", "Pick me!", "How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay well let me just tell you who died...")
x.chattyphrase()
