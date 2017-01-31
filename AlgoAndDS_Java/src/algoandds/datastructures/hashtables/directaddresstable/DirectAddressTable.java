package algoandds.datastructures.hashtables.directaddresstable;

import algoandds.beans.Employee;

public class DirectAddressTable {

	private Employee[] employeesDATArray;
	private int maxCapacity;
	
	public DirectAddressTable(int maxCapacity) {

		this.maxCapacity = maxCapacity;
		employeesDATArray = new Employee[this.maxCapacity];
	}
	
	public void insert(Employee emp) {
		employeesDATArray[emp.getEmpId()] = emp;
	}
	
	public Employee search(int empId) {
		return employeesDATArray[empId];
	}
	
	public boolean delete(Employee emp) {
		if(employeesDATArray[emp.getEmpId()] == null) {
			return false;
		} else {
			employeesDATArray[emp.getEmpId()] = null;
			return true;
		}
	}
	
	@Override
	public String toString() {
		String retValue = "";
		for (Employee emp : employeesDATArray) {
			if(emp != null) {
				retValue += emp.getEmpId() + "-" + emp.getName() + ", ";	
			}
		}
		return retValue;
	}
}

class DirectAddressTableTester {
	public static void main(String[] args) {
		DirectAddressTable table = new DirectAddressTable(10);
		Employee employeeA = new Employee(3, "A", "PUNE");
		Employee employeeB = new Employee(6, "B", "PUNE");
		Employee employeeC = new Employee(1, "C", "PUNE");
		Employee employeeD = new Employee(9, "D", "PUNE");
		Employee employeeE = new Employee(8, "E", "PUNE");
		Employee employeeF = new Employee(2, "F", "PUNE");
		table.insert(employeeA);
		table.insert(employeeB);
		table.insert(employeeC);
		table.insert(employeeD);
		table.insert(employeeE);
		table.insert(employeeF);
		System.out.println(table);
		System.out.println();
		System.out.println("Search 1:" + table.search(1));
		System.out.println("Search 3:" + table.search(3));
		System.out.println("Search 5:" + table.search(5));
		System.out.println();
		System.out.println("Delete 1:" + table.delete(new Employee(1)));
		System.out.println("Delete 3:" + table.delete(new Employee(3)));
		System.out.println("Delete 5:" + table.delete(new Employee(5)));
		System.out.println();
		System.out.println("Search 1:" + table.search(1));
		System.out.println("Search 3:" + table.search(3));
		System.out.println("Search 5:" + table.search(5));
	}
}