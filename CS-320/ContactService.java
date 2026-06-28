package contactservice;

import java.util.HashMap;
import java.util.Map;

public class ContactService {
	//Hash map creation for contact storage
	private final Map<String, Contact> contacts = new HashMap<>();
	
	//Add contacts to contacts hash map
	public void addContact(Contact contact) {
		if (contact == null || contacts.containsKey(contact.getContactId())) {
			throw new IllegalArgumentException("Contact ID must be unique");
		}
		
		contacts.put(contact.getContactId(), contact);
	}
	
	//Remove contacts from hash map
	public void deleteContact(String contactId) {
		if (!contacts.containsKey(contactId)) {
			throw new IllegalArgumentException("Contact Does Not Exist!");
		}
		
		contacts.remove(contactId);
	}
	
	//Update contact info using these functions
	public void updateFirstName(String contactId, String first) {
		getContact(contactId).setFirstName(first);
	}
	
	public void updateLastName(String contactId, String last) {
		getContact(contactId).setLastName(last);
	}
	
	public void updatePhone(String contactId, String phone) {
		getContact(contactId).setPhone(phone);
	}
	
	public void updateAddress(String contactId, String address) {
		getContact(contactId).setAddress(address);
	}
	
	//getContact retrieves the contact from the hashmap, contacts, as a Contact object
	public Contact getContact(String contactId) {
		Contact contact = contacts.get(contactId);
		
		if (contact == null) {
			throw new IllegalArgumentException("Contact Does Not Exist!");
		}
		
		return contact;
	}
}