# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import json
import os.path
import time
import random

# Creating Dictionary to store data
available_products = {1001: {"name": "Mango", "price": 2130,
							"origin": "Vietnam",
							"quantity": 10, "date": "10/06/2023"},
					1002: {"name": "Kiwi", "price": 2900,
							"origin": "Thailand",
							"quantity": 160,
							"date": "15/06/2023"},
					1003: {"name": "Banana", "price": 5000,
							"origin": "Sri-Lanka",
							"quantity": 200, "date": "12/06/2023"},
					1004: {"name": "Pineapple", "price": 12000,
							"origin": "Sri-Lanka",
							"quantity": 50, "date": "07/06/2023"},
					1005: {"name": "Apple", "price": 700,
							"origin": "Thailand",
							"quantity": 1005,
							"date": "06/06/2023"},
					1006: {"name": "Orange", "price": 1500,
							"origin": "Vietnam",
							"quantity": 56, "date": "12/06/2023"},
					1007: {"name": "Grape", "price": 9500,
							"origin": "Thailand",
							"quantity": 70,
							"date": "11/06/2023"},
					1008: {"name": "Melon", "price": 7000,
							"origin": "Sri-Lanka",
							"quantity": 90, "date": "16/06/2023"},
					1009: {"name": "Papaya", "price": 8000,
							"origin": "Vietnam",
							"quantity": 50, "date": "07/06/2023"},
					1010: {"name": "Peach", "price": 2400,
							"origin": "Sri-Lanka", "quantity": 60,
							"date": "20/05/2023"},
					}

# Formatting Dictionary into JSON format
js = json.dumps(available_products)

# json.dumps() function converts a
# Python object into a json string
js # so we got all data in json string format here

# Create Json File for DataBase and Write data Into File
fd = open("data.json", 'w')
# it will open file into write mode if file
# does not exists then it will create file too'''
fd.write(js) # writing string into file
fd.close() # Close File After Inserting Data

def admin():
	print("========\
	Fruit Inventory Management System _ Admin \
	==============")
	while (1):
		print("1)Display All Products with details")
		print("2)Display Specific Product with details")
		print("3)Add new Product to the Database")
		print("4)Update a Product in the Database")
		print("5)Delete a Product in the DataBase")
		print("6)Display User Purchase Reports")
		print("7)Exit")
		print("Enter Your Choice :- ")
		n = int(input())
		if (n == 1):
			display_data()
		elif (n == 2):
			display_specific_data()
		elif (n == 3):
			add_new()
		elif (n == 4):
			update_prod_data()
		elif (n == 5):
			delete_prod()
		elif (n == 6):
			display_reports_admin()
		elif (n == 7):
			break
		else:
			print("Invalid Choice...!!!")


def display_data():

	fd = open("data.json", 'r')
	txt = fd.read() # reading data from file
	data = json.loads(txt)
	
	# This will parse the JSON data, populates a
	# Python dictionary with the data
	fd.close()
	print("Enter '0' To Display Data origin Wise or '1' \
	To Show Data As its Sequence Of Insertion :- ")
	n = int(input())
	
	# Display All Records
	if (n == 1):
		table = pd.DataFrame(
			columns=['ID', 'name', 'price', 'origin', 'quantity', 'date'])
		
		# Creating Pandas dataframe to show data in table format later
		for i in data.keys():
		
			# Fetch all keys in dictionary
			temp = pd.DataFrame(columns=['ID'])
			temp['ID'] = [i]
			for j in data[i].keys():
				temp[j] = [data[i][j]]
			table = table.append(temp)
		table = table.reset_index(drop=True)
		'''This will reset index of dataframe'''
		from IPython.display import display
		display(table)
		
	elif (n == 0):
	
		# Display Records by Category
		table = pd.DataFrame(
			columns=['ID', 'name', 'price', 'origin',
					'quantity', 'date'])
		cat = []
		
		for i in data.keys():
			temp = pd.DataFrame(columns=['ID'])
			temp['ID'] = [i]
			for j in data[i].keys():
				temp[j] = [data[i][j]]
				if (j == 'origin'):
					cat.append(data[i][j])
			table = table.append(temp)
			table = table.reset_index(drop=True)
			cat = set(cat)
			cat = list(cat)
			
		for k in cat:
			temp = pd.DataFrame()
			temp = table[table['origin'] == k]
			print("Data Of Products Of origin "+k+" are: ")
			from IPython.display import display
			display(temp)
	else:
		print("Enter Valid Choice...!!!")
		
