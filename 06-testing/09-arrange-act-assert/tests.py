import pytest
from datetime import date, timedelta
from calendars import CalendarStub
from tasks import Task, TaskList

def test_creation():
    today = date(2000,1,1)
    calendar = CalendarStub(today)

    sut = TaskList(calendar)

    assert len(sut) == 0
    assert sut.due_tasks == []
    assert sut.overdue_tasks == []
    assert sut.finished_tasks == []

def test_adding_task_with_due_day_in_future():
    today = date(2000,1,1)
    tomorrow = today + timedelta(days=1)
    calendar = CalendarStub(today)
    task = Task('description',tomorrow)
    sut = TaskList(calendar)

    sut.add_task(task)


    assert len(sut) == 1
    assert sut.due_tasks == [task]

def test_adding_task_with_due_day_in_past():
    today = date(2000,1,1)
    yesterday = today - timedelta(days=1)
    calendar = CalendarStub(today)
    task = Task('description', yesterday)
    sut = TaskList(calendar)

    with pytest.raises(RuntimeError):
        sut.add_task(task)

    assert len(sut) == 0

def test_task_becomes_overdue():
    today = date(2000,1,1)
    tomorrow = today + timedelta(days=1)
    next_week = today + timedelta(days=7)
    calendar = CalendarStub(today)
    task = Task('description', tomorrow)
    sut = TaskList(calendar)
    sut.add_task(task)

    calendar.today = next_week

    assert sut.overdue_tasks == [task]

def test_task_becomes_finished():
    today = date(2000,1,1)
    tomorrow = today + timedelta(days=1)
    calendar = CalendarStub(today)
    task = Task('description', tomorrow)
    sut = TaskList(calendar)
    sut.add_task(task)

    task.finished = True

    assert sut.due_tasks == []
    assert sut.finished_tasks == [task]

