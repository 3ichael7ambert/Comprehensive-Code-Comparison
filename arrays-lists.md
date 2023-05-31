# Lists/Arrays in Different Programming Languages

In this markdown file, you will find examples of creating and manipulating lists or arrays in various programming languages. Lists or arrays are used to store multiple values in a single variable. Each programming language has its own syntax and conventions for working with lists or arrays, including creating, accessing elements, modifying values, and performing common operations.

## Python

```python
# Creating a list
my_list = [1, 2, 3, 4, 5]

# Accessing elements
first_element = my_list[0]
last_element = my_list[-1]

# Modifying elements
my_list[0] = 10
my_list[-1] = 50

# Common operations
length = len(my_list)
my_list.append(6)
my_list.insert(2, 7)
my_list.remove(4)
```

## R

```r
# Creating a vector (similar to a list)
my_vector <- c(1, 2, 3, 4, 5)

# Accessing elements
first_element <- my_vector[1]
last_element <- my_vector[length(my_vector)]

# Modifying elements
my_vector[1] <- 10
my_vector[length(my_vector)] <- 50

# Common operations
length <- length(my_vector)
my_vector <- c(my_vector, 6)
my_vector <- c(my_vector[1:2], 7, my_vector[3:length(my_vector)])
my_vector <- my_vector[my_vector != 4]
```

## Ruby

```ruby
# Creating an array
my_array = [1, 2, 3, 4, 5]

# Accessing elements
first_element = my_array[0]
last_element = my_array[-1]

# Modifying elements
my_array[0] = 10
my_array[-1] = 50

# Common operations
length = my_array.length
my_array << 6
my_array.insert(2, 7)
my_array.delete(4)
```

## C

```c
#include <stdio.h>

int main() {
    // Creating an array
    int my_array[] = {1, 2, 3, 4, 5};

    // Accessing elements
    int first_element = my_array[0];
    int last_element = my_array[sizeof(my_array) / sizeof(my_array[0]) - 1];

    // Modifying elements
    my_array[0] = 10;
    my_array[sizeof(my_array) / sizeof(my_array[0]) - 1] = 50;

    // Common operations
    int length = sizeof(my_array) / sizeof(my_array[0]);
    // Note: Array size is fixed in C, so you cannot directly append or insert elements.
    // You would need to create a new array with the desired size and copy elements.
    // Similarly, removing elements requires shifting elements and creating a new array.
    // These operations are more involved in C compared to dynamic languages like Python or Ruby.

    return 0;
}
```

## JavaScript

```javascript
// Creating an array
const my_array = [1, 2, 3, 4, 5];

// Accessing elements
const first_element = my_array[0];
const last_element = my_array[my_array.length - 1];

// Modifying elements
my_array[0] = 10;
my_array[my_array.length - 1] = 50;

// Common operations
const length = my_array.length;
my_array.push(6);
my_array.splice(2, 0, 7);
my_array.splice(my_array.indexOf(4), 1);


```

## Java

```java
public class ArrayManipulation {
    public static void main(String[] args) {
        // Creating an array
        int[] my_array = {1, 2, 3, 4, 5};

        // Accessing elements
        int first_element = my_array[0];
        int last_element = my_array[my_array.length - 1];

        // Modifying elements
        my_array[0] = 10;
        my_array[my_array.length - 1] = 50;

        // Common operations
        int length = my_array.length;
        // Note: Java arrays have a fixed size, so you cannot directly append or insert elements.
        // You would need to create a new array with the desired size and copy elements.
        // Similarly, removing elements requires shifting elements and creating a new array.
        // These operations are more involved in Java compared to dynamic languages like Python or Ruby.
    }
}
```

## Swift

```swift
// Creating an array
var my_array = [1, 2, 3, 4, 5]

// Accessing elements
let first_element = my_array[0]
let last_element = my_array[my_array.count - 1]

// Modifying elements
my_array[0] = 10
my_array[my_array.count - 1] = 50

// Common operations
let length = my_array.count
my_array.append(6)
my_array.insert(7, at: 2)
my_array.removeAll(where: { $0 == 4 })
```

## PHP

```php
// Creating an array
$my_array = array(1, 2, 3, 4, 5);

// Accessing elements
$first_element = $my_array[0];
$last_element = $my_array[count($my_array) - 1];

// Modifying elements
$my_array[0] = 10;
$my_array[count($my_array) - 1] = 50;

// Common operations
$length = count($my_array);
$my_array[] = 6;
array_splice($my_array, 2, 0, 7);
$my_array = array_filter($my_array, function ($value) {
    return $value != 4;
});
```

## Go

```go
package main

import "fmt"

func main() {
    // Creating a slice (similar to an array)
    my_slice := []int{1, 2, 3, 4, 5}

    // Accessing elements
    first_element := my_slice[0]
    last_element := my_slice[len(my_slice)-1]

    // Modifying elements
    my_slice[0] = 10
    my_slice[len(my_slice)-1] = 50

    // Common operations
    length := len(my_slice)
    my_slice = append(my_slice, 6)
    my_slice = append(my_slice[:2], append([]int{7}, my_slice[2:]...)...)
    for i := 0; i < len(my_slice); i++ {
        if my_slice[i] == 4 {
            my_slice = append(my_slice[:i], my_slice[i+1:]...)
            break
        }
    }

    fmt.Println(my_slice)
}
```

## Kotlin

```kotlin
fun main() {
    // Creating a list
    val my_list = listOf(1, 2, 3, 4, 5)

    // Accessing elements
    val first_element = my_list[0]
    val last_element = my_list[my_list.size - 1]

    // Modifying

 elements
    // Note: Kotlin lists are immutable, so you cannot directly modify elements.
    // You would need to create a new list with the desired modifications.

    // Common operations
    val length = my_list.size
    val modified_list = my_list + 6
    val inserted_list = my_list.subList(0, 2) + 7 + my_list.subList(2, my_list.size)
    val filtered_list = my_list.filter { it != 4 }
}
```

## Rust

```rust
fn main() {
    // Creating a vector (similar to an array)
    let mut my_vector = vec![1, 2, 3, 4, 5];

    // Accessing elements
    let first_element = my_vector[0];
    let last_element = my_vector[my_vector.len() - 1];

    // Modifying elements
    my_vector[0] = 10;
    my_vector[my_vector.len() - 1] = 50;

    // Common operations
    let length = my_vector.len();
    my_vector.push(6);
    my_vector.insert(2, 7);
    my_vector.retain(|&x| x != 4);
}
```

These examples demonstrate how to create and manipulate lists or arrays in various programming languages. You can use the provided syntax and conventions to work with lists or arrays, such as accessing elements, modifying values, and performing common operations specific to each programming language. Feel free to explore and experiment with these examples in your preferred programming language.

Happy coding!

\[3ichael 7ambert\]