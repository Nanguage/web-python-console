# Web Python Console 🐍

A web based Python console powered by [Pyodide](https://github.com/pyodide/pyodide) and [ImJoy](https://imjoy.io/#/).
It allows you to run Python code in the browser, and you can also directly execute code / python file from URL.

## Features

- Run Python code in browser
- Directly execute code / python file from URL
- Better Matplotlib support
- Integrate with ImJoy ecosystem
    + Control by ImJoy plugins
    + Control other ImJoy plugins

This project is a fork of [Pyodide's console](https://github.com/pyodide/pyodide/blob/main/src/templates/console.html).


## Usage

### URL Parameters

- `code`: the Python code to be executed
- `file`: the URL of the Python file to be executed
- `show_code`: whether to show the code in console, default is `true`

### ImJoy API

The console is integrated with ImJoy, you can use the ImJoy API to control the console.

| API | Description | Parameters |
| --- | --- | --- |
| `.echo` | Print a message to the console | `msg: string` |
| `.clear` | Clear the console | |
| `.exec` | Execute Python code | `code: string; show_code: bool = true` |
| `.restart` | Restart the console | |
| `.get_content` | Get the content of the console | |
