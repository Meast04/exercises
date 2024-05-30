import pytest
from datetime import date, timedelta
from calendars import CalendarStub
from tasks import Task, TaskList


@pytest.fixture
def today():
    return date(2000,1,1)

@pytest.fixture
def tomorrow(today):
    return today + timedelta(days=1)

@pytest.fixture
def yesterday(today):
    return today - timedelta(days=1)

@pytest.fixture
def calendar(today):
    return CalendarStub(today)

@pytest.fixture
def sut(calendar):
    return TaskList(calendar)

def test_creation(sut):


    assert len(sut) == 0
    assert sut.due_tasks == []
    assert sut.overdue_tasks == []
    assert sut.finished_tasks == []

def test_adding_task_with_due_day_in_future(sut,tomorrow):

    task = Task('description',tomorrow)

    sut.add_task(task)


    assert len(sut) == 1
    assert sut.due_tasks == [task]

def test_adding_task_with_due_day_in_past(sut,yesterday):

    task = Task('description', yesterday)

    with pytest.raises(RuntimeError):
        sut.add_task(task)

    assert len(sut) == 0

def test_task_becomes_overdue(sut,today,tomorrow,calendar):
   
    next_week = today + timedelta(days=7)
    task = Task('description', tomorrow)
    sut.add_task(task)

    calendar.today = next_week

    assert sut.overdue_tasks == [task]

def test_task_becomes_finished(sut,tomorrow):

    task = Task('description', tomorrow)
    sut.add_task(task)

    task.finished = True

    assert sut.due_tasks == []
    assert sut.finished_tasks == [task]

