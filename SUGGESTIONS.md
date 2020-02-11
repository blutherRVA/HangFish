# Suggestions

I'm pretty impressed with what you've done here, this must have taken you quite a while because it took me a while to re-implement it. There definitely is some room for improvement though and the rest of this document will focus on explaining how to improve it.
You seem to be at the stage where you have a pretty strong grasp on control flow and how to import modules and invoke methods, the next thing you want to focus on is not just something that works, but something that is organized.
I'm mostly going to provide feedback on version 3 of your script since you have the most code there.

## Naming Files: use `kebab-caseed-file-names.py` to name your files

- MacOS and Windows do not have case sensitive file systems so `Hello World.py` will be seen as the same filename as `hello world.py` on these systems. Linux does (in general) have a case sensitive file system so when you make mistakes with imports, which happens to everyone, your modules will not be able to load. For that reason people mostly use lower cased file names.
- Also, use a `-` dash instead of spaces. We use `-` instead of space so that you don't have to `\` escape the spaces in the terminal when typing out the filepath. This may seem like a nitpick right now but it will make more sense when you start writing command line utilities and you want to pass arguments to those scripts through the command line.
- Include the `.py` file extension as this will automatically give you syntax highlighting in github and in your editor of choice. It also just helps people understand your code at a glance.

## Code Structure

- Use modules
  - read these docs, you will find them very helpful for organizing your code
  - https://docs.python.org/3/tutorial/modules.html
  - https://docs.python.org/3/reference/import.html
  - as a general principal, one module === do one thing

## Best Practices

Dependency management is an important thing to pay attention to. Python has built in modules, but also 3rd party modules that can be installed easily with the dependency manager `pip` that ships with python. You have a few external dependencies

You want to always put your import statements at the very top of your module before you do anything else. I would hoist these statements above the rest of your code.

```python
import random
# Initiate turtle module, window
import turtle
```

## Managing External Dependencies

You will often find yourself working with multiple python projects on the same computer. Python manages dependencies globally, so when you run `pip install random3rdpartymodule` it will install `random3rdpartymodule` globally, so every Python project on your system will have access to that installation. Often you will have projects that depend on a specific version of a dependency and you cannot have two versions of a dependency installed side by side in the same python installation. You can hopefully see how this might become a problem quickly. Different languages handle this in different ways, but python uses something called virtual environments, which basically creates multiple "copies" of python in your environment and lets you switch between them. Virtualenvwrapper makes this easier to manage.

- https://docs.python-guide.org/dev/virtualenvs/
- https://virtualenvwrapper.readthedocs.io/en/latest/
  - this can be a challenge to setup but it's worth it to stay organized

## Code Style

### Linting

Programming languages have a grammar and syntax that are non-optional but beyond that there are code style conventions for each language that most people adhere to. There is something called "linting" that will automatically help you avoid both style and syntax mistakes _before_ you run your code. You can think about this kind of like a highly configurable spell checker with various "rules" that you can configure. You can invoke these tools using the command line but most of the time they will be integrated with your editor and will show you issues as you type, but you will have to do some setup. Teams will add and remove these rules and enforce them automatically using the linter from the command line in their code integration pipelines. Some will be turned on as warnings and others will be strictly enforced. Some linters can also automatically "fix" some issues in your code and automatically format it for you. For example `autopep8` will automatically format your python code.

Python is somewhat unique in that the language maintainers have provided a recommended style guide that is widely conformed to within the industry, this is called PEP-8 and it is a good thing to know. Most teams writing python use [PEP-8](https://www.python.org/dev/peps/pep-0008/) as a baseline and then relax some of its recommendations and add others so that the style is consistent across the codebase. Writing "Clean Code" will help you greatly both in reading and maintaining your own code, but also sharing it.

This isn't going to be terribly important right now but I recommend that you start learning about it because it will put you ahead of the pack in many ways.

https://dbader.org/blog/python-code-linting
https://www.python.org/dev/peps/pep-0008/

## Modules, Classes, Functions

You should organize your code by purpose into modules.
Generally you want one module to contain one "thing", this can be a class or a function or a group of constants.
Rather than having a bunch of code at the top level of one module, break things up into classes and functions that group and encapsulate a particular "functionality" or a group of related functionalities.
Classes can be used to encapsulate state.
You create instances of a class, and you should read up on this.
https://docs.python.org/3/tutorial/classes.html

Using these features will help you DRY (Dont Repeat Yourself) out your code, which is a desireable quality.

## List comprehensions

There are some places where I've used the following syntax, which is used to iterate through an existing list and create a new one.

https://www.programiz.com/python-programming/list-comprehension
https://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/

```python
[ thing for thing in listOfThings ]
```

## General Recommendations

- don't deeply nest if statements, at most you should have one if statement nested inside another. If you find that you have three or more, it's a good indication that you need to break things up into functions.
- don't use single letter variable names, those are convenient but they make it harder for other people to read your code.
- if **name** == '**main**':
  - https://stackoverflow.com/questions/419163/what-does-if-name-main-do
- use magic methods to make things iterable https://rszalski.github.io/magicmethods/
- learn about string formatting https://docs.python.org/3/library/string.html
- use data structures https://docs.python.org/3/tutorial/datastructures.html
- \*\*kwargs syntax https://realpython.com/python-kwargs-and-args/
