import java.util.Scanner;
public class Program {
public static void main(String[] args) {
Scanner sc = new Scanner(System.in);
double x, y, average;
System.out.print("Insira um numero: ");
x = sc.nextInt();
System.out.print("Insira outro numero: ");
y = sc.nextInt();
average = (x + y) / 2;
System.out.printf("Media = %.2f%n", average);
sc.close();
}
}
