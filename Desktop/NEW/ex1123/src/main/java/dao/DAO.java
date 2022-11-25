package dao;

import java.io.InputStream;
import java.util.List;

import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;

public class DAO {
		
		private static SqlSessionFactory sqlSessionFactory;

		static {

			try {
				String resource = "dao/config.xml"; // 쿼리맵퍼와 데이터베이스 프로퍼티가 연결된 리소스파일 가져오기
				InputStream inputStream = Resources.getResourceAsStream(resource); // 인풋스트림을 통해 데이터 읽어오기
				sqlSessionFactory = new SqlSessionFactoryBuilder().build(inputStream); // 마이바티스와 데이터베이스 서버를 연결해주는 객체

			} catch (Exception e) {
				e.printStackTrace();
			}

		}
		public List<VO> List(){
			SqlSession session = sqlSessionFactory.openSession();
			List<VO> list = session.selectList("List");
			session.close(); //반납
			return list;
			
		}
		
		public VO Login(VO vo) {
			SqlSession session = sqlSessionFactory.openSession();
			//Login -> mapper 아이디값 
			VO loginVO=session.selectOne("Login",vo);
			session.close();
			return loginVO;
			
		}
		
		public void signupMethod(userVO vo) {
			SqlSession session = sqlSessionFactory.openSession();
			session.insert("signupMethod", vo);
			session.commit();
			session.close();
		}
		
		
		
		
	}

