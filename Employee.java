package assignment;

import java.util.Scanner;

class Employee {
	int id;
	String firstName;
	String lastName;
	long salary;
	
	//Default Constructor	
	public Employee() {}
	
	//Parameterized constructor
	public Employee(int id, String firstName, String lastName, long salary) {
		this.id = id;
		this.firstName = firstName;
		this.lastName = lastName;
		this.salary = salary;
	}
	
	// getter setter for taking data
	
	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getFirstName() {
		return firstName;
	}

	public void setFirstName(String firstName) {
		this.firstName = firstName;
	}

	public String getLastName() {
		return lastName;
	}

	public void setLastName(String lastName) {
		this.lastName = lastName;
	}

	public long getSalary() {
		return salary;
	}

	public void setSalary(long salary) {
		this.salary = salary;
	}

	// print employee date
	public void print() {
		System.out.println();
		System.out.format("%5s%15s%15s%15s", id, firstName, lastName, salary);
	}
}
