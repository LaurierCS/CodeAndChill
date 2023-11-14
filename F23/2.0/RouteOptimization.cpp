#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <list>

struct Node {
    std::string location;
    int coordinates;
    std::list<Node*> next;

    Node(const std::string& loc, int coord) : location(loc), coordinates(coord) {}
};

class DoublyLinkedList {
private:
    std::unordered_map<std::string, Node*> nodes;

public:
     void addNode(const std::string& location, int coordinates) {
          Node* newNode = new Node(location, coordinates);
          nodes[location] = newNode;
     }

     void connectNodes(const std::string& source, const std::string& destination) {
          if (nodes.find(source) != nodes.end() && nodes.find(destination) != nodes.end()) {
               nodes[source]->next.push_back(nodes[destination]);
               nodes[destination]->next.push_back(nodes[source]);
          }
     }

     std::string findShortestPath(const std::string& source, const std::string& destination) {
          if (nodes.find(source) == nodes.end() || nodes.find(destination) == nodes.end()) {
               return "Invalid source or destination";
          }

          Node* sourceNode = nodes[source];
          Node* destNode = nodes[destination];

          std::unordered_set<Node*> visitedForward, visitedBackward;
          std::queue<Node*> forwardQueue, backwardQueue;

          forwardQueue.push(sourceNode);
          backwardQueue.push(destNode);
          visitedForward.insert(sourceNode);
          visitedBackward.insert(destNode);

          while (!forwardQueue.empty() || !backwardQueue.empty()) {
               if (!forwardQueue.empty()) {
                    Node* current = forwardQueue.front();
                    forwardQueue.pop();

                    for (Node* neighbor : current->next) {
                         if (visitedForward.find(neighbor) == visitedForward.end()) {
                              forwardQueue.push(neighbor);
                              visitedForward.insert(neighbor);

                              if (visitedBackward.find(neighbor) != visitedBackward.end()) {
                                   return constructPath(neighbor, sourceNode, destNode, visitedForward, visitedBackward);
                              }
                         }
                    }
               }

               if (!backwardQueue.empty()) {
                    Node* current = backwardQueue.front();
                    backwardQueue.pop();

                    for (Node* neighbor : current->next) {
                         if (visitedBackward.find(neighbor) == visitedBackward.end()) {
                              backwardQueue.push(neighbor);
                              visitedBackward.insert(neighbor);

                              if (visitedForward.find(neighbor) != visitedForward.end()) {
                                   return constructPath(neighbor, sourceNode, destNode, visitedForward, visitedBackward);
                              }
                         }
                    }
               }
          }
          
          return "No path found";
     }

     std::string constructPath(Node* intersection, Node* source, Node* destination, std::unordered_set<Node*>& visitedForward, std::unordered_set<Node*>& visitedBackward) {
          std::string path = intersection->location;
          Node* current = intersection;

          while (current != source) {
               for (Node* neighbor : current->next) {
                    if (visitedForward.find(neighbor) != visitedForward.end()) {
                         path = neighbor->location + " -> " + path;
                         current = neighbor;
                         break;
                    }
               }
          }

          current = intersection;
          while (current != destination) {
               for (Node* neighbor : current->next) {
                    if (visitedBackward.find(neighbor) != visitedBackward.end()) {
                         path += " -> " + neighbor->location;
                         current = neighbor;
                         break;
                    }
               }
          }

          return path;
     }
};

int main() {
     DoublyLinkedList network;

     network.addNode("A", 100);
     network.addNode("B", 200);
     network.addNode("C", 300);
     network.addNode("D", 400);
     network.addNode("E", 500);

     network.connectNodes("A", "B");
     network.connectNodes("B", "C");
     network.connectNodes("C", "D");
     network.connectNodes("D", "E");

     std::cout << network.findShortestPath("A", "D") << std::endl;

     return 0;
}