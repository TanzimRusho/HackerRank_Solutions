import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;



public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        List<List<Integer>> arr = new ArrayList<>();

        for (int i = 0; i < 6; i++) {
            String[] arrRowTempItems = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

            List<Integer> arrRowItems = new ArrayList<>();

            for (int j = 0; j < 6; j++) {
                int arrItem = Integer.parseInt(arrRowTempItems[j]);
                arrRowItems.add(arrItem);
            }

            arr.add(arrRowItems);
        }

        bufferedReader.close();
        /*
        int[][] arr_;
        
        for (int i = 0; i < arr.size(); i++) {
            List<Integer> boxedRow = arr.get(i);
            
            int[] unboxedRow = new int[boxedRow.length];
            
            for (int j = 0; j < boxedRow.length; j++)
                unboxedRow[j] = boxedRow[j];
            
            arr_[i] = unboxedRow;
        }
        */
        int sum, max = 0;
        
        for(int i = 0; i < 6; ++i)
        {
            for(int j = 0; j < 6; ++j)
            {
                sum = arr_[i-1][j-1] + arr_[i-1][j] + arr_[i-1][j+1] + arr_[i][j] 
                    + arr_[i+1][j-1] + arr_[i+1][j] + arr_[i+1][j+1];
                
                if (sum > max)
                    max = sum;
            }
        } 
        
        System.out.println(max);
    }
}
