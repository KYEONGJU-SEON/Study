package dao;

public class userVO {


	private String id;
	private String pw;
	private String name;
	private String gender;
	private String email;
	

	
	
	public String getId() {
		return id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getPw() {
		return pw;
	}

	public void setPw(String pw) {
		this.pw = pw;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getGender() {
		return gender;
	}

	public void setGender(String gender) {
		this.gender = gender;
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public userVO() {
		super();
		this.id = id;
		this.pw = pw;
		this.name = name;
		this.gender = gender;
		this.email = email;
	}

	@Override
	public String toString() {
		return "userVO [id=" + id + ", pw=" + pw + ", name=" + name + ", gender=" + gender + ", email=" + email + "]";
	}
	
}
