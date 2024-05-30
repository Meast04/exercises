import pytest
from datetime import date, timedelta
from calendars import CalendarStub
from tasks import Task, TaskList


def today():
    return date(2000,1,1)

def tomorrow():
    return today() + timedelta(days=1)

def yesterday():
    return today() - timedelta(days=1)

def create_calendar():
    return CalendarStub(today())


def create_empty_task_list(calendar=None):
    calendar = calendar or create_calendar()
    return TaskList(calendar)

def create_task(*,description = 'default',due_date = None, finished = False):
    due_date = due_date or date(2000,1,1)
    task = Task(description,due_date)
    if finished:
        task.finished = True
    return task



def test_creation():
    sut = create_empty_task_list()

    assert len(sut) == 0
    assert sut.due_tasks == []
    assert sut.overdue_tasks == []
    assert sut.finished_tasks == []

def test_adding_task_with_due_day_in_future():
    
    sut = create_empty_task_list()
    task = create_task(due_date=tomorrow())

    sut.add_task(task)


    assert len(sut) == 1
    assert sut.due_tasks == [task]

def test_adding_task_with_due_day_in_past():

    task = create_task(due_date=yesterday())
    sut = create_empty_task_list()

    with pytest.raises(RuntimeError):
        sut.add_task(task)

    assert len(sut) == 0


def test_task_becomes_overdue():

    next_week = today() + timedelta(days=7)
    task = create_task(due_date=tomorrow())
    calendar = create_calendar()
    sut = create_empty_task_list(calendar=calendar)
    sut.add_task(task)

    calendar.today = next_week

    assert sut.overdue_tasks == [task]

def test_task_becomes_finished():

    task = create_task(due_date=tomorrow())
    sut = create_empty_task_list()
    sut.add_task(task)

    task.finished = True

    assert sut.due_tasks == []
    assert sut.finished_tasks == [task]

