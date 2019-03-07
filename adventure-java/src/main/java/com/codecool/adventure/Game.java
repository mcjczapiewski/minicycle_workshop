package com.codecool.adventure;

import java.util.HashMap;
import java.util.Map;

public class Game {
    String roomName = "outside";
    Map<String, Room> rooms = new HashMap<>();

    Game() {
        createRooms();
    }

    private void createRooms() {
        Room outside = new Room(
                "Outside",
                "You're standing outside a huge cave."
        );
        rooms.put("outside", outside);

        Room cave = new Room(
                "Cave",
                "You're in a cave."
        );
        rooms.put("cave", cave);
    }

    public void run() {
        describeRoom();
        boolean playing = true;
        while (playing) {
            System.out.println();
            String command = Ui.input("> ");
            switch (command) {
                case "l":
                case "look":
                    describeRoom();
                    break;

                case "q":
                case "quit":
                    System.out.println("Goodbye!");
                    playing = false;
                    break;

                default:
                    System.out.println("Unrecognized command: " + command);
                    break;
            }
        }
    }

    private void describeRoom() {
        Room room = rooms.get(roomName);
        System.out.println();
        System.out.println(room.title);
        System.out.println();
        System.out.println(room.description);
    }
}
