# Python-Basics
This is a teaching course for kids on the basics of programming in Python.
## …or create a new repository on the command line
echo "# Python-Basics" >> README.md 

git init 

git add README.md 

git commit -m "first commit" 

git branch -M main 

git remote add origin git@github.com:gkrampah/Python-Basics.git 

git push -u origin main 


## or push an existing repository on your local machine from the command line
git remote add origin git@github.com:gkrampah/Python-Basics.git 

git branch -M main 

git push -u origin main 


# Problem solving through programming

The process of learning to program is an excellent opportunity to practice problem-solving skills

Python is an example of a high-level language; other high-level languages you might have heard of are C++, PHP, Pascal, C#, and Java. There are also low-level languages, sometimes referred to as machine languages or assembly languages. computers can only execute programs written in low-level languages. Thus, programs written in a high-level language have to be translated into something more suitable before they can run. 

### why programme with high-level languages?

It is much easier to program in a high-level language so programs take less time to write and easier to read. They are shorter and are more likely to be correct. Secondly, high-level languages are portable, meaning that they can run on different kinds of computers with few or no modifications.

The engine that translates and runs Python is called the Python Interpreter which can be use in two ways; immediate mode or script mode

### what is a program?
A program is a sequence of instructions that specifies how to perform a computation.

A computer program is a sequence of instructions that a computer can execute to perform some task or solve a particular problem. These instructions are written in a programming language, which is a formal language designed to communicate algorithms and processes to a computer in a way that is both executable and human-readable.

A computer program typically performs a series of operations or calculations based on input data, manipulates this data according to specified rules, and then produces output data. The program may also interact with various hardware components (e.g., the processor, memory, input/output devices) and software components (e.g., operating systems, libraries) of a computer system.

Computer programs can be as simple as a few lines of code that add two numbers together or as complex as entire operating systems, database management systems, or advanced scientific simulations.

Programs generally consist of the following basic elements:

* Variables: Containers that hold data values.
* Data Types: Specify the kind of data (e.g., integers, floating-point numbers, strings, etc.) that can be stored in variables.
* Operators: Symbols that perform operations (e.g., addition, multiplication) on variables and values.
* Control Structures: Mechanisms for directing the flow of execution (e.g., loops, conditional statements).
* Functions/Procedures: Modular blocks of code designed to perform specific tasks.
* Input/Output: Mechanisms for receiving data from and sending data to the external world (e.g., keyboard, mouse, files, network).
* Comments: Non-executable lines that are used to describe what the code is doing.

### What is debugging?

Programming is a complex process, and because it is done by human beings, it often leads to errors. Programming errors are called bugs and the process of identifying and fixing errors, or "bugs," in a computer program, script, or other set of instructions is called debugging. These errors may be syntactic, logical (semantic), or runtime errors, among others:

* Syntactic Errors: Mistakes in the code's syntax, such as missing parentheses or incorrect indentation, that prevent the program from running. Syntax refers to the structure of a program and the rules about that structure. 
* Logical (or Semantic) Errors: Errors in the algorithm or logic that cause the program to produce incorrect results. If there is a semantic error in your program, it will run successfully, in the sense that the computer will not generate any error messages, but it will not do the right thing. It will do something else. Specifically, it will do what you told it to do.
* Runtime Errors: Errors that occur while the program is running, often due to illegal operations such as division by zero, attempting to access invalid memory locations, or issues related to resource management. So called because the error does not appear until you run the program. These errors are also called exceptions because they usually indicate that something exceptional (and bad) has happened.

#### Types of Debugging Techniques
* Print-Based Debugging: Adding print statements to the code at various points to display the values of variables and the flow of execution. This method is often the simplest way to debug but can be cumbersome for large or complex programs.

* Automated Debugging: Using specialized debugging tools that allow you to step through the code, inspect variables, set breakpoints, and perform other debugging tasks. Examples include gdb for C/C++, pdb for Python, and built-in debuggers in IDEs like Visual Studio and IntelliJ IDEA.

* Static Analysis: Using tools that analyze the code without executing it to identify potential issues such as unused variables, null pointer dereferences, or possible syntax errors.

* Dynamic Analysis: Running the program under conditions that allow the debugger to check for specific types of errors, like memory leaks or buffer overflows.

* Code Reviews: Manually reviewing the source code, often as a team, to identify potential issues.

* Rubber Duck Debugging: Explaining the problem out loud, as if to a rubber duck or another inanimate object, can often help identify logical errors or oversights in the code.

* Test-Driven Development (TDD): Writing unit tests to check small pieces of functionality. If a test fails, you debug the code to find out why.

* Logging: Incorporating a logging system into the program to record various events, variable states, or errors for later analysis.

* Profiling: Using specialized tools to analyze the program's run-time behavior. While this is often used for performance optimization, it can also reveal bugs related to resource usage.

# Python variables, expressions and statements

## Variables
Computer programs manipulates values. Values are classified into various classes called data types. A Python function to identify a data type is the 'type' function eg: type(12).

One of the most powerful features of a programming language is the ability to manipulate variables. A variable is a name that refers to a value. The assignment statement gives a value to a variable: message = "What's up, Doc?", n = 17, pi = 3.14159

The assignment statement binds a name, on the left-hand side of the operator, to a value, on the right-hand side. When reading or writing code, say to yourself “n is assigned 17” or “n gets the value 17”. Don’t say “n equals 17”. We use variables in a program to “remember” things and these things can change within the program. 

