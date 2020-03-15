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
		
		
class Stack:  ##create stack class for interleaving and reverse of a specific part of queue
	def __init__(self):
		self.stk=[]
	def is_empty(self):
		return len(self.stk)<=0
	def push(self,item):
		self.stk.append(item)
	def pop(self):
		if len(self.stk)<=0:
			print("stack underflow")
		else:
			self.stk.pop()
	def size(self):
		return len(self.stk)
	
		
		
	def interleaving(self):##to check wheather given Queu is interleave or not 
		                  #Exmpple=input-[1,2,3,4,5,6,7,8,9,10]  // output=[1,6,2,7,3,8,4,9,5,10]                                       
		stk=Stack()
		half=que.size()//2
		for i in range(0,half):
			stk.push(que.dqueu())
		while not stk.is_Empty():
			que.enqueu(stk.pop())
		for i in range(0,half):
			que.enqueu(que.dqueu())
		for i in range(0,half):
			stk.push(que.dqueu())
		while not stk.is_Empty():
			que.enqueu(stk.pop())
			que.enqueu(que.dqueu())
			
			
	def reverseK(self,k): ##to reverse a part of Queue and reamainig queue intactas it is 
		                #emple=[1,2,3,4,5,6,7,8,9]//k=4// output =[4,3,2,1,5,6,7,8,9]
		stk=Stack()
		if self.q==0 or k>len(self.q):
			return
		for i in range(0,k):
			stk.push(que.dqueu())
		while not stk.is_Empty():
			que.enqueu(stk.pop())
		for i in range(0,len(self.q)-k):
			que.enqueu(que.dqueu())		
			

				

					
										
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

