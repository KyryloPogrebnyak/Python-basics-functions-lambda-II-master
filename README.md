# Python-basics-functions-lambda-II-master
# Lambda functions II

## Description

In this exercise, we will get used to creating and using lambda functions on decorators and other high-order functions.

*In each function created throughout these exercises the body of the function must contain a **dosctring** (a first line with a string explaining what the function does).*

##

## Tasks

###

### Task 1

Sort the following list of tuples using Lambda. The `sort()` method of list objects has a parameter named `key` that takes a function returning the value to use as a reference for the sorting.

Your task is to pass a lambda function as argument to the `key` parameter of the `sort()` method of `subject_marks` so that the tuples are sorted according to the marks.

```
subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
subject_marks.sort(key=**your_lambda_function**)
print(subject_marks)
```

- Your result should look like this:

```
[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
```

###

### Task 2

Use the built-in `filter()` function to filter a list of integers to get only those that are even using a lambda function.

The `filter()` function takes two arguments: a function and an iterable. The function should return a Boolean indicating if a particular value matches our query.

Use the following iterable on your call to `filter()`:

```
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

- Your result should look like this:

```
[2, 4, 6, 8, 10]
```