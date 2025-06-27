from datetime import date
import json
import os
class Habit:
    def __init__(self):
        self.tasks=[]
        self.com={}
        self.load_data()
    def save_data(self):
        data={"task":self.tasks,"completed":self.com}
        with open("habit_data.json","w") as f:
            json.dump(data,f)
            
    def load_data(self):
        if os.path.exists("habit_data.json"):
            with open("habit_data.json","r") as f:
                data=json.load(f)
                self.tasks=data.get("tasks",[])
                self.com=data.get("com",{})
                
    def add(self,task):
        task=[t.strip().lower() for t in task.split(',')]
        self.tasks.extend(task)
        self.save_data()
        
    def delete(self,task):
        task=task.strip().lower() 
        if task in self.tasks:
            self.tasks.remove(task)
            print("Your task is removed successfully")
        else:
            print("Task not found! Try again")
        self.save_data()
        
    def mark(self,task,st=None):
        task=task.strip().lower()
        if st is None:
            st=date.today().strftime("%d-%m-%y")
        if task in self.tasks:
            if st not in self.com:
                self.com[st]=[]
            self.com[st].append(task)
            print("Task {} is marked on {}".format(task,st))
        self.save_data()
        
    def streak(self):
        streak=0
        for date in sorted(self.com):
            completed=set(self.com[date])
            required=set(self.tasks)
            if(completed==required):
                streak+=1
            else:
                break
        print("Your current streak is {}".format(streak))  
o=Habit()
while True:
    print("--Habit Tacker--")
    print("1.To Add the tasks")
    print("2.To Delete a Task")
    print("3.Mark tasks done")
    print("4.View Streak")
    print("5.View Tasks")
    print("6.Exit")
    try:
        n = int(input("Enter a number: "))
        if n == 1:
            task = input("Enter your task to add and separate them with commas:")
            o.add(task)
        elif n == 2:
            task = input("Enter the task you want to delete: ")
            o.delete(task)
        elif n == 3:
            task = input("Enter the task you completed: ")
            o.mark(task)
        elif n == 4:
            o.streak()
        elif n == 5:
            print("Your current tasks are:", o.tasks)
        elif n == 6:
            print("Thank You!")
            exit()
        else:
            print("Invalid Choice, Please try again!")
    except ValueError:
        print("Please enter a valid number!")

            
