interface Result {
    int thoery();
}
interface Project{
    int marks();
}
interface Exam extends Result,Project{
    
}
class Student implements Exam,Project  {
    
}
public class MultiInherit {
    public static void main(String[] args) {
        
    }
}
