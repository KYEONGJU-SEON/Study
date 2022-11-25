package frontcontroller;

public class ViewResolver {

	public static String makeView(String nextPath) {
		return "project/" + nextPath + ".jsp";
	}
}
