//Zoe Dyer IT386-001 program02 – Distributed App with RMI
import java.io.*;
import java.rmi.Naming;
import java.rmi.server.*;
//remote server class 
public class Server {
    

    public static void main(String args[]){
        //check if arguments are provided
       try{
        if(args.length != 1){
            System.out.println("Usage: java RMIServer <port number>");
            return;

        }
        int portNumber = Integer.parseInt(args[0]);

        ComputeImpl obj = new ComputeImpl();
        //bind this object instance to the name server
        Naming.rebind("//localhost:" +portNumber +"/Server", obj);
        System.out.println("The server is ready");

    } catch (Exception e){
        System.out.println("Server failed: " + e.getMessage());
        e.printStackTrace();
    }
}
}
