/* Brandon Fluegge
*  CS300
*  Project Two
*  8/14/2025
*/

#include <iostream>
#include <String>
#include <fstream>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

//Define course structure
struct Course {
	string courseNumber;
	string courseName;
	vector<string> prereq;
	Course() {             //Constructor
		courseNumber = "0";
		courseName = "nil";
	}
};

//HashTable class definitions
class HashTable {

private:

	// Node structure
	struct Node {
		Course course;
		int key;
		Node* next;

		//Constructors
		Node() {
			key = UINT_MAX;
			next = nullptr;
		}

		Node(Course c) : Node() {
			course = c;
		}

		Node(Course c, unsigned int k) : Node() {
			course = c;
			key = k;
		}

	};

	//Nodes vector
	vector<Node> nodes;

	unsigned int tableSize = 179;

	unsigned int hash(int key);

public:
	HashTable();
	HashTable(unsigned int Size);
	virtual ~HashTable();
	void Insert(Course c);
	void PrintAll();
	void Remove(string courseNumber);
	Course Search(string courseNumber);

};

//Hash table constructors
HashTable::HashTable() {
	nodes.resize(tableSize);
}

HashTable::HashTable(unsigned int Size) {
	nodes.resize(Size);
}

//Hash table deconstructor
HashTable::~HashTable() {
	nodes.erase(nodes.begin());
}

//Hashing
unsigned int HashTable::hash(int key) {
	return key % tableSize;
}

//Insertion into table
void HashTable::Insert(Course course) {

	//hash key generated from course number
	unsigned int key = hash(atoi(course.courseNumber.c_str()));

	Node* node = &nodes[key];

	//If first node is empty
	if (node->key == UINT_MAX) {
		node->course = course;
		node->key = key;
	}
	
	//If first node in bucket is not empty
	else {
		Node* curr = node;
		while (curr->next != nullptr) {
			curr = curr->next;
		}
		curr->next = new Node();
		curr = curr->next;
		curr->course = course;
		curr->key = key;
	}
}

//Printing function that performs alphanumeric sorting
void HashTable::PrintAll() {
	vector<Course> allCourses;

	// Iteration through nodes
	for (unsigned int i = 0; i < nodes.size(); i++) {

		// pointer creation
		Node* node = &nodes[i];

		//traverse the list at this bucket
		// Check for valid node and non-empty key
		while (node != nullptr && node->key != UINT_MAX) {

			// Add the Course object to the vector for sorting
			allCourses.push_back(node->course);
			node = node->next;
			}

			//sort alphanumerically
			sort(allCourses.begin(), allCourses.end(), [](const Course& a, const Course& b) {
			return a.courseNumber < b.courseNumber;
			});
		}

	//output all courses and course information
	for (const auto& course : allCourses) {
		std::cout << "Course Number: " << course.courseNumber
			<< ", Course Title: " << course.courseName
			<< ", Prerequisites: ";
		for (unsigned int j = 0; j < course.prereq.size(); j++) {
			std::cout << course.prereq[j] << "; ";
		}
		std::cout << std::endl;
	}
}

//Remove nodes (unused)
void HashTable::Remove(string courseNumber) {
	unsigned int key = hash(atoi(courseNumber.c_str()));
	nodes.erase(nodes.begin() + key);
}

//Search for single course to print info
Course HashTable::Search(string courseNumber) {

	//Find correct key based on hash
	unsigned int key = hash(atoi(courseNumber.c_str()));

	//create pointer at first item in hashed key's bucket
	Node* currNode = &nodes[key];

	// Loop through the bucket
	while (currNode != nullptr) {
		// If the current node's key is valid and matches the course number
		if (currNode->key != UINT_MAX && currNode->course.courseNumber == courseNumber) {

			//print that courses information
			std::cout << "Course number: " << currNode->course.courseNumber << ", Course Title: " << currNode->course.courseName << ", Prerequisites: ";// Found the course, return it
			for (unsigned int i = 0; i < currNode->course.prereq.size(); i++) {
				std::cout << currNode->course.prereq[i] << endl;
				return currNode->course;
			}
		}
		// Move to the next node
		currNode = currNode->next;
	}

	// If course not found return empty object
	Course course;
	std::cout << "Error: Course not found." << endl;
	return course;
}


//file loading and parsing
void loadData(string filePath, HashTable* hashTable) {

	string line;
	string token;
	vector<string> tokens;

	//open file at specified location
	ifstream file(filePath);

	//Check for open errors
	if (file.is_open()) {
		std::cout << "Opening file..." << endl;

		//Get lines from file
		while (getline(file, line)){

			//Add lines to vector using delimiter ','
			istringstream currLine(line);
			while (getline(currLine, token, ',')) {
				tokens.push_back(token);
			}

			//Create new course based on tokens vector
			Course course;
			course.courseNumber = tokens[0];
			course.courseName = tokens[1];
			if (tokens.size() > 2) {
				course.prereq.insert(course.prereq.end(), tokens.begin() + 2, tokens.end());
			}

			//Insert into hash table
			hashTable->Insert(course);

			//reset tokens for next iteration
			tokens.resize(0);
		}
	}

	//In case of file failure
	else {
		std::cout << "ERROR: File failed to open." << endl;
	}
}

//main
int main() {
	char usrInput = '0';
	HashTable* courseTable;
	courseTable = new HashTable();
	string filePath;
	string usrNum;

	//Checking for Exit option
	while (usrInput != '9') {

		// Main input gathering
		std::cout << "Main Menu: \n" << "[1]: Load Course Data\n" << "[2]: Print Course List\n" << "[3]: Search For Course\n" << "[9]: Exit Program" << endl;
		cin >> usrInput;

		//Switch for menu options
		switch(usrInput) {

			//load data
			case '1':
				std::cout << "Enter Path of File" << endl;
				cin.ignore();
				getline(cin, filePath);
				loadData(filePath, courseTable);
				break;
			
			//Print all data
			case '2':
				courseTable->PrintAll();
				break;

			//Search and print data for course
			case'3':
				std::cout << "Enter Course Number: " << endl;
				cin >> usrNum;
				courseTable->Search(usrNum);
				break;

			//Default case
			default:
				break;
		}
	}

	//End of Program
	return 0;
}