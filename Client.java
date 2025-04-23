
/*
 * Zoe Dyer IT386-001 program02 – Distributed App with RMI
 */
import java.io.*;
import java.rmi.Naming;
import java.util.*;



public class Client {
    public static void main(String[] args) {
        try{
            //check if arguments are provided
            if (args.length !=1){
                System.out.println("Usage: java RMIClient <port number>");

                return;
            }
            int portNumber= Integer.parseInt(args[0]);
            ComputeInterface remoteObj=
            (ComputeInterface) Naming.lookup("//localhost:" +portNumber+"/Server");
           Scanner input = new Scanner(System.in);
           System.out.println(" input the first integer:");
           int a = input.nextInt();
           System.out.println(" input the second integer:");
           int b = input.nextInt();
            System.out.println("sum: " + remoteObj.sum(a,b));
            System.out.println("subtract: " +remoteObj.subtract(a,b));
            System.out.println("multiplication: "+remoteObj.multiplication(a,b));
            System.out.println("division: "+remoteObj.division(a,b));
            System.out.println("GCD: "+remoteObj.gcd(a,b));
            System.out.println("Area of Circle: "+remoteObj.areaOfCircle(a));
            System.out.println("Area of Rectangle: "+remoteObj.areaOfRectangle(a,b));
            int[]ab={a,b};
            int[]evenOddResult = remoteObj.evenOrOdd(ab);
            boolean[] primeResult =remoteObj.isPrime(ab);
            System.out.println("\n--- Even(0) or Odd(1) Check ---");
            for(int i = 0; i < ab.length; i++){
                System.out.println("Input: " + ab[i] + " = " + evenOddResult[i]);
            }
            
            System.out.println("\n--- Prime Number Check ---");
            for (int i = 0; i < ab.length; i++) {
                System.out.println("Input: " + ab[i] + " = " + primeResult[i]);
            }
            input.close();
        }catch(Exception e){
            System.out.println("Client exception: " + e);
        }
    }
}
