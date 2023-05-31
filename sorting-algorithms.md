# Sorting Algorithms in Different Programming Languages

In this markdown file, we will explore different sorting algorithms and their implementation in various programming languages. Sorting algorithms are used to arrange elements in a particular order, such as ascending or descending, based on a comparison between the elements.

## Bubble Sort

### Python

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Usage
my_array = [5, 2, 1, 4, 3]
bubble_sort(my_array)
print(my_array)  # Output: [1, 2, 3, 4, 5]
```

### JavaScript

```javascript
function bubbleSort(arr) {
    const n = arr.length;
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j+1]) {
                [arr[j], arr[j+1]] = [arr[j+1], arr[j]];
            }
        }
    }
}

// Usage
let myArray = [5, 2, 1, 4, 3];
bubbleSort(myArray);
console.log(myArray);  // Output: [1, 2, 3, 4, 5]
```

### Java

```java
class BubbleSort {
    public static void bubbleSort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j+1]) {
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                }
            }
        }
    }

    public static void main(String[] args) {
        int[] myArray = {5, 2, 1, 4, 3};
        bubbleSort(myArray);
        for (int num : myArray) {
            System.out.print(num + " ");
        }
        // Output: 1 2 3 4 5
    }
}
```

### Ruby

```ruby
def bubble_sort(arr)
    n = arr.length
    for i in 0...n
        for j in 0...(n-i-1)
            if arr[j] > arr[j+1]
                arr[j], arr[j+1] = arr[j+1], arr[j]
            end
        end
    end
end

# Usage
my_array = [5, 2, 1, 4, 3]
bubble_sort(my_array)
puts my_array.inspect  # Output: [1, 2, 3, 4, 5]
```

### C++

```cpp
#include <iostream>

void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j+1]) {
                std::swap(arr[j], arr[j+1]);
            }
        }
    }
}

int main() {
    int myArray[] = {5, 2, 1, 4, 3};
    int n = sizeof(myArray) / sizeof(myArray

[0]);
    bubbleSort(myArray, n);
    for (int i = 0; i < n; i++) {
        std::cout << myArray[i] << " ";
    }
    // Output: 1 2 3 4 5

    return 0;
}
```

### PHP

```php
function bubbleSort(&$arr) {
    $n = count($arr);
    for ($i = 0; $i < $n; $i++) {
        for ($j = 0; $j < $n - $i - 1; $j++) {
            if ($arr[$j] > $arr[$j+1]) {
                [$arr[$j], $arr[$j+1]] = [$arr[$j+1], $arr[$j]];
            }
        }
    }
}

// Usage
$myArray = [5, 2, 1, 4, 3];
bubbleSort($myArray);
print_r($myArray);  // Output: Array ( [0] => 1 [1] => 2 [2] => 3 [3] => 4 [4] => 5 )
```

## Selection Sort

### Python

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Usage
my_array = [5, 2, 1, 4, 3]
selection_sort(my_array)
print(my_array)  # Output: [1, 2, 3, 4, 5]
```

### JavaScript

```javascript
function selectionSort(arr) {
    const n = arr.length;
    for (let i = 0; i < n; i++) {
        let minIndex = i;
        for (let j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }
        [arr[i], arr[minIndex]] = [arr[minIndex], arr[i]];
    }
}

// Usage
let myArray = [5, 2, 1, 4, 3];
selectionSort(myArray);
console.log(myArray);  // Output: [1, 2, 3, 4, 5]
```

### Java

```java
class SelectionSort {
    public static void selectionSort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n; i++) {
            int minIndex = i;
            for (int j = i + 1; j < n; j++) {
                if (arr[j] < arr[minIndex]) {
                    minIndex = j;
                }
            }
            int temp = arr[i];
            arr[i] = arr[minIndex];
            arr[minIndex] = temp;
        }
    }

    public static void main(String[] args) {
        int[] myArray = {5, 2, 1, 4, 3};
        selectionSort(myArray);
        for (int num : myArray) {
            System.out.print(num + " ");
        }
        // Output: 1 2 3 4 5
    }
}
```

### Ruby

```ruby
def selection_sort(arr)
    n = arr.length
    for i in 0...n
        min_index = i
        for j in (i+

1)...n
            if arr[j] < arr[min_index]
                min_index = j
            end
        end
        arr[i], arr[min_index] = arr[min_index], arr[i]
    end
end

# Usage
my_array = [5, 2, 1, 4, 3]
selection_sort(my_array)
puts my_array.inspect  # Output: [1, 2, 3, 4, 5]
```

### C++

```cpp
#include <iostream>

void selectionSort(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        int minIndex = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }
        std::swap(arr[i], arr[minIndex]);
    }
}

int main() {
    int myArray[] = {5, 2, 1, 4, 3};
    int n = sizeof(myArray) / sizeof(myArray[0]);
    selectionSort(myArray, n);
    for (int i = 0; i < n; i++) {
        std::cout << myArray[i] << " ";
    }
    // Output: 1 2 3 4 5

    return 0;
}
```

### PHP

```php
function selectionSort(&$arr) {
    $n = count($arr);
    for ($i = 0; $i < $n; $i++) {
        $minIndex = $i;
        for ($j = $i + 1; $j < $n; $j++) {
            if ($arr[$j] < $arr[$minIndex]) {
                $minIndex = $j;
            }
        }
        [$arr[$i], $arr[$minIndex]] = [$arr[$minIndex], $arr[$i]];
    }
}

// Usage
$myArray = [5, 2, 1, 4, 3];
selectionSort($myArray);
print_r($myArray);  // Output: Array ( [0] => 1 [1] => 2 [2] => 3 [3] => 4 [4] => 5 )
```

These are just a few examples of sorting algorithms implemented in different programming languages. Each algorithm has its own advantages and disadvantages in terms of time complexity, space complexity, and performance characteristics. You can choose the most suitable sorting algorithm based on your specific requirements and constraints.

Happy sorting!

\[3ichael 7ambert\]