from pprint import pprint
from loremipsum import get_paragraphs, get_sentences
from datetime import datetime
import time

user_attr = {'type': 'user', 'data': ['id', 'username', 'lastname', 'password', 'birth_date', 'phone', 'created_at', 'adress', 'group']}
group_attr = {'type': 'group', 'data': ['id', 'role']}
category_attr = {'type': 'category', 'data': ['id', 'name', 'parent']}
product_attr = {'type': 'product', 'data': ['id', 'name', 'price', 'description', 'reference', 'supplier', 'maker', 'stock', 'category']}
supplier_attr = {'type': 'supplier', 'data': ['id', 'name']}
maker_attr = {'type': 'maker', 'data': ['id', 'name']}
order_attr = {'type': 'order', 'data': ['id', 'quantity', 'total', 'created_at', 'user', 'event_sale']}

def jsonify(attr):
	response_file = file('json_files/'+attr['type']+'.json' , 'w')
	response = []
	for x in xrange(1,10):
		one_user = {}
		for el in attr['data']:
			# print el
			if el == "id":
				one_user[el] = x
			elif el == "created_at":
				one_user[el] = time.strftime("%A %d %B %Y %H:%M:%S")
			else:
				one_user[el] = get_sentences(1)
		response.append(one_user)
		response_file.write(str(one_user))
	response_file.close()
	return response

def randword(count_letters):
	word = ""
	for x in xrange(1,count_letters):
		word += str(x)
	return word

pprint(jsonify(user_attr))
pprint(jsonify(group_attr))
pprint(jsonify(category_attr))
pprint(jsonify(product_attr))
pprint(jsonify(supplier_attr))
pprint(jsonify(maker_attr))
pprint(jsonify(order_attr))