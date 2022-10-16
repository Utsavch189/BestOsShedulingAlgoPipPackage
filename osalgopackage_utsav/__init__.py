
class BestShedulingAlgo:

	processes=[]

	constant_dicts={
		"time_quantum":3,
		"waiting_time":0,
		"reminder":0
		}

	def __init__(self,size):
		self.size=size
		print(f"{size} length size is initialized")

	def taking_input(self):

		print('Enter input in this manner --> processName AT BT P')

		for i in range(0,self.size):
			name=input('Enter process name: ')
			at=input('Enter AT(Arrival Time): ')
			bt=input('Enter BT(Burst Time): ')
			p=input('Enter P(Priority): ')
			inpt={
				"name":name,
				"AT":int(at),
				"BT":int(bt),
				"P":int(p)
			}
			self.processes.append({**inpt,**self.constant_dicts})
		return self.processes	


a=BestShedulingAlgo(2)
print(a.taking_input())
