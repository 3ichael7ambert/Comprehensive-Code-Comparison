# Graphical User Interfaces (GUI) in Different Programming Languages

In this markdown file, you will find information about creating Graphical User Interfaces (GUI) in various programming languages. Each programming language offers different libraries, frameworks, or tools for building GUI applications.

## Python

- **Popular GUI Libraries**: Tkinter, PyQt, PySide, Kivy
- **Example Using Tkinter**:

```python
import tkinter as tk

def greet():
    label.config(text="Hello, World!")

root = tk.Tk()
root.title("GUI Application")

label = tk.Label(root, text="Click the button to greet")
label.pack()

button = tk.Button(root, text="Greet", command=greet)
button.pack()

root.mainloop()
```

## R

- **Popular GUI Libraries**: Shiny, RGtk2, tcltk
- **Example Using Shiny**:

```r
library(shiny)

ui <- fluidPage(
  titlePanel("GUI Application"),
  mainPanel(
    h3("Click the button to greet"),
    actionButton("greetButton", "Greet"),
    textOutput("greeting")
  )
)

server <- function(input, output) {
  observeEvent(input$greetButton, {
    output$greeting <- renderText({
      "Hello, World!"
    })
  })
}

shinyApp(ui, server)
```

## Ruby

- **Popular GUI Libraries**: Shoes, QtRuby, FXRuby
- **Example Using Shoes**:

```ruby
require 'shoes'

Shoes.app(title: "GUI Application") do
  stack do
    caption "Click the button to greet"
    button "Greet" do
      alert "Hello, World!"
    end
  end
end
```

## C

- **Popular GUI Libraries**: GTK, Qt, WinAPI
- **Example Using GTK**:

```c
#include <gtk/gtk.h>

void greet(GtkWidget *widget, gpointer data) {
    g_print("Hello, World!\n");
}

int main(int argc, char *argv[]) {
    GtkWidget *window;
    GtkWidget *button;

    gtk_init(&argc, &argv);

    window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
    g_signal_connect(window, "destroy", G_CALLBACK(gtk_main_quit), NULL);

    button = gtk_button_new_with_label("Greet");
    g_signal_connect(button, "clicked", G_CALLBACK(greet), NULL);
    gtk_container_add(GTK_CONTAINER(window), button);

    gtk_widget_show_all(window);

    gtk_main();

    return 0;
}
```

## JavaScript

- **Popular GUI Libraries**: React, Vue.js, Angular, Electron
- **Example Using Electron**:

```javascript
const { app, BrowserWindow, ipcMain } = require('electron')

function createWindow() {
    const win = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            nodeIntegration: true
        }
    })

    win.loadFile('index.html')

    ipcMain.on('greet', (event, arg) => {
        event.reply('greeting', 'Hello, World!')
    })
}

app.whenReady().then(() => {
    createWindow()

    app.on('activate', function () {
        if (BrowserWindow.getAllWindows().length === 0) createWindow()
    })
})

app.on('window-all-closed', function () {
    if (process.platform !== 'darwin') app.quit()
})
```

## Java

- **Popular GUI Libraries**: Swing, JavaFX, AWT
- **Example Using Swing**:

```java
import javax.swing.*;

public class GUIApplication {
    public static void main(String[] args) {
       

 JFrame frame = new JFrame("GUI Application");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JButton button = new JButton("Greet");
        button.addActionListener(e -> JOptionPane.showMessageDialog(frame, "Hello, World!"));

        frame.getContentPane().add(button);
        frame.pack();
        frame.setVisible(true);
    }
}
```

## Swift

- **Popular GUI Libraries**: SwiftUI, AppKit, UIKit
- **Example Using SwiftUI**:

```swift
import SwiftUI

struct ContentView: View {
    @State private var greeting: String = ""

    var body: some View {
        VStack {
            Text("Click the button to greet")
            Button(action: {
                greeting = "Hello, World!"
            }) {
                Text("Greet")
            }
            Text(greeting)
        }
        .padding()
    }
}

@main
struct GUIApplicationApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}
```

## PHP

- **Popular GUI Libraries**: Laravel Livewire, Symfony, Zend Framework
- **Example Using Laravel Livewire**:

```php
<?php

namespace App\Http\Livewire;

use Livewire\Component;

class GreetingComponent extends Component
{
    public $greeting = '';

    public function greet()
    {
        $this->greeting = 'Hello, World!';
    }

    public function render()
    {
        return view('livewire.greeting-component');
    }
}
```

## Go

- **Popular GUI Libraries**: gotk3, fyne, walk
- **Example Using gotk3**:

```go
package main

import (
	"log"

	"github.com/gotk3/gotk3/gtk"
)

func greet() {
	log.Println("Hello, World!")
}

func main() {
	gtk.Init(nil)

	builder, err := gtk.BuilderNew()
	if err != nil {
		log.Fatal("Error:", err)
	}

	err = builder.AddFromFile("gui.glade")
	if err != nil {
		log.Fatal("Error:", err)
	}

	obj, err := builder.GetObject("button1")
	if err != nil {
		log.Fatal("Error:", err)
	}

	button, ok := obj.(*gtk.Button)
	if !ok {
		log.Fatal("Unable to cast object to Button")
	}

	button.Connect("clicked", greet)

	win, err := builder.GetObject("window1")
	if err != nil {
		log.Fatal("Error:", err)
	}

	window, ok := win.(*gtk.Window)
	if !ok {
		log.Fatal("Unable to cast object to Window")
	}

	window.ShowAll()

	gtk.Main()
}
```

## Kotlin

- **Popular GUI Libraries**: JavaFX, TornadoFX, Swing
- **Example Using JavaFX**:

```kotlin
import javafx.application.Application
import javafx.scene.Scene
import javafx.scene.control.Button
import javafx.scene.layout.VBox
import javafx.stage.Stage

class GUIApplication : Application() {
    override fun start(primaryStage: Stage) {
        val button = Button("Greet")
        val label = Label()

        button.setOnAction {
            label.text = "Hello, World!"
        }

        val root = VBox()
        root.children.addAll(button, label)

        primaryStage.title = "GUI Application"
        primaryStage.scene = Scene(root, 300.0, 200.0)
        primaryStage.show()
    }
}

fun main(args: Array<String>) {
    Application.launch(GUIApplication::class.java, *args)
}
```

## Rust

- **Popular GUI Libraries**: gtk-rs, iced, Druid
- **Example Using gtk-rs**:

```rust
extern crate gtk;
use gtk::prelude::*;
use gtk::{Button, Window, WindowType};

fn greet() {
   

 println!("Hello, World!");
}

fn main() {
    gtk::init().expect("Failed to initialize GTK.");

    let window = Window::new(WindowType::Toplevel);
    let button = Button::with_label("Greet");

    button.connect_clicked(|_| greet());

    window.add(&button);
    window.show_all();

    window.connect_delete_event(|_, _| {
        gtk::main_quit();
        Inhibit(false)
    });

    gtk::main();
}
```

These examples demonstrate how to create simple GUI applications in various programming languages. Each language has its own set of libraries, frameworks, or tools for building graphical user interfaces. Feel free to explore and experiment with these examples to create your own GUI applications in your preferred programming language.

Happy coding!

\[3ichael 7ambert\]