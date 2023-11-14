import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

public class Solution {
     public static void main(String[] args) throws IOException {
          BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

          String word = bufferedReader.readLine();

          int[] ascii_map = new int[128];
          Arrays.fill(ascii_map, 0);
          
          int n = word.length();
          
          int num = 0;
          
          for (int i = 0; i < n; i++) {
               int ascii = (char) word.charAt(i);
               int value_in_ascii_map = ascii_map[ascii];
               if (value_in_ascii_map == 1) {
                    num += 1;
               }
               ascii_map[ascii] = value_in_ascii_map += 1;
          }
          
          System.out.println(num);
          
          bufferedReader.close();
     }
}