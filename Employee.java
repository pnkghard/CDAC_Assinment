package assignment;

import java.util.Scanner;

//		Core Java Day-1
//1.	Demonstrate the use of main method by printing Hello World in the console.
//2.	Create Employee class having id, name and salary as data members and print() as member function.
//3.	Create objects of Employee class in main class and pass valid data.
//4.	Print the details of all the employee objects.
//5.	Create a class Student having id, name and marks.
//6.	Create objects of Student class in main class and pass valid data.
//7.	Print the details of all the student objects.


class Employee {
	Scanner sc = new Scanner(System.in);
	int id;
	String firstName;
	String lastName;
	long salary;
	
		
	public Employee() {}

	public Employee(int id, String firstName, String lastName, long salary) {
		this.id = id;
		this.firstName = firstName;
		this.lastName = lastName;
		this.salary = salary;
	}

	// function for setting data of employee
	public void setDetails() {
		System.out.println();
		System.out.print("Enter Employee id, name and salary : ");
		id = sc.nextInt();
		firstName = sc.next();
		lastName = sc.next();
		salary = sc.nextLong();
	}
	
	// print employee date
	public void print() {
		System.out.println();
		System.out.format("%5s%15s%15s%15s", id, firstName, lastName, salary);
	}
}
