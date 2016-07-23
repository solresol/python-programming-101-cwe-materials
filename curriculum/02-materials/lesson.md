---
title: Python Programming 101
duration: "2:50"
creator:
    name: J Rogel-Salazar
    city: LDN
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Python Programming 101

### LEARNING OBJECTIVES
*After this lesson, you will be able to:*

- Discuss the history of Python and its use across different industries.
- Define how Python compares to other programming languages.
- Describe the benefits of a Python workflow when working with data.
- Demonstrate basic Python programming fundamentals to solve real world problems.
- Create a custom learning plan to help you continue to build fundamental python skills after this workshop.

### STUDENT PRE-WORK
*Before this lesson, you should already be able to:*

- Bring a laptop with [Anaconda](https://www.continuum.io/downloads) using [Python 2.7](https://www.python.org/download/releases/2.7/) installed. Note: Make sure to choose the *Python 2.7* version for your operating system. 
- If you are using a PC, also install [git-bash terminal](https://git-for-windows.github.io).
- *Optional*: Install a text editor like [Sublime Text 3](http://www.sublimetext.com) or [Atom](https://atom.io) on your computer. If you are using Anaconda, **Spyder** is included in the distribution.

### INSTRUCTOR PREP
*Before this lesson, instructors will need to:*

- Review & modify lesson plan & slide deck
- Write learning objectives & relevant information on board
- Review Student Roster and Instructor Checklist
- Prepare handout to distribute to students.

### WORKSHOP AGENDA
| TIMING  | TYPE  | TOPIC  |
|:-:|---|---|
| 10 min  | [Opening](#opening)  | Greetings + The GA Experience  |
| 15 min  | [Introduction](#intro1)   | Why Python? What Can Python Do For Me? |
| 15 min  | [Demo](#demo1)  | Implementing Python into your Workflow |
| 20 min  | [Guided Practice](#guided-practice1)  | Installing & Configuring Common Python Libraries |
| 20 min  | [Independent Practice](#ind-practice1)  | Applying Python Pseudocode to Sample Data |
| 5-10 min  | BREAK  |   |
| 15 min  | [Introduction](#intro2)   | Python Programming Fundamentals |
| 15 min  | [Demo](#demo2)  | Writing Programs in Python   |
| 20 min  | [Guided Practice](#guided-practice2)  | Dive into Data with Python   |
| 20 min  | [Independent Practice](#ind-practice2)  | More Python Practice |
| 10 min  | [Conclusion](#conclusion) | Review + Recap |
| 10 min  | [Takeaways](#takeaway) | Learning Plan + Q&A |

---

<a name="opening"></a>
## Opening (10 mins)

> Note: Let people know where restrooms and kitchen are located, as needed.

#### Instructor Bio

Welcome to Python Programming 101! Here's a bit about me:

> Provide your name and brief bio, including: your background in python programming, any experience you've had with GA, and one "fun fact" about yourself.

#### Introduce Yourselves

Before we dive in, a bit about you!

> Have students introduce themselves: name, what brings them to GA (ask for their current career & any specific goals), & one "fun fact".

> **Example Exercise**: *Have students submit their info one per line on a CSV file (via google doc, etc). Instructors can then use Python to briefly analyse and pull out interesting information (e.g. create dictionary, append, sort, etc).*


#### Our Expectations

- You're ready to take charge of your learning experience.
- You've installed Anaconda & Python 2.7.
- You're interested in learning about Python!

#### Our Objectives

> Note: Write workshop objectives on board before class

What we’ll cover:

* Why Python & What can Python do for me?
* Implementing Python into your workflow
* Python Libraries
* Programming (pseudocode and Python)
* Dive into data with Python

Why this topic matters:

* Programming is a sought-after skill 
* Python has been gaining popularity (why will se why!)  
Why this topic rocks:

* Python opens up a door to a variety of opportunities, from data science to research in cosmology 

> Note: Tailor these points to student interests. Relate to their career info & goals students described during attendance.

***

<a name="intro1"></a>
## Introduction: Why Python? What Can Python Do For Me? (15 mins)

**What is Python?**

- Created by Guido Van Rossum in 1991
- Emphasises **productivity** and code **readability**
	* The language is easy to pick up and learn
	* This gentle learning curve brings makes it easier for many to contribute to production level code
	* Readable code means that almost anyone can pick up a piece of code and understand what it is doing
- Interpreted, object-oriented, high-level programming language with dynamic semantics
	* **Interpreted**: Code implementations execute instructions without having to *compile* them into machine-language instruction. In contrast, compiled code is executed by the computer's CPU (hardware)
		* Interpreted code may run less quickly, but can be executed on multiple platforms without modification
	* **Object-oriented** (OO): Instead of concentrating on isolated "actions", object-orientation enables us to focus on "objects" that contain data (attributes). Objects have specific procedures, known as methods (code) that can access and modify the attributes of the object.
		* OO makes it easier to reuse code in other programs
	* **High-level programming**: Related to the code readability mentioned earlier
		* The use of language similar to natural language makes it easy to use and automate
	* **Dynamic semantics**: Once data has been specified, the machine must be instructed to perform operations on the data. Dynamic semantics (also known as execution semantics)  defines how and when the various constructs of a language should produce a program behaviour, providing flexibility at run-time.

> Instructor Note:
> 
> KNOWLEDGE CHECK
> 
> Ask students to recall what they just learned. For example get them to explain terms to each other.

**Why Python?**

* Python is extremely fun to develop in.
* Everything can be done with Python.
* If something can't be done, you can create an extension for it.
* Everything can not only be done, but it can be done fast. For example a program that takes you weeks in C++ might take you a day in Python.
* Great for prototyping, and even for usage in a commercial setting.
* Because it is a modern, elegant, highest level OO language.
* Because it is highly expressive, i.e., you will earn higher productivity.
* Because it comes with "batteries included" i.e. libraries for whatever you want.
* Because it is well documented and has a well-established and growing community.

> Instructor Note
> 
> KNOWLEDGE CHECK
> 
> Provide an example of your day-to-day work with Python.
> Ask students how they manage their data work and whether they have had any experience with Python (or any other programming languages).
> Ask students to  generate answers - why are these things good? Why does this matter?


***

<a name="demo1"></a>
## Demo: Implementing Python into Your Workflow (15 mins)

**Where is Python used?**


* Everywhere! Both in industry and Academia
* Art Middleware – Tools and Plugins
* Research
* Web Development and Web Applications
* Game Development
* Windows Applications
* You name it!

### Examples:

* Industry
	- [Drug discovery](https://www.python.org/about/success/astra/)
	- [Financial services](https://www.python.org/about/success/resolver/)
	- [Films and special effects](https://www.python.org/about/success/ilm/)
* Academia
	- [Gravitational waves](https://software.intel.com/en-us/blogs/2016/02/14/python-brings-us-the-ligo-gravity-wave-sound)
	- [Scientific visualisation](https://www.python.org/about/success/mayavi/)
	- [Biomolecule simulation](https://www.python.org/about/success/mmtk/)

> Instructor Note: Examples to be presented can be drawn from your own experience with the language. If you need inspiration, there are plenty of examples in [this page](https://www.python.org/about/success/)

**Python v other languages**

> Instructor Note:
> 
> ACTIVITY AND DISCUSSION
> 
> What other languages have the students heard of? what are they familiar with, if any? Then ask how they think those might compare to Python.

[Comparing Python to Other Languages](https://www.python.org/doc/essays/comparisons/)

Python is often compared to other interpreted languages such as Java, JavaScript, Perl, Tcl, or Smalltalk. Comparisons to C++, Common Lisp and Scheme can also be enlightening.

#### EXAMPLE
Let us what a Python program looks like, starting with the typical "Hello World!" program: In essence we are writing code to print the message "Hello World!" in the screen.

- **Python**

```python
print("hello world")
```

- **C++**

```c++
#include<iostream>
using namespace std;

int main()
{
	cout << "Hello World!";
	return 0;
}

```

The Python version of this program is very simple: one line of code that will `print` the string `'Hello World!`.  It is easy to read and understand.

The C++ version does exactly the same, but it requires us to write more information. For example we need to define a `main` function, we have to be careful with the use of punctuation (notice the semicolons at the end of some of the lines) and `cout` is not very understandable in plain terms.

Let us see the same program in Java:

- **Java**

```java
public class HelloWorld
{
    public static void main (String[] args)
    {
        System.out.println("Hello, world!");
    }
}
```

Notice that in the Java version we define the code inside the context of class.

In Object Oriented Programming a *class* is a template definition of the methods and variables in a particular kind of object. In other words, an object is a specific instance of a class: it contains actual values instead of variables.

> Instructor Note:
> 
> OTHER EXAMPLES
> 
> You are encouraged to use other specific examples of an element python does particularly well, using a simple statement or function. This depends on your familiarity with other programming languages, as well with the abilities of the students in your class.

#### Python interactive shell v scripts

In the example shown above, we are assuming that we are using an interactive shell, i.e. we are writing code that is executed immediately by the Python interpreter and we are able to "interact" with the results of the commands we pass. We can do this via:

- python shell: Look and feel similar to a terminal shell. This can be launched with:

```
> python
```

- ipython shell: Look and feel is more interesting than a plain terminal, providing syntax colouring and shortcuts to interact with our code. This can be launched with:

```
> ipython
```

- jupyter notebook: Uses a web interface that let's us use formatting along side our code and we highly recommend using it. This can be launched with:

```
> jupyter notebook
```

Alternatively, there may be instances where we do not need to interact with our Python code. Instead we may want to execute a program, in bach mode for instance, and simply get the results at the end of the execution.

In those cases we need to create a Python script. We can use any plain text editor of our choice and save the code in a file with extension `.py`.

Plain text, as you might have guessed, is rather plain. It supports standard ASCII characters, including numbers, symbols, and spaces, but does not support any type of text formatting. Therefore you cannot apply bold, italic, or underlined styles, and you cannot use different fonts or font sizes in a plain text document.

Some common plain text editors include Atom, NotePad (Win), TextEdit (Mac), Nano (Linux, Mac), NotePad++ (Win) or TextWrangler (Mac).

An alternative to using plain text editors is the use of an integrated development environment (IDE), which  provides comprehensive facilities to computer programmers for software development. A good IDE consists of a source code editor, build automation tools and a debugger as well as intelligent code completion.

Common Python IDEs:

- [PyCharm](https://www.jetbrains.com/pycharm/)
- Eclipse with [PyDev](http://www.pydev.org)
- [Atom](https://atom.io)
- Anaconda distributions (Mac, Win, Linux) come with an IDE called `Spyder`.

A barebones script for the "Hello World!" program (saved to a file called `hi.py`) looks like this:

```python
print("Hello world!")
```

To run the script by passing it as a command to the Python interpreter we need to write:

```python
> python hi.py
```

Please note that all of the code that is at indentation level 0 gets executed. Functions and classes that are defined but not on at the 0-th level indentation are not executed.

Unlike other languages, there's no `main()` function that gets run automatically - the `main()` function is implicitly all the code at the top level.

In this case, the top-level code is an if block.  `__name__` is a built-in variable which evaluates to the name of the current module. We can test whether our script is being run directly or being imported by something else by testing

```python
if __name__ == "__main__":
    ...
```

A more sophisticated version of the "Hello World!" script is therefore:

```python
def main():
	print("hello world")

if __name__ == '__main__':
    main()
```

***

## Demo: Plotly

> Instructor Note: This demo is intended to show the students some of the visualisation capabilities of Python. 
> The code in the file
[Python_101_Demo_Plotly.ipynb](./code/Python_101_Demo_Plotly.ipynb) may be more intricate than you may want the students to grasp on their own. We suggest giving the students a copy of the complete notebook above and run through the code with them in class. 
>
> Make sure the students understand that this is a demo and that some of the instructions in the demo will become clearer as the lesson progresses. It will also give them an opportunity to continue their learning process.
> 
> 
> # DISCUSSION
> 
> 1. Start by asking the students about the importance of visualising data: when is it needed? what does it add? what tools do they tend to use in their daily work (if any)? 
> 
> Instructor Note: Start a Jupyter notebook and remind the students how to use it.

### Instructions for students
We recommend using a Jupyter notebook for this demo. This makes it easier for all as it is homogenous for various environments (mac, win, linux).

1. Save the file called [Python_101_Demo_Plotly.ipynb](./code/Python_101_Demo_Plotly.ipynb) in a known location in your file system
2. Open Jupyter: in a terminal type
`jupyter notebook`
3. Navigate to the folder where you saved your file in step 1.
4. Click on the name of the file
5. Voilà, you are ready to follow the demo


<a name="guided-practice1"></a>
## Guided Practice: Installing and Configuring Common Python Libraries (20 mins)

> Instructor Note:
> ### IDE to be used
> You can show the following commands and concepts using a python/ipython shell. We encourage you to use a **Jupyter notebook** in the second part of the workshop.

### Instructions for students
We recommend using a Jupyter notebook for this guided practice. This makes it easier for all as it is homogenous for various environments (mac, win, linux).

1. Open Jupyter: in a terminal type
`jupyter notebook`
2. Navigate to an appropriate folder where your work will be saved
3. On the top-right-hand-side click in the button called "New" and select "Python 2"
4. Voilà, you are ready to type the commands we will cover below

**Packages**

Libraries of code written to solve particular set of problems

In Python there are many related packages relevant to data science: pandas, Scikit-learn, NumPy, etc

These are installed with PIP, Conda, etc. For example we can use:

`pip install <package-name>`

We saw how this was used in the demo section (see above) to install `plotly`

Other packages that are widely used:

* pandas
	* Ever used Excel? How do yo fancy working with data structured in a similar way, but without the irritation of formatting, long formulae and better graphics. Well, use *pandas*
* SciPy/NumPy
	* Does your application require the use of advanced mathematical functions or numerical operations with arrays, vectors or matrices? Try *SciPy* (scientific python) and *NumPy* (numerical python)
* Scikit-Learn
	* Are you interested in using python in a data science workflow and exploit the use of machine learning in your applications? Look no further than *Scikit-learn*
* matplotlib
	* Are you tired of the boring-looking charts produced with Excel? Are you bored of looking for the write menu to move a label in your plot? Take a look at the visuals offered by *matplotlib* 	
* statsmodels: statistical tests
	* Is your boss asking about significance testing and confidence intervals? Are you interested in descriptive statistics, statistical tests, plotting functions, and result statistics? Well *statsmodels* offers you that and more.
* Beautiful Soup
	* All the data you require is available freely on the web but there is no download button and *You* need to scrape the website? You can  extract data from HTML using *Beautiful soup*

### Importing a module
```python
import math
x = math.cos(2 * math.pi)
print(x)

from math import *

log(10)

log(10,2)
```

### Types, Variables, assignment

```python
# variable assignments
x = 1.0
my_variable = 12.2
type(x)

y = 1
type(y)

b1 = True
type(b1)

s = "String"
type(s)
```
```python
import types
print(dir(types))

1+2, 1-2, 1*2, 1/2

1.0+2.0, 1.0-2.0, 1.0*2.0, 1.0/2.0

# Comment

# Comparison: >, <, <=, <=, ==
2 > 1

# Testing for equality
2 == 2
```

**Lists**

```python
l = [1,2,3,4]
print(type(l))
print(l)
print(l)
print(l[1:3])
print(l[::2])

# Python starts counting from 0
print(l[0])
```

**Tuples**

```python
point = (10, 20)
print(point, type(point))

x, y = point
print("x =", x)
print("y =", y)
```

**Dictionaries**

```python
params = {"parameter1" : 1.0, "parameter2" : 2.0,
"parameter3" : 3.0,}
print(type(params))
print(params)
```

***

<a name="ind-practice1"></a>
## Independent Practice: Applying Python Pseudo-code to Sample Data (20 mins)

Pseudocode is a language very close to English that allows us to represent a program concisely. The only thing you need is a statement to show where you are
starting and where you are ending a program.

> Instructor Note: Run through the following example with the students. Then ask them to tackle problems similar to the ones proposed below.

Calculate and print the average of three numbers: 5, 10, and 15.

```
Start
	num1 = 5
	num2 = 10
	num3 = 15
	sum = num1 + num2 + num3
	average = sum/3.0
	print average
End
```

### Proposed problems:

<details>
<summary>
1. Create a complete programme that will calculate the area circle with radius r.
</summary>
```python
Start
	pi = 3.14159265359
	radius = r
	area = pi * r * r
	print area
End
```
</details>

<details>
<summary>
2. Calculate and print the square of a number. If the number is larger than 10 also calculate the cube.
</summary>
```python
Start
	number = n
	square = n^2
	print square 
	
	if n > 10 then
		cube n^3
		print cube
	else
		do nothing
	end if

End
```
</details>

<details>
<summary>
3. List the letters in the sentence "Python is awesome"
</summary>
```python
Start
	MyString = "Python is awesome"
	
	for each letter in MyString
		print letter
	end for
End
```
</details>

***

> **BREAK** (5-10 min)
***

<a name="intro2"></a>
## Introduction: Python Programming Fundamentals (15 mins)

> Instructor Note: Remind the students about the concepts learnt in the first part of the workshop. Review the first Python code introduced and the types you have covered.
> 
> # DISCUSSION
> 
> 1. Start by surveying what students already know or don't know
> 
> 2. Then state which fundamentals you are going to cover
> 
> 3. Give a high level overview of what these fundamentals do (e.g. allow programs to store and remember information, etc)

> Instructor Note: Start a Jupyter notebook and remind the students how to use it.

### Instructions for students
We recommend using a Jupyter notebook for this guided practice. This makes it easier for all as it is homogenous for various environments (mac, win, linux).

1. Open Jupyter: in a terminal type
`jupyter notebook`
2. Navigate to an appropriate folder where your work will be saved
3. On the top-right-hand-side click in the button called "New" and select "Python 2"
4. Voilà, you are ready to type the commands we will cover below

## Programming fundamentals

Understanding core programming concepts and why they are used is just as important as knowing how to write code. 

Before we start, let us review some basic concepts of any programming language:

- **Variables**: A variable is a storage location and an associated symbolic name which contains some known or unknown quantity or information, a value. Variables can be of different `types`
	- `r = 3` 

- **Control Structures**: A control structure is a block of programming that analyses variables and chooses a direction in which to go based on given parameters. The term flow control details the direction the program takes (which way program control “flows”). Hence it is the basic decision-making process in computing; flow control determines how a computer will respond when given certain conditions and parameters. Some typical structures include
	- If statement
	- For loop
	- Functions 

- **Data Structures**: Data structure is a particular way of storing and organising data in a computer so that it can be used efficiently. Some examples include:
	- Lists
	- Tuples
	- Arrays
	- Matrices
	- Dataframes

- **Syntax**: the syntax of a programming language is the set of rules that define the combinations of symbols that are considered to be correctly structured programs in that language

The interrelationship of these elements make it possible for us to write programs to implement algorithms and solve problems


### Control Flow

* The term flow control details the direction the program takes (which way program control “flows”). 

* It determines how a computer will respond when given certain conditions and parameters.

#### **If**

An `if` statement is a conditional structure that, if proved true, performs a function or displays information. 

Think of this as a decision that moves the flow of your program depending on the answer to a TRUE-FALSE question. 

```
IF a person is older than 18
THEN they can drive
ELSE they cannot drive
```

We can express the pseudo-code above into Python as follows:

```python
if age_person > 18:
	return "They can drive"
else:
	return "They cannot drive"	
```

Let us see another example:

```python
A = 10
B = 100
if A>B:
	print("A is larger than B")
elif A==B:
	print("A is equal to B")
else:
	print("A is smaller than B")
```

##### Activity: Can you explain what the code above is doing?

#### **For loop**

A loop statement in programming performs a predefined set of instructions or tasks while or until a predetermined condition is met. 

Think of this as a repetitive action that has to be performed until further notice. 

``` 
FOR each user of a service in a list
   PRINT greet them
```

In the pseudo-code above, the condition we are asked to greet each user in a list. We stop the repetition when we reach the end of the list. 

We can express this loop in Python as follows:
```python
users = ["Jeff", "Jay", "Theresa"]

for user in users:
    print("Hello %s" % user)
```

**Tip**: When creating a for loop, make sure it's condition will always be met to help prevent an endless loop.

Let us see another example. Can you explain what the program is doing?

```python
for x in [1,2,3]:
    print(x)

for key, value in params.items():
    print(key + " = " + str(value))
```

##### List comprehension

List comprehension is an elegant way to define and create list in Python. It uses a for loop inside the definition of the list itself.

Let us take a look at one, and see if you can figure out what is happening:

```python
l1 = [x**2 for x in range(0,5)]
```

#### **Functions**

A function is a group of instructions, also known as a named procedure, used by programming languages to return a single result or a set of results. 

Functions are a convenient way to divide our code into useful blocks, providing us with order, making the code more readable and reusable.

Functions are a key way to define interfaces so programmers can share their code.

Here is how you define a function in python

```
def function_name(input1, input2...): 
    1st block of instructions 
    2nd block of instructions
    ...
```

Let us define a function that returns the square of the input value:

```python
def square(x):
	"""
	Return the square of x.
	"""
	return x ** 2
```

We can call this function as follows:

```python
var1 = 7

var2 = square(var1)

print(var2)
```

***

<a name="demo2"></a>
## Demo: Writing Programs in Python (15 mins)

Show the students how to put together a programme in Python.

Python is an *interpreted* language, which means you can run the program as soon as you make changes to the file. This makes iterating, revising, and troubleshooting programs is much quicker than many other languages.

> Walk the students through translating the first pseudocode problem from [Part 1 - Independent Practice](#ind-practice1). Then encourage the students to write Python code for the other two exercises from [Part 1 - Independent Practice](#ind-practice1).

<details>
<summary>
1. Create a complete programme that will calculate the area circle with radius r.
</summary>
```python
# Explain that the mathematical constant Pi
# is included in the math module
# We are importing the value of pi from 
# that module - Easy to read, right?
from math import pi

def circ_area(r):
	return pi * r**2

r = 3
area = circ_area(r)
print(area)
```
</details>

***

<a name="guided-practice2"></a>
## Guided Practice: Dive into Data with Python (20 mins)

> Instructor Note:
> 
> Use the Jupyter notebook [Python101_Part2_GuidedPractice.ipynb](./code/Python101_Part2_GuidedPractice.ipynb) 
> 
> ### IDE suggestion
> We encourage you to use a Jupyter notebook. It makes it easier to keep the class together as students will be using a common IDE. 
> 
> ### Activity
>  We suggest making the code below available to the students and get them to work in pairs going through the code in the notebook

Let us create a new Jupyter notebook for this practice. We will work in pairs.

1. Save the file called [Python101_Part2_GuidedPractice.ipynb](./code/Python101_Part2_GuidedPractice.ipynb) in a known location in your file system
2. Start Jupyter and navigate to the location where you saved the file
3. Open the file 
4. Voilà,  you can start the Guided Practice


***

<a name="ind-practice2"></a>
## Independent Practice: More Python Practice (20 mins)

### DISCUSION

Given your interests and knowledge, which are you more interested in learning about:

- practical applications of python, or
- python fundamentals?

> Instructor Note:
> ### ACTIVITY CHOICES
>
> You can chose either of the two options outlined below. You can do this running a discussion with the students or a poll? For instance - *which are you more interested in learning about - python fundamentals or practical applications of python?*
>
> #### OPTION 1
>
> You can use the [Iris Dataset notebook included in the materials](./code/Python101_Part2_IndPractice.ipynb) to follow up the introduction to pandas in the previous section. Note that the notebook makes reference to the [Iris Dataset included here](./code/data/iris.csv).
>
> This activity lets the students to see practical applications of python  
>
> #### OPTION 2
>  Alternatively, you can tackle programming tasks to cover the python fundamentals covered earlier on. See the suggestions below:

### Suggested programming tasks (Option 2)

> Instructor Note:
>
> Depending on the size and abilities of the class you can ask students to tackle the tasks individually or in groups.
>  
> 1. **Individually**: Each student tackles the tasks and discuss the answers in pairs before discussing with the entire class.
> 2. **Pairs**: Ask the students to answer the problems in  pair and discuss the answers with the entire class
> 3. **For larger classes**, you can split the students into 3 groups and assign one problem per group then have the groups present back how to do it to the rest of the class

<details>
<summary>1. A recipe you are reading states how many grams you need for the ingredient. Unfortunately, your store only sells items in ounces. Create a program to convert grams to ounces.

`ounces = 28.3495231 * grams`
</summary>
```python
def gr2oz(x):
	return 28.3495231 * x

grams = 10
ounces = gr2oz(grams)
print(ounces)
```
</details>

<details>
<summary>
2. Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature. The following formula is used for the conversion:

`C = (5 / 9) * (F – 32)`
</summary>
```python
def F2C(F):
    return (5.0/9.0) * (F - 32)

f=86
c= F2C(f)

print("{0} Fahrenheit is {1} centigrade".format(f,c))
```
</details>

<details>
<summary>
3. Calculate the amount obtained by investing the principal P for N years at the rate of R. The following formula is used for the conversion:

`A = P * (1 + R) ^ N`
</summary>
```python
def compound_interest(P, R, N):
    return P * (1 + R)**N

P = 1000
R = 0.1
N = 2

Interest = compound_interest(P, R, N)

print(Interest)
```
</details>

>Instructor Note:
> ### FOLLOW UP ACTIVITY
>Once the students have finished with the 3 tasks above, ask them to transform the pseudocode they completed in the [Independent Practice](#ind-practice1) of the first part.


***

<a name="conclusion"></a>
## Conclusion: Review + Recap Topics (10 mins)

### Class discussion

- What have you accomplished today? 


> Instructor Note:
>
> ### Review Topics Covered
>  
> Gather some thoughts from the class answering the question above. After a quick discussion restate learning objectives and describe how we met them.

In the workshop you have covered the following topics:

* Discuss the history of Python and its use across different industries.
* Compare Python with programming languages.
* The benefits of a Python workflow
* Python programming fundamentals.
* Use Python code to solve real world data problems.

> Instructor Note:
>
> ### Review Deliverables
>
>  Use this to encourage discussion, e.g. ask students to generate takeaways

**Discussion points**

- What did we learn about python?
- How does it compare to other programming languages? (C++, java, etc)

**Takeaways**

* Python is a popular, flexible programming language
	- Easy to use
	- Readable
	- Powerful
* Python has application in many areas
	- From drug discovery to gravitational wave detection
	- Business and R&D
* Understand the basics of Python programming
	- types
	- variables
	- functions
	- data manipulation
	- etc
* Use Python to solve actual problems

***

<a name="takeaway"></a>
## Takeways: Learning Plan + Q&A (15 mins)

#### What Should You Do Next?

Encourage the students to continue learning by producing a plan based on the topics discussed in the workshop.

Suggest some resources such as books, podcasts, GA courses, etc.

* For beginner programmers:
	* go through [Learn Python the hard way](http://learnpythonthehardway.org)
	* read up on and familiarise yourself with the language by going through the tutorials [A Beginner's Python Tutorial](https://en.wikibooks.org/wiki/A_Beginner%27s_Python_Tutorial)

* For programmers new to python
	*  Read the information in [Moving to Python From Other Languages](https://wiki.python.org/moin/MovingToPythonFromOtherLanguages)
	* [Python for java developers](https://antrix.net/static/pages/python-for-java/online/)
	* [Python for MATLAB users](http://bastibe.de/2013-01-20-a-python-primer-for-matlab-users.html)

* For more seasoned programmers:
	* Challenge yourself by tackling the [Python Challenge](http://www.pythonchallenge.com) 

* If you are interested to apply Python in Data Science
	* Look at the Data Science workshops and courses in [General Assembly](https://generalassemb.ly/education/data-science?&gclid=CjwKEAjwk6K8BRDM3aCSkdCtzSQSJAA3Vf38leCWKuRFD33jAqNkjHhIqVTVv6i6PiiBtxse7DW1SRoCFE3w_wcB)

#### Q & A

> Instructor Notes: Encourage the students to share any thoughts or questions before closing the session.


***

## ADDITIONAL RESOURCES

- [Python success stories](https://www.python.org/about/success/)
- [Learn Python the hard way](http://learnpythonthehardway.org)
- [Beginners' Guide to Python](https://wiki.python.org/moin/BeginnersGuide)
- [10 Minutes to Pandas](http://pandas.pydata.org/pandas-docs/stable/10min.html)
