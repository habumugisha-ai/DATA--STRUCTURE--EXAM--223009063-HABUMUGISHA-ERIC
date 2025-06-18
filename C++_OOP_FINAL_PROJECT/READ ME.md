# my project question
 # 14.Quiz Application
 Description: Build a console quiz app where questions are in a dynamic array and user 
classes process answers differently under a common interface.
 Tasks:
 • Define struct Question { char prompt[100]; char choices[4]
 [40]; int correctIdx; }; and allocate a dynamic Question* 
questions.
 • Create an abstract class User with virtual int takeQuiz(Question*, 
int) = 0;, then derive StudentUser : User (stores int* score) and 
GuestUser : User (only displays correct answers) to demonstrate inheritance 
and polymorphism.
 • Store User* in a dynamic User** participants; calling 
participants[i]->takeQuiz(questions, n) dispatches correctly.
 • Use pointer arithmetic to traverse questions and record answers.
 • Implement addQuestion(Question) and removeQuestion(int index)
 by resizing Question*.

# the main purpuse of this project is:
The purpose of this project is to create a simple quiz application using C++. It demonstrates object-oriented programming concepts, dynamic memory management, and polymorphism by allowing different user types (student and guest) to interact with quiz questions in unique ways—either by answering or viewing correct responses.

# the screenshot of result of my project:
<img width="246" alt="image" src="https://github.com/user-attachments/assets/5b19391e-987a-42f7-bba9-af4acf227107" />
![image](https://github.com/user-attachments/assets/6e5f8b2c-8a87-4702-a171-c506578ee9dd)


