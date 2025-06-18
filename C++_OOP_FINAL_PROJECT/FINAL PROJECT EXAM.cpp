#include <iostream>
#include <cstring>
using namespace std;

// Struct for questions
struct Question {
    char prompt[100];
    char choices[4][40];
    int correctIdx;
};

// Add a question to dynamic array
void addQuestion(Question*& questions, int& count, const Question& q) {
    Question* newArr = new Question[count + 1];
    for (int i = 0; i < count; ++i) {
        *(newArr + i) = *(questions + i); // pointer arithmetic
    }
    *(newArr + count) = q;
    delete[] questions;
    questions = newArr;
    ++count;
}

// Remove a question by index
void removeQuestion(Question*& questions, int& count, int index) {
    if (index < 0 || index >= count) return;
    Question* newArr = new Question[count - 1];
    for (int i = 0, j = 0; i < count; ++i) {
        if (i != index) {
            *(newArr + j) = *(questions + i);
            ++j;
        }
    }
    delete[] questions;
    questions = newArr;
    --count;
}

// Abstract base class
class User {
public:
    virtual int takeQuiz(Question* questions, int count) = 0;
    virtual ~User() {}
};

// StudentUser: takes quiz and keeps score
class StudentUser : public User {
    int* score;
public:
    StudentUser() {
        score = new int(0);
    }

    int takeQuiz(Question* questions, int count) override {
        *score = 0;
        for (int i = 0; i < count; ++i) {
            Question* q = questions + i;
            cout << "\nQ" << i + 1 << ": " << q->prompt << "\n";
            for (int j = 0; j < 4; ++j) {
                cout << j + 1 << ") " << q->choices[j] << "\n";
            }

            int ans;
            cout << "Your answer (1-4): ";
            cin >> ans;

            while (ans < 1 || ans > 4 || cin.fail()) {
                cin.clear();
                cin.ignore(1000, '\n');
                cout << "Invalid. Enter 1-4: ";
                cin >> ans;
            }

            if (ans - 1 == q->correctIdx)
                ++(*score);
        }

        cout << "Your score: " << *score << "/" << count << "\n";
        return *score;
    }

    ~StudentUser() {
        delete score;
    }
};

// GuestUser: shows questions and correct answers
class GuestUser : public User {
public:
    int takeQuiz(Question* questions, int count) override {
        for (int i = 0; i < count; ++i) {
            Question* q = questions + i;
            cout << "\nQ" << i + 1 << ": " << q->prompt << "\n";
            for (int j = 0; j < 4; ++j) {
                cout << j + 1 << ") " << q->choices[j] << "\n";
            }
            cout << "Correct answer: " << q->correctIdx + 1 << ") " << q->choices[q->correctIdx] << "\n";
        }
        return 0;
    }
};

// Main function
int main() {
    int questionCount = 0;
    Question* questions = new Question[0]; // No nullptr

    // Create and add Question 1
    Question q1;
    strcpy(q1.prompt, "What is the capital of Kenya?");
    strcpy(q1.choices[0], "Nairobi");
    strcpy(q1.choices[1], "Lagos");
    strcpy(q1.choices[2], "Cairo");
    strcpy(q1.choices[3], "Addis Ababa");
    q1.correctIdx = 0;
    addQuestion(questions, questionCount, q1);

    // Create and add Question 2
    Question q2;
    strcpy(q2.prompt, "Which number is prime?");
    strcpy(q2.choices[0], "4");
    strcpy(q2.choices[1], "6");
    strcpy(q2.choices[2], "7");
    strcpy(q2.choices[3], "8");
    q2.correctIdx = 2;
    addQuestion(questions, questionCount, q2);

    // Create participants
    User** participants = new User*[2];
    participants[0] = new StudentUser();
    participants[1] = new GuestUser();

    for (int i = 0; i < 2; ++i) {
        cout << "\n--- Participant " << i + 1 << " ---\n";
        participants[i]->takeQuiz(questions, questionCount);
    }

    // Clean up
    for (int i = 0; i < 2; ++i)
        delete participants[i];
    delete[] participants;
    delete[] questions;

    return 0;
}

