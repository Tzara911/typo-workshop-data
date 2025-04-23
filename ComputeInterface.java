
//Zoe Dyer IT386-001 program02 – Distributed App with RMI
import java.rmi.*;



public interface ComputeInterface extends Remote{
     
    int sum(int a,int b) throws RemoteException;

    int subtract(int a, int b) throws RemoteException;

    int multiplication(int a,  int b) throws RemoteException;

    int division(int a , int b) throws RemoteException;

    int gcd(int a, int b) throws RemoteException;
    
    int[] evenOrOdd(int[] a ) throws RemoteException;

    boolean[] isPrime(int[] a ) throws RemoteException;

    double areaOfCircle(int r) throws RemoteException;

    int areaOfRectangle(int length, int wide) throws RemoteException;
    

}