# display_data() # Uncomment This Line To Run This Function
def display_specific_data():
	fd = open("data.json", 'r')
	txt = fd.read()
	data = json.loads(txt)
	fd.close()
	print("Enter Product ID Whose Details You Want to Have a Look on : ")
	i = input()
	
	# Following Code will Filter out Product ID from Records
	if i in data.keys():
		temp = pd.DataFrame(columns=['ID'])
		temp['ID'] = [i]
		for j in data[i].keys():
			temp[j] = [data[i][j]]
		from IPython.display import display
		display(temp)
	else:
		print("You Have Entered Wrong Product ID\
		that is not Present in DataBase...!!!")


# display_specific_data() # Uncomment This Line To Run This Function
def add_new():
	fd = open("data.json", 'r')
	txt = fd.read()
	data = json.loads(txt)
	fd.close()
	print("Enter New Product ID :- ")
	id = input()
	
	if id not in data.keys():
		print("Enter Product Name : ")
		name = input()
		print("Enter Price of Product (price for product quantity as 1) : ")
		price = input()
		print("Enter origin of Product : ")
		origin = input()
		print("Enter Quantity of Product : ")
		quantity = input()
		print("Enter The Date on Which Product is Added in Inventory : ")
		date = input()
		data[id] = {'name': name, 'price': price,
					'origin': origin, 'quantity': quantity, 'date': date}
		print("Please Press '0' to Add New\
		Attributes/Properties of Product or Press '1' to Continue : ")
		z = int(input())
		if(z == 0):
			print("Enter Number of New Attributes/Properties of Product : ")
			n = int(input())
			for i in range(n):
				print("Enter Attribute Name That you Want To Add : ")
				nam = input()
				print("Enter The "+str(nam)+" of Product : ")
				pro = input()
				data[id][nam] = pro
		print("Product ID "+str(id)+" Added Successfully...!!!")
	else:
		print("The Product ID you Have Entered Is\
		Already Present in DataBase Please Check...!!!")
	js = json.dumps(data)
	fd = open("data.json", 'w')
	fd.write(js)
	fd.close()
	
# add_new() # Uncomment This Line To Run This Function
def delete_prod():
	fd = open("data.json", 'r')
	txt = fd.read()
	data = json.loads(txt)
	fd.close()
	print("Enter The Product ID of The Product Which You Want To Delete :- ")
	temp = input()
	if temp in data.keys():
		data.pop(temp) # here we are removing that particular data
		print("Product ID "+str(temp)+" Deleted Successfully...!!!")
	else:
		print("Invalid Product ID...!!!")
	js = json.dumps(data)
	fd = open("data.json", 'w')
	fd.write(js)
	fd.close()
	
# delete_prod() # Uncomment This Line To Run This Function
def update_prod_data():
	fd = open("data.json", 'r')
	txt = fd.read()
	data = json.loads(txt)
	fd.close()
	print("Enter The Product ID of The Product\
	Which You Want To Update :- ")
	temp = input()
	
	if temp in data.keys():
		print("Want to update whole product data\
		press '0' else '1' for specific data :- ")
		q = int(input())
		
		if (q == 0):
			print("Enter Product Name :- ")
			name = input()
			print("Enter Price of Product(price for\
			product quantity as 1) :- ")
			price = input()
			print("Enter Category of Product :- ")
			origin = input()
			print("Enter Quantity of Product :- ")
			quantity = input()
			print("Enter The Date on Which Product\
			is Added in Inventory :- ")
			date = input()
			data[temp] = {'name': name, 'price': price,
						'origin': origin, 'quantity': quantity,
						'date': date}
			print(
				"Please Press '0' to Add more Attributes/Properties of Product or Press '1' to Continue :- ")
			z = int(input())
			
			if(z == 0):
				print("Enter Number of New Attributes/Properties of Product :- ")
				n = int(input())
				for i in range(n):
					print("Enter Attribute Name That you Want To Add :- ")
					nam = input()
					print("Enter The "+str(nam)+" of Product :- ")
					pro = input()
					data[temp][nam] = pro
			print("Product ID "+str(temp)+" Updated Successfully...!!!")
			
		elif(q == 1):
			print("Enter Which Attribute of Product You want to Update :- ")
			p = input()
			
			if p in data[temp].keys():
				print("Enter "+str(p)+" of Product :- ")
				u = input()
				data[temp][p] = u
				print("Product ID "+str(temp)+"'s attribute " +
					str(p)+" is Updated Successfully...!!!")
			else:
				print("Invalid Product Attribute...!!!")
		else:
			print("Invalid Choice...!!!")
	else:
		print("Invalid Product ID...!!!")
	js = json.dumps(data)
	fd = open("data.json", 'w')
	fd.write(js)
	fd.close()
	
