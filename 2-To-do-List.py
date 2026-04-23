"""
Advanced To-Do List Application
A task management system with file persistence, task completion tracking,
and a user-friendly menu interface.
"""
import json
import os
from datetime import datetime


class TodoListManager:
    """Manages tasks with file storage and manipulation."""
    
    def __init__(self, filename: str = "tasks.json"):
        """
        Initialize the To-Do List Manager.
        
        Args:
            filename: JSON file to store tasks
        """
        self.filename = filename
        self.tasks = []
        self.load_tasks()
    
    def load_tasks(self):
        """Load tasks from JSON file if it exists."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    self.tasks = json.load(file)
            except (json.JSONDecodeError, IOError):
                self.tasks = []
        else:
            self.tasks = []
    
    def save_tasks(self):
        """Save tasks to JSON file."""
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.tasks, file, indent=4)
            print("✅ Tasks saved successfully!\n")
        except IOError as e:
            print(f"❌ Error saving tasks: {e}\n")
    
    def add_task(self, title: str, priority: str = "medium") -> None:
        """
        Add a new task to the list.
        
        Args:
            title: Task description
            priority: Priority level (low/medium/high)
        """
        if not title.strip():
            print("❌ Task title cannot be empty!\n")
            return
        
        task = {
            "id": len(self.tasks) + 1,
            "title": title.strip(),
            "priority": priority.lower(),
            "completed": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"✅ Task added: '{title}' (Priority: {priority})\n")
    
    def view_all_tasks(self) -> None:
        """Display all tasks in a formatted table."""
        if not self.tasks:
            print("📭 No tasks available! Add a task to get started.\n")
            return
        
        print("\n" + "=" * 80)
        print(f"{'ID':<4} {'Status':<10} {'Title':<35} {'Priority':<10} {'Created':<20}")
        print("=" * 80)
        
        for task in self.tasks:
            status = "✅ Done" if task["completed"] else "⏳ Pending"
            priority_display = task["priority"].upper()
            print(f"{task['id']:<4} {status:<10} {task['title']:<35} "
                  f"{priority_display:<10} {task['created_at']:<20}")
        
        print("=" * 80 + "\n")
    
    def view_pending_tasks(self) -> None:
        """Display only incomplete tasks."""
        pending_tasks = [task for task in self.tasks if not task["completed"]]
        
        if not pending_tasks:
            print("🎉 All tasks completed! Great job!\n")
            return
        
        print("\n" + "=" * 80)
        print(f"{'ID':<4} {'Title':<35} {'Priority':<10} {'Created':<20}")
        print("=" * 80)
        
        for task in pending_tasks:
            print(f"{task['id']:<4} {task['title']:<35} "
                  f"{task['priority'].upper():<10} {task['created_at']:<20}")
        
        print("=" * 80 + "\n")
    
    def mark_complete(self, task_id: int) -> None:
        """
        Mark a task as completed.
        
        Args:
            task_id: ID of the task to complete
        """
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                self.save_tasks()
                print(f"✅ Task '{task['title']}' marked as completed!\n")
                return
        
        print(f"❌ Task with ID {task_id} not found!\n")
    
    def delete_task(self, task_id: int) -> None:
        """
        Delete a task from the list.
        
        Args:
            task_id: ID of the task to delete
        """
        for i, task in enumerate(self.tasks):
            if task["id"] == task_id:
                deleted_title = task["title"]
                self.tasks.pop(i)
                # Recalculate IDs
                for j, t in enumerate(self.tasks):
                    t["id"] = j + 1
                self.save_tasks()
                print(f"🗑️ Task deleted: '{deleted_title}'\n")
                return
        
        print(f"❌ Task with ID {task_id} not found!\n")
    
    def update_task(self, task_id: int, new_title: str) -> None:
        """
        Update a task's title.
        
        Args:
            task_id: ID of the task to update
            new_title: New task title
        """
        if not new_title.strip():
            print("❌ Task title cannot be empty!\n")
            return
        
        for task in self.tasks:
            if task["id"] == task_id:
                old_title = task["title"]
                task["title"] = new_title.strip()
                self.save_tasks()
                print(f"✏️ Task updated: '{old_title}' → '{new_title}'\n")
                return
        
        print(f"❌ Task with ID {task_id} not found!\n")
    
    def get_statistics(self) -> None:
        """Display task statistics."""
        total = len(self.tasks)
        completed = sum(1 for task in self.tasks if task["completed"])
        pending = total - completed
        
        print("\n" + "=" * 40)
        print("📊 TASK STATISTICS")
        print("=" * 40)
        print(f"Total Tasks: {total}")
        print(f"Completed: {completed}")
        print(f"Pending: {pending}")
        if total > 0:
            completion_rate = (completed / total) * 100
            print(f"Completion Rate: {completion_rate:.1f}%")
        print("=" * 40 + "\n")
    
    def display_menu(self) -> None:
        """Display main menu and handle user interactions."""
        while True:
            print("=" * 50)
            print("📝 TO-DO LIST APPLICATION")
            print("=" * 50)
            print("1. Add Task")
            print("2. View All Tasks")
            print("3. View Pending Tasks")
            print("4. Mark Task Complete")
            print("5. Update Task")
            print("6. Delete Task")
            print("7. View Statistics")
            print("8. Exit")
            print("=" * 50)
            
            choice = input("Enter your choice (1-8): ").strip()
            
            if choice == "1":
                title = input("Enter task title: ").strip()
                priority = input("Enter priority (low/medium/high) [default: medium]: ").strip() or "medium"
                if priority not in ["low", "medium", "high"]:
                    print("❌ Invalid priority! Using 'medium'.\n")
                    priority = "medium"
                self.add_task(title, priority)
            
            elif choice == "2":
                self.view_all_tasks()
            
            elif choice == "3":
                self.view_pending_tasks()
            
            elif choice == "4":
                self.view_all_tasks()
                try:
                    task_id = int(input("Enter task ID to mark complete: "))
                    self.mark_complete(task_id)
                except ValueError:
                    print("❌ Invalid ID! Please enter a number.\n")
            
            elif choice == "5":
                self.view_all_tasks()
                try:
                    task_id = int(input("Enter task ID to update: "))
                    new_title = input("Enter new title: ").strip()
                    self.update_task(task_id, new_title)
                except ValueError:
                    print("❌ Invalid ID! Please enter a number.\n")
            
            elif choice == "6":
                self.view_all_tasks()
                try:
                    task_id = int(input("Enter task ID to delete: "))
                    confirm = input("Are you sure? (yes/no): ").lower()
                    if confirm == "yes":
                        self.delete_task(task_id)
                except ValueError:
                    print("❌ Invalid ID! Please enter a number.\n")
            
            elif choice == "7":
                self.get_statistics()
            
            elif choice == "8":
                print("👋 Thanks for using To-Do List! Goodbye!\n")
                break
            
            else:
                print("❌ Invalid choice! Please try again.\n")


def main():
    """Entry point of the application."""
    todo_manager = TodoListManager()
    todo_manager.display_menu()


if __name__ == "__main__":
    main()
