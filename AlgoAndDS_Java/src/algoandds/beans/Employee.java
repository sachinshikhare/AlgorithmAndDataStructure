package algoandds.beans;

public class Employee {

	private int empId;
	private String name;
	private String address;
	
	public Employee() {
	}
	
	public Employee(int empId) {
		this.empId = empId;
	}

	public Employee(int empId, String name, String address) {
		this.empId = empId;
		this.name = name;
		this.address = address;
	}

	public int getEmpId() {
		return empId;
	}

	public void setEmpId(int empId) {
		this.empId = empId;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getAddress() {
		return address;
	}

	public void setAddress(String address) {
		this.address = address;
	}

	@Override
	public String toString() {
		return "Emp Id: " + empId + ", Name: " + name + ", Address: " + address + "\n"; 
	}
	
	@Override
	public boolean equals(Object obj) {
		if(obj instanceof Employee){
			return empId == ((Employee)obj).getEmpId();	
		} else {
			return false;
		}
	}
	
	@Override
	public int hashCode() {
		return this.empId + this.name.hashCode();
	}
}
