# Object Relations Code Challenge - Pet Store

We have three models: `Owner`, `Purchase`, and `Animal`. (For our purposes, "Animal" is a type of animal, not a specific individual animal, and the individual animal's name is part of the Purchase relationship.)

An `Owner` has many `Purchase`s, an `Animal` has many `Purchase`s, and `Purchase`s belong to both `Owner` and `Animal`.

`Owner` - `Animal` is a many to many relationship.

## Instructions

To get started, run `pipenv install` while inside of this directory.

Build out all of the methods listed in the deliverables. The methods are listed in a suggested order, but you can feel free to tackle the ones you think are easiest. Be careful: some of the later methods rely on earlier ones.

**Remember!** This code challenge does not have tests. You cannot run `pytest`. You'll need to create your own sample instances so that you can try out your code on your own. Make sure your relationships and methods work in the console before submitting.

We've provided you with a tool that you can use to test your code. To use it, run `python tools/debug.py` from the command line. This will start a `ipdb` session with your classes defined. You can test out the methods that you write here. You can add code to the `tools/debug.py` file to define variables and create sample instances of your objects.

Writing error-free code is more important than completing all of the deliverables listed - prioritize writing methods that work over writing more methods that don't work. You should test your code in the console as you write.

Similarly, messy code that works is better than clean code that doesn't. First, prioritize getting things working. Then, if there is time at the end, refactor your code to adhere to best practices. When you encounter duplicated logic, extract it into a shared helper method.

**Before you submit!** Save and run your code to verify that it works as you expect. If you have any methods that are not working yet, feel free to leave comments describing your progress.

## Deliverables

Write the following methods in the classes in the files provided. Feel free to build out any helper methods if needed.

### Initializers, Readers, and Writers

#### Owner

- `Owner __init__(self, name)`
  - An owner is initialized with a name, as a string.
  - A name **cannot** be changed after it is initialized.
- `Owner name()`
  - Returns the name of the owner.

#### Animal

- `Animal __init__(self, name, type)`
  - An animal is initialized with a name ('dog', 'lizard', 'parrot', 'spider', etc) as a string and a type ('mammal', 'reptile', 'bird', 'amphibian', etc) as a string
  - The name and type of the animal cannot be changed after being initialized.
- `Animal property name`
  - Returns the name of this animal.
- `Animal property type`
  - Returns the category of this animal.

#### Purchase

- `Purchase __init__(self, owner, animal, price, animal_name)`
  - A purchase is initialized with an owner as an Owner object, a pet as a Pet object, a price as a number, and an animal_name as a string.
  - The animal_name of the purchase can be changed after being initialized, but the price cannot.
- `Purchase property price`
  - Returns the name for that purchase.
- `Purchase property animal_name`
  - Returns the name for the purchased animal.

### Object Relationship Methods

#### Purchase

- `Purchase property owner`
  - Returns the owner for that given purchase.
- `Purchase property animal`
  - Returns the animal for that given purchase.

#### Owner

- `Owner property purchases`
  - Returns a list of purchases (Purchase objects) for an owner.
- `Owner property animals`
  - Returns a **unique** list of Animal instances that the owner has purchased.

#### Animal

- `Animal property owners`
  - Returns a **unique** list of Owner instances who have purchased this type of animal.

### Associations and Aggregate Methods

#### Owner

- `Owner purchase_animal(animal, price, animal_name)`
  - Given an animal (as Animal instance), a price (as an int) and an animal_name (as a string), creates a new Purchase instance and associates it with that owner and that animal.
- `Owner all_purchases()`
  - Returns a list of all purchases that the owner has made.
- `Owner total_purchases()`
  - Returns an int representing the total price of all the purchases the owner has made.

#### Animal

- `Animal animal_names()`
  - Returns an list of strings of all the animal_names given to this type of animal through purchases.
- `Animal biggest_enthusiast()`
  - Returns the name of the owner who has purchased this type of animal the most.
