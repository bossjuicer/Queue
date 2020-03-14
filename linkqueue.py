class Node:
	def __init__(self,data):
		self.data=data
		self.next=None
class Queue:
	def __init__(self):
		self.front=None
		self.rear=None
	def enque(self,data):
		if self.rear is None:
			self.rear=Node(data)
			self.front=self.rear
		else:
			self.rear.next=Node(data)
			self.rear=self.rear.next
			# cur=self.rear
			# while True:
				# if cur.next is None:
					# break
				# cur=cur.next	
			# newNode=Node(data)
			# cur.next=newNode	
	def dqueue(self):
		if self.front is None:
			print("queue is empty")
		else:
			result=self.front.data
			temp=self.front.next
			del self.front
			self.front=temp
			print("deque element is",result)	

	def printL(self):
		cur=self.front
		while cur:
			print(cur.data)
			cur=cur.next

class Stack:
	def __init__(self):
		self.s1=[]
		self.s2=[]
	def enquue(self,data):
		self.s1.append(data)
	def dqueue(self):
		if not self.s2:
			while self.s1:
				self.s2.append(self.s1.pop())
		return self.s2.pop()
					
l=Stack()
for i in xrange(5):
	l.enquue(i)
for i in xrange(5):
	print(l.dqueue())	
# link=Queue()
# link.enque(4)
# link.enque(2)					
# link.enque(5)
# link.enque(7)
# link.printL()
# link.dqueue()
# link.dqueue()
print("---------")
# link.printL()