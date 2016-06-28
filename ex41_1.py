# coding=utf-8
## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass

class Dog(Animal):

	def __init__(self, name):
		## a Dog has a name
		self.name = name


class Cat(Animal):

	def __init__(self, name):
		## a Cat has a name
		self.name = name

## a person has a name and salary
class Person(object):

	def __init__(self, name):
		## Person has-a name
		self.name = name

		## Person has-a pet of some kind
		self.pet = None

## a Employee is a person
class employee(Person):

	def __init__(self, name, salary):
		## ?? hmm what is this strange magic?
		super(Employee, self).__init__(name)
		## ??
		self.salary = salary

## has-a
class Fish(object):
	pass


## Salmon is-a Fish
class Salmon(Fish):
	pass


## Halibut is-a Fish
class Halibut(Fish):
	pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")


