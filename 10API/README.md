# Application Programming Interfaces (APIs)

APIs—**Application Programming Interfaces**—allow two pieces of software to communicate.
They define *how* you ask for information and *what form* that information comes back in.

Think of an API like * a **vending machine panel** (you press the right button → get the right snack)

In programming, an API is the panel that says:

> “If you send a request in *this* format, the server will send back *this* information.”

APIs let your code * fetch **real-world data** (weather, MBTA schedules, air quality, earthquakes)

# Most API Responses Are JSON

**JSON** (JavaScript Object Notation) is the most common data format.

It is:

* human-readable
* easy for Python to parse
* built from simple structures like lists

Example JSON:

```json
{
  "name": "Ada Lovelace",
  "age": 36,
  "languages": ["English", "French"]
}
```

Python turns JSON into:

* lists (`list`)
* numbers (`int/float`)
* strings (`str`)

# Making API Requests in Python

### Two main ways:

## 1. **`urllib.request`**

* built into Python
* no installation required
* more verbose and lower-level

## 2. **`requests`** (recommended)

* must install with `pip`
* simpler, more readable
* handles errors more gracefully

For teaching, `urllib.request` is useful because it requires no installation on a clean system.

# Example: Tracking the ISS (International Space Station)

We’ll use a **public, key-free** API:

```
http://api.open-notify.org/astros.json
```

This returns JSON listing:

* how many astronauts are in space
* their names
* which craft they’re on

# Fetch Astronaut Data with our IDE

```python
import json
import urllib.request  # built-in HTTP client

url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)

# Read raw bytes, decode JSON into Python structures
result = json.loads(response.read())

print(result)
```

### What’s happening?

* `urlopen(url)` → sends an HTTP GET request
* `.read()` → downloads the response body as raw bytes
* `json.loads()` → converts JSON text → Python dictionary

Example output:

```python
{
  'number': 7,
  'people': [
    {'craft': 'ISS', 'name': 'Oleg Kononenko'},
    {'craft': 'ISS', 'name': 'Tracey Dyson'},
    ...
  ],
  'message': 'success'
}
```

# Saving Astronaut Data to a File

```python
with open("iss.txt", "w") as file:
    file.write(f"There are currently {result['number']} astronauts on the ISS:\n\n")
    for person in result["people"]:
        file.write(person["name"] + " - onboard\n")
```

### Why use `with open(...)`?

It:

* automatically closes the file
* avoids accidental data corruption
* is the modern Python style

When you run this program, you’ll get a simple text file listing the astronauts.

# DOGS in the Command Line (CLI)

We’ll use the Dog CEO API:

```
https://dog.ceo/api/breeds/image/random
```

This returns JSON with a URL of a random dog image.

### 1. Install packages (only once)

```bash
pip3 install requests pillow
```

* **requests** → makes web calls easy
* **pillow (PIL)** → opens and displays images

### 2. Run your program

```bash
python3 {{{your/path/to/dogs.py}}}
```

Your script can:

* fetch the image URL
* download the image
* display it using Pillow (opens Preview on macOS)

# BAD PROGRAMMING JOKES in the CLI

Using this API:

```
https://official-joke-api.appspot.com/random_joke
```

Example Python script:

```bash
python3 {{{your/path/to/jokes.py}}}
```

Your program will:

* fetch a JSON object with `setup` and `punchline`
* print them in sequence
* act like a little command-line comedy club



