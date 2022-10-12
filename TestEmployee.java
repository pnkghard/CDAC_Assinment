package assignment;

import java.util.ArrayList;
import java.util.Scanner;

class TestEmployee {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.print("Enter number of record you want to enter : ");
		int n = sc.nextInt();
		Employee[] emp = new Employee[n];
		for(int i=0; i<n; i++) {
			emp[i] = new Employee(sc.nextInt(), sc.next(), sc.next(), sc.nextLong());
		}
		double avgSalary = 0;
		System.out.printf("%5s%15s%15s%15s", "ID", "FirstName", "LastName", "Salary");
		for (Employee employee : emp) {
			employee.print();
			avgSalary += employee.salary;
		}
		System.out.println();
		System.out.print("Average Salary of all employee is " + avgSalary/n);
	}
}

/*
5
1 Aditya Nagose 50000
2 Avishkara Gayakwad 60000
3 Prasad Pawar 70000
4 Sanket Thakare 80000
5 Pankaj Gharde 60000
*/