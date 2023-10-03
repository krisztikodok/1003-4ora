#funcitons
def init(x):
  print(2*x)

init(3)

"""
def valami():
  pass #nem csinál semmit
"""
def hello(myname):
  print("Hello "+myname+"!")

hello("Emilia")

def fullname(a,b):
  print(a+" "+b)

fullname("Kovács","Béla")

#function input is a list:
def kindergarden(*kids):     #arg nr is unknown: *
  size=len(kids)
  print("There are ", size ," kids in out group.")
  print("The youngest is "+kids[4]+".")

kindergarden("Anna","Caren","Billy","Junior","Dave")

#számtani/mértani közép,átlag

#https://www.geeksforgeeks.org/sorting-algorithms/
#rendezések - bubble
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

numbers = [64, 34, 25, 12, 22, 11, 90]
print("\n---Bubble sort---\nOriginal list:", numbers)
print("Sorted list:", bubble_sort(numbers))

#rendezések - selection
def selection_sort(lst):
    for i in range(len(lst)):
        min_idx = i
        for j in range(i+1, len(lst)):
            if lst[min_idx] > lst[j]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst


numbers = [64, 34, 25, 12, 22, 11, 90]
print("\n---Selection sort---\nOriginal list:", numbers)
print("Sorted list:", selection_sort(numbers))


#rendezések - insertion

#rendezések - merge

#rendezések - quicksort

#rendezések - heap

#rendezések - cocktail



#invert a string
def reverse_string(input_string):
    return input_string[::-1]

print(reverse_string("Hello, World!"))