# Application Programming Interfaces (APIs)

APIs—**Application Programming Interfaces**—allow two pieces of software to communicate.
They define *how* you ask for information and *what form* that information comes back in.

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

# [JSON FILES AND LIVECODING](https://strudel.cc/learn/samples/#loading-samples-from-file-urls)

# Making API Requests in Python

### Two main ways:

## 1. **`urllib.request`**

* built into Python

## 2. **`requests`** (recommended)

* must install with `pip`


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
import urllib.request  

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

# JOKES and DOGS in the CLI

### Install packages

```bash
pip3 install requests pillow
```

* **requests** → makes web calls easy
* **pillow (PIL)** → opens and displays images

