//Zoe Dyer IT386-001 program02 – Distributed App with RMI
import java.rmi.*;
import java.rmi.server.*;



public class ComputeImpl extends UnicastRemoteObject implements ComputeInterface{
   
    public ComputeImpl() throws RemoteException {
        super();
    }
  //addtion
      public int sum(int a, int b) throws RemoteException{
             
               int result = a+b;
               return result;

      }
// subtraction 
      public int subtract(int a, int b) throws RemoteException{
          
              int  result = a-b;
              return result;
      }
//multiplication
      public  int multiplication(int a , int b ) throws RemoteException{
              
              int result = a*b;
               return result;
            
      }
// division
    public int division( int a , int b) throws RemoteException{
          
        int result;
        if(b !=0)
        {
            result = a/b;
            return result;
        }else {
             return  0;
        }
 }
//    Euclidean Algorithm 
    public int gcd(int a, int b) throws RemoteException{
        int result ;
        if ( b ==0) {
           result = a ;
        }else{
            result = gcd(b,a%b);
        }
        return result;
        
    }
 //even or odd
    public int[] evenOrOdd(int[] a ) throws RemoteException{
            int[] result = new int[a.length]; // Default result
        for(int i = 0; i <a.length; i++)     
         {    int n = a[i];
            
            if (n % 2 == 0){
             result[i] = 0; // Even
            } else {
             result[i] = 1; // Odd
            }
        }
        return result; // Return the result after the loop
    }
//prime or not
   public boolean[] isPrime(int[]a) throws RemoteException{
       boolean[] result = new boolean[a.length]; 
       for(int i = 0; i<a.length;i++){
        result[i] = checkPrime(a[i]);
       }
       return result;
   }

   //helper function for isPrime
   private boolean checkPrime(int n ){
    if (n<=1) return false;
    for(int i =2; i<=Math.sqrt(n);i++){
        if(n%i==0) return false;
    }
     return true;
   }
// area of cricle
   public double areaOfCircle(int r) throws RemoteException{
          double result = Math.PI * r * r;
          return result;
   }
//area of rectangle
   public int areaOfRectangle(int length, int wide) throws RemoteException{
           int result = length * wide;
           return  result;
   }

}
