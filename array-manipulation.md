# Array Manipulation

In this markdown file, you will find examples of manipulating arrays in different programming languages. Arrays are used to store multiple values in a single variable. The examples provided demonstrate common array manipulation operations such as adding elements, removing elements, modifying values, and performing array-specific operations.

## Python

```python
# Creating an array
my_array = [1, 2, 3, 4, 5]

# Adding elements
my_array.append(6)
my_array.extend([7, 8, 9])

# Removing elements
my_array.remove(3)
del my_array[0]

# Modifying values
my_array[2] = 10

# Array-specific operations
length = len(my_array)
sum_of_elements = sum(my_array)
```

## JavaScript

```javascript
// Creating an array
let my_array = [1, 2, 3, 4, 5];

// Adding elements
my_array.push(6);
my_array = my_array.concat([7, 8, 9]);

// Removing elements
my_array.splice(2, 1);
my_array.pop();

// Modifying values
my_array[0] = 10;

// Array-specific operations
let length = my_array.length;
let sum_of_elements = my_array.reduce((a, b) => a + b, 0);
```

## Java

```java
import java.util.ArrayList;

public class ArrayManipulation {
    public static void main(String[] args) {
        // Creating an array
        ArrayList<Integer> my_array = new ArrayList<>();
        my_array.add(1);
        my_array.add(2);
        my_array.add(3);
        my_array.add(4);
        my_array.add(5);

        // Adding elements
        my_array.add(6);
        my_array.add(7);
        my_array.add(8);
        my_array.add(9);

        // Removing elements
        my_array.remove(Integer.valueOf(3));
        my_array.remove(0);

        // Modifying values
        my_array.set(2, 10);

        // Array-specific operations
        int length = my_array.size();
        int sum_of_elements = 0;
        for (int element : my_array) {
            sum_of_elements += element;
        }
    }
}
```

## Ruby

```ruby
# Creating an array
my_array = [1, 2, 3, 4, 5]

# Adding elements
my_array << 6
my_array.concat([7, 8, 9])

# Removing elements
my_array.delete(3)
my_array.pop

# Modifying values
my_array[0] = 10

# Array-specific operations
length = my_array.length
sum_of_elements = my_array.sum
```

## C++

```cpp
#include <iostream>
#include <vector>

int main() {
    // Creating an array
    std::vector<int> my_array = {1, 2, 3, 4, 5};

    // Adding elements
    my_array.push_back(6);
    my_array.insert(my_array.end(), {7, 8, 9});

    // Removing elements
    my_array.erase(my_array.begin() + 2);
    my_array.pop_back();

    // Modifying values
    my_array[0] = 10;

    // Array-specific operations
    int length = my_array.size();
    int sum_of_elements = 0;
    for (int element : my_array) {
        sum_of_elements += element;
    }

    return 0;
}
```

## PHP

```php
// Creating an array
$my_array = array(1, 2, 

3, 4, 5);

// Adding elements
$my_array[] = 6;
$my_array = array_merge($my_array, array(7, 8, 9));

// Removing elements
$index = array_search(3, $my_array);
if ($index !== false) {
    unset($my_array[$index]);
}
array_pop($my_array);

// Modifying values
$my_array[0] = 10;

// Array-specific operations
$length = count($my_array);
$sum_of_elements = array_sum($my_array);
```

These examples demonstrate how to manipulate arrays in various programming languages. You can use the provided syntax and conventions to add elements, remove elements, modify values, and perform array-specific operations in your preferred programming language.

Happy coding!

\[3ichael 7ambert\]