"""
#funcitons
def init(x):
  print(2*x)

init(3)


def valami():
  pass #nem csinál semmit

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
"""
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
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key
    return lst
numbers = [64, 34, 25, 12, 22, 11, 90]
print("\n---Insertion sort---\nOriginal list:", numbers)
print("Sorted list:", insertion_sort(numbers))

#rendezések - merge
def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left_list = merge_sort(lst[:mid])
    right_list = merge_sort(lst[mid:])

    return merge(left_list, right_list)

def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0

    # Merge smaller elements first
    while left_list_index < len(left_list) and right_list_index < len(right_list):
        if left_list[left_list_index] <= right_list[right_list_index]:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1
        else:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1

    # If left list has more items, append them to sorted_list
    while left_list_index < len(left_list):
        sorted_list.append(left_list[left_list_index])
        left_list_index += 1

    # If right list has more items, append them to sorted_list
    while right_list_index < len(right_list):
        sorted_list.append(right_list[right_list_index])
        right_list_index += 1

    return sorted_list

print("\n---Insertion sort---\nUnsorted:")
numbers = [4, 2, 9, 6, 5, 1]
for i in numbers:
  print(i,end=" ")
sorted_numbers = merge_sort(numbers)
print("\nSorted: ")
for i in sorted_numbers:
  print(i,end=" ")
  

#rendezések - quicksort
def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        pivot = lst[0]
        less_than_pivot = [element for element in lst[1:] if element <= pivot]
        greater_than_pivot = [element for element in lst[1:] if element > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

print("\n---Quick sort---\nUnsorted:")
numbers = [4, 2, 9, 6, 5, 1]
for i in numbers:
  print(i,end=" ")
sorted_numbers = quick_sort(numbers)
print("\nSorted: ")
for i in sorted_numbers:
  print(i,end=" ")

#rendezések - heap

#rendezések - cocktail


"""
#invert a string
def reverse_string(input_string):
    return input_string[::-1]

print(reverse_string("Hello, World!"),"\n")

#passing a list as arg:
def fruitbowl(fruits):
  for i in fruits:
    print(i)
fruits=["banana","grapes","strawberry","blueberry","watermelone"]
fruitbowl(fruits)

#convert number to different numeric systems
def convert(num,sys):
  if sys==2:
    return print(round(num/2))
  elif sys==8:
    
convert(10.4,2)
"""

#hozam kiszámolása
def hozam(alap,ev,kamat):
  sum=(100+kamat)/100
  return alap*sum**ev

print("\n\nHOZAMOK\n")
print(hozam(100,1,5))
print(hozam(100,1,6))

#recursion
print("\n\nMicimackó, ez rekurzióóóóóóóó")

def rec(i):
  if(i>0):
    result=i+rec(i-1)
    print(result)
  else:
    result=0
  return result

print("Results:")
rec(8)