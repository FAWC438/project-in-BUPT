package test1;

import java.util.*;

public class Main
{
	static Scanner sc = new Scanner(System.in);
	static StudentManager sm = new StudentManager();

	public static void main(String[] args)
	{
		int n = sc.nextInt();
		int temp;
		for (int i = 0; i < n; i++)
		{
			temp = sc.nextInt();
			switch (temp)
			{
			case 1:
				add();
				break;
			case 2:
				delete();
				break;
			case 3:
				update();
				break;
			default:
				avg();
				break;
			}
		}
		sc.close();
	}

	public static void add()
	{
		Student student = new Student(sc.next(), sc.next(), sc.nextInt(), sc.nextInt(), sc.nextInt());
		System.out.println(sm.addStudent(student));
	}

	public static void delete()
	{
		System.out.println(sm.delStudent(sc.next()));
	}

	public static void update()
	{
		System.out.println(sm.upStudent(sc.next(), sc.nextInt(), sc.nextInt(), sc.nextInt()));
	}

	public static void avg()
	{
		System.out.println(sm.avgStudent(sc.next()));
	}
	
}

class Student
{
	private String number;
	private String name;
	private int mScore;
	private int eScore;
	private int cScore;

	public int getcScore()
	{
		return cScore;
	}

	public void setcScore(int cScore)
	{
		this.cScore = cScore;
	}

	public int geteScore()
	{
		return eScore;
	}

	public void seteScore(int eScore)
	{
		this.eScore = eScore;
	}

	public int getmScore()
	{
		return mScore;
	}

	public void setmScore(int mScore)
	{
		this.mScore = mScore;
	}

	public String getName()
	{
		return name;
	}

	public void setName(String name)
	{
		this.name = name;
	}

	public String getNumber()
	{
		return number;
	}

	public void setNumber(String number)
	{
		this.number = number;
	}

	public Student(String number, String name, int mScore, int eScore, int cScore)
	{
		this.number = number;
		this.name = name;
		this.eScore = eScore;
		this.mScore = mScore;
		this.cScore = cScore;
	}

	public String toString()
	{
		double avg = (double) (getcScore() + geteScore() + getmScore()) / 3;
		String avgString = String.format("%.1f", avg);
		return "Student ID:" + getNumber() + "\n" + "Name:" + getName() + "\n" + "Average Score:" + avgString;
	}

}

class StudentManager
{
	private ArrayList<Student> students;

	public StudentManager()
	{
		students = new ArrayList<>();
	}

	public int find(Student student) // 由对象找下标
	{
		for (int i = 0; i < students.size(); i++)
		{
			if (students.get(i).getNumber().equals(student.getNumber()))
			{
				return i;
			}
		}
		return -1;
	}

	public Student findByNumber(String id) // 由学号找对象
	{
		for (Student student : students)
		{
			if (student.getNumber().equals(id))
			{
				return student;
			}
		}
		return null;
	}

	public String addStudent(Student student)
	{
		if (find(student) != -1)
		{
			return "Students already exist";
		} else
		{
			students.add(student);
			return "Add success";
		}
	}

	public String delStudent(String number)
	{
		Student temp = findByNumber(number);
		if (temp == null)
		{
			return "Students do not exist";
		} else
		{
			int index = find(temp);
			students.remove(index);
			return "Delete success";
		}
	}

	public String upStudent(String number, int mScore, int eScore, int cScore)
	{
		Student temp = findByNumber(number);
		if (temp == null)
		{
			return "Students do not exist";
		} else
		{
			int index = find(temp);
			temp.setcScore(cScore);
			temp.seteScore(eScore);
			temp.setmScore(mScore);
			students.set(index, temp);
			return "Update success";
		}
	}

	public String avgStudent(String number)
	{
		Student temp = findByNumber(number);
		if (temp == null)
		{
			return "Students do not exist";
		} else
		{

			return temp.toString();
		}
	}

}
