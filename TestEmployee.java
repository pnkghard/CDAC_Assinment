package assignment;

//		Core Java Day-1
//1.	Demonstrate the use of main method by printing Hello World in the console.
//2.	Create Employee class having id, name and salary as data members and print() as member function.
//3.	Create objects of Employee class in main class and pass valid data.
//4.	Print the details of all the employee objects.
//5.	Create a class Student having id, name and marks.
//6.	Create objects of Student class in main class and pass valid data.
//7.	Print the details of all the student objects.

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