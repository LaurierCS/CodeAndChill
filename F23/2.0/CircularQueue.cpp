#include <iostream>
#include <vector>

struct Task {
     std::string name;
     int executionTime;
};

class CircularQueue {
private:
     std::vector<Task> queue;
     int front, rear, maxSize;

public:
     CircularQueue(int size) : front(-1), rear(-1), maxSize(size), queue(size) {}

     bool isFull() {
          return (front == 0 && rear == maxSize - 1) || (front == rear + 1);
     }

     bool isEmpty() {
          return front == -1;
     }

     void enqueue(const Task& newTask) {
          if (isFull()) {
               std::cout << "Queue is full - enqueue failed" << std::endl;
          }
          else {
               if (front == -1) {
                    front = 0;
               }

               rear = (rear + 1) % maxSize;
               queue[rear] = newTask;
               std::cout << newTask.name << " enqueued to the queue" << std::endl;
          }
     }

     Task dequeue() {
          Task task;

          if (isEmpty()) {
               std::cout << "Queue is empty - dequeue failed" << std::endl;
          }

          else {
               task = queue[front];
               if (front == rear) {
                    front = rear = -1;
               }
               else {
                    front = (front + 1) % maxSize;
               }
               return task;
          }
     }

     void displayQueue() {
          int i = front;

          if (isEmpty()) {
               std::cout << "Queue is empty" << std::endl;
               return;
          }

          std::cout << "Tasks in the queue: ";

          while (i != rear) {
               std::cout << queue[i].name << " ";
               i = (i + 1) % maxSize;
          }

          std::cout << queue[rear].name << std::endl;
     }
};

void roundRobinCPU(CircularQueue& queue, int timeQuantum) {
     while (!queue.isEmpty()) {
          Task currentTask = queue.dequeue();

          if (currentTask.executionTime <= timeQuantum) {
               std::cout << "Task " << currentTask.name << "  - completed" << std::endl;
          }
          else {
               currentTask.executionTime -= timeQuantum;
               std::cout << "Task " << currentTask.name << " - partially completed with " << currentTask.executionTime << " remaining" << std::endl;
               queue.enqueue(currentTask);
          }
     }
}

int main() {
     CircularQueue cpuQueue(10);

     Task task1 = { "Cow", 5 };
     Task task2 = { "Dog", 3 };
     Task task3 = { "Cat", 4 };
     Task task4 = { "Elephant", 8 };
     Task task5 = { "Tiger", 6 };
     Task task6 = { "Juan", 1 };
     Task task7 = { "Nausher", 2 };
     Task task8 = { "Shahrukh", 3 };
     Task task9 = { "Aidan", 30 };


     cpuQueue.enqueue(task1);
     cpuQueue.enqueue(task2);
     cpuQueue.enqueue(task3);
     cpuQueue.enqueue(task4);
     cpuQueue.enqueue(task5);
     cpuQueue.enqueue(task6);
     cpuQueue.enqueue(task7);
     cpuQueue.enqueue(task8);
     cpuQueue.enqueue(task9);


     cpuQueue.displayQueue();

     roundRobinCPU(cpuQueue, 3);

     return 0;
}