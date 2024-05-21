# 0x14. JavaScript - Web Scraping

This project contains JavaScript scripts for web scraping using Node.js. Each script performs different tasks related to reading, writing, and fetching data from files and APIs.

## Requirements

- Node.js 14.x
- `semistandard` for code style checking
- `request` module for making HTTP requests

## Installation

1. Install Node.js:
    ```sh
    curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
    sudo apt-get install -y nodejs
    ```

2. Install `semistandard`:
    ```sh
    sudo npm install semistandard --global
    ```

3. Install `request` module:
    ```sh
    sudo npm install request --global
    export NODE_PATH=/usr/lib/node_modules
    ```

## Files

- `0-readme.js`: Reads and prints the content of a file.
- `1-writeme.js`: Writes a string to a file.
- `2-statuscode.js`: Displays the status code of a GET request.
- `3-starwars_title.js`: Prints the title of a Star Wars movie by episode number.
- `4-starwars_count.js`: Prints the number of movies where the character "Wedge Antilles" is present.
- `5-request_store.js`: Gets the contents of a webpage and stores it in a file.
- `6-completed_tasks.js`: Computes the number of tasks completed by user ID.
- `100-starwars_characters.js`: Prints all characters of a Star Wars movie.
- `101-starwars_characters.js`: Prints all characters of a Star Wars movie in order of appearance.
