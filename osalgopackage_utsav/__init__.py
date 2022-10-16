
class BestShedulingAlgo:

	lists=[]

	def __init__(self,size):
		self.size=size
		print(f"{size} length size is initialized")

	def merge(dict1,dict2):

		return {**dict1,**dict2}

	def taking_input(self):
		constant_dict={
			"time_quantum":3,
			"waiting_time":0,
			"reminder":0
		}
		print('Enter input in this manner --> processName AT BT P')

		for i in range(0,self.size):
			name=input('Enter process name')
			at=input('Enter AT(Arrival Time)')
			bt=input('Enter BT(Burst Time)')
			p=input('Enter P(Priority)')
			inpt={
				"name":name,
				"AT":int(at),
				"BT":int(bt),
				"P":int(p)
			}
			lists.append(merge(inpt,constant_dict))
		return lists	


a=BestShedulingAlgo(2)
a.taking_input()
