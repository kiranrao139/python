# creating a class Employee
class Employee:

  # creating a data member to count the number of employees
  employee_count=0

  # creating a data member to count the total of employees
  totalSalary = 0

  #  Creating a default constructor to initialize name, family, salary, department of the employees
  def __init__(self,ename,family,sal,depart):

      self.ename=ename
      self.family=family
      self.sal=sal
      self.depart=depart

      # counting the number of employees
      Employee.employee_count+=1

      # counting the total salary of the employees
      Employee.totalSalary += self.sal

      # after counting the total no. of employees, it calls the following function
      # to find the average salary of the employees
      if(Employee.employee_count == 4):
        self.averageSal()

  def averageSal(self):
      print("\nAverage salary:", self.totalSalary/Employee.employee_count)

  # this method is written to display the details of all the employees
  def display(self):
      print("\nname:",self.ename,"family:",self.family,"salary:",self.sal,"department:",self.depart)

# using inheritance concept here. It acquiring the properties of the Employee class
class FulltimeEmployee(Employee):
    def __init__(self,n,f,s,d):
        Employee.__init__(self,n,f,s,d)


emplpoyee1=Employee("kiran,","son,",1000,"chairman")
emplpoyee2=Employee("srikanth,","son,",1500,"generalmanager")
emplpoyee3=Employee("keerthi,","friend,",2000,"executive")
emplpoyee4=Employee("varsha,","friend,",3000,"programmer")

emplpoyee1.display()
emplpoyee2.display()
emplpoyee3.display()
emplpoyee4.display()

# printing the total number of employees
print("\ntotal employees", Employee.employee_count)

