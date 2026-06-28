package contactservice;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class ContactServiceTest {
	
	@Test
	public void addContactTest() {
		ContactService service = new ContactService();
		
		Contact contact = new Contact("12345", "Brandon", "Fluegge", "1231231234", "123 MyHouse Rd.");
		
		service.addContact(contact);
		
		assertEquals(contact, service.getContact("12345"));
	}
	
	@Test
	public void duplicateTest() {
		ContactService service = new ContactService();
		
		Contact contactOne = new Contact("12345", "Brandon", "Fluegge", "1231231234", "123 MyHouse Rd.");
		Contact contactTwo = new Contact("12345", "Brenda", "Glueffe", "1231231233", " 123 YourHouse Rd.");
		
		service.addContact(contactOne);
		
		assertThrows(IllegalArgumentException.class, () -> {
			service.addContact(contactTwo);
		});
	}
	
	@Test
	public void deleteTest() {
		ContactService service = new ContactService();
		
		Contact contact = new Contact("12345", "Brandon", "Fluegge", "1231231234", "123 MyHouse Rd.");
		
		service.addContact(contact);
		service.deleteContact("12345");
		
		assertThrows(IllegalArgumentException.class, () -> {
			service.getContact("12345");
		});
	}
	
	@Test
	public void updateFirstNameTest() {
		ContactService service = new ContactService();
		
		Contact contact = new Contact("12345", "Brandon", "Fluegge", "1231231234", "123 MyHouse Rd.");
		
		service.addContact(contact);
		service.updateFirstName("12345", "Ashlee");
		
		assertEquals("Ashlee", service.getContact("12345").getFirstName());
	}
	
	@Test
	public void updateLastNameTest() {
		ContactService service = new ContactService();
		
		Contact contact = new Contact("12345", "Brandon", "Fluegge", "1231231234", "123 MyHouse Rd.");
		
		service.addContact(contact);
		service.updateLastName("12345", "Eggeulf");
		
		assertEquals("Eggeulf", service.getContact("12345").getLastName());
	}
	
	@Test
	public void updatePhoneTest() {
		ContactService service = new ContactService();
		
		Contact contact = new Contact("12345", "Brandon", "Fluegge", "1231231234", "123 MyHouse Rd.");
		
		service.addContact(contact);
		service.updatePhone("12345", "3213214321");
		
		assertEquals("3213214321", service.getContact("12345").getPhone());
	}
	
	@Test
	public void updateAddressTest() {
		ContactService service = new ContactService();
		
		Contact contact = new Contact("12345", "Brandon", "Fluegge", "1231231234", "123 MyHouse Rd.");
		
		service.addContact(contact);
		service.updateAddress("12345", "123 YourHouse Rd.");
		
		assertEquals("123 YourHouse Rd.", service.getContact("12345").getAddress());
	}
}
