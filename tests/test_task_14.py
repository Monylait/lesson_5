import pytest
import random as rnd
import tasks.task_14 as task_14


@pytest.mark.task_14
def test_fizz_buzz():
    assert "Fizz" == task_14.fizz_buzz(6)
    assert "Buzz" == task_14.fizz_buzz(5)
    assert "Buzz" == task_14.fizz_buzz(10)
    assert "FizzBuzz" == task_14.fizz_buzz(15)
