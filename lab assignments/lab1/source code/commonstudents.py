# list of students who took python
Python = {"Kiran Rao", "Vinay", "Bhavesh", "kranthi", "Yuvesh", "vinnetha", "shrisha"}

# list of students who took web
web = {"kamal", "Bhavesh", "kranthi", "Yuvesh", "karthik"}

# printing the common students who took both python and web using & operator
print(Python & web)

# storing the list of students who took only python to the variable 'a'
a = Python-web

# storing the list of students who took only web to the variable 'a'
b = web-Python

# printing the list of students who are not in common in both python and web
print(a.union(b))