#include <iostream>
#include <string>
#include <stack>
#include <cctype>
#include <cmath>

using namespace std;

int getPrecedence(char op) {
    if (op == '+' || op == '-') return 1;
    if (op == '*' || op == '/') return 2;
    if (op == '^') return 3;
    return 0;
}

bool isOperator(char c) {
    return c == '+' || c == '-' || c == '*' || c == '/' || c == '^';
}

string infixToPostfix(const string& infix) {
    stack<char> opStack;
    string postfix = "";

    for (size_t i = 0; i < infix.length(); i++) {
        char c = infix[i];

        if (isspace(c)) continue;

        if (isalnum(c)) {
            while (i < infix.length() && isalnum(infix[i])) {
                postfix += infix[i];
                i++;
            }
            postfix += " ";
            i--;
        }
        else if (c == '(') {
            opStack.push(c);
        }
        else if (c == ')') {
            while (!opStack.empty() && opStack.top() != '(') {
                postfix += opStack.top();
                postfix += " ";
                opStack.pop();
            }
            if (!opStack.empty()) opStack.pop();
        }
        else if (isOperator(c)) {
            while (!opStack.empty() && getPrecedence(opStack.top()) >= getPrecedence(c)) {
                if (c == '^' && opStack.top() == '^') break;
                postfix += opStack.top();
                postfix += " ";
                opStack.pop();
            }
            opStack.push(c);
        }
    }

    while (!opStack.empty()) {
        postfix += opStack.top();
        postfix += " ";
        opStack.pop();
    }

    return postfix;
}

int evaluatePostfix(const string& postfix) {
    stack<int> valStack;

    for (size_t i = 0; i < postfix.length(); i++) {
        char c = postfix[i];

        if (isspace(c)) continue;

        if (isdigit(c)) {
            int num = 0;
            while (i < postfix.length() && isdigit(postfix[i])) {
                num = num * 10 + (postfix[i] - '0');
                i++;
            }
            valStack.push(num);
            i--;
        }
        else if (isOperator(c)) {
            int val2 = valStack.top(); valStack.pop();
            int val1 = valStack.top(); valStack.pop();

            switch (c) {
                case '+': valStack.push(val1 + val2); break;
                case '-': valStack.push(val1 - val2); break;
                case '*': valStack.push(val1 * val2); break;
                case '/': valStack.push(val1 / val2); break;
                case '^': valStack.push(pow(val1, val2)); break;
            }
        }
    }

    return valStack.top();
}

int main() {
    string symbolicInfix = "A+(B*C)";
    cout << "Infix (Symbolic): " << symbolicInfix << endl;
    cout << "Postfix Output  : " << infixToPostfix(symbolicInfix) << endl;
    

    string numericInfix = "5 + ( 3 * 4 ) - 8 / 2";
    string postfixExpr = infixToPostfix(numericInfix);

    cout << "Infix (Numeric) : " << numericInfix << endl;
    cout << "Converted Postfix: " << postfixExpr << endl;
    cout << "Evaluated Result: " << evaluatePostfix(postfixExpr) << endl;

    return 0;
}