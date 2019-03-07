package com.codecool.adventure;

import java.util.Scanner;

public class Ui {
    public static String input(String prompt) {
        Scanner scanner = new Scanner(System.in);
        System.out.print(prompt);
        return scanner.nextLine();
    }
}
