Generate a semantic HTML and Tailwind CSS "Contact Support" form consisting of the user's name, email, issue type, and message. The form elements should be stacked vertically and placed inside a card.



Generate a semantic HTML and Tailwind CSS, ReactJS "Beyblade X Point Calculator".


Here are the requirements


The system accepts an input that contains the number of Beyblades they will use for a tournament.
Default to 3.

They will need to choose what format to use: Limited (No repeating parts) and Unlimited (Repeating
parts are okay). Default to Limited


They will need to input the total points allowed for all of the beyblades. Default to 17 points


They will then be asked to build each beyblade based on the number of beyblades.


They will performing the following in order:
1. Choose Blade
  - There will be a list of blades to choose from
2. Choose Ratchet
  - There will be a list of ratchets to choose from
3. Bit
  - There will be a list of bits to choose from


When a part has already been chosen, they should be grayed out since there should be no repeating
parts.


Everytime they choose, dynamically calculate the current total points and it should not exceed the
total maximum points allowed.


Here is a sample json:

```json
[
    {
        "type": "Blade",
        "name": "Wizard Rod",
        "image": "./images/blades/wizard-rod.webp"
        "points": 3,
    },
    {
        "type": "Ratchet",
        "name": "9-60"
        "image": "./images/ratchets/ratchet-960.webp",
        "points": 1
    },
    {
        "type": "Bit",
        "name": "Point (P)",
        "image": "./images/bits/point.webp",
        "points": 2
    }
]
```