# update_prod_data() # Uncomment This Line To Run This Function
def display_reports_admin():
	if (os.path.isfile("user_data.json") is False):
		# Check for if file is present or not
		# File will be generated only if any user will do some purchase
		print("No User Reports are Present")
		return
	fd = open("user_data.json", 'r')
	txt = fd.read()
	user_data = json.loads(txt)
	fd.close()
	print("Enter '0' to Check All Bills/Reports\
	and '1' To Check Specific User Bills/Reports :- ")
	n = int(input())
	if (n == 1):
		print("Enter User ID Whose Details You Want to Have a Look on")
		i = input()
		temp = pd.DataFrame()
		if i in user_data.keys():
			for j in user_data[i].keys():
				d = dict()
				d['User ID'] = i
				d['Purchase Number'] = j
				for k in user_data[i][j].keys():
					d[k] = user_data[i][j][k]
				temp = temp.append(d, ignore_index=True)
				d = dict()
			temp = temp.reset_index(drop=True)
			from IPython.display import display
			display(temp)
		else:
			print("You Have Entered Wrong User ID that is not Present in DataBase...!!!")
	elif (n == 0):
		table = pd.DataFrame()
		for i in user_data.keys():
			temp = pd.DataFrame()
			for j in user_data[i].keys():
				d = dict()
				d['User ID'] = i
				d['Purchase Number'] = j
				for k in user_data[i][j].keys():
					d[k] = user_data[i][j][k]
				temp = temp.append(d, ignore_index=True)
				d = dict()
			table = table.append(temp)
		table = table.reset_index(drop=True)
		from IPython.display import display
		display(table)
	else:
		print("Please Enter Valid Choice...!!!")

# display_reports_admin() # Uncomment This Line To Run This Function
def delete_all():
	fd = open("data.json", 'r')
	txt = fd.read()
	data = json.loads(txt)
	fd.close()
	data = {} # Replacing Data with NULL Dictionary
	js = json.dumps(data)
	fd = open("data.json", 'w')
	fd.write(js)
	fd.close()


def user():
	print("======= Fruit Inventory Management System _ User ====")
	while (1):
		print("1)Buy Product")
		print("2)Display purchase report")
		print("3)Generate purchase Bills")
		print("4)Exit")
		print("Enter Your Choice :- ")
		n = int(input())
		if (n == 1):
			buy_product()
		elif (n == 2):
			display_user_data()
		elif (n == 3):
			display_user_data()
		elif (n == 4):
			break
		else:
			print("Invalid Choice...!!!")


def display_user_data():

	if (os.path.isfile("user_data.json") is False):
		print("No User Reports are Present")
		return
	fd = open("user_data.json", 'r')
	txt = fd.read()
	user_data = json.loads(txt)
	fd.close()
	print("Enter your User ID to Display All your Bills :- ")
	i = input()
	temp = pd.DataFrame()
	
	if i in user_data.keys():
		for j in user_data[i].keys():
			d = dict()
			d['User ID'] = i
			d['Purchase Number'] = j
			for k in user_data[i][j].keys():
				d[k] = user_data[i][j][k]
			temp = temp.append(d, ignore_index=True)
			d = dict()
		temp = temp.reset_index(drop=True)
		from IPython.display import display
		display(temp)
	else:
		print("You Have Entered Wrong User ID that is not Present in DataBase...!!!")


def generate_bill(user_id, prod_id, price, time_date, purchase_no,
				name, category, quantity_all, transaction_id):
	print("========= Bill ========")
	print("#######################")
	print(" User ID :-", user_id)
	print("#################")
	amount = 0
	n = len(purchase_no)
	
	for i in range(n):
		print("-----------------------------------------")
		amount = amount+float(price[i])*float(quantity_all[i])
		print("Purchase number", purchase_no[i],
			"\nPurchase Time :-", time_date[i], "\nProduct ID :-",
			prod_id[i], "\nName Of Product :-",
			name[i], "\nCategory Of Product :-", category[i],
			"\nPrice of Product per Item :-", price[i],
			"\nPurchase Quantity :-", quantity_all[i])
		print("-----------------------------------")
	print("*****************************************")
	print(" Total Payable Bill :-",
		amount, "Transaction ID :-", transaction_id)
	print("***************************************")


