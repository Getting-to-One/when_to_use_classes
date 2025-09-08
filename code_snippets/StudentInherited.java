public class Student extends YourMom {
    private String name;
    private String major;
    private int id;
    private float gpa;

    public Student(String name, String major, int id, float gpa) {
        this.name = name;
        this.major = major;
        this.id = id;
        this.gpa = gpa;
    }

    public float getGpa() {
        return gpa;
    }

    public void updateGpa(float newGpa) {
        this.gpa = newGpa;
    }

    public String toString() {
        return "Student{" +
                "name='" + name + '\'' +
                ", major='" + major + '\'' +
                ", id=" + id +
                ", gpa=" + gpa +
                '}';
    }
}