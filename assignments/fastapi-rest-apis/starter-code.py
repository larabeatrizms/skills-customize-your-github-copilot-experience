# Starter Code: REST APIs with FastAPI

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Task(BaseModel):
    title: str
    completed: bool = False


tasks = [
    {"id": 1, "title": "Review FastAPI basics", "completed": False},
    {"id": 2, "title": "Build first endpoint", "completed": True},
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the Student Task Tracker API"}


@app.get("/tasks")
def get_tasks():
    return tasks


@app.post("/tasks")
def create_task(task: Task):
    new_id = max([item["id"] for item in tasks], default=0) + 1
    new_task = {"id": new_id, **task.model_dump()}
    tasks.append(new_task)
    return {"message": "Task created", "task": new_task}


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    for item in tasks:
        if item["id"] == task_id:
            item["title"] = task.title
            item["completed"] = task.completed
            return {"message": "Task updated", "task": item}
    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for index, item in enumerate(tasks):
        if item["id"] == task_id:
            removed_task = tasks.pop(index)
            return {"message": "Task deleted", "task": removed_task}
    raise HTTPException(status_code=404, detail="Task not found")


# Run locally with:
# uvicorn starter-code:app --reload