Variable names can be arbitrarily long. They can contain both letters and digits, but they have to begin with a letter or an underscore. Although it is legal to use uppercase letters, by convention we don’t. If you do, remember that case matters. Bruce and bruce are different variables. Keywords define the language’s syntax rules and structure, and they cannot be used as variable names.

## Statements
A statement is an instruction that the Python interpreter can execute but does not produce a result. Eg: while, if, for, import etc statements

## Expressions
An expression is a combination of values, variables, operators, and calls to functions. The evaluation of an expression produces a value, which is why expressions can appear on the right hand side of assignment statements. A value all by itself is a simple expression, and so is a variable.

## Operators and operands
Operators are special tokens that represent computations like addition, multiplication and division. The values the operator uses are called operands. The asterisk (*) is the token for multiplication, and (**) is the token for exponentiation. 

In Python 3, the division operator / always yields a floating point result. What we might have wanted to know was how many whole hours there are, and how many minutes remain. Python gives us two different flavors of the division operator. The second, called floor division uses the token //. Its result is always a whole number

## Type converter functions
Python functions, int, float and str, which will (attempt to) convert their arguments into types int, float and str respectively. We call these type converter functions. The int function can take a floating point number or a string, and turn it into an int. For floating point numbers, it discards the decimal portion of the number — a process we call truncation towards zero on the number line.

## Order of operations
When more than one operator appears in an expression, the order of evaluation depends on the rules of precedence. Python follows the same precedence rules for its mathematical operators that mathematics does. 

Interestingly, the + operator does work with strings, but for strings, the + operator represents concatenation, not addition. Concatenation means joining the two operands by linking them end-to-end. The * operator also works on strings; it performs repetition

## Input
There is a built-in function in Python for getting input from the user. eg: n = input("Please enter your name: ")

## The modulus operator
The modulus operator works on integers (and integer expressions) and gives the remainder when the first number is divided by the second. In Python, the modulus operator is a percent sign (%). The syntax is the same as for other operators. It has the same precedence as the multiplication operator.

# Functions

A Python function is a reusable block of code or sequence of statements that perform a specific task. Functions allow for code modularity and reusability, making it easier to structure and manage complex programs. Functions can take input as arguments, execute a set of statements, and return output.

def function_name(parameters):
    """docstring"""
    # function body
    return output

We can make up any names we want for the functions we create, except that we can’t use a name that is a Python keyword, and the names must follow the rules for legal identifiers.

There can be any number of statements inside the function, but they have to be indented from the def. In the examples in this book, we will use the standard indentation of four spaces. Function definitions are the second of several compound statements we will see, all of which have the same pattern. 

* Pure Functions (fruitful functions): These functions take an input and produce an output without modifying any data outside their scope or producing any side-effects. Their output is solely determined by their input.
def square(x):
    return x * x
    
* Impure Functions (void functions): These functions have side-effects (e.g., modifying a global variable, writing to a file) or depend on external states.
global_variable = 0

def impure_function(x):
    global global_variable
    global_variable += x
    
In Python, a "void function" is a term borrowed from other programming languages like C or Java to describe a function that doesn't return any value. In Python, such functions actually return a special value called None. So technically, all functions in Python return a value, but a "void function" returns None, either implicitly or explicitly. In Python, "void functions" are those that don't return any meaningful value and are used for their side effects. While they implicitly return None, you can also explicitly return None for clarity.

## Conditionals

###  Boolean values and expressions
A Boolean value is either true or false. It is named after the British mathematician, George Boole, who first formulated Boolean algebra — some rules for reasoning about and combining these values. This is the basis of all modern computer logic.

In Python, the two Boolean values are True and False (the capitalization must be exactly as shown), and the Python type is bool. Six common comparison operators which all produce a bool result; here are all six: ==, !=, <,>,<=,>=. Also, there is no such thing as =< or =>.

### Logical operators
There are three logical operators, and, or, and not, that allow us to build more complex Boolean expressions from simpler Boolean expressions. The semantics (meaning) of these operators is similar to their meaning in English. For example, x > 0 and x < 10 produces True only if x is greater than 0 and at the same time, x is less than 10.

n % 2 == 0 or n % 3 == 0 is True if either of the conditions is True, that is, if the number n is divisible by 2 or it is divisible by 3. (What do you think happens if n is divisible by both 2 and by 3 at the same time? Will the expression yield True or False? Try it in your Python interpreter.)

Finally, the not operator negates a Boolean value, so not (x > y) is True if (x > y) is False, that is, if x is less than or equal to y.

The expression on the left of the or operator is evaluated first: if the result is True, Python does not (and need not) evaluate the expression on the right — this is called short-circuit evaluation. Similarly, for the and operator, if the expression on the left yields False, Python does not evaluate the expression on the right.

So there are no unnecessary evaluations.

## Fruitful functions

### Return values
Code that appears after a return statement, or any other place the flow of execution can never reach, is called dead code, or unreachable code.

In a fruitful function, it is a good idea to ensure that every possible path through the program hits a return statement. 

def absolute_value(x):
    if x < 0:
        return -x
    else:
        return x
        
The following version of absolute_value fails to do this:

def bad_absolute_value(x):
    if x < 0:
        return -x
    elif x > 0:
        return x

It is also possible to use a return statement in the middle of a for loop, in which case control immediately returns from the function. Let us assume that we want a function which looks through a list of words. It should return the first 2-letter word. If there is not one, it should return the empty string:

def find_first_2_letter_word(xs):
    for wd in xs:
        if len(wd) == 2:
           return wd
    return ""
    
find_first_2_letter_word(["This",  "is", "a", "dead", "parrot"])