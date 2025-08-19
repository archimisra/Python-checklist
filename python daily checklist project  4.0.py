
def create_checklist():
    """allows the user to input the task for the day"""
    tasks = []
    print("enter your tasks for the day(type a'done' when finished): ")
    while True:
        task = input(">")
        if task.lower() == 'done':
            break
        tasks.append(task)
    return tasks

def review_tasks(initial_tasks):
    """review tasks and categorizes them into complete and incomplete."""
    completed_tasks = []
    incomplete_tasks = []

    print("\nReview your tasks:")
    for task in initial_tasks:
            status = input(f"Did you complete '{task}'? (yes/no): ")
            if status == 'yes':
                completed_tasks.append(task)
            else:
                incomplete_tasks.append(task)
    return completed_tasks, incomplete_tasks
def display_summary(completed, incomplete):
        """Displays a summary of completed and incomplete tasks."""
        print("\n---Daily Task Summary---")
        print("completed tasks:")
        if completed:
            for task in completed:
                print(f"-{task}")
        else:
            print("no tasks completed today.")

            print("\nIncomplete tasks: ")
            if incomplete:
                for task in incomplete:
                    print(f"-{task} (needs attention)")
            else:
                print("all tasks completed!")


 #main program starts from here(not inside the function)
if __name__ == "__main__" :
   daily_checklist = create_checklist()
   if daily_checklist:
      completed, incomplete = review_tasks(daily_checklist)
      display_summary(completed, incomplete)
   else:
       print("no tasks were added for today.")

   input("\nPress enter to exit....")