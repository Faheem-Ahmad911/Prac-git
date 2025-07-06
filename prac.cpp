#include <iostream>
using namespace std;

// Node structure
class Node {
public:
    int data;
    Node* next;

    // Constructor to create a new node
    Node(int value) {
        data = value;
        next = nullptr;
    }
};

// Linked list class
class LinkedList {
private:
    Node* head;

public:
    // Constructor
    LinkedList() {
        head = nullptr;
    }

void insert_at_end(int val){
    if (!head) head=new Node(val);
    else{
        Node * temp =head;
        while(temp->next != nullptr){
            temp=temp->next;

        }
        temp->next=new Node(val);
    }   
}

    // Function to display the list
    void display() {
        Node* temp = head;
        while (temp != nullptr) {
            cout << temp->data << " -> ";
            temp = temp->next;
        }
        cout << "NULL" << endl;
    }
    void delete_at_end(){
        if (!head) return;
        if (!head->next) {
            Node* to_del = head;
            head = nullptr;
            delete to_del;
            return;
        }
        Node* temp = head;
        while (temp->next->next != nullptr) {
            temp = temp->next;
        }
        Node* to_del = temp->next;
        temp->next = nullptr;
        delete to_del;
    }
};

int main() {
    LinkedList list;

    // Insert some values
list.insert_at_end(12);
// list.insert_at_end(1);
// list.insert_at_end(12);
// list.insert_at_end(121);
// list.insert_at_end(2);
list.delete_at_end();

    // Display the linked list
    list.display();

    return 0;
}
