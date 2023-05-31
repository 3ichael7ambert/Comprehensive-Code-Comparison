# Conditional Statements in Different Programming Languages

In this markdown file, we will explore how to use conditional statements in different programming languages. Conditional statements allow you to make decisions in your code based on certain conditions. They typically use expressions and logical operators to determine which block of code to execute.

## Python

```python
# If-else statement
x = 5
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")

# Nested if-else statement
num = 10
if num % 2 == 0:
    if num % 3 == 0:
        print("Divisible by both 2 and 3")
    else:
        print("Divisible by 2 but not 3")
else:
    print("Not divisible by 2")
```

## JavaScript

```javascript
// If-else statement
let x = 5;
if (x > 0) {
    console.log("Positive");
} else if (x < 0) {
    console.log("Negative");
} else {
    console.log("Zero");
}

// Nested if-else statement
let num = 10;
if (num % 2 === 0) {
    if (num % 3 === 0) {
        console.log("Divisible by both 2 and 3");
    } else {
        console.log("Divisible by 2 but not 3");
    }
} else {
    console.log("Not divisible by 2");
}
```

## Java

```java
// If-else statement
int x = 5;
if (x > 0) {
    System.out.println("Positive");
} else if (x < 0) {
    System.out.println("Negative");
} else {
    System.out.println("Zero");
}

// Nested if-else statement
int num = 10;
if (num % 2 == 0) {
    if (num % 3 == 0) {
        System.out.println("Divisible by both 2 and 3");
    } else {
        System.out.println("Divisible by 2 but not 3");
    }
} else {
    System.out.println("Not divisible by 2");
}
```

## Ruby

```ruby
# If-else statement
x = 5
if x > 0
  puts "Positive"
elsif x < 0
  puts "Negative"
else
  puts "Zero"
end

# Nested if-else statement
num = 10
if num % 2 == 0
  if num % 3 == 0
    puts "Divisible by both 2 and 3"
  else
    puts "Divisible by 2 but not 3"
  end
else
  puts "Not divisible by 2"
end
```

## C++

```cpp
#include <iostream>

int main() {
    // If-else statement
    int x = 5;
    if (x > 0) {
        std::cout << "Positive" << std::endl;
    } else if (x < 0) {
        std::cout << "Negative" << std::endl;
    } else {
        std::cout << "Zero" << std::endl;
    }

    // Nested if-else statement
    int num = 10;
    if (num % 2 == 0) {
        if (num % 3 == 0) {
            std::cout << "Divisible by both 2 and 3" << std::endl;
        } else {
            std::cout << "Divisible by 2 but not 

3" << std::endl;
        }
    } else {
        std::cout << "Not divisible by 2" << std::endl;
    }

    return 0;
}
```

## PHP

```php
// If-else statement
$x = 5;
if ($x > 0) {
    echo "Positive";
} elseif ($x < 0) {
    echo "Negative";
} else {
    echo "Zero";
}

// Nested if-else statement
$num = 10;
if ($num % 2 == 0) {
    if ($num % 3 == 0) {
        echo "Divisible by both 2 and 3";
    } else {
        echo "Divisible by 2 but not 3";
    }
} else {
    echo "Not divisible by 2";
}
```

These examples demonstrate the usage of conditional statements in various programming languages. You can use the provided syntax and conventions to implement conditional logic in your code and make decisions based on different conditions.

Happy coding!

\[3ichael 7ambert\]