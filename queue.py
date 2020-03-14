class Queue:
	def __init__(self,limit=5):
		self.que=[]
		self.limit=limit
		self.rear=0
		self.front=0
		self.size=0
	def Enqueue(self,item):
		if self.size>=self.limit:
			print("Queue Overflow")
			return 
		else:
			self.que.append(item)

		if self.front==None:
			self.front=self.rear=0
		else:
			self.rear=self.size
		self.size+=1
		print("after enqueue",self.que)
	def Dequeue(self):
		if self.size<=0:
			print("Queue underflow")
		else:
			self.que.pop(0)
			self.size-=1	
			if self.size==0:
				self.front=self.rear=None
			else:
				self.rear=self.size-1	
			# print("after deque ",self.que)	
			print("after Dequeue",self.que)	
	def is_empty(self):
		return self.que==[]
	def qRear(self):
		if self.rear==None:
			print("q is emppty")
			raise IndexError
		print(self.que[self.rear])
	def qfront(self):
		if self.front==None:
			print("q is empty")
		print(self.que[self.front])

				

					
										
q=Queue()
q.Enqueue(1)
q.Enqueue(2)
q.Enqueue(3)
q.qfront()
q.qRear()
q.Enqueue(4)
q.Enqueue(5)
# q.Enqueue(6)
q.qRear()
q.Dequeue()
q.qRear()
q.qfront()
# q.Dequeue()
# q.qfront()
# q.qRear()
# q.Dequeue()
# q.Dequeue()
# q.Dequeue()
# q.Dequeue()

