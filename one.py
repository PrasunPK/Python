import sys

# parameter passing in functions an dintro to functions
# def factorial(no):
#     if no == 0 or no == 1:
#         return 1;
#     return no * factorial(no-1)
#
# print "Factorial of 6 is ", factorial(6)

# overriding previous arguments
# i = 4
# def f(arg=i):
#     print arg
# f()

# appending in an array an printing
# def f(arg, ar=[]):
#     ar.append(arg)
#     return ar
#
# print f(1)
# print f(2)
# print f(3)

#keyword paramenters and arguments
# def fun(time, hour=13,day="None"):
#     print "Now : ",time
#     print "Hour : ",hour
#     print "Day : ", day
#
# fun(01)
# fun(13,hour=12)
# fun(time='12:55',hour='8',day='Sunday')
# fun(time=12)

#usages of passing
# def fun(a):
#     pass
#
# fun(a=10)

#prioritizing parameters in function arguments
# def doSomething(arg, *arg1, **arg2):
#     print "First argument ", arg
#     print "Second argument ", arg1
#     print "Third argument ", arg2.keys()
#
# # doSomething(0)
# doSomething(0,1,2,3,newArg=10,testArg='hello')

#Object and function parameters
# '*' takes like function parameters (1,2,3)
# '**' takes like objects. any object operations can be done using this
# def showDetails(name,age,occupation):
#     print "Name : ",name
#     print "Age : ",age
#     print "Occupation : ",occupation
#
# arg = {"name":"John","age":22,"occupation":"Engineer"}
# arg1 = {"name":"Jaccob","age":21,"occupation":"Teacher"}
#
# showDetails(**arg)
# showDetails(**arg1)

#list operations
# def main():
#     a = [3,4,1,6,3,9,17]
#     # print a.count(3) #counts the elements given to it
#     a.insert(1,99)
#     a.append(10)
#     # print a.index(3)
#     print a
#     a.reverse()
#     a.pop()
#     print a
#
# main()

#Queue operations
# from collections import deque
# def collection():
#     queue = deque(['John','Ravi','Suhas'])
#     queue.append('Ferra')
#     print queue
#
# collection()

#map filter reduce using function
# def square(x): return x*x
# def isEven(x): return x%2 == 0
# def sum(x,y): return x+y
# def operate():
#     mapped = map(square, range(1,11))
#     print "Mapped with square : ",mapped
#     filtered = filter(isEven, range(1,11))
#     print "Filtered by evens : ", filtered
#     reduced = reduce(sum, range(1,11))
    # print "Reduced to sum : ", reduced
#
# operate()

#combinaton of numbers
# def combinaton():
#     print [(x, y) for x in [1,2,3] for y in [1,2,3] if x != y]
#
# combinaton()


#command line argument
def showArguments():
    print sys.argv

showArguments()
