package contactservice;

public class Contact {
	
	//Variable definitions
	private final String contactId;
	private String firstName;
	private String lastName;
	private String phoneNumber;
	private String address;
	
	//Constructor
	public Contact(String id, String first, String last, String phone, String address) {
		if(id == null || id.length() > 10) {
			throw new IllegalArgumentException("Invalid contact ID");
		}
		
		this.contactId = id;
		
		setFirstName(first);
		setLastName(last);
		setPhone(phone);
		setAddress(address);
	}
		
	//Getters (Accessors)
	public String getContactId() {
		return contactId;
	}
		
	public String getFirstName() {
		return firstName;	
	}
	
	public String getLastName() {
		return lastName;
	}
	
	public String getPhone() {
		return phoneNumber;
	}
	
	public String getAddress() {
		return address;
	}
	
	//Setters (Mutators)
	public void setFirstName(String first) {
		if(first == null || first.length() > 10) {
			throw new IllegalArgumentException("Invalid First Name");
		}
		
		this.firstName = first;
	}
	
	public void setLastName(String last) {
		if(last == null || last.length() > 10) {
			throw new IllegalArgumentException("Invalid Last Name");
		}
		
		this.lastName = last;
	}
	
	public void setPhone(String phone) {
		if(phone == null || !phone.matches("\\d{10}")) {
			throw new IllegalArgumentException("Invalid Phone Number");
		}
		
		this.phoneNumber = phone;
	}
	
	public void setAddress(String address) {
		if(address == null || address.length() > 30) {
			throw new IllegalArgumentException("Invalid Address");
		}
		
		this.address = address;
	}
}