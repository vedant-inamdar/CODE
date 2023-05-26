import java.util.Scanner;
import java.util.*;

public class expertsystem {
    public static void checkDisease(ArrayList<String> ai) {
        if (ai.contains("Headache") && ai.contains("Sore_throat") && ai.contains("Runny_nose") && ai.contains("Snezzing")) {
            System.out.println("The Disease is Cold");
        } 
        else if (ai.contains("Headache") && ai.contains("Sore_throat") && ai.contains("Fever") && ai.contains("Body_ache")) {
            System.out.println("The disease is Influenza");
        } 
        else if (ai.contains("Headache") && ai.contains("Dizziness") && ai.contains("Fever") && ai.contains( "Chills") && ai.contains("Body_ache")) {
            System.out.println("The disese is Typhoid");
        }
        else {
            System.out.println("You have no disease");
        }
    }

    public static void main(String args[]) {
        ArrayList<String> ai = new ArrayList<String>();
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter Symptoms");
        String s[] = { "Headache", "Sore_throat", "Runny_nose", "Snezzing", "Fever", "Chills","Body_ache","Dizziness"};
        String y = "y";
        
        for (int i = 0; i < s.length; i++) {
            System.out.println("Do you have " + s[i]);
            String c = sc.nextLine();
            if (y.equals(c)) {
                ai.add(s[i]);
            }
        }
        checkDisease(ai);
    }
}