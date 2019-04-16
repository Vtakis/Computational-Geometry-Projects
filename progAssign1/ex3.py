class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

class Stack:
    def __init__(self):
        self.stack=list()
    def push(self,point):
        if point not in self.stack:
            self.stack.append(point)
    def pop(self):
        return self.stack.pop()
    def size(self):
        return len(self.stack)


