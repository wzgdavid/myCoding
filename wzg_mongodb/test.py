import sys
sys.path.insert(0, 'C:\\Users\\Administrator\\Desktop\\myCoding')

from wzg_mongodb.config import *
from wzg_mongodb import MongoApp

app = MongoApp(HOST, PORT, 'test', 'company')
info = {
	'field': 'staff',
    'field_d': 'name',
    'value': 'jimi',
        
}

#print(app.get_embdoc_in_array(11,info))


import collections
import bisect
class SortedItems(collections.Sequence):
	def __init__(self, initial=None):
		self._items = sorted(initial) if initial is None else []

	def __getitem__(self, index):
		return self._items[index]
	def __len__(self):
		return len(self._items)

	def add(self, item):
		bisect.insort(self._items, item)

a = SortedItems([3,6,1])



class Items(collections.MutableSequence):
	def __init__(self, initial=None):
		self._items = list(initial) if initial is not None else []
	# Required sequence methods
	def __getitem__(self, index):
		print('Getting:', index)
		return self._items[index]
	def __setitem__(self, index, value):
		print('Setting:', index, value)
		self._items[index] = value
	def __delitem__(self, index):
		print('Deleting:', index)
		del self._items[index]
	def insert(self, index, value):
		print('Inserting:', index, value)
		self._items.insert(index, value)
	def __len__(self):
		print('Len')
		return len(self._items)	

b = Items([1,2,3])
print(b[0], len(b))
b.append(5)
b.extend([7,8,9])
print(b[0], len(b))
