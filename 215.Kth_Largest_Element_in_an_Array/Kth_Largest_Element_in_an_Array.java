import java.io.*;
import java.util.*;

class Heap
{
    public int[] A;
    public int length;
    public Heap(int[] a){
        A = Arrays.copyOf(a, a.length);
        length = A.length;
        for(int i=length/2-1;i>=0;i--){
            Heapify(i);
        }
    }
    public void Heapify(int i){
        int left = 2*i+1;
        int right = 2*i+2;
        int largest_index;
        if(left<length && A[left]>A[i]){
            largest_index = left;
        }
        else
            largest_index = i;
        if(right<length && A[right]>A[largest_index]){
            largest_index = right;
        }
        if(largest_index != i){
            int tmp = A[i];
            A[i] = A[largest_index];
            A[largest_index] = tmp;
            Heapify(largest_index);
        }
    }
    public void Print(){
        for(int a: A){
            System.out.println(a);
        }
    }
    public int DeleteRoot(){
        int largest = A[0];
        A[0] = A[length-1];
        length--;
        Heapify(0);
        return largest;
    }
}

public class Kth_Largest_Element_in_an_Array{
    public static void main(String[] args){
        int[] a = new int[] {2};
        Heap h = new Heap(a);
        h.Print();
        int res = h.DeleteRoot();
        System.out.println(res);
    }
}


