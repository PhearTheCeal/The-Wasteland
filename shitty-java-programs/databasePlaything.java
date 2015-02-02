import java.sql.*;
import java.util.ArrayList;

public class databasePlaything 
{
    //so java has no built in sqlite library, and I'm
    //too lazy to fuck around with that shit, so here's
    //a virtual database.
    public static ArrayList<String[]> database = new ArrayList<String[]>();

    public static boolean validAge(String age) 
    {
        try // this try/catch block returns false if it's not
        {   // convertible to an int
            if (Integer.parseInt(age) > 0)
            {
                return true;
            }
            return false;

        } 
        catch(NumberFormatException e) 
        { 
            return false; 
        }
    }

    public static boolean validName(String name) 
    {
        if (name.length() > 0 && name.length() < 64) 
        {
            return true;
        }
        else {
            return false;
        }
    }

    public static void insertData(String name, String age) 
    {
        String[] input = {name, age};
        database.add(input);

    }

    public static void viewData() 
    {
        for (int i = 0; i < database.size(); i++) {
            System.out.println(database.get(i)[0] + " " + database.get(i)[1]);
        }
    }

    public static void takeInput() 
    {
        String userInput = "";
        String name = "";
        String age = "";
        while (userInput != "exit" && !validName(name)) 
        {
            userInput = System.console().readLine("Name, please: ");
            name = userInput;
        }
        while (userInput != "exit" && !validAge(age)) 
        {
            userInput = System.console().readLine("Age, please: ");
            age = userInput;
        }
        insertData(name, age);
    }
    
    public static void main(String[] args) 
    {
        System.out.println("Welcome to Critter's amazing database thing!");
        System.out.println("'insert' to add entries, 'view' to view shit");
        String userInput = "";
        while (userInput != "exit") 
        {
            userInput = System.console().readLine(">>> ");
            if (userInput.equals("insert"))
            {
                takeInput();
            }
            else if (userInput.equals("view"))
            {
                viewData();    
            }

        }
    }

}