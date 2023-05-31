# Data Structures in Different Programming Languages

In this markdown file, we will explore different data structures and their implementation in various programming languages. Data structures are used to organize and store data in an efficient and structured manner, allowing for easy access, manipulation, and retrieval of data.

## Arrays

### Python

```python
# Declaration and initialization
my_array = [1, 2, 3, 4, 5]

# Accessing elements
print(my_array[0])  # Output: 1

# Modifying elements
my_array[2] = 6
print(my_array)  # Output: [1, 2, 6, 4, 5]
```

### JavaScript

```javascript
// Declaration and initialization
let myArray = [1, 2, 3, 4, 5];

// Accessing elements
console.log(myArray[0]);  // Output: 1

// Modifying elements
myArray[2] = 6;
console.log(myArray);  // Output: [1, 2, 6, 4, 5]
```

### Java

```java
// Declaration and initialization
int[] myArray = {1, 2, 3, 4, 5};

// Accessing elements
System.out.println(myArray[0]);  // Output: 1

// Modifying elements
myArray[2] = 6;
System.out.println(Arrays.toString(myArray));  // Output: [1, 2, 6, 4, 5]
```

### Ruby

```ruby
# Declaration and initialization
my_array = [1, 2, 3, 4, 5]

# Accessing elements
puts my_array[0]  # Output: 1

# Modifying elements
my_array[2] = 6
puts my_array  # Output: [1, 2, 6, 4, 5]
```

### C++

```cpp
#include <iostream>
#include <array>

int main() {
    // Declaration and initialization
    std::array<int, 5> myArray = {1, 2, 3, 4, 5};

    // Accessing elements
    std::cout << myArray[0] << std::endl;  // Output: 1

    // Modifying elements
    myArray[2] = 6;
    for (int element : myArray) {
        std::cout << element << " ";
    }
    std::cout << std::endl;  // Output: 1 2 6 4 5

    return 0;
}
```

### PHP

```php
// Declaration and initialization
$myArray = array(1, 2, 3, 4, 5);

// Accessing elements
echo $myArray[0] . "\n";  // Output: 1

// Modifying elements
$myArray[2] = 6;
echo implode(" ", $myArray) . "\n";  // Output: 1 2 6 4 5
```

## Linked Lists

### Python

```python
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked list class
class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current

.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next

# Usage
my_list = LinkedList()
my_list.insert(1)
my_list.insert(2)
my_list.insert(3)
my_list.display()  # Output: 1 2 3
```

### JavaScript

```javascript
// Node class
class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

// Linked list class
class LinkedList {
    constructor() {
        this.head = null;
    }

    insert(data) {
        const newNode = new Node(data);
        if (this.head === null) {
            this.head = newNode;
        } else {
            let current = this.head;
            while (current.next) {
                current = current.next;
            }
            current.next = newNode;
        }
    }

    display() {
        let current = this.head;
        while (current) {
            console.log(current.data);
            current = current.next;
        }
    }
}

// Usage
const myList = new LinkedList();
myList.insert(1);
myList.insert(2);
myList.insert(3);
myList.display();  // Output: 1 2 3
```

### Java

```java
// Node class
class Node {
    int data;
    Node next;

    public Node(int data) {
        this.data = data;
        this.next = null;
    }
}

// Linked list class
class LinkedList {
    Node head;

    public void insert(int data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
        } else {
            Node current = head;
            while (current.next != null) {
                current = current.next;
            }
            current.next = newNode;
        }
    }

    public void display() {
        Node current = head;
        while (current != null) {
            System.out.print(current.data + " ");
            current = current.next;
        }
    }
}

// Usage
LinkedList myList = new LinkedList();
myList.insert(1);
myList.insert(2);
myList.insert(3);
myList.display();  // Output: 1 2 3
```

### Ruby

```ruby
# Node class
class Node
  attr_accessor :data, :next

  def initialize(data)
    @data = data
    @next = nil
  end
end

# Linked list class
class LinkedList
  attr_accessor :head

  def initialize
    @head = nil
  end

  def insert(data)
    new_node = Node.new(data)
    if @head.nil?
      @head = new_node
    else
      current = @head
      while current.next
        current = current.next
      end
      current.next = new_node
    end
  end

  def display
    current = @head
    while current
      print current.data, " "
      current = current.next
    end
  end
end

# Usage
my_list = LinkedList.new
my_list.insert(1)
my_list.insert(2)
my_list.insert(3)
my_list.display  # Output: 1 2 3
```

### C++

```cpp
#include <iostream>

struct Node {
    int data;
    Node* next;

    Node(int data) : data(data), next(nullptr) {}
};

class LinkedList {
public:
    LinkedList() : head(nullptr) {}

    void insert(int data) {
        Node* newNode = new Node(data);
        if (head == nullptr) {
            head = newNode;
        }

 else {
            Node* current = head;
            while (current->next) {
                current = current->next;
            }
            current->next = newNode;
        }
    }

    void display() {
        Node* current = head;
        while (current) {
            std::cout << current->data << " ";
            current = current->next;
        }
    }

private:
    Node* head;
};

// Usage
LinkedList myList;
myList.insert(1);
myList.insert(2);
myList.insert(3);
myList.display();  // Output: 1 2 3
```

### PHP

```php
// Node class
class Node
{
    public $data;
    public $next;

    public function __construct($data)
    {
        $this->data = $data;
        $this->next = null;
    }
}

// Linked list class
class LinkedList
{
    public $head;

    public function __construct()
    {
        $this->head = null;
    }

    public function insert($data)
    {
        $newNode = new Node($data);
        if ($this->head === null) {
            $this->head = $newNode;
        } else {
            $current = $this->head;
            while ($current->next) {
                $current = $current->next;
            }
            $current->next = $newNode;
        }
    }

    public function display()
    {
        $current = $this->head;
        while ($current) {
            echo $current->data . " ";
            $current = $current->next;
        }
    }
}

// Usage
$myList = new LinkedList();
$myList->insert(1);
$myList->insert(2);
$myList->insert(3);
$myList->display();  // Output: 1 2 3
```

These examples demonstrate the implementation of arrays and linked lists in different programming languages. Arrays allow you to store and access elements in a sequential manner, while linked lists provide dynamic memory allocation for storing and organizing data. Choose the appropriate data structure based on your requirements to effectively manage and manipulate data in your programs.

Happy coding!

\[3ichael 7ambert\]