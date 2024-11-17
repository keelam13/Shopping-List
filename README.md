# Shopping List

Shopping List is a Python terminal app that lets user make a list of what to buy, or pretty much everything needing items, quantity and measurements, such as the ingridients of a recipe. It runs in the Code Institute mock terminal on Heroku.

It's a simple app where users can create and name as many lists as they need to. They are also able to view existing lists and add items to the list or delete items. And if users don't need the list anymore, they can also delete the list.

View the deployed site: [Shopping List](https://what-to-buy-9270a4324841.herokuapp.com/)


![Am I responsive?](documentation/)

## User Stories

In order not to forget something, this project was inspired by the users constant need to make a list when grocery shopping.

## Features

### Existing Features
The users are welcomed at the start of the app and will be shown existing lists if there is any. The users are also asked what they would like to do:
 * Exit main menu - to exit the app
 * Add new list - to create and name a new list, then users will also be given the options to:
      - Exit new list menu - to go back to the main menu, or
      - Add items - to add new items to the list, where the users will enter item, quantity and unit of measurement.
 * View lists - to view the shopping list and the items in it. A numbered list of the shopping lists will be shown to the users where they can select the number of the list they want to view the items. The users are shown a tabulated display of the items in the list. In this option the users will also be given the options to:
      - Exit list menu - to go back to the main menu, or
      - Add new item - to add items to the list, or
      - Delete an item - to delete an item from the list. The items will be shown again for users to select which item to delete. The Users will be asked to enter the item they want to delete and will also be asked to confirm deletion of the item before proceeding to execute the deletion.
 * Delete list - to delete a list. The numbered list of shopping lists wil be shown again for users to select which list to delete. After entering which list, the users will also be asked to confirm deletion before proceeding to delete the list.

### Future Features
* Allow users to quit anytime in the process.
* Allow users to edit items.

## Logic Flow Chart

The Shopping List project was built from this logic flow chart.
![Shopping List Logic Flow Chart](documentation/)


## Technologies Used

### Languages Used

* Python3

### Other Technologies

* [Git](https://git-scm.com/) - For version control.

* [Github](https://github.com/) - To save and store the files for the website.

* [Heroku](https://heroku.com) - To deploy the website.

* [Am I Responsive?](https://ui.dev/amiresponsive) To show the website image on a range of devices.

* [Miro](https://miro.com) - Used to create the logic flow chart.

* [Google API's](https://developers.google.com/sheets/api) were used to enable me to access and update the Google Sheets.


## Deployment & Local Development

### Deployment

The site is deployed using GitHub Pages - [Shopping List](https://keelam13.github.io/)

To Deploy the site using GitHub Pages:
1. Login (or signup) to Github.
2. Go to the repository for this project, keelam13/
3. Click the settings button.
4. Select pages in the left hand navigation menu.
5. From the source dropdown select main branch and press save.
6. The site has now been deployed, please note that this process may take a few minutes before the site goes live.

### Local Development

#### How to Fork

To fork the Shopping List repository:

1. Log in (or sign up) to Github.
2. Go to the repository for this project, keelam13/.
3. Click the Fork button in the top right corner.

#### How to Clone

To clone the Shopping List repository:

1. Log in (or sign up) to GitHub.
2. Go to the repository for this project, keelam13/.
3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
5. Type 'git clone' into the terminal and then paste the link you copied in step 3. Press enter.


## Testing

Testing was carried out throughout the build of the project by utilising print statements to ensure the project was running as envisioned.

Tested in my local terminal and the Code Institute Heroku terminal giving invalid inputs to check for the functionality of the validation codes. 

The code was also run through a [PEP8 Linter](https://pep8ci.herokuapp.com/) and confirmed there are no errors.

![PEP8 testing for run.py file](documentation/)


## Bugs

### Solved Bugs

1. The app still continues to ask user to enter item name when 2 is entered  where there are only 0 and 1 options provided in the new list menu.
     Solution: Added an if clause for when 1 is entered, else other than 0 and 1 is invalid.
2. The app creates a list with the same name.
     Solution: Added a validation code to check if the entered list name is already exists.
3. Errors were raised for a variable not defined.
     Solution: While modifying some functions some variables were renamed while some were not unnoticed. These variables were renamed and others which are typo were also corrected.

### Remaining Bugs

1. Arrow keys, page up and page down are accepted when entering a list name or an item. And while the special characters (ex. ^[[D) appear on the spreadsheet, it does not show on the terminal.
 

## Credits

* A video tutorial from Andy Dolinski for [Making a Menu in Python](https://www.youtube.com/watch?v=63nw00JqHo0).

###  Acknowledgements

- The Almighty for the opportunity to do coding.
- My family for their unending support.
- My other half for the love and understanding.
- Cici my girl for the inspiration.
- [Iuliia Konovalova](https://github.com/IuliiaKonovalova) my mentor for the advice, tips and guiding me through the project.
- [Kera Cudmore](https://github.com/kera-cudmore) for the great help on constructing a README file.
- [Code Institute](https://codeinstitute.net/) lessons, tutors and Slack community members for their support and help.
- [Slack overflow](https://stackoverflow.com/) and [Geek for Geeks](https://www.geeksforgeeks.org/) for being my run-to references when I have questions. 