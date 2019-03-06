# User stories

<!-- toc -->

- [Basic program](#basic-program)
- [Movement](#movement)
- [Colors](#colors)
- [Items](#items)
- [Help](#help)
- [Characters](#characters)

<!-- tocstop -->

First, a screenshot for inspiration:

![screenshot](screenshot.png)

(want a cool terminal? install `cool-retro-term`)

## Basic program

*This should already be in your starting code*.

I should be able to run the game, see my surroundings, and quit.

- Display information about surroundings
- Ask for a command
- The command `quit`, or `q` should exit
- The command `look`, or `l` should describe the room again

<details>
<summary>Example</summary>

```
Outside

You're standing outside a large cave.

> xxx
I don't recognize that command.

> quit
Goodbye!
```

</details>

## Movement

I want to move between rooms.

- There are at least 2 rooms, connected by exits
- Commands: `north`, `south`, `east`, `west` (or `n`, `s`, `e`, `w`) move between rooms
- Display which exits are available (e.g. `north`, `south`)
- Display room information when moving

Hint: Store a dictionary of exits in a room: `'east': 'room1', 'west': 'room2'` etc.

<details>
<summary>Example</summary>

```
Outside

You're standing outside a large cave.
There are the following exits: north

> north

Cave

You're inside a huge cave.
There are the following exits: south
```

</details>

## Colors

I want to see information visually highlighted, so that it's easier to notice important details.

For example, you can use different colors for:
- Room title
- Exits (north, south etc.)
- Items
- Characters
- Prompt (the beginning `"> "`)

In Python, you can use the [termcolor](https://pypi.org/project/termcolor/) library.

## Items

I want to find items, and pick them up.

- There are some items in rooms
- Items are described when room is described
- The command `get` should pick the item up -- now the player has it
- The command `inventory` (or `i`) should display player's list of items


<details>
<summary>Example</summary>

```
Outside

You're standing outside a large cave.
There are items on the floor: key

> get
Get what? key
Taken.

> i
You are carrying: key
```

</details>

## Help

I want to see a list of commands.

- The command `help` (or `h`, or `?`) should display a list of available commands
- Remember to add new commands to help after you implement them!

## Characters

I want to meet some non-player characters!

- There is a Wizard in one of the rooms. Describe him when the room is described
- The command `talk` causes him to say something

<details>
<summary>Example</summary>

```
Cave

You're in a cave.
The Wizard is here.

> talk
Talk to who? The Wizard
The Wizard says, "Greetings, adventurer!"
```

</details>

## Characters move between rooms

## Bigger game scenario

## Keys and opening doors

## Keeping score

## Winning the game
