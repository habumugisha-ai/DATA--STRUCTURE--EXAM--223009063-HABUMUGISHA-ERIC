1.	#include <iostream>:
## Including the iostream Library

At the very beginning of our C++ program, we have `#include <iostream>`.  This line is crucial because it *includes* the `iostream` library `iostream` specifically provides the tools for input and output operations
2.	using namespace std;:
## Using the Standard Namespace

`using namespace std;`.  This line tells the compiler to use the `std` (standard) namespace.  Namespaces are like containers for names.  `iostream` By using this line, we can use the names of these components (like `cout` and `cin`) directly without having to write `std::cout` and `std::cin` every time
3.	int main() 
## The Main Function: Where Execution Begins

Every C++ program *must* have a `main()` function.  This is the entry point of your program – it's where the execution begins.  The `int` before `main` indicates that the function returns an integer value.  
4.	cout <<:
## Displaying Output with cout

Inside the `main()` function, we often use `cout` to display output to the console (your screen).  `cout` is an object from the `iostream` library. The `<<` operator is used to "insert" data into the output stream.
endl is another useful tool from iostream. 

5.	cin >> ...; (Input):
## Getting Input with cin

`cin` is used to get input from the user.  It's also an object from the `iostream` library. The `>>` operator is used to extract data from the input stream.

6.	return 0;:
Markdown
## Returning from Main

At the end of the `main()` function

