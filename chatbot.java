import java.util.*;
public class chatbot{
    public static HashMap<String,String>responses=new HashMap<>();
    static String username;

    chatbot(){
        responses.put("weather condition","pleasant weather \nask me something");
        responses.put("name","myself bot \nask me something");
        responses.put("are you robot","yes, i'm a robot with human feelings \nask me something");
    }
    public static String getResponse(String input){
        return responses.getOrDefault(input, "This is a Default Message");
    }
    public static void main(String[] args){
        chatbot ch=new chatbot();
        Scanner sc=new Scanner(System.in);
        System.out.println("Welcome to Chatbot, \nPlease Enter Your Name : ");
        username=sc.nextLine();
        System.out.println("Hello "+ username + "\nAsk me something");

        while(true){
            String input=sc.nextLine();
            if(input.equalsIgnoreCase("Exit")){
                System.out.println("Session Ended");
                break;
            }
            else{
                String response=getResponse(input);
                System.out.println(response);
            }
        }
    }
}