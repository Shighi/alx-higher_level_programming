# JavaScript Web Scraping

This project contains a collection of JavaScript scripts for performing various web scraping and file operations tasks. The scripts demonstrate working with file systems, making HTTP requests, and interacting with APIs.

## Project Structure

* `0-readme.js`: Script to read and print file contents
* `1-writeme.js`: Script to write a string to a file
* `2-statuscode.js`: Script to display the status code of a GET request
* `3-starwars_title.js`: Script to print Star Wars movie titles using the Star Wars API
* `4-starwars_count.js`: Script to count movies featuring Wedge Antilles
* `5-request_store.js`: Script to get webpage contents and store in a file
* `6-completed_tasks.js`: Script to compute completed tasks by user ID
* `100-starwars_characters.js`: Script to print all characters of a Star Wars movie
* `101-starwars_characters.js`: Script to print Star Wars characters in API response order

## Requirements

* All files are interpreted on Ubuntu 14.04 LTS using Node.js (version 10.14.x)
* All files should end with a new line
* The first line of all files should be exactly `#!/usr/bin/node`
* Code should be semistandard compliant (version 16.x.x)
* All files must be executable
* The length of files will be tested using `wc`
* Not allowed to use `var`
* Required to use the `request` module for sending HTTP requests

## Installation

```bash
# Install Node.js if not already installed
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt-get install -y nodejs

# Install the request module
npm install request
```

## Usage Examples

### Reading a File
```bash
./0-readme.js cisfun
```

### Writing to a File
```bash
./1-writeme.js my_file.txt "Python is cool"
```

### Getting HTTP Status Code
```bash
./2-statuscode.js https://alx-intranet.hbtn.io/status
```

### Star Wars API Interaction
```bash
./3-starwars_title.js 1
```

## Tasks Description

0. **Read File** - Script that reads and prints the content of a file in UTF-8.
1. **Write File** - Script that writes a string to a file in UTF-8.
2. **Status Code** - Script that displays the status code of a GET request.
3. **Star Wars Movie Title** - Script that prints the title of a Star Wars movie based on the episode number.
4. **Star Wars Wedge Antilles** - Script that prints the number of movies where the character "Wedge Antilles" is present.
5. **Loripsum** - Script that gets the contents of a webpage and stores it in a file.
6. **How Many Completed?** - Script that computes the number of tasks completed by user id.
7. **Who Was Playing in This Movie?** - Script that prints all characters of a Star Wars movie.
8. **Right Order** - Script that prints all characters of a Star Wars movie in the same order as the API response.

## Author
Shighi