def buy_product():
	
	if (os.path.isfile("user_data.json") is False):
		user_data = {}
	else:
		fd = open("user_data.json", 'r')
		txt = fd.read()
		user_data = json.loads(txt)
		fd.close()
	fd = open("data.json", 'r')
	txt = fd.read()
	data = json.loads(txt)
	fd.close()
	print("Enter Your User ID if You are Old \
	Customer else press '0' To New User ID :- ")
	p = int(input())
	if (p == 0):
		if (len(user_data.keys()) == 0):
			user_id = 1000
		else:
			user_id = int(list(user_data.keys())[-1])+1
	else:
		if str(p) in user_data.keys():
			user_id = p
		else:
			user_id = -1
	if (user_id != -1):
		user_id = str(user_id)
		price = []
		time_date = []
		purchase_no = []
		name = []
		origin = []
		quantity_all = []
		prod_id = []
		transaction_id = ''.join(random.choice(
			'0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(10))
		print("Enter Number of Products You Want To Buy :- ")
		n = int(input())
		print("Enter Data As Follows :- ")
		if user_id not in user_data.keys():
			user_data[user_id] = {}
			g = 0
		else:
			g = int(list(user_data[user_id].keys())[-1])+1
		for i in range(n):
			print("Enter Product ID of Product " +
				str(i+1)+" that you want to buy")
			id = input()
			if id in data.keys():
				user_data[user_id][str(i+1+g)] = {}
				user_data[user_id][str(i+1+g)]['time_date'] = str(time.ctime())
				time_date.append(str(time.ctime()))
				if(float(data[id]['quantity']) == 0.0):
					print("Product You Want is Currently Out Of Stock...!!!")
					continue
				purchase_no.append(i+1+g)
				name.append(data[id]['name'])
				user_data[user_id][str(i+1+g)]['name'] = data[id]['name']
				prod_id.append(id)
				user_data[user_id][str(i+1+g)]['product_id'] = id
				origin.append(data[id]['origin'])
				user_data[user_id][str(
					i+1+g)]['origin'] = data[id]['origin']
				print("For Product "+str(data[id]['name']) +
					" Available Quantity is :- "+str(data[id]['quantity']))
				print("Enter Quantity of Product " +
					str(i+1)+" that you want to buy")
				quantity = input()
				if (float(quantity) <= float(data[id]['quantity'])):
					data[id]['quantity'] = str(
						float(data[id]['quantity'])-float(quantity))
					quantity_all.append(quantity)
					user_data[user_id][str(i+1+g)]['quantity'] = str(quantity)
					price.append(data[id]['price'])
					user_data[user_id][str(i+1+g)]['price'] = data[id]['price']
					user_data[user_id][str(
						i+1+g)]['Transaction ID'] = str(transaction_id)
				else:
					print(
						"The Quantity You Have Asked is Quite High Than\
						That is Available in Stock")
					print(
						"Did you Want To buy According to The Quantity\
						Available in Stock then Enter '0' Else '1'\
						to skip This Product")
					key = int(input())
					if (key == 0):
						print("Enter Quantity of Product " +
							str(i+1)+" that you want to buy")
						quantity = int(input())
						if (float(quantity) <= float(data[id]['quantity'])):
							data[id]['quantity'] = str(
								float(data[id]['quantity'])-float(quantity))
							quantity_all.append(quantity)
							user_data[user_id][str(
								i+1)]['quantity'] = str(quantity)
							price.append(data[id]['price'])
							user_data[user_id][str(
								i+1)]['price'] = data[id]['price']
							user_data[user_id][str(
								i+1+g)]['Transaction ID'] = str(transaction_id)
						else:
							print("Invalid Operation Got Repeated...!!!")
					elif (key == 1):
						continue
					else:
						print("Invalid Choice...!!!")
			else:
				print("Invalid Product ID...!!!")
		if(len(purchase_no) != 0):
			generate_bill(user_id, prod_id, price, time_date, purchase_no,
						name, origin, quantity_all, transaction_id)
	else:
		print("User ID Doesn't Exists...!!!")
	js = json.dumps(data)
	fd = open("data.json", 'w')
	fd.write(js)
	fd.close()
	js = json.dumps(user_data)
	fd = open("user_data.json", 'w')
	fd.write(js)
	fd.close()


while (1):
	print("Choose Any One of The Following :- ")
	print("1)Admin")
	print("2)User")
	print("3)Exit")
	print("Enter Your Choice Here :- ")
	n = int(input())
	if (n == 1):
		admin()
	elif (n == 2):
		user()
	elif (n == 3):
		break
	else:
		print("Invalid Choice...!!!")

