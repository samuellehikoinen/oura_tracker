# Oura tracker

©Samuel Lehikoinen 2021

Oura tracker is created to quickly check personal health status from terminal. 

## Getting started

Clone the project

`git clone https://github.com/samuellehikoinen/oura_tracker.git`

Run the main.py file

`python main.py`

The program requires your Oura authentication token.

- Navigate to the Personal Access Tokens page

 `https://cloud.ouraring.com/personal-access-tokens`
 
- In the upper-right corner of the page click the "Create A New Personal Access Token" Button

- Enter a unique note for the new Personal Access Token you are about to generate

- Click "Create Personal Access Token" to submit the form and create your new Personal Access Token

- You should now have a new access token listed on the Personal Access Tokens page

More at [Oura API docs](https://cloud.ouraring.com/docs/authentication#personal-access-tokens)

The authentication token is stored in your local file, _auth.txt_

## A step further

MacOS users can add _'oura'_ command to .zshrc file for easier access.

Change path to this function.

```
function oura() {
  clear
  python ~/PATH/oura_tracker/main.py
}
```
