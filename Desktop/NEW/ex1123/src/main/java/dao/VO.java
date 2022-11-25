package dao;

public class VO {
	
	// VO = 사용자 정의 자료형
    // 1. 필드
    // - 이 자료형이 저장해야 하는 변수들 (String id, String pw)
    // - 캡슐화를 만족시켜야함 => 접근제한자(private -> 해당 클래스 안에서만, protected -> 하위클래스까지, public -> 누구나)	
	private String id;
	private String pw;

	
	// 디폴트 생성자	
	public VO() {
		
	}
		
	// 2. 생성자 메소드
    // - 일반 메소드는 호출하여 실행가능 but 생성자 메소드는 객체 생성(new) 할 때 딱 한번만 자동으로 실행
    // - 이러한 특성 때문에 보통 필드 초기화(메모리에 최초로 값을 지정) 하는 용도로 사용 -> 변수에 값 저장하는 용도로 사용
    // - 일반 메소드가 생성자 메소드가 되려면 -> void를 적지않고 메소드의 이름을 클래스의 이름과 동일하게 작성한다
	public VO(String id, String pw) {
		super();
		this.id = id;
		this.pw = pw;
	}
			
	// 3. get/set
    // - 필드가 캡슐화를 만족하고 있기 때문에 (private 걸려있기 때문에) 접근이 아예 불가능..
    // - 확인하는 용도로 필드값을 리턴하는 getter
    // - 수정하는 용도로 매개변수값을 전달받아 필드에 저장하는 setter
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

	
	// 4. toString
    // - 모든 클래스들의 최상위 클래스인 object 클래스에 정의된 메소드
    // - 오브젝트에 정의된 내용은 객체의 주소를 리턴 -> 그래서 println(객체)하면 주소값이 출력
    // - VO에서는 toString 메소드를 오버라이딩(재정의)하여 필드값을 문자열로 만들어 리턴
	
	@Override
	public String toString() {
		return "VO [id=" + id + ", pw=" + pw + "]";
	}

}
