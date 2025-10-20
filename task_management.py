# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
from datetime import datetime
class Task:
    def __init__(self, title, description, due_date, priority, assigned_to, assigned_by):
        self.title=title
        self.description=description
        self.due_date=due_date
        self.priority=priority
        self.assigned_to= assigned_to
        self.assigned_by =assigned_by
        
class TaskExecutor:
    def __init__(self, reminder_system):
        self.reminder_system = reminder_system
    
    def assign_task(self, task, user):
        task.assigned_to = user
        print(f'Task {task.title} is assigned to {user}')
    
    def mark_complete(self, task):
        task.status = 'completed'
        print(f'Task {task.title} marked as completed!')
    
    def remind_task(self, task):
        if (task.due_date - datetime.now()).days <=3:
            self.reminder_system.notify(task)


class TaskObsever:
    def update(self, task):
        raise NotImplementedError

   
class EmailNotifier(TaskObsever):
    def update(self, task):
        print(f"Remnder: Task {task.title} is due soon!")
        
class ReminderSystem:
    def __init__(self):
        self.observers = []
    
    
    def register(self, observer: TaskObsever):
        self.observers.append(observer)
    
    def notify(self, task):
        for obs in self.observers:
            obs.update(task)
    
    
if __name__=='__main__':
    reminder_system = ReminderSystem()
    reminder_system.register(EmailNotifier())
    executor = TaskExecutor(reminder_system=reminder_system)
    task1 = Task("Submit Report", "Submit Q4 report", datetime(2025,10,20), "High", "Pranali", "Pranali")
    executor.assign_task(task1, "Pranali")
    executor.remind_task(task1)
    executor.mark_complete(task1)

    
        
        
        
        
