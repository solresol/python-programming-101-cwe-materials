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
- Demonstrate basic understanding of Python programming fundamentals.
- Use Python code to solve real world data problems.
- Create a custom learning plan to help you continue to build fundamental python skills after this workshop.

### STUDENT PRE-WORK
*Before this lesson, you should already be able to:*

- Bring a laptop with [Python 2.7](#) and [Anaconda](#) installed.
- If you are using a PC, install [git-bash terminal](#).
<<<<<<< HEAD
<<<<<<< HEAD
- Curiosity and open mind
=======
- Optional: Install a text editor like Sublime Text 3 or Atom on your computer.
>>>>>>> master
=======
- Optional: Install a text editor like Sublime Text 3 or Atom on your computer.
>>>>>>> master

### INSTRUCTOR PREP
*Before this lesson, instructors will need to:*

- Review & modify lesson plan & slide deck as needed
- Write learning objectives & relevant information on board
- Review Student Roster and Instructor Checklist

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
| 20 min  | [Guided Practice](#guided-practice2)  | Cleaning Data with Python  |
| 20 min  | [Independent Practice](#ind-practice2)  | Applying Your Own Python Workflow |
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

> **Example Exercise**: *Have students submit their info one per line on a CSV file (via google doc, etc). Instructors can then use Python to briefly analyze and pull out interesting information (e.g. create dictionary, append, sort, etc).*


#### Our Expectations

- You're ready to take charge of your learning experience.
- You've installed Anaconda & Python 2.7.
- You're interested in learning about Python!

#### Our Objectives

> Note: Write workshop objectives on board before class

- Why this topic matters (general relevance)
- Why this topic rocks (interest/hook)

> Note: Tailor these 2 points to student interests. Relate to their career info & goals students described during attendance.


***

<a name="intro1"></a>
## Introduction: Why Python? What Can Python Do For Me? (15 mins)

**What is Python?**

- Created by Guido Van Rossem in 1991
- Emphasises **productivity** and code **readability**
	* The language is easy to pick up and learn
	* This gentle learning curve brings makes it easier for many to contribute to production level code
	* Readable code means that almost anyone can pick up a puece of code and understand what it is doing
- Interpreted, object-oriented, high-level programming language with dynamic semantics
	* **Interpreted**: Code implementations execute instructions without having to *compile* them into machine-language instruction. In contrast, compiled code is executed by the computer's CPU (hardware)
		* Interpreted code may run less quickly, but can be executed on multiple platforms without modification
	* **Object-oriented** (OO): Instead of concentraing on isolated "actions", object-orientation enables us to focus on "objects" that contain data (attributes). Objects have specific procedures, known as methods (code) that can access and modify the attributes of the object.
		* OO makes it easoer to reuse code in other programs
	* **High-level programming**: Related to the code readability mentioned earlier
		* The use of language similar to natural language makes it easy to use and automate 
	* **Dynamic semantics**: Once data has been specified, the machine must be instructed to perform operations on the data. Dynamic semantics (also known as execution semantics)  defines how and when the various constructs of a language should produce a program behaviour, providing flexibility at run-time. 

> Instructor Note: 
> #### KNOWLEDGE CHECK
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
> ### KNOWLEDGE CHECK
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
> ### ACTIVITY AND DISCUSSION
> What other languages have the students heard of? what are they familiar with, if any? Then ask how they think those might compare to Python.

[Comparing Python to Other Languages](https://www.python.org/doc/essays/comparisons/)

Python is often compared to other interpreted languages such as Java, JavaScript, Perl, Tcl, or Smalltalk. Comparisons to C++, Common Lisp and Scheme can also be enlightening.

#### EXAMPLE 
Let us what a Python program looks like, starting with the typical "Hello World!" program: In essence we are writing code to print the message "Hello World!" in the screen.

- **Python**

```
	print("hello world")
```

- **C++**

```
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

```
public class HelloWorld
{
    public static void main (String[] args)
    {
        System.out.println("Hello, world!");
    }
}
```

Notice that in the Java versionm we define the code inside the context of class.

In Object Oriented Programming a *class* is a template definition of the methods and variables in a particular kind of object. In other words, an object is a specific instance of a class: it contains actual values instead of variables.

> Instructor Note: 
> ### OTHER EXAMPLES
> You are encouraged to use other specific examples of an element python does particularly well, using a simple statement or function. This depends on your familiarity with other programming languages, as wel with the abilities of the students in your class.

#### Python interactive shell v scripts

In the example shown above, we are assuming that we are using an interactive shell, i.e. we are writing code that is executed immediately by the Python interpreter and wer are able to "interact" with the results of the commands we pass. We can do this via:

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

In those cases we need to create a Python script (we can use any plain text editor of our choice) and save the code in a file with extension `.py`. 

Anaconda distributions (Mac, Win, Linux) come with an IDE called `Spyder`. 

Other IDEs:

- [PyCharm](https://www.jetbrains.com/pycharm/)
- Eclipse with [PyDev](http://www.pydev.org)
- [Atom](https://atom.io)

A barebones script for the "Hello World!" program (saved to a file called `hi.py`) looks like this:

```
print("Hello world!")
```

To run the script by passing it as a command to the Python interpreter we need to write:

```
> python hi.py
```

Plese note that all of the code that is at indentation level 0 gets executed. Functions and classes that are defined but not on at the 0-th level indentation are not executed.

Unlike other languages, there's no `main()` function that gets run automatically - the `main()` function is implicitly all the code at the top level.

In this case, the top-level code is an if block.  `__name__` is a built-in variable which evaluates to the name of the current module. We can test whether our script is being run directly or being imported by something else by testing

```
if __name__ == "__main__":
    ...
```

A more sophisticated vesion of the "Hello World!" script is therefore:

```	
	def main():
	    print("hello world")
	    
	if __name__ == '__main__':
	    main()
```	

***

### Demo: Plotly

We will be working in a Jupyter Notebook

See file here:
[Python_101_Demo_Plotly.ipynb](./code/Python_101_Demo_Plotly.ipynb)


<a name="guided-practice1"></a>
## Guided Practice: Installing and Configuring Common Python Libraries (20 mins)

> Instructor Note: You can show the following commands and concepts using a python/ipython shell. We encourage you to use a Jupyter notebook in the second part of the workshop.

**Packages**

Libraries of code written to solve particular set of problems

In Python there are many related packages relevant to data science: pandas, Scikit-learn, NumPy, etc

These are installed with PIP, Conda, etc

`pip install <package-name>`

* pandas: manipulate data
* SciPy/NumPy:  scientific computing and numerical calculations
* Scikit-Learn: machine learning methods
* matplotlib: visualise data
* statsmodels: statistical tests
* Beautiful Soup: HTML/XML data
* Jupyter: interactive programming

### Importing a module
```
import mathx = math.cos(2 * math.pi)print(x)

from math import *

log(10)

log(10,2)
```

### Types, Variables, assignment

```
# variable assignments 
x = 1.0my_variable = 12.2
type(x)

y = 1
type(y)

b1 = True
type(b1)

s = "String"
type(s)

import types
print(dir(types))

1+2,1-2,1*2,1/2

1.0+2.0,1.0-2.0,1.0*2.0,1.0/2.0

# Comment

# Comparison: >, <, <=, <=, ==
2 > 1 

# Testing for equality
2 == 2
```

**Lists**

```
l = [1,2,3,4] 
print(type(l))print(l)
print(l) 
print(l[1:3])print(l[::2])

# Python starts counting from 0
print(l[0])
```

**Tuples**

```
point = (10, 20)print(point, type(point))

x, y = point 
print("x =", x)print("y =", y)
```

**Dictonaries**

```
params = {"parameter1" : 1.0, "parameter2" : 2.0,"parameter3" : 3.0,} 
print(type(params))print(params)
```

***

<a name="ind-practice1"></a>
## Independent Practice: Applying Python Pseudo-code to Sample Data (20 mins)

Pseudocode is a language very close to English that allows us to represent a program concisely. The only thing you need is a statement to show where you arestarting and where you are ending a program. 

> Instructor Note: Run through the following example wiht the students. Then ask them to tackle problems similar to the ones proposed below.

Calculate and print the average of three numbers: 5, 10, and 15.

```
Start	num1 = 5	num2 = 10	num3 = 15	sum = num1 + num2 + num3	average = sum/3.0	print averageEnd
```
Proposed problems:

1. Create a complete program that will calculate the area circle with radius r. 
2. Calculate and print the square of a number. If the number is larger then 10 also calculate the calculate the cube.
3. List the letters in the sentence "Python is awesome" 

***

> **BREAK** (5-10 min)
***

<a name="intro2"></a>
## Introduction: Python Programming Fundamentals (15 mins)

> Intructor Note: Remind the students about the concepts learnt in the first part of the workshop. Review the first Python code introduced and the types you have covered.

> Instructore Note: Start a Jupyter notebook and show the students how to use it.


### Control Flow

**If**

```
A = 10B = 100if A>B: 
	print("A is larger than B")elif A==B: 
	print("A is equal to B")else:	print("A is smaller than B")
```

**For loop**

```
for x in [1,2,3]:    print(x)
    
for key, value in params.items(): 
    print(key + " = " + str(value))
    
# List comprehension
l1 = [x**2 for x in range(0,5)]
```

**Functions**

```
def square(x): 
	"""	Return the square of x. 
	"""	return x ** 2
```

***

<a name="demo2"></a>
## Demo: Writing Programs in Python (15 mins)

Show the students how to put together a programme in Python. 

Python is an interpreted language, which means you can run the program as soon as you make changes to the file. This makes iterating, revising, and troubleshooting programs is much quicker than many other languages.

> Encourage the students to write Python code for the pseudo-code exercises from [Part 1 - Independent Practice](#ind-practice1).

***

<a name="guided-practice2"></a>
## Guided Practice: Delving into Data with Python (20 mins)

```

# It is possible to invoke the terminal 
# with the use of "!" (bang). For example 
# a list of the # exisiting files under 
# the current path can be obtained 
# as follows:

!ls

import pandas as pd
import numpy as np

states = pd.Series(['GA','GA','GA','GA','GA',
"NY","NY","NY","FL","FL"])
cities  = pd.Series(['Atlanta','Lilburn','Athens',
'Auburn','Augusta','NYC','Buffalo','Albany',
'Miami','Tallahassee'])

city_avg_incomes = pd.Series([55000,40000,50000,45000,
30000,60000,57000,56000,65000,40000])
city_populations = pd.Series([5000000,250000,100000,
50000, 200000,6000000,3000000,400000,
4000000,5000000])


city_table = pd.DataFrame( {'cities': cities,  
             'states': states, 
             'city_avg_incomes':city_avg_incomes, 
             'city_populations':city_populations 
              } )

city_table.head()


# We can create a column to state the 
# population in millions and another 
# one for the income in thousands

city_table['pop_in_millions'] = city_table['city_populations'].apply(
    lambda x: float(x)/1000000)

city_table['income_in_k'] =
city_table['city_avg_incomes'].
apply(lambda x: float(x)/1000)

city_table

city_table.shape

city_table[0:4][["pop_in_millions",'income_in_k']]

city_table.sort_values('pop_in_millions',
ascending=0)

city_table[(city_table['income_in_k']<=30)]

city_table.describe()


# Visualising Data

# Display the plots in the notebook with 
#the following command

%pylab inline
# Import the graphing libraries we will use 
import matplotlib.pyplot as plt

city_table['income_in_k'].plot(kind='bar')

```


***

<a name="ind-practice2"></a>
## Independent Practice: Applying Your Own Python Workflow (20 mins)

> Instructor Note: You can use the Iris Data set example included in the materials to follow up the introduction to pandas in the previous section. Alternatively, you can tackle programming tasks like the ones suggested below:

1. A recipe you are reading states how many grams you need for the ingredient. Unfortunately, your store only sells items in ounces. Create a program to convert grams to ounces.

`ounces = 28.3495231 * grams`

2. Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature. The following formula is used for the conversion:`C = 5 / 9 * (F – 32)`

3. Calculate the amount obtained by investing the principal P for N years at the rate of R. The flowchart in Figure 1.5 shows the sequence of steps necessary to accomplish this task. The following formula is used for the conversion:

`A = P * (1 + R) ^ N`


***

<a name="conclusion"></a>
## Conclusion: Review + Recap Topics (10 mins)

> Review Deliverables

> Review Topics Covered

In the workshop you have covered the following topics:

* Discuss the history of Python and its use across different industries.
* Compare Python with programming languages.
* Thebenefits of a Python workflow 
* Python programming fundamentals.
* Use Python code to solve real world data problems.

***

<a name="takeaway"></a>
## Takeways: Learning Plan + Q&A (15 mins)

#### What Should You Do Next?

Encourage the students to continue learning by producing a plan based on the topics discussed in the workshop.

Suggest sonme resources such as books, podcasts, GA courses, etc.

#### Q & A

> Instructor Notes: Encourage the students to share any thoughts or questions before closing the session. 


***

## ADDITIONAL RESOURCES

- [Python success stories](https://www.python.org/about/success/)
- [Learn Python the hard way](http://learnpythonthehardway.org)
- [Beginners' Guide to Python](https://wiki.python.org/moin/BeginnersGuide)
- [10 Minutes to Pandas](http://pandas.pydata.org/pandas-docs/stable/10min.html)
