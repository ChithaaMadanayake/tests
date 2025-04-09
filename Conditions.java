import java.util.Scanner;

public class Conditions {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        System.out.print("Enter Your Marks: ");
        int marks = input.nextInt();  // Read user input
        
        if (marks > 74) {
            System.out.println("Grade: A");
        } else if (marks >= 60) {  // 60 to 74
            System.out.println("Grade: B");
        } else if (marks >= 40) {  // 40 to 59
            System.out.println("Grade: C");
        } else {  // Below 40
            System.out.println("Grade: F");
        }
	
        input.close();  // Close scanner
    }
}
